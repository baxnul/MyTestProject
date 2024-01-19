import logging
import logging.handlers
import os


def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    current_dir = os.path.abspath(os.path.dirname("__file__"))
    log_dir = "/".join(current_dir.rsplit("/", 1)[:-1]) + "/logger"
    log_file = f"{log_dir}/test.log"
    if not os.path.exists(log_file):
        open(log_file, 'w').close()
    if not os.access(log_file, os.W_OK):
        raise Exception("No write access to log file")
    handler = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=500000000, backupCount=1, encoding="utf-8"
    )
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
