import logging
import os
from logging import Formatter


class EmojiFormatter(Formatter):
    def __init__(self, rank, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rank = rank
        self.rank_emoji = self._get_rank_emoji(rank)

    def _get_rank_emoji(self, rank):
        if rank == 0:
            return "[0️⃣ ]"
        elif rank == 1:
            return "[1️⃣ ]"
        elif rank == "Proxy":
            return "[🅿️ ]"
        elif rank == 2:  # Assuming this is for the Trusted Third Party
            return "[🔐]"
        else:
            return ""  # Default case

    def _get_level_emoji(self, level):
        if level == logging.DEBUG:
            return "[🐞]"  # Debug (bug)
        elif level == logging.INFO:
            return "[ℹ️ ]"  # Info
        elif level == logging.WARNING:
            return "[🚨]"  # Warning
        elif level == logging.ERROR:
            return "[❌]"  # Error
        elif level == logging.CRITICAL:
            return "[🔥]"  # Critical (siren)
        else:
            return ""  # Default case

    def format(self, record):
        level_emoji = self._get_level_emoji(record.levelno)
        return f"{level_emoji}{self.rank_emoji}{super().format(record)}"


def setup_logger(rank, logging_level=logging.INFO):
    # Set logging level based on AIVM_LOG environment variable
    aivm_log = os.environ.get("AIVM_LOG", None)
    if aivm_log:
        logging_level = getattr(logging, aivm_log.upper(), logging.INFO)
    else:
        # Fallback logic for RANK environment variable
        if "RANK" in os.environ and os.environ["RANK"] != "0":
            logging_level = logging.CRITICAL
        else:
            logging_level = logging.INFO

    # Set up the root logger
    logger = logging.getLogger()
    logger.setLevel(logging_level)

    # Remove any existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Create console handler and set level to INFO
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Create formatter
    formatter = EmojiFormatter(rank, "%(message)s")

    # Add formatter to ch
    ch.setFormatter(formatter)

    # Add ch to logger
    logger.addHandler(ch)

    return logger
