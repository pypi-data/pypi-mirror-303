import copy, json, codecs, os
import typing as t
from dacite import from_dict
from dataclasses import dataclass, field


@dataclass
class ReplicaItem:
    Body: str
    Role: bool
    DateTime: str


@dataclass
class InnerContextItem:
    Replicas: t.List[ReplicaItem] = field(default_factory=list)


@dataclass
class OuterContextItem:
    Sex: bool
    Age: int
    UserId: str
    SessionId: str
    ClientId: str
    TrackId: str = ""


@dataclass
class ChatItem:
    OuterContext: OuterContextItem = field(default_factory=OuterContextItem)
    InnerContext: InnerContextItem = field(default_factory=InnerContextItem)


class DigitalAssistantDataset:
    """
    Represents a dataset for a digital assistant, loading and preparing data from chat and label files.
    """

    def __init__(self, chats_path: str, labels_path: str):
        """
        Initializes the DigitalAssistantDataset.

        Args:
            chats_path (str): Path to the directory containing chat JSON files.
            labels_path (str): Path to the directory containing label JSON files.
        """
        self.raw_chats, self.raw_labels = self.load_raw_data(chats_path, labels_path)
        self.cases, self.labels = self.prepare_data()
        self.index = 0

    def load_raw_data(
        self, chats_path: str, labels_path: str
    ) -> t.Tuple[t.List[dict], t.List[dict]]:
        """
        Loads raw chat and label data from the specified directories.

        Args:
            chats_path (str): Path to the directory containing chat JSON files.
            labels_path (str): Path to the directory containing label JSON files.

        Returns:
            Tuple[List[dict], List[dict]]: A tuple containing a list of chat dictionaries and a list of label dictionaries.

        Raises:
            FileNotFoundError: If no matching files are found between the chats and labels directories.
        """
        labels_files = set(os.listdir(labels_path))
        chats_files = set(os.listdir(chats_path))

        # Find matching chat and label files based on a portion of their filenames
        oper_files = [
            file_name
            for file_name in labels_files
            if file_name[file_name.find("chatid") :] in chats_files
        ]

        if not oper_files:
            raise FileNotFoundError(
                "No matching files found between chats and labels directories."
            )

        chats = []
        labels = []
        for file_name in oper_files:
            chat_file_path = os.path.join(
                chats_path, file_name[file_name.find("chatid") :]
            )
            label_file_path = os.path.join(labels_path, file_name)

            with codecs.open(chat_file_path, encoding="utf8") as f:
                chat = json.load(f)
            with codecs.open(label_file_path, encoding="utf8") as f:
                label = json.load(f)

            chats.append(chat)
            labels.append(label)

        return chats, labels

    def create_messages_label_from_chat_label(
        self, label: dict, messages: t.List[dict]
    ) -> list:
        """
        Creates a list of message labels based on the provided chat label and messages.

        Args:
            label (dict): The chat label dictionary.
            messages (List[dict]): The list of message dictionaries.

        Returns:
            list: A list of message labels, where each element corresponds to a message in the input list.
                If a message has a 'Role' key, its label is set to None, otherwise it takes the chat label.
        """
        return [label if not m.get("Role") else None for m in messages]

    def prepare_data(
        self,
    ) -> t.Tuple[t.List[t.Tuple[str, ChatItem]], t.List[dict]]:
        """
        Prepares the loaded data into a format suitable for training or evaluation.

        Returns:
            Tuple[List[Tuple[str, ChatItem]], List[dict]]: A tuple containing:
                - A list of tuples, where each tuple consists of a replica (user utterance) and a ChatItem object
                representing the conversation context up to that point.
                - A list of labels corresponding to each replica in the first list.

        Raises:
            ValueError: If neither "messagesLabel" nor "chatLabel" is provided in a label dictionary.
            AssertionError: If the number of messages and labels do not match.
        """
        cases = []
        labels = []
        for chat, label in zip(self.raw_chats, self.raw_labels):
            messages = chat["InnerContext"]["Replicas"]

            # Determine message labels based on available label types
            if label.get("messagesLabel") is not None:
                m_labels = label["messagesLabel"]
            elif label.get("chatLabel") is not None:
                m_labels = self.create_messages_label_from_chat_label(
                    label["chatLabel"], messages
                )
            else:
                raise ValueError(
                    'Either "messagesLabel" or "chatLabel" must be provided for each label.'
                )

            assert len(messages) == len(
                m_labels
            ), "Number of messages and labels do not match."

            for idx, (m, l) in enumerate(zip(messages, m_labels)):
                if l is not None:
                    replica = m["Body"]
                    case_chat = copy.deepcopy(chat)
                    case_chat["InnerContext"]["Replicas"] = copy.deepcopy(
                        messages[:idx]
                    )
                    case_chat["OuterContext"]["Age"] = int(
                        case_chat["OuterContext"]["Age"]
                    )
                    case_chat = from_dict(ChatItem, case_chat)

                    cases.append((replica, case_chat))
                    labels.append(l)
        return cases, labels

    def make_table(self) -> t.Dict[str, list]:
        cases, labels = self.prepare_data()
        return {
            "sex": [case[1].OuterContext.Sex for case in cases],
            "age": [case[1].OuterContext.Age for case in cases],
            "user": [case[1].OuterContext.UserId for case in cases],
            "session": [case[1].OuterContext.SessionId for case in cases],
            "client": [case[1].OuterContext.ClientId for case in cases],
            "track": [case[1].OuterContext.TrackId for case in cases],
            "replica": [case[0] for case in cases],
            "label": labels,
        }

    def __len__(self):
        """
        Returns the total number of cases in the dataset.
        """
        return len(self.cases)

    def __getitem__(self, index: int):
        """
        Allows accessing a specific case in the dataset using its index.

        Args:
            index (int): The index of the desired case.

        Returns:
            Tuple[str, ChatItem, dict]: A tuple containing the replica, chat context, and label for the specified index.

        Raises:
            IndexError: If the provided index is out of range.
        """
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range.")
        replica, chat = self.cases[index]
        label = self.labels[index]
        return replica, chat, label

    def __iter__(self):
        """
        Makes the dataset iterable, allowing you to iterate through its cases.
        """
        self.index = 0
        return self

    def __next__(self):
        """
        Returns the next case in the iteration.

        Raises:
            StopIteration: If there are no more cases to iterate over.
        """
        if self.index >= len(self):
            raise StopIteration
        result = self[self.index]
        self.index += 1
        return result
