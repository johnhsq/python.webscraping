### Server side redirects:
# urllib library hands directs automatically. 
# Using requests library, set allow-redirects flag to True:
# r = requests.get('http://github.com', allow_redirects=True)


### Client side redirects:
# http://pythonscraping.com/pages/javascript/redirectDemo1.html 
# the page redirects after 2 seconds to
# http://pythonscraping.com/pages/javascript/redirectDemo2.html


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
import time

def waitForLoad(driver):
    elem = driver.find_element_by_tag_name('html')
    count = 0 
    while True:
        count += 1
        # time out after 10 seconds
        if count > 20:
            print('Timing out after 10 seconds and returning')
            return
        # check page every half second
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name('html')
        except StaleElementReferenceException:
            return

chrome_options = Options()
#chrome_options.add_argument('--headless')
driver = webdriver.Chrome(
    executable_path='drivers/chromedriver',
    options = chrome_options
)
driver.get('http://pythonscraping.com/pages/javascript/redirectDemo1.html')
waitForLoad(driver)
print(driver.page_source)


print("="*100)

### use WebDriverWait to do the same thing
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
try:
    bodyElement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH, '//body[contains(text(), "This is the page you are looking for!")]'
            )
        )
    )
    print(bodyElement.text)
except TimeoutException:
    print('Did not find the element')

driver.close()