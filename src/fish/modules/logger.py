import os
import logging
from logging.handlers import RotatingFileHandler
from .utils import full_imagePath

global logger
logger = None

def log_init():
    global logger  # Declare logger as a global variable so it can be accessed outside the function
    if logger is not None:
        return
    g_log_path = full_imagePath("log.txt")
    # logging.basicConfig(
    # level=logging.INFO,  # Set logging level, such as DEBUG, INFO, WARNING, ERROR, CRITICAL
    # format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    # handlers=[
    #     logging.FileHandler(g_log_path, encoding='utf-8'),  # Output to file
    #     # logging.StreamHandler()  # Also output to console (optional)
    # ]
    #)
    logger = logging.getLogger('my_app_logger')
    logger.setLevel(logging.DEBUG) # Output all information
    #logger.setLevel(logging.INFO)
    # Set log format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Maximum single log file size: 1 MB (unit is bytes, 5 * 1024 * 1024 = 5MB)
    max_bytes = 1 * 1024 * 1024  # 1 MB
    backup_count = 3  # Keep a maximum of 3 backup log files (plus the current one, a total of 4)

    # Create RotatingFileHandler
    file_handler = RotatingFileHandler(
        filename=g_log_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)

    # # Also output to console (optional)
    # console_handler = logging.StreamHandler()
    # console_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(file_handler)
    # logger.addHandler(console_handler)
    logger.info("Log initialization successful")
def GetLogger():
    global logger
    return logger

if __name__ == '__main__':
    if logger == None:
        log_init()