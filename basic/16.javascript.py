### http://pythonscraping.com/pages/javascript/ajaxDemo.html
# This page contains some sample text, hardcoded into the page’s HTML, that is replaced by Ajax-generated content after a two-second delay. 


### The WebDriver object is a bit like a browser in that it can load websites, 
# but it can also be used like a BeautifulSoup object to find page elements, 
# interact with elements on the page (send text, click, etc.), and do other actions to drive the web scrapers.

### before run this code, download ChromeDriver based on your Chrome Version
# http://chromedriver.chromium.org/downloads
# and store it in your local folder: $ mkdir -p ./drivers/
# $ cd ./drivers 
# $ xattr -d com.apple.quarantine chromedriver # enable security and privacy compliance to Mac
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# using the --headless option in order to make the WebDriver run in the background (memory without showing a web browser)
# use headless mode in production; 
# use non-headeless mode for trouble shooting, debuging in web browser developer tool
chrome_options = Options()
# chrome_options.add_argument('--headless')
# creates a new Selenium WebDriver, using the Chrome library
driver = webdriver.Chrome(executable_path='drivers/chromedriver', options=chrome_options)
# tells the WebDriver to load a page and then pauses execution for three seconds 
# before looking at the page to retrieve the (hopefully loaded) content.
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
try:
    # wait 10 seconds or until get 'loadedButton'
    # "Locators" are not the same as selectors. A locator is an abstract query language, 
    # using the "By" object, which can be used in a variety of ways, including to make selectors.
    # driver.find_element(By.ID, 'content').text
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'loadedButton')))
finally:
    # Selenium Selectors:
    # driver.find_element_by_css_selector('#content')
    # driver.find_element_by_tag_name('div')
    print(driver.find_element_by_id('content').text)
    # if you prefer BeautifulSoup to parse the page
    # pageSource = driver.page_source
    # bs = BeautifulSoup(pageSource, 'html.parser')
    # print(bs.find(id='content').get_text())
    driver.close()