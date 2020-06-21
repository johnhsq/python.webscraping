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