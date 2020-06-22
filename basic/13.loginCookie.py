### login
# login form: http://pythonscraping.com/pages/cookies/login.html
# the user can be anything; while the password must be "password"
# the form processor: http://pythonscraping.com/pages/cookies/welcome.php


import requests

### Login form
# <form method="post" action="welcome.php">
#   Username (use anything!): <input type="text" name="username"><br>
#   Password (try "password"): <input type="password" name="password"><br>
#   <input type="submit" value="Login">
# </form>
### 

# a basic solution to use requests.cookie
params = {'username': 'johnhsq', 'password': 'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
print('Cookie is set to:')
print(r.cookies.get_dict())
print('Going to profile page...')
# the welcome.php requires cookies to be set before you can access the page
r = requests.get('http://pythonscraping.com/pages/cookies/welcome.php', 
                 cookies=r.cookies)
print(r.text)


print("-"*100)
# http://www.editthiscookie.com/ is a Chrome extension to help you analyze the site cookie usage
# Requests library will be unable to handle many cookies produced by modern tracking software, such as Google Analytics, which are set only after the execution of javascripts.
# Selenium and Chrome WebDrivers have to be used
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(
    executable_path='drivers/chromedriver', 
    options=chrome_options)
driver.get('http://pythonscraping.com')
driver.implicitly_wait(1)
# print the cookies
savedCookies = driver.get_cookies()
print(savedCookies)

# To manipulate cookies, you can call the delete_cookie(), add_cookie(), and delete_all_cookies() functions. 
driver2 = webdriver.Chrome(
    executable_path='drivers/chromedriver',
    options=chrome_options)

driver2.get('http://pythonscraping.com')
driver2.delete_all_cookies()
# use the previously saved cookies for this scraper
# According to Google Analytics, this second webdriver is now identical to the first one, 
# and they will be tracked in the same way. 
# If the first webdriver was logged into a site, the second webdriver will be as well.
for cookie in savedCookies:
    driver2.add_cookie(cookie)

driver2.get('http://pythonscraping.com')
driver.implicitly_wait(1)
print(driver2.get_cookies())