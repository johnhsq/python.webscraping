# optical character recognition, aka OCR

# Pillow performs the first pass, cleaning and filtering images,  
# Tesseract attempts to match the shapes found in those images to its library of known text.from PIL import Image, ImageFilter

### Pillow
from PIL import Image


### Tesseract
# install CMD tesseract 
# $ brew install tesseract
# $ export TESSDATA_PREFIX=/usr/local/share/tessdata
# use python wrapper pytesseract
import pytesseract
# convert image to string
print(pytesseract.image_to_string(Image.open('images/captcha.png')))
print("-"*10)
# estimate pixel locations for the boundaries of each character
print(pytesseract.image_to_boxes(Image.open('images/captcha.png')))
print("-"*10)
# return a complete output of all data, such as confidence scores, page and line numbers, box data, as well as other information
print(pytesseract.image_to_data(Image.open('images/captcha.png')))