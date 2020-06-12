from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print('The Page could not be found! {0}'.format(e))
        return None
    except URLError as e:
        print('The server could not be found! {0}'.format(e))
        return None
    
    try:
        ###
        # html.parser vs lxml vs html5lib
        # html.parser can only handle well organized html
        # lxml can handle html errors, faster than html.parser, fastest parser
        # html5lib can handle extreme messy html code, slowest parser
        # messy html, no worry about speed -> html5lib
        # messy html, speed is important -> lxml
        # clean html -> html.parser
        bs = BeautifulSoup(html.read(),'html.parser')
        title = bs.body.h1

        # the below "whatever" is hard to maintain
        # try to look for "Print this page" or "Mobile version", which has better-formated HTML
        # whatever = bs.find_all('table')[4].find_all('tr')[2].find('td').find_all('div')[1].find('a')
        # read CSS, which has better format and organized information than HTML
        nameList = bs.find_all('span', {'class':{'green','red'}})
        nameList = bs.find_all(class_='green')  # class is a reserved word in Python, so you will use "class_"
        for name in nameList:
            print(name.get_text() + "\n")
    except AttributeError as e:
        return None
    return title

def test_run():
    title=getTitle('https://johnhsq.github.io/01.page.html')
    if title == None:
        print('Title could not be found')
    else:
        print(title)

test_run()