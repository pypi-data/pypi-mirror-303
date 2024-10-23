import logging
import sys

logger = logging.getLogger('notion_automation')
logger.setLevel(logging.DEBUG)

c_handler = logging.StreamHandler(sys.stdout)
f_handler = logging.FileHandler('notion_automation.log')
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.DEBUG)

c_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)
