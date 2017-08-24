# -*- coding: utf-8 -*-
# monitor.py

# Imports
import requests               #for download the page
import logging                #for adding the logs
import logs
from bs4 import BeautifulSoup #for parsing the http response data
import time                   #for adding the delay

def monitor_pages():
    '''Download a web page and try to find a validation text from the page content.
       Process will be repeated according to the time specified by the user or config.
    '''
    logging.info('start monitor_pages')
    # set the headers for request
    headers = {'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
    print('headers: {!s}'.format(headers))
    logging.info('headers: {!s}'.format(headers))
    while True:
        # set the urls
        # TODO: read the URLs from file. URL is set by the user or config
        #url = "http://www.Google.com/"
        #url = "http://www.yle.fi/"
        url = "http://www.kaleva.fi/"		
        #url = "http://www.fdkfjjdsaföjasöf.fi/"
		
	    # download the homepage
        response = None
        try:
            start = time.time()
            response = requests.get(url, headers=headers)
            roundtrip = time.time() - start
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
            # parse the downloaded homepage and grab all text
            soup = BeautifulSoup(response.text, "lxml")

            # if the number of times the word "Google" occurs on the page is less than 1
		    # TODO: read the validation text from file. Text is set by the user or config
		
		    # The log file contain the checked URLs, their status and the response times.
		    # Validating the webpage content
            if str(soup).find("Yle") == -1:
                msg = ('Validation failed for {!s} with HTTP status {!s} with roundtrip {!s}'.format(url, response.status_code, roundtrip))
                print('Warning: ' + msg)
                logging.warning(msg)
                if response.status_code != 200:
                    msg = ('HTTP STATUS {!s} from URL {!s} with roundtrip {!s}'.format(response.status_code, url, roundtrip))
                    print('Error: ' + msg)
                    logging.error(msg)

            # but if the word "Google" occurs any other number of times
            else:
                # we are fine
                msg = ('Validation ok with HTTP status {!s} from URL {!s} with roundtrip {!s}'.format(response.status_code, url, roundtrip))
                # Print the log
                print('info: ' + msg)
                logging.info(msg)
				
        # wait 5 seconds,
        time.sleep(5)
        # continue with the script
        continue
