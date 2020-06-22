from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(
    executable_path='drivers/chromedriver',
    options=chrome_options
)
driver.get('http://www.wikipedia.com/')
driver.get_screenshot_as_file('images/wikipedia.png')