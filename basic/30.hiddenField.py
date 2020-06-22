# http://pythonscraping.com/pages/itsatrap.html
'''
<html>
<head> 
    <title>A bot-proof form</title>
</head>
<style>
    body { 
        overflow-x:hidden;
    }
    .customHidden { 
        position:absolute; 
        right:50000px;
    }
</style>
<body> 
    <h2>A bot-proof form</h2>
    <a href=
     "http://pythonscraping.com/dontgohere" style="display:none;">Go here!</a>
    <a href="http://pythonscraping.com">Click me!</a>
    <form>
        <input type="hidden" name="phone" value="valueShouldNotBeModified"/><p/>
        <input type="text" name="email" class="customHidden" 
                  value="intentionallyBlank"/><p/>
        <input type="text" name="firstName"/><p/>
        <input type="text" name="lastName"/><p/>
        <input type="submit" value="Submit"/><p/>
   </form>
</body>
</html>
'''
# the above page has 3 hidden fields with different hidden methods
# The first link is hidden with a simple CSS display:none attribute.
# The phone field is a hidden input field.
# The email field is hidden by moving it 50,000 pixels to the right (presumably off the screen of everyone’s monitors) and hiding the telltale scroll bar.

# Selenium is able to distinguish between elements that are visually present on the page and those that aren’t. 
# Whether the element is present on the page can be determined by the is_displayed() function.
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(
    executable_path='drivers/chromedriver',
    options=chrome_options)
driver.get('http://pythonscraping.com/pages/itsatrap.html')
links = driver.find_elements_by_tag_name('a')
for link in links:
    if not link.is_displayed():
        print('The link {} is a trap'.format(link.get_attribute('href')))

fields = driver.find_elements_by_tag_name('input')
for field in fields:
    if not field.is_displayed():
        print('Do not change value of {}'.format(field.get_attribute('name')))