import logging
import os


USER = os.getlogin()
ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)
LOG_FILE = os.path.join(ROOT_DIR, f"{USER}.log")


class CustomFormatter(logging.Formatter):
    FORMAT = "%(asctime)s [%(pathname)s:%(lineno)d] %(levelname)-8s | %(message)s"
    LEVEL_COLORS = {
        "DEBUG": "\033[0;36m",  # Cyan
        "INFO": "\033[0;37m",  # White
        "WARNING": "\033[0;33m",  # Yellow
        "ERROR": "\033[0;31m",  # Red
        "CRITICAL": "\033[1m\033[1;31m"  # Bold Red
    }
    RESET = "\033[0m"
    TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self, colored: bool = None):
        super().__init__(self.FORMAT)
        self.colored = colored

    def format(self, record: logging.LogRecord):
        if self.colored:
            log_format = self.LEVEL_COLORS.get(record.levelname, "") + self.FORMAT + self.RESET
        else:
            log_format = self.FORMAT

        # Truncate the pathname from the root directory
        if "pathname" in record.__dict__.keys() and ROOT_DIR in record.pathname:
            record.pathname = record.pathname[len(ROOT_DIR) + 1:]

        return logging.Formatter(log_format, self.TIME_FORMAT).format(record)


class LogFilter(logging.Filter):
    def filter(self, record):
        return all(map(lambda keyword: keyword not in record.name, ["botocore", "urllib", "s3transfer", "playsound"]))


class CustomLogger(logging.Logger):
    def __init__(self, name: str):
        super().__init__(name, logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_formatter = CustomFormatter(colored=True)

        console_handler.setFormatter(console_formatter)

        self.addFilter(LogFilter())
        self.addHandler(console_handler)


logging.setLoggerClass(CustomLogger)

logger = logging.getLogger("EEIA 2023")

if __name__ == "__main__":
    logger.debug("A debug")
    logger.info("An info")
    logger.warning("A warning")
    logger.error("An error")
    logger.critical("A critical")

    try:
        x = 3 / 0
    except ZeroDivisionError:
        logger.exception("An exception")
