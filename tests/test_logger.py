from app.logger import get_logger


def test_logger_singelton():
    logger_1 = get_logger()
    logger_2 = get_logger()
    assert logger_1 == logger_2
