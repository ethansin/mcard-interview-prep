import logging
import sys
import os
from logging import Logger
from pathlib import Path
from datetime import datetime

def get_dummy_logger() -> Logger:
    logging.basicConfig(filename="dummy.log", format='%(asctime)s %(message)s', filemode="w")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(console_handler)
    return logger

class StreamToLogger:
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ""

    def write(self, message):
        if message.strip():
            self.logger.log(self.log_level, message.strip())

    def flush(self):
        pass

def create_logger(log_dir: Path = Path("./logs")) -> Logger:

    if not log_dir.exists():
        os.mkdir(log_dir)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = log_dir / f"{timestamp}.log"

    logging.basicConfig(filename=log_path, format='%(asctime)s %(message)s', filemode="w")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.__stdout__)  # Use original stdout
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(console_handler)

    sys.stdout = StreamToLogger(logger, logging.INFO)
    sys.stderr = StreamToLogger(logger, logging.ERROR)

    return logger