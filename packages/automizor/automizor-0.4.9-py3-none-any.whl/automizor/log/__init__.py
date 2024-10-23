from functools import lru_cache

from ._log import VALUE


@lru_cache
def _get_log():
    from ._log import Log

    return Log()


def debug(msg: VALUE):
    """
    Writes a debug log message with a level of "DEBUG".

    Parameters:
        msg (VALUE): The log message to write. This can be a boolean, string, integer, float
            or a JSON-serializable dictionary or list.
    """

    _get_log().write_log("DEBUG", msg)


def info(msg: VALUE):
    """
    Writes an info log message with a level of "INFO".

    Parameters:
        msg (VALUE): The log message to write. This can be a boolean, string, integer, float
            or a JSON-serializable dictionary or list.
    """

    _get_log().write_log("INFO", msg)


def warning(msg: VALUE):
    """
    Writes a warning log message with a level of "WARNING".

    Parameters:
        msg (VALUE): The log message to write. This can be a boolean, string, integer, float
            or a JSON-serializable dictionary or list.
    """

    _get_log().write_log("WARNING", msg)


def error(msg: VALUE):
    """
    Writes an error log message with a level of "ERROR".

    Parameters:
        msg (VALUE): The log message to write. This can be a boolean, string, integer, float
            or a JSON-serializable dictionary or list.
    """

    _get_log().write_log("ERROR", msg)


def critical(msg: VALUE):
    """
    Writes a critical log message with a level of "CRITICAL".

    Parameters:
        msg (VALUE): The log message to write. This can be a boolean, string, integer, float
            or a JSON-serializable dictionary or list.
    """

    _get_log().write_log("CRITICAL", msg)


def set_level(level: str):
    """
    Set the log level for filtering log messages.

    Parameters:
        level (str): The log level to set. Valid log levels are "DEBUG", "INFO",
            "WARNING", "ERROR", and "CRITICAL".

    Raises:
        ValueError: If an invalid log level is provided.
    """

    _get_log().set_level(level)


__all__ = [
    "debug",
    "info",
    "warning",
    "error",
    "critical",
    "set_level",
]
