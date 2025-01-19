import logging
from logging import Logger

def get_dummy_logger() -> Logger:
    logging.basicConfig(filename="dummy.log", format='%(asctime)s %(message)s', filemode="w")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(console_handler)
    return logger
