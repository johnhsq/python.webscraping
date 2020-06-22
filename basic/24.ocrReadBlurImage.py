# optical character recognition, aka OCR

# Pillow performs the first pass, cleaning and filtering images,  
# Tesseract attempts to match the shapes found in those images to its library of known text.from PIL import Image, ImageFilter

### Pillow
from PIL import Image, ImageFilter

### Tesseract
import pytesseract

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    # Using the Pillow library to create a threshold filter to get rid of the gray in the background, 
    # bring out the text, and make the image clearer for Tesseract to read.
    image = image.point(lambda x:0 if x < 143 else 255)
    image.save(newFilePath)
    return image
image = cleanFile('images/imageBad.png','images/imageCleaned.png')

# call tesseract to do OCR on the old image
print("Before the image enhancement, OCR reads:")
print(pytesseract.image_to_string(Image.open('images/imageBad.png')))
# call tesseract to do OCR on the newly created image
print("After the image enhancement, OCR reads:")
print(pytesseract.image_to_string(image))