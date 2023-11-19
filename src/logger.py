import logging


def setup_logging():
    """
    возращает логгер с настройками по умолчанию.
    """
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
    return logging.getLogger()
