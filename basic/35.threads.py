from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

import _thread
import time

# for vistised links, no need to visit again
# it may have race conditions while two threads visit the same page at the same time. Ignore it for now
visited = []
def get_links(thread_name, bs):
    print('Getting links in {}'.format(thread_name))
    links = bs.find('div', {'id':'bodyContent'}).find_all('a',
        href=re.compile('^(/wiki/)((?!:).)*$'))
    return [link for link in links if link not in visited]

# Define a function for the thread
def scrape_article(thread_name, path):
    visited.append(path)
    html = urlopen('http://en.wikipedia.org{}'.format(path))
    # prevent from putting too much load to the server
    time.sleep(5)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1').get_text()
    print('Scraping {} in thread {}'.format(title, thread_name))
    links = get_links(thread_name, bs)
    if len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        scrape_article(thread_name, newArticle)

# Create two threads as follows
try:
   _thread.start_new_thread(scrape_article, ('Thread 1', '/wiki/Kevin_Bacon',))
   _thread.start_new_thread(scrape_article, ('Thread 2', '/wiki/Monty_Python',))
except:
   print ('Error: unable to start threads')

while 1:
    pass