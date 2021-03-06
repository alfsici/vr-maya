import logging
from QtHandler import QtHandler

logger = logging.getLogger(__name__)
if not len(logger.handlers):
    handler = QtHandler()
    handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(handler)
logger.setLevel(logging.DEBUG)