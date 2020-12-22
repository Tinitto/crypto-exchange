import os
import logging

from dotenv import load_dotenv
load_dotenv()

from judah.utils.assets import get_asset_path
from judah.utils.logging import setup_rotating_file_logger

from app import start


if __name__ == '__main__':
    logger = logging.getLogger()
    setup_rotating_file_logger(file_path=get_asset_path('error.log'), logger=logger)
    logging.disable(getattr(logging, os.getenv('LOGGING_LEVEL_DISABLE', 'NOTSET')))

    start()
