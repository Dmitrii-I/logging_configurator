from logging.config import dictConfig
from logging import getLogger
import sys
from datetime import datetime


def now() -> str:
    return datetime.utcnow().strftime('%Y%m%dT%H%M%S.%fZ')


def get_logger(name: str, path: str, log_level: str='INFO', append: bool=True, stdout: bool=True):

    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': "[%(asctime)s] [%(name)-25.25s] [%(levelname)-7.7s] %(message)s",
                'datefmt': "%Y-%m-%d %H:%M:%S"
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
                'stream': sys.stdout  # otherwise stderr will be used if not specified
            },
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'simple',
                'filename': path,
                'encoding': 'utf8',
                'mode': 'a' if append else 'w',
            }
        },

        'root': {
            'level': log_level,
            'handlers':  ['file', 'console'] if stdout else ['file']
        }

    }

    dictConfig(config)
    logger = getLogger(name)

    def handle_exception(exc_type, exc_value, exc_traceback):
        logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

    sys.excepthook = handle_exception

    return logger
