from app.logger import Logger


def test_logger_singelton():
    logger_1 = Logger().get_logger()
    logger_2 = Logger().get_logger()
    assert logger_1 == logger_2
