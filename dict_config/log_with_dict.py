import logging
import logging.config

config = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        }
    },
    'handlers': {
        'info': {
            'level': logging.DEBUG,
            'class': 'logging.FileHandler',
            'filename': 'info.log'
        },
    },
    "root": {
        "level": logging.DEBUG,
        "handlers": ["info"]
    }
}

logging.config.dictConfig(config)

# create logger
logger = logging.getLogger(__name__)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
