"""Tests copy this script to a a temporary directory and then run it."""

from logging_configurator import configure_logging
import logging
import os.path


if __name__ == "__main__":
    configure_logging(
        os.path.join(os.path.dirname(__file__), "log.txt"), log_level="INFO", append=False, stdout_and_stderr=True
    )

    logger = logging.getLogger("logging_configurator_test")

    logger.info(111)
    logger.info(222)
    logger.warning(333)
    logger.error(444)
    raise ValueError(666)
