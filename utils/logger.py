import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class Logger:

    @staticmethod
    def log_debug(message):
        return logging.debug(message)

    @staticmethod
    def log_info(message):
        return logging.info(message)

    @staticmethod
    def log_error(message):
        return logging.error(message)
