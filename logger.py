import logging


logging.basicConfig(filename='logs.txt',
                    filemode='w',
                    format='%(asctime)s %(message)s',
                    encoding='utf-8',
                    level='DEBUG',)
logger = logging.getLogger('Parser_logger')


def debug_log(message, ex=''):
    if ex:
        logger.debug(f'[DEBUG] *** {message} {ex} ***')
    else:
        logger.debug(f'[DEBUG] *** {message} ***')


def info_log(message, ex=''):
    if ex:
        logger.info(f'[INFO] *** {message} {ex} ***')
    else:
        logger.info(f'[INFO] *** {message} ***')


def warning_log(message, ex=''):
    if ex:
        logger.warning(f'[WARNING] *** {message} {ex} ***')
    else:
        logger.warning(f'[WARNING] *** {message} ***')


def exception_log(message, ex=''):
    if ex:
        logger.exception(f'[EXCEPTION] *** {message} {ex} ***')
    else:
        logger.exception(f'[EXCEPTION] *** {message} ***')
