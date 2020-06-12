import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = './downloaded'
baseUrl = 'https://pythonscraping.com'

# baseUrl: the main url to be scraped, e.g https://wikipedia.com
# source: the <src> tag in the baseUrl page, e.g. /img/image.jpg
# return: "https://<domain>/source", e.g. https://wikipedia.com/img/image.jpg
def getAbsoluteURL(baseUrl, source):
    # replace 'http:' with 'https:'
    source=source.replace('http:','https:')
    if source.startswith('https://www.'):
        # change "https://www.<anything>" to "http://<anything>"
        url='https://{}'.format(source[12:])
    elif source.startswith('https://'):
        url=source
    elif source.startswith('www.'):
        url=source[4:]
        url='https://{}'.format(source)
    else:
        url='{}/{}'.format(baseUrl, source)
    # if the file is from another domain, return None
    if baseUrl not in url:
        return None
    return url

# baseUrl: the main url to be scraped, e.g. https://wikipedia.com
# aboluteUrl: the src url with full domain url, e.g. https://wikipedia.com/img/image.jpg
# downloadDirectory: the local folder where you want to store the files
# return: the folder created
def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace('www.','')
    path = path.replace(baseUrl,'')
    path = downloadDirectory+path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

html = urlopen(baseUrl)
bs = BeautifulSoup(html,'html.parser')
downloadList = bs.find_all(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl+" downloaded")
        # download the file from fileUrl and store in local folder
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))