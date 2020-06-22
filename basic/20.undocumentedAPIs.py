### undocumented APIs are usually used by the website to query additional data to rendor the page
# These APIs are not meant for public to use; but it is very useful for web scraping

### To find such APIs
# Chrome Developer Tools -> Network & Sources page to find these APIs
# They often have JSON or XML returns; you can use "Filter" in the network tab
# Type: xhr

### To document the APIs:
# HTTP method used
# Inputs
#   Path parameters
#   Headers (including cookies)
#   Body content (for PUT and POST calls)
# Outputs
#   Response headers (including cookies set)
#   Response body type
#   Response body fields

### Find and Document APIs automatically
# https://github.com/REMitchell/apiscraper
'''
apicall.py
Contains attributes that define an API call (path, parameters, etc.) as well as logic to decide whether two API calls are the same.
apiFinder.py
Main crawling class. Used by webservice.py and consoleservice.py to kick off the process of finding APIs.
browser.py
Has only three methods—initialize, get, and close—but encompasses relatively complicated functionality to tie together the BrowserMob Proxy server and Selenium. Scrolls through pages to ensure that the entire page is loaded, saves HTTP Archive (HAR) files to the appropriate location for processing.
consoleservice.py
Handles commands from the console and kicks off the main APIFinder class.
harParser.py
Parses HAR files and extracts API calls.
html_template.html
Provides a template to display API calls in the browser.

Download the BrowserMob Proxy binary files from https://bmp.lightbody.net/ and place the extracted files in the apiscraper project directory.

Download ChromeDriver and place this in the apiscraper project directory.

The following Python libraries required:
    tldextract
    selenium
    browsermob-proxy

Search a page on http://target.com for an API returning product data to populate the product page:
$ python consoleservice.py -u https://www.target.com/p/rogue-one-a-star-wars-\
story-blu-ray-dvd-digital-3-disc/-/A-52030319 -s "Rogue One: A Star Wars Story"

All collected data is stored as a HAR file, in the default directory /har in the project root
'''