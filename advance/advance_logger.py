import sys
import logging
import logging.config

LOGGING_FMT = '%(asctime)s: - %(filename)s:%(funcName)s:%(lineno)d - %(levelname)8s - %(message)s'
LOGGING_DATEFMT = '%Y-%m-%d %H:%M:%S %p'


def custom_logger(file_name: str, level: logging = logging.DEBUG):
    logging.basicConfig(filename=f'{file_name}.log', filemode='w', level=level, format=LOGGING_FMT)
    obj = logging.getLogger()
    obj.setLevel(level)

    screen_handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter(fmt=LOGGING_FMT)
    screen_handler.setFormatter(formatter)
    logging.getLogger().addHandler(screen_handler)

    print("Logger object created successfully..")
    return obj
