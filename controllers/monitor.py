# -*- coding: utf-8 -*-

# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Download an URL and try to find a validation text from the page.
# Process is logged.
# Process will be repeated according to the time specified in config.ini or by the user.

# while this is true (it is true by default),
while True:
    # set the urls
    url = "http://Google.com/"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text
    soup = BeautifulSoup(response.text, "lxml")

    # if the number of times the word "Google" occurs on the page is less than 1,
    if str(soup).find("Google") == -1:
        # wait 60 seconds,
        time.sleep(60)
        # continue with the script,
        continue

    # but if the word "Google" occurs any other number of times,
    else:
        # report incident to the log,
        msg = 'Subject: This is Chris\'s script talking, CHECK GOOGLE!'
        # Print the log
        print('Error: ' + msg)

        break
