import logging


logging.basicConfig(filename='logs.txt',
                    filemode='w',
                    format='%(asctime)s %(message)s',
                    encoding='utf-8',
                    level='DEBUG',)
logger = logging.getLogger('Program_logger')


def debug_log(message, filename='', classname='', funcname=''):
    logger.info(f'[DEBUG][{filename}//{classname}//{funcname}] {message}.')


def info_log(message, filename='', classname='', funcname=''):
    logger.info(f'[INFO][{filename}//{classname}//{funcname}] {message}.')


def warning_log(message, filename='', classname='', funcname=''):
    logger.info(f'[WARNING][{filename}//{classname}//{funcname}] {message}.')


def exception_log(message, filename='', classname='', funcname='',  ex=''):
    if ex:
        logger.exception(f'[EXCEPTION]{filename}//{classname}//{funcname}] {message}. Exception: {ex}')
    else:
        logger.exception(f'[EXCEPTION][{filename}//{classname}//{funcname}] {message}.')
