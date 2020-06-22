import time
from urllib.request import urlretrieve
from PIL import Image
import pytesseract
from selenium import webdriver
import subprocess

def getImageText(imageUrl):
    urlretrieve(image, 'page.jpg')
    # call tesseract command in your local system to process
    p = subprocess.Popen(['tesseract','page.jpg','page'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
        )
    p.wait()
    f = open('page.txt','r')
    print(f.read())

# create new Selenium driver
driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
driver.get('https://www.amazon.com/Death-Ivan-Ilyich-Nikolayevich-Tolstoy/dp/1427027277')
time.sleep(2)

# click on the book preview button
driver.find_element_by_id('imgBlkFront').click()
imageList = []

# wait for the page to load
time.sleep(5)

while 'pointer' in driver.find_element_by_id('sitbReaderRightPageTurner').get_attribute('style'):
    # while the right arrow is available for clicking, turn through pages
    driver.find_element_by_id('sitbReaderRightPageTurner').click()
    time.sleep(2)
    # get any new pages that have loaded(multiple pges can load at once,)
    # but duplicates will not be added to a set)
    pages = driver.find_elements_by_xpath('//div[@class=\'pageImage\']/div/img')
    if not len(pages):
        print('No pages found')
    for page in pages:
        image = page.get_attribute('src')
        print('Found image: {}'.format(image))
        if image not in imageList:
            imageList.append(image)
            getImageText(image)

driver.quit()