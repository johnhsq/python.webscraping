### TOR
# download and install TOR from https://www.torproject.org/download/
# $ brew install tor

# TOR tutorial: 
# https://www.youtube.com/watch?v=KDsmVH7eJCs
# https://www.sylvaindurand.org/use-tor-with-python/
# https://techmonger.github.io/68/tor-new-ip-python/


### PySocks with TOR
import socks
import socket
from urllib.request import urlopen

# The Tor service must be running on port 9150 (the default port) while running this code
socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
# http://icanhazip.com displays only the IP address for the client connecting to the server 
# and can be useful for testing purposes. 
# When this script is run, it should display an IP address that is not your own.
print(urlopen('http://icanhazip.com').read())


### Selenium with TOR
# Tor is currently running and add the optional proxy-server chrome option, 
# specifying that Selenium should connect on the socks5 protocol on port 9150
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:9150")
driver = webdriver.Chrome(executable_path='drivers/chromedriver',
                          options=chrome_options)

driver.get('http://icanhazip.com')
print(driver.page_source)
driver.close()