# website_monitor
Python  program that monitors web sites and reports their availability

Python 2.7.13 used (https://www.python.org/downloads/)

If using Windows remember to add the python to the path:
http://www.anthonydebarros.com/2015/08/16/setting-up-python-in-windows-10/

# How to install website_monitor:
Download website_monitor from https://github.com/teurajarvi/website_monitor as a zip file

Windows:
Unzip the website_monitor-master.zip to your hard drive:
Right click on .zip file, and click on "Extract All" in context menu. In "Extract Compressed (Zipped) Folders" dialog, enter or browse folder path where you want files to be extracted.

Run the following commands in terminal (cmd.exe):
>cd [root forder of the website_monitor]

>python setup.py install

Linux:
Unzip the wesite_monitor-master.zip to your hard drive:
>sudo apt-get install unzip

>unzip website_monitor-master.zip -d [destination_folder]

Run the following commands in terminal:
>cd [folder_website_monitor-master]

>python setup.py install --user
  
# Run the application with command:
Windows:
>main.py

Linux:
>python main.py

# Output and config
Check website_monitor output from the monitor_log.log file. 
Command line observation also available.
Change the application settings from the private/appconfig.ini file.

# More info
website_monitor requires the following python libraries:

1. requests (http://docs.python-requests.org/en/latest/)
"Requests is an elegant and simple HTTP library for Python".
How to install
Windows:
  >cd C:/Python27/Scripts
  
  >pip install requests

Linux:

  >pip install requests

2. beautifulsoup4 (https://pypi.python.org/pypi/beautifulsoup4)
"Beautiful Soup sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree."
How to install
Windows:
  >cd C:/Python27/Scripts
  
  >pip install beutifulsoup4

Linux:

  >pip install beutifulsoup4

3. lxml parser (http://lxml.de/installation.html)
"lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language."
How to install
Windows:
  >cd C:/Python27/Scripts
  
  >pip install lxml
  
Linux:

  >pip install lxml

4. configparser (https://docs.python.org/2/library/configparser.html)
"The ConfigParser class implements a basic configuration file parser language which provides a structure similar to what you would find on Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily."

How to install
Windows:
  >cd C:/Python27/Scripts
  
  >pip install configparser
  
Linux:

  >pip install configparser


