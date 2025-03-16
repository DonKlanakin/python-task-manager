from datetime import datetime
import logging

class Log:
    @staticmethod
    def info(class_name, message):
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.info(f":: {class_name} :: {message}")

    @staticmethod
    def debug(class_name, message):
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.debug(f":: {class_name} :: {message}")

    @staticmethod
    def error(class_name, message):
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.error(f":: {class_name} :: {message}")