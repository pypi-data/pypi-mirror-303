import json
import os
from datetime import datetime, timezone
from typing import Dict, List, Union

LOG_LEVELS = {
    "DEBUG": 1,
    "INFO": 2,
    "WARNING": 3,
    "ERROR": 4,
    "CRITICAL": 5,
}

JSON = Union[str, int, float, bool, None, Dict[str, "JSON"], List["JSON"]]
VALUE = Union[str, int, float, bool, JSON]


class Log:
    """
    `Log` is a class that facilitates logging messages to a local file, which can be
    useful for debugging and monitoring purposes. It provides a simple interface for
    writing log messages with different levels, such as "info", "warning", "error", etc.

    The log messages are stored in a JSON file, which can be easily parsed and analyzed
    later. This class does not provide any log rotation or cleanup mechanisms, so it is
    recommended to manage log files manually or use external log management tools.

    Example usage:

    .. code-block:: python

        from automizor import log

        # Set log level to INFO
        log.set_level("INFO")

        # Write a log message
        log.info("This is an info message")
    """

    def __init__(self):
        self.level = "INFO"

    def set_level(self, level: str):
        """
        Set the log level for filtering log messages.

        Parameters:
            level (str): The log level to set. Valid log levels are "DEBUG", "INFO",
                "WARNING", "ERROR", and "CRITICAL".

        Raises:
            ValueError: If an invalid log level is provided.
        """

        if level not in LOG_LEVELS:
            raise ValueError(f"Invalid log level: {level}")

        self.level = level

    def write_log(self, level: str, msg: VALUE):
        """
        Write a log message with the specified log level.

        Parameters:
            level (str): The log level of the message. Valid log levels are "DEBUG", "INFO",
                "WARNING", "ERROR", and "CRITICAL".
            msg (VALUE): The log message to write. This can be a boolean, string, integer, float
                or a JSON-serializable dictionary or list.

        Raises:
            ValueError: If an invalid log level is provided.
        """

        if level not in LOG_LEVELS:
            raise ValueError(f"Invalid log level: {level}")

        if LOG_LEVELS[level] < LOG_LEVELS[self.level]:
            return

        data = []
        file_path = "output/log.json"
        try:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
        except json.JSONDecodeError:
            pass

        if isinstance(msg, (dict, list)):
            msg = json.dumps(msg, ensure_ascii=False)

        timestamp = datetime.now(timezone.utc).isoformat()
        data.append({"level": level, "msg": msg, "timestamp": timestamp})

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)
