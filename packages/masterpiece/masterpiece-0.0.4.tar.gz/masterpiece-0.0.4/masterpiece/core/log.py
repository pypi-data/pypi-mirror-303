import argparse
import logging
import sys

class Log(logging.Logger):
    """Default logger for logging events to application log and/or to
    console."""


    def __init__(self, name, level=logging.DEBUG) -> None:
        """Creates and initializes default logger with the given name and
        logging level. Typically the name is the name of the application.

        Args:
            name: name of the logger
            level: logging level, the default is logging.DEBUG
        """
        super().__init__(name, level)

        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument(
            "-f", "--log_name", type=str, default=name, help="Name of the log file"
        )
        parser.add_argument(
            "-l", "--log_level", type=int, default=logging.INFO, help="Logging level"
        )
        args, remaining_argv = parser.parse_known_args()
        sys.argv = [sys.argv[0]] + remaining_argv

        # create logger
        logger = logging.getLogger(name)
        logger.setLevel(args.log_level)

        # log file
        file_formatter = logging.Formatter(
            "%(asctime)s [%(levelname)-5.5s]  %(message)-0.280s"
        )
        file_handler = logging.FileHandler(args.log_name)
        file_handler.setFormatter(file_formatter)
        self.addHandler(file_handler)

        # console
        console_formatter = logging.Formatter(
            "[%(levelname)-5.5s]  %(message)-0.280s"
        )
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(console_formatter)
        self.addHandler(console_handler)
