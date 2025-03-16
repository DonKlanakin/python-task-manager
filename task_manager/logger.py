from datetime import datetime
import logging

class Log:
    @staticmethod
    def info(class_info, message):
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.info(f":: {class_info} :: {message}")

    @staticmethod
    def debug(class_info, message, arg):
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.debug(f":: {class_info} :: {message} :: {arg}")

    @staticmethod
    def error(class_info, message, e):
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.error(f":: {class_info} :: {message} :: {e}")