import logging
from logging.handlers import SysLogHandler

def custom_logger(name, filepath):
  logger = logging.getLogger(name)
  
  # Remove existing handlers if they exist.
  if logger.hasHandlers():
    logger.handlers.clear()
  
  handler = logging.FileHandler(filepath)
  formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
  handler.setFormatter(formatter)
  logger.addHandler(handler)
  logger.propagate = False  # Prevent logs from being passed to the root logger

  return logger