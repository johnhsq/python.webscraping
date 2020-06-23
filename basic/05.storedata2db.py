from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import sqlite3
import re

db='/Users/huang/Documents/Workspace/python.webscraping/basic/scraping.db'
conn =sqlite3.connect(db)
print("opened sqlite3 database successfully")

random.seed(datetime.datetime.now())

### DB operation
# $ sqlite3
# sqlite> attach database '/Users/huang/Documents/Workspace/python.webscraping/basic/scraping.db' as scraping;
# sqlite> .database
# sqlite> .exit
# $ sqlite3 /Users/huang/Documents/Workspace/python.webscraping/basic/scraping.db
# sqlite> .database
# sqlite> CREATE TABLE pages (
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    title TEXT,
#    content TEXT,
#    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# sqlite> .tables
# sqlite> .schema pages

# insert a record into db table
def store(title, content):
    conn.execute('INSERT INTO pages (title, content) VALUES ("%s","%s")' % (title, content))
    conn.commit()

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org'+articleUrl)
    bs = BeautifulSoup(html,'html.parser')
    title = bs.find('h1').get_text(strip=True)
    content = bs.find('div',{'id':'mw-content-text'}).find('p').get_text(strip=True)
    store(title, content)
    return bs.find('div',{'id':'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:
    conn.close()
    print("closed sqlite3 database successfully")