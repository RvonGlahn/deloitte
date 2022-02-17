import os

from logging import Logger
from logs.my_logger import create_file_logger


FILE_PATH = os.path.dirname(os.path.abspath(__file__))


def test_my_logger():
    test_logger = create_file_logger("test_file_logger")
    test_logger.info('Test')

    assert type(test_logger) == Logger
    assert os.path.exists(os.path.join(FILE_PATH, "..", "logs", "test_file_logger.log"))


