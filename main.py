from advance.advance_logger import custom_logger


def test_custom_logger():
    logger = custom_logger("advance")
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


test_custom_logger()
