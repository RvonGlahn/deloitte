import logging
import os


FILE_PATH = os.path.dirname(os.path.abspath(__file__))


def create_file_logger(logger_name: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # FileHandler for File
    log_path = os.path.join(FILE_PATH, logger_name + ".log")
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.INFO)

    # Create Formatter
    file_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_format)

    # Add Handler to logger
    logger.addHandler(file_handler)

    return logger