# optical character recognition, aka OCR

# Pillow performs the first pass, cleaning and filtering images,  
# Tesseract attempts to match the shapes found in those images to its library of known text.from PIL import Image, ImageFilter

### Pillow
from PIL import Image

### Tesseract
import pytesseract
from pytesseract import Output
import numpy as np

def cleanFile(filePath, threshold):
    image = Image.open(filePath)

    # Using the Pillow library to create a threshold filter to get rid of the gray in the background, 
    # bring out the text, and make the image clearer for Tesseract to read.
    image = image.point(lambda x:0 if x < threshold else 255)
    return image

# Takes in the cleaned PIL image object and runs it through Tesseract. 
# It calculates the average confidence of each recognized string (weighted by the number of characters in the string),
# as well as the number of recognized characters
# return the average confidence and number of recognized charactors
def getConfidence(image):
    data = pytesseract.image_to_data(image, output_type=Output.DICT)
    text = data['text']
    confidences = []
    numChars = []
    for i in range(len(text)):
        if int(data['conf'][i]) > -1:
            confidences.append(data['conf'][i])
            numChars.append(len(text[i]))
    return np.average(confidences, weights=numChars), sum(numChars)

filePath = 'images/imageBad.png'

start = 80
step = 5
end = 200

largestNumChars=0
largestConfidence=0.0
bestThreshold=143   # 143 is the best guess
for threshold in range(start, end, step):
    image = cleanFile(filePath, threshold)
    scores = getConfidence(image)
    print("threshold: "+str(threshold)+", confidence: " + str(scores[0]) + " numChars "+str(scores[1]))
    if scores[1]>=largestNumChars and scores[0]>=largestConfidence:
        largestNumChars=scores[1]
        largestConfidence=scores[0]
        bestThreshold = threshold
print("Best Threshold is : "+str(bestThreshold))

# call tesseract to do OCR on the old image
print("Before the image enhancement, OCR reads:")
print(pytesseract.image_to_string(Image.open('images/imageBad.png')))
# call tesseract to do OCR on the newly created image
print("After the image enhancement, OCR reads:")
print(pytesseract.image_to_string(cleanFile(filePath,bestThreshold)))