import logging


logging.basicConfig(filename='download_logs.txt',
                    filemode='w',
                    encoding='utf-8',
                    level='DEBUG',)
logger = logging.getLogger('Download_logger')


def download_debug_log(message):
    logger.info(f'[DEBUG] {message}.')

