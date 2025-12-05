from loguru import logger

from xutility import setup_logger

if __name__ == "__main__":
    setup_logger("test_logger", rotation=True)
    logger.info("Test log...")
