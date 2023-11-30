import logging.config
import os

outputs_folder = os.path.dirname(os.path.abspath(__file__)) + os.sep + '_outdict'
print(outputs_folder)

config_dict = {
    'version': 1,
    'formatters': {
        'formatter1': {
            'format': '%(asctime)s:%(name)s:%(message)s',
        },
        'formatter2': {
            'format': '%(asctime)s:%(name)s:%(levelname)s:%(module)s:%(funcName)s:::%(message)s',
        },
    },
    'handlers': {
        'file_handler1': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(outputs_folder, 'logger1_h1.log'),
            'formatter': 'formatter1',
        },
        'stream_handler1': {
            'class': 'logging.StreamHandler',
            'formatter': 'formatter1',
        },
        'file_handler2': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(outputs_folder, 'logger2_h2.HTML'),
            'formatter': 'formatter2',
            'level': 'DEBUG',
        },
        'handler3_time': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(outputs_folder, 'time_rotation', 'logger2_h3_rot.HTML'),
            'when': 's',
            'interval': 1,
            'backupCount': 5,
            'formatter': 'formatter2',
            'level': 'DEBUG',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file_handler1', 'stream_handler1'],
    },
    'loggers': {
        'logger2': {
            'level': 'DEBUG',
            'handlers': ['file_handler2', 'handler3_time'],
        },
    },
}

logging.config.dictConfig(config_dict)

# Test the loggers
root_logger = logging.getLogger()
root_logger.debug('This is a debug message')

logger2 = logging.getLogger('logger2')
logger2.debug('This is a debug message for logger2')