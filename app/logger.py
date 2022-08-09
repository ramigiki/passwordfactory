import logging.handlers as handlers
from os import path
import logging


class LoggingException(Exception):
    """Custom class for logging-related exceptions."""

    pass


LOG_FORMAT = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# TODO: configurable log directory. logs/ should be fallback
LOG_FILE = path.join("logs", "password-factory.log")


def setup_log_handler():
    """
    Returns log handler with log rotation enabled.

    """
    info_log_handler = handlers.RotatingFileHandler(
        LOG_FILE, maxBytes=5000000, backupCount=1
    )
    info_log_handler.setLevel(logging.INFO)
    info_log_handler.setFormatter(LOG_FORMAT)
    return info_log_handler


def setup_logger():
    """
    collect the pieces and setup logger
    App should break if logger is not initiated
    """
    try:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        log_handler = setup_log_handler()
        logger.addHandler(log_handler)
        return logger
    except IOError as ex:
        raise LoggingException(str(ex))
