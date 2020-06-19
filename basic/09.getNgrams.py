from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

# splits the sentence into words, strips punctuation and whitespace, and removes single-character words besides I and a.
def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation+string.whitespace)
        for word in sentence]
    sentence = [word for word in sentence if len(word) > 1
        or (word.lower() == 'a' or word.lower() == 'i')]
    return sentence

# removes newlines and citations
# also splits the text into “sentences” based on the location of periods followed by a space
def cleanInput(content):
    content = re.sub('\n|[[\d+\]]', ' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    sentences = content.split('. ')
    return [cleanSentence(sentence) for sentence in sentences]

# get n-gram per sentence, which ensures that n-grams are not created that span multiple sentences.
def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

def getNgrams(content, n):
    content = cleanInput(content)
    ngrams = []
    for sentence in content:
        ngrams.extend(getNgramsFromSentence(sentence, n))
    return(ngrams)

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
ngrams = getNgrams(content, 2)
print(ngrams)
print('2-grams count is: '+str(len(ngrams)))