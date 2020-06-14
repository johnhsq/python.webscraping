### Text file
from urllib.request import urlopen
textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
print("document is read as ASCII by default")
# print the first 100 char
print(textPage.read()[:100])
print("-"*100)
print("convert the document as utf-8")
print(str(textPage.read()[:100], 'utf-8'))


### Html file
from bs4 import BeautifulSoup
html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
print("="*100)
print("raw text")
print(content[:100])
# encoding the string as 'UTF-8'
content = bytes(content, 'UTF-8')
# decoding the string using 'UTF-8'
content = content.decode('UTF-8')
print(content[:100])


### CSV file
from io import StringIO
import csv
print("="*100)
# Retrieve the file as a string from the web, and wrap the string in a StringIO object so that it behaves like a file.
# no need to store the file in local file system
data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')
dataFile = StringIO(data)
# return as a list
csvReader = csv.reader(dataFile)
for row in csvReader:
    print('The album "'+row[0]+'" was released in '+str(row[1]))

print("="*100)
# return as a dictionary object
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile)
print(dictReader.fieldnames)
for row in dictReader:
    print(row)


### PDF
print("="*100)
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage
import io
import urllib.request
import requests


def pdf_to_text(pdf_file):
    text_memory_file = io.StringIO()

    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, text_memory_file, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # get first 3 pages of the pdf file
    for page in PDFPage.get_pages(pdf_file, pagenos=(0, 1, 2)):
        interpreter.process_page(page)
    text = text_memory_file.getvalue()
    text_memory_file.close()
    return text

# online pdf to text by requests
response = requests.get('http://pythonscraping.com/pages/warandpeace/chapter1.pdf')
pdf_memory_file = io.BytesIO()
pdf_memory_file.write(response.content)
print(pdf_to_text(pdf_memory_file))