### Training Tesseract
# 1. save the image files in a local folder. Name the file with the solution, e.g ./captcha/4MmC3.jpg
# 2. create box file (4MmC3.box) to tell Tesseract what each character is and where it is in the image
#   4 15 26 33 55 0
#   M 38 13 67 45 0
#   m 79 15 101 26 0
#   C 111 33 136 60 0
#   3 147 17 176 45 0
#   the first letter is the "letter", the next four number is the coodinates of the box, the last letter is a "page number"
#   There are some online tool like Tesseract OCR Chopper can help.
# 3. back the image and box files
# https://github.com/REMitchell/tesseract-trainer


### Retriving CAPTCHAs and Submit it
# through http://www.pythonscraping.com/humans-only
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess
import requests
from PIL import Image
from PIL import ImageOps

def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = image.point(lambda x: 0 if x<143 else 255)
    borderImage = ImageOps.expand(image,border=20,fill='white')
    borderImage.save(imagePath)

html = urlopen('http://www.pythonscraping.com/humans-only')
bs = BeautifulSoup(html, 'html.parser')
#Gather prepopulated form values
imageLocation = bs.find('img', {'title': 'Image CAPTCHA'})['src']
formBuildId = bs.find('input', {'name':'form_build_id'})['value']
captchaSid = bs.find('input', {'name':'captcha_sid'})['value']
captchaToken = bs.find('input', {'name':'captcha_token'})['value']

captchaUrl = 'http://pythonscraping.com'+imageLocation
urlretrieve(captchaUrl, 'captcha.jpg')
cleanImage('captcha.jpg')
p = subprocess.Popen(['tesseract', 'captcha.jpg', 'captcha'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p.wait()
f = open('captcha.txt', 'r')

#Clean any whitespace characters
captchaResponse = f.read().replace(' ', '').replace('\n', '')
print('Captcha solution attempt: '+captchaResponse)

if len(captchaResponse) == 5:
    params = {'captcha_token':captchaToken, 'captcha_sid':captchaSid,   
              'form_id':'comment_node_page_form', 'form_build_id': formBuildId, 
              'captcha_response':captchaResponse, 'name':'Ryan Mitchell', 
              'subject': 'I come to seek the Grail', 
              'comment_body[und][0][value]': 
               '...and I am definitely not a bot'}
    r = requests.post('http://www.pythonscraping.com/comment/reply/10', 
                          data=params)
    responseObj = BeautifulSoup(r.text, 'html.parser')
    if responseObj.find('div', {'class':'messages'}) is not None:
        print(responseObj.find('div', {'class':'messages'}).get_text())
else:
    print('There was a problem reading the CAPTCHA correctly!')