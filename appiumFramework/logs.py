import logging
import os
from datetime import datetime as dt


class CustomFormatter(logging.Formatter):
    def format(self, record):
        record_time = dt.fromtimestamp(record.created).strftime("%Y-%m-%d %H:%M:%S")
        record_line = f"{record.filename}:{record.lineno}"

        return f"[{record.levelname}] | {record_time} | {record_line} | {record.msg} |"


def create_logger(name='name', filename=None):
    filename = filename.replace(".py", ".log")
    custom_formatter = CustomFormatter()
    file_path = os.path.dirname(os.path.abspath(__file__))
    filename = file_path + f"/{filename}"
    if not os.path.isfile(filename):
        open(filename, 'w').close()

    file_handler = logging.FileHandler(filename=filename, mode="a")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(custom_formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(custom_formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


logger = create_logger(name="main_logs", filename=os.path.basename(__file__))
