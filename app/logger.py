import logging.handlers as handlers
from os import path
import logging


class LoggingException(Exception):
    """Custom class for logging-related exceptions."""

    pass


LOG_FORMAT = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ERROR_LOG_FILE = path.join("logs", "error.log")
INFO_LOG_FILE = path.join("logs", "info.log")


def setup_error_handler():
    """
    Returns error log handler

    """
    error_log_handler = handlers.RotatingFileHandler(
        ERROR_LOG_FILE, maxBytes=5000000, backupCount=1
    )
    error_log_handler.setLevel(logging.ERROR)
    error_log_handler.setFormatter(LOG_FORMAT)
    return error_log_handler


def setup_info_handler():
    """
    Returns info log handler

    """
    info_log_handler = handlers.RotatingFileHandler(
        INFO_LOG_FILE, maxBytes=5000000, backupCount=1
    )
    info_log_handler.setLevel(logging.INFO)
    info_log_handler.setFormatter(LOG_FORMAT)
    return info_log_handler


def setup_logger():
    """
    collect the pieces and setup logger

    """
    try:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        info_handler = setup_info_handler()
        error_handler = setup_error_handler()
        logger.addHandler(info_handler)
        logger.addHandler(error_handler)
        return logger
    except IOError as ex:
        raise LoggingException(str(ex))


# logger should have only one instance across the application
_instance = None


def get_logger():
    global _instance
    if not _instance:
        _instance = setup_logger()
    return _instance
