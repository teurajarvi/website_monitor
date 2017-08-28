# -*- coding: utf-8 -*-
# storage.py
	
def get_headers():
    '''
    Read User-Agent header value
    '''
    print("start get_headers")
    headers = {'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
    print("finish get_headers")
    return headers
	
def get_urls():
    '''
    Read URLs by validation text from appconfig.ini
    '''
    import configparser
    config = configparser.ConfigParser()
    config.read("./private/appconfig.ini")
    print("start get_urls")
    URLs = config.items('URLS')
    print("finish get_urls")
    return URLs

def get_timeout():
    '''
    Read timeout/sleep value from appconfig.ini
    '''
    import configparser
    config = configparser.ConfigParser()
    config.read("./private/appconfig.ini")
    print("start get_timeout")
    timeout = int(config.get('MONITOR_TIMERS', 'MONITOR_SLEEP_TIMEOUT'))
    print("finish get_timeout")
    return timeout
