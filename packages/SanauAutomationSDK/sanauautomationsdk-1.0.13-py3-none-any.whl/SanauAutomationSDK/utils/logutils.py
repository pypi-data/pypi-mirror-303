import logging.handlers
import os
import sys

formatter = logging.Formatter("%(asctime)s %(levelname)s %(filename)s %(funcName)s: %(message)s")

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler(filename='storage/logs/info.log', mode="a", encoding="utf-8")
file_handler.setFormatter(formatter)

logger = logging.getLogger("Main Logger")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

dispatcher_file_handler = logging.FileHandler(filename=os.path.join('storage/logs', 'dispatcher.log'), mode="a", encoding="utf-8")
dispatcher_log = logging.getLogger("Dispatcher Log")
dispatcher_log.setLevel(logging.INFO)
dispatcher_log.addHandler(dispatcher_file_handler)
dispatcher_log.addHandler(stream_handler)

health_file_handler = logging.FileHandler(filename=os.path.join('storage/logs', 'health.log'), mode="a", encoding="utf-8")
health_log = logging.getLogger("Helth Log")
health_log.setLevel(logging.INFO)
health_log.addHandler(health_file_handler)
health_log.addHandler(stream_handler)