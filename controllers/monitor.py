# -*- coding: utf-8 -*-
# monitor.py
'''
This is the main controller of the website_monitor
'''

# Imports for all methods in package
import logging  #for adding the logs
import time     #for calculating the roundtrip time and setting sleep time

def get_page_with_text_content():
    '''
    Method for making a HTTP request to desired web page and
    counting the roundtrip time of the request-response.
    '''
    # for downloading the page with content
    import requests
    # for getting the User-Agent headers used in request
    from models.storage import get_headers, get_urls
	
    # get and set the headers for request
    headers = get_headers()
    print('headers: {!s}'.format(headers))
	
    print("start get_page_with_text_content")
    # Get the urls
    urls = get_urls()
	
    for (validation_text, url) in urls:
        response = None
		
	    # Get the web page content and record roundtrip time
        try:
            # Start interval timer to get roundtrip time of the HTTP request-response
            start = time.time()
            # Get the HTTP page with content
            response = requests.get(url, headers=headers)
            # Stop the interval timer and count the roundtrip time
            roundtrip = time.time() - start
		
	    # Exception handling for connection etc errors related to the HTTP request
        except requests.exceptions.HTTPError as e:
            msg = ('HTTPError URL {!s}, details: {!s}'.format(url, e.message))
            print(msg)
            logging.error(msg)
        except requests.exceptions.ConnectionError as e:
            msg = ('ConnectionError URL {!s}, details: {!s}'.format(url, e.message))
            print(msg)
            logging.error(msg)
        except requests.exceptions.Timeout as e:
            msg = ('Timeout URL {!s}, details: {!s}'.format(url, e.message))
            print(msg)
            logging.error(msg)
        except Exception as e:
            print e.message
            msg = ('CONNECTION ERROR from URL {!s}, details: {!s}'.format(url, e.message))
            print(msg)
            logging.error(msg)
		
        if response != None:
            validate_page_context(url=url, response=response, roundtrip=roundtrip, validation_text=validation_text)
			
    print("finish get_page_with_text_content")
	
    return

def validate_page_context(url, response, roundtrip, validation_text):
    '''
    Method for validating the page content. 
    The validation is based on user initialized string (text).
	
	If the text is found from the page the validation is passed.
	If the text is not found from the page the validation is failed.
    '''
    from bs4 import BeautifulSoup #for parsing the http response data

    print("start validate_page_context")
    # parse the downloaded homepage with all text content
    soup = BeautifulSoup(response.text, "lxml")

	# TODO: read the validation text from file. Text is set by the user or config
	
	# The log file contain the checked URLs, their status and the response times.
	# Validate the webpage content using the validation text.
    if str(soup).find(str(validation_text)) == -1:
        msg = ('Validation failed with HTTP status {!s} from {!s} with roundtrip {!s}'.format(response.status_code, url, roundtrip))
        print('Warning: ' + msg)
        logging.warning(msg)
        
		# Validate the webpage response using the HTTP status.
        if response.status_code != 200:
            msg = ('HTTP status {!s} from {!s} with roundtrip {!s}'.format(response.status_code, url, roundtrip))
            print('Error: ' + msg)
            logging.error(msg)
		
    # if validation text found page should be fine
    else:
        msg = ('Validation ok with HTTP status {!s} from {!s} with roundtrip {!s}'.format(response.status_code, url, roundtrip))
        print('info: ' + msg)
        logging.info(msg)
		
    print("finish validate_page_context")

def monitor_pages():
    '''
	Download a web page and try to find a validation text from the page content.
    Process will be repeated according to the time specified by the user or config.
    '''
    from models.storage import get_timeout
	
    logging.info('start monitor_pages')

    while True:
		
        get_page_with_text_content()
				
        # wait for user defined seconds,
        time.sleep(get_timeout())
        continue
