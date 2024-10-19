import logging
import string


def init_logger(level, log_file='', mode='a'):
    logger = logging.getLogger()

    if logger.hasHandlers():
        logger.warning('Re-initialize logger.')
        return logger

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(Formatter())
    stream_handler.setLevel(level)
    logger.addHandler(stream_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file, mode=mode, encoding='utf-8')
        file_handler.setFormatter(Formatter(disable_color=False))
        file_handler.setLevel(level)
        logger.addHandler(file_handler)

    logger.setLevel('DEBUG')
    return logger


class Formatter(logging.Formatter):
    """Custom logging formatter."""

    WHITE = "\x1b[37m"
    CYAN = "\x1b[36m"
    YELLOW = "\x1b[33m"
    RED = "\x1b[31m"
    BOLD_RED = "\x1b[31;1m"
    GREEN = "\x1b[32m"
    PURPLE = "\x1b[35m"
    RESET = "\x1b[0m"

    # Example when having custom keys
    # "%(asctime)s %(name)s %(levelname)s %(localrank)s %(message)s"
    fmt_ = string.Template("$color[%(levelname)s]$reset %(message)s")

    # Full version example:
    # %y-%m-%d %H:%M:%S,uuu
    DATEFMT = "%y-%m-%d %H:%M:%S"

    colors = {
        logging.DEBUG: CYAN,
        logging.INFO: GREEN,
        logging.WARNING: PURPLE,
        logging.ERROR: RED,
        logging.CRITICAL: BOLD_RED,
    }

    def __init__(self, disable_color=False):
        super().__init__()
        self._disable_color = disable_color

    def format(self, record):
        # Example when having custom keys
        # defaults = {'localrank': '\b'}
        defaults = {}

        if self._disable_color:
            color = ''
            reset = ''
        else:
            color = self.colors.get(record.levelno, self.RESET)
            reset = self.RESET
        fmt = self.fmt_.substitute(color=color, reset=reset)
        formatter = logging.Formatter(fmt, self.DATEFMT)
        return formatter.format(record)
