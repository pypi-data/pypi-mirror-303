import sys
from loguru import logger
from .constants import *

def init_log(_hdr, _dir='./logs2'):
    logger.remove()
    logger.add(
        sink=sys.stdout,
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | <level>{level:<7}</level> | {message}",
        level="TRACE",
        colorize=True
    )
    logger.level("DEBUG", color="<dim>")
    logger.level("INFO", color="<cyan>")

__all__ = ['logger', 'init_log']