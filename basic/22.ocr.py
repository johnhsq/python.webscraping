# optical character recognition, aka OCR

# Pillow performs the first pass, cleaning and filtering images,  
# Tesseract attempts to match the shapes found in those images to its library of known text.from PIL import Image, ImageFilter

###
# the image kitten.jpg will open in your default image viewer 
# with a blur added to it and will also be saved in its blurrier state as kitten_blurred.jpg in the same directory
from PIL import Image, ImageFilter
kitten = Image.open('images/kitten.jpg')
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save('images/kitten_blurred.jpg')
blurryKitten.show()