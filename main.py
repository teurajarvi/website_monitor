# -*- coding: utf-8 -*-
# main.py
import sys
sys.path.insert(0, sys.path[0]+'\\controllers')

import logging
from monitor import monitor_pages

logging.basicConfig(filename='monitor.log', level=logging.INFO)
logging.info('main started')
monitor_pages()
logging.info('main finished')

