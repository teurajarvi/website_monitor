# Definitions for website_monitor logging

import logging
logging.basicConfig(filename='monitor_log.log', format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p', level=logging.INFO)
