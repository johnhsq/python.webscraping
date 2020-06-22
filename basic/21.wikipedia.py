from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all('a', 
        href=re.compile('^(/wiki/)((?!:).)*$'))

# searches for the contents of all links with the class mw-anonuserlink 
# (indicating an anonymous user with an IP address, rather than a username) and returns it as a set.
def getHistoryIPs(pageUrl):
    #Format of revision history pages is: 
    #http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace('/wiki/', '')
    historyUrl = 'http://en.wikipedia.org/w/index.php?title={}&action=history'.format(pageUrl)
    print('history url is: {}'.format(historyUrl))
    html = urlopen(historyUrl)
    bs = BeautifulSoup(html, 'html.parser')
    #finds only the links with class "mw-anonuserlink" which has IP addresses 
    #instead of usernames
    ipAddresses = bs.find_all('a', {'class':'mw-anonuserlink'})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

def getCountry(ipAddress):
    try:
        response = urlopen(
            'http://ip-api.com/json/{}'.format(ipAddress)).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get('country')

# starts by retrieving the histories of all Wikipedia articles linked to by the starting page 
# (in this case, the article on the Python programming language)
links = getLinks('/wiki/Python_(programming_language)')

while(len(links) > 0):
    for link in links:
        print('-'*20) 
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print('{} is from {}'.format(historyIP, country))
    # randomly selects a new starting page, and retrieves all revision history pages of articles linked to by that page. 
    # It will continue until it hits a page with no links.
    newLink = links[random.randint(0, len(links)-1)].attrs['href']
    links = getLinks(newLink)