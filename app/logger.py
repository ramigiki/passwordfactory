import logging.handlers as handlers
from os import path
import logging


class LoggingException(Exception):
    """Custom class for logging-related exceptions."""

    pass


class LoggerBaseSingelton(type):
    """
    This class ensures that logger class is a singleton class

    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(LoggerBaseSingelton, cls).__call__(
                *args, **kwargs
            )
        return cls._instances[cls]


class Logger(metaclass=LoggerBaseSingelton):
    """
    Logger class that returns a logger object

    Args:
        metaclass (LoggerBaseSingelton): To ensure singleton
    """

    def __init__(self, name):
        """
        logger initialisation method.

        Args:
            name (string): logger name
        """
        self.logger_name = name
        self.log_format = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        self.error_log_file = path.join("logs", "error.log")
        self.info_log_file = path.join("logs", "info.log")

    def setup_error_handler(self):
        """
        Returns error log handler

        """
        error_log_handler = handlers.RotatingFileHandler(
            self.error_log_file, maxBytes=5000000, backupCount=1
        )
        error_log_handler.setLevel(logging.ERROR)
        error_log_handler.setFormatter(self.log_format)
        return error_log_handler

    def setup_info_handler(self):
        """
        Returns info log handler

        """
        info_log_handler = handlers.RotatingFileHandler(
            self.info_log_file, maxBytes=5000000, backupCount=1
        )
        info_log_handler.setLevel(logging.INFO)
        info_log_handler.setFormatter(self.log_format)
        return info_log_handler

    def setup_logger(self):
        """
        collect the pieces and setup logger

        """
        try:
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            info_handler = self.setup_info_handler()
            error_handler = self.setup_error_handler()
            logger.addHandler(info_handler)
            logger.addHandler(error_handler)
            return logger
        except IOError as ex:
            raise LoggingException(str(ex))

    def get_logger(self):
        """
        Returns logger to the calling request

        """
        logger = self.setup_logger()
        return logger
