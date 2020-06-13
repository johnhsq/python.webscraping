import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')

# the main table is the first table on the page
table = bs.find_all('table',{'class':'wikitable'})[0]
rows = table.find_all('tr')

csvFile = open('editors.csv','wt+', encoding='utf-8_sig')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        print("-"*100)
        for cell in row.find_all(['td','th']):
            print("|")
            print(cell.get_text(strip=True))
            csvRow.append(cell.get_text(strip=True))
        writer.writerow(csvRow)
finally:
    csvFile.close()