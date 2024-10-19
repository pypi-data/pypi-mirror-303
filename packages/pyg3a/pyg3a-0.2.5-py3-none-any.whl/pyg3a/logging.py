import logging
from typing import Final, override

logger: Final[logging.Logger] = logging.getLogger("pyg3a")


def setup_logger(debug: bool = False) -> None:
    # Set level of custom logger
    logger.setLevel(logging.DEBUG if debug else logging.WARNING)

    # Setup handler for some reason
    custom_handler: logging.StreamHandler = logging.StreamHandler()
    custom_handler.setLevel(logging.DEBUG if debug else logging.WARNING)
    custom_handler.setFormatter(LoggingFormatter(debug))

    # Add new handler to our logger
    logger.addHandler(custom_handler)


class LoggingFormatter(logging.Formatter):
    debug: bool

    grey = "\033[37;1m"
    yellow = "\033[33;1m"
    red = "\033[31;1m"
    bold_red = "\033[31;1m"
    reset = "\033[0m"
    bold = "\033[1m"
    reset_colour = "\033[39m"
    underline = "\033[4m"

    FORMATS = {
        logging.DEBUG: grey,
        logging.INFO: grey,
        logging.WARNING: yellow,
        logging.ERROR: red,
        logging.CRITICAL: underline + red,
    }

    def __init__(self, debug: bool = False) -> None:
        super().__init__()

        self.debug = debug

    @override
    def format(self, record: logging.LogRecord) -> str:
        log_fmt: str = (
            f"{self.bold}{self.FORMATS[record.levelno]}%(levelname)s{self.reset_colour}{' (%(filename)s:%(lineno)d)' if self.debug else ''}: %(message)s"
        )
        return logging.Formatter(log_fmt).format(record)
