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

# a better solution to use requests.session;
# it's better because you don't need to deal with cookies directly
# Session object keeps track of session information, such as cookies, headers, protocols, etc.
session = requests.Session()
params = {'username': 'johnhsq', 'password': 'password'}
s = session.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
print('Cookie is set to:')
print(s.cookies.get_dict())
print('Going to profile page...')
s = session.get('http://pythonscraping.com/pages/cookies/welcome.php')
print(s.text)