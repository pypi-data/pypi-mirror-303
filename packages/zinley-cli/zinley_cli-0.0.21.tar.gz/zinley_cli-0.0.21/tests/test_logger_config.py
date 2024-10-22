import os
import logging
from zinley.v2_new.code.log.logger_config import get_logger
import logging.handlers

def test_get_logger(tmpdir):
    # Create a temporary directory for testing
    temp_dir = ".zinley"
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)

    # Call the get_logger function
    logger = get_logger('test_module', '.')

    # Assert that the logger is an instance of logging.Logger
    assert isinstance(logger, logging.Logger)

    # Assert that the logger level is set to DEBUG
    assert logger.level == logging.DEBUG

    # Assert that the logger has the console handler
    assert any(isinstance(handler, logging.StreamHandler) for handler in logger.handlers)

    # Assert that the logger has the file handler
    assert any(isinstance(handler, logging.handlers.RotatingFileHandler) for handler in logger.handlers)

    # Assert that the log directory is created
    assert os.path.exists(os.path.join(temp_dir, 'logs'))

    # Assert that the log file is created
    assert os.path.exists(os.path.join(temp_dir, 'logs', 'app.log'))