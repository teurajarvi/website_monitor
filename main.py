# -*- coding: utf-8 -*-
# main.py
'''
This is the main of the mebsite_monitor
'''
import sys
sys.path.insert(0, sys.path[0]+'\\')

import logging
from monitor import monitor_pages

logging.basicConfig(filename='monitor.log', level=logging.INFO)
logging.info('main of the system_monitor started')
monitor_pages()
logging.info('main of the system_monitor finished')

