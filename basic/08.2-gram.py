from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# takes in an input string, splits it into a sequence of words (assuming all words are separated by spaces), 
# and adds the n-gram (in this case, a 2-gram) that each word starts into an array.
def getNgrams(content, n):
    # replace escape characters (such as \n) with a space; removes citations like [123]
    content = re.sub('\n|[[\d+\]]', ' ', content)
    # remove any Unicode characters
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    
    content = content.split(' ')
    content = [word for word in content if word != '']
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
ngrams = getNgrams(content, 2)
print(ngrams)
print('2-grams count is: '+str(len(ngrams)))