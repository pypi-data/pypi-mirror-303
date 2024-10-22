import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Protocol

from pythonjsonlogger import jsonlogger
from sys import stdout

from ..dig_ass.db import make_session_id
from ..extentions import SingletonMeta


class SomeLogger(Protocol):
    def error(self, msg: object, *args, **kwargs) -> None:
        pass


class JsonFormatter(jsonlogger.JsonFormatter):
    """
    additional json formatting possible
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.json_ensure_ascii = False


class LoggerSingleton(metaclass=SingletonMeta):
    __slots__ = ("_logger",)

    def __init__(self, logger_config: dict) -> None:
        """
        :param logger_config: dict
        Example:
            {
                "name": "foo",
                "level_common": "DEBUG",
                "stdout_json": False,
                "format_stdout": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "level_stdout_handler": "DEBUG",
                "file_dir": "./logs",
                "format_file": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "level_file_handler": "DEBUG"
            }
        """
        self._logger = logging.getLogger(name=logger_config["name"])
        self._logger.setLevel(logger_config["level_common"])
        self._init_stdout_handler(logger_config)
        # configure logging to file
        if logger_config.get("write_to_file"):
            self._init_file_handler(logger_config)

    def _init_stdout_handler(self, logger_config: dict) -> None:
        stdout_handler = logging.StreamHandler(stdout)
        # configure logging to stdout
        # stdout_json == True -> set json Formatter
        if logger_config.get("stdout_json"):
            stdout_formatter = JsonFormatter(logger_config["format_stdout"])
        else:
            stdout_formatter = logging.Formatter(logger_config["format_stdout"])

        stdout_handler.setFormatter(stdout_formatter)
        stdout_handler.setLevel(logger_config["level_stdout_handler"])
        self._logger.addHandler(stdout_handler)

    def _init_file_handler(self, logger_config: dict) -> None:
        log_file_dir = Path(logger_config["file_dir"])
        if not log_file_dir.exists():
            self._logger.warning(
                f"Folder {log_file_dir.absolute()} is not exist. Creating..."
            )
            log_file_dir.mkdir()
        log_name: str = logger_config["name"]
        file: str = f"{log_name}_{make_session_id()}.json"
        log_file_path: Path = log_file_dir / file
        max_bytes: int = 100 * 1024 * 1024  # 100 MB
        file_handler = RotatingFileHandler(log_file_path, mode="a", maxBytes=max_bytes)
        json_formatter = JsonFormatter(logger_config["format_file"])
        file_handler.setFormatter(json_formatter)
        file_handler.setLevel(logger_config["level_file_handler"])
        self._logger.addHandler(file_handler)

    def get(self):
        return self._logger

    @property
    def logger(self) -> logging.Logger:
        return self._logger


def log_llm_error(
    text: str | None = None,
    vector: list[float] | None = None,
    model: str = "gigachat",
    logger: SomeLogger = None,
) -> None:
    if not logger:
        raise AttributeError("Logger in function log_llm_error is required")
    if text is not None and not text:
        logger.error(f"No response from {model}!!!")
        return None
    if vector is not None and all(not item for item in vector):
        logger.error(f"No response from {model} encoder!!!")
        return None
    return None
