from enum import Enum


class StrEnum(str, Enum):
    """
    Базовый класс для перечислений строковых значений.
    Наследуется от str и Enum, чтобы обеспечить строковое поведение.
    """

    def __str__(self):
        return str(self.value)
