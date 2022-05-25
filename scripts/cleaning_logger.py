from asyncio.log import logger
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('../logs/data_cleaning.log')

file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)
