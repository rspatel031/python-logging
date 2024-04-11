import logging


def basic_logger(filename: str, level: logging = logging.DEBUG):
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename=f'{filename}.log', encoding='utf-8', level=level, filemode='w')
    return logger


def test_custom_logger():
    log = basic_logger("basic")
    log.debug("Hello")
    log.info("Hello")
    log.critical("Hello")
    log.error("Hello")
    log.warning("Hello")


test_custom_logger()
