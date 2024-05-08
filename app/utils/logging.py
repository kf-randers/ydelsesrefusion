import sys
import logging

from prometheus_client import Gauge

from utils.config import DEBUG

# Prometheus
APP_RUNNING = Gauge('up', '1 - app is running, 0 - app is down', labelnames=['name'])


# Logging
def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG) if DEBUG else logger.setLevel(logging.INFO)
    logger.addHandler(get_handler())
    return logger


def get_handler():
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('[%(levelname)s]%(name)s:%(asctime)s - %(message)s', "%d-%m-%Y %H:%M:%S")
    handler.setFormatter(formatter)
    return handler
