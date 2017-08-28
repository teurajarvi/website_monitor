# -*- coding: utf-8 -*-
# main.py
'''
This is the main of the mebsite_monitor
'''
import sys
sys.path.insert(0, sys.path[0]+'\\')

import logging
import logs.log
from controllers.monitor import monitor_pages

logging.info('main of the system_monitor started')
# start monitoring the web pages
monitor_pages()
logging.info('main of the system_monitor finished')

