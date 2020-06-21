import requests

### To see what exactly been sent through Form, you can do
# Open "Developer Tool" in the browser
# Go to "Network"
# Submit the form
# click the web page in "Name" tab, e.g. "procssing.php" from the example
# click "Headers"
# scroll down to the "Form Data" section


### To fill in a webform like:
# url: http://pythonscraping.com/pages/files/form.html 
# <form method="post" action="processing.php">
# First name: <input type="text" name="firstname"><br>
# Last name: <input type="text" name="lastname"><br>
# <input type="submit" value="Submit">
# </form>
###

### The params work for 
# text, radio button, checkbox and other inputs
params = {'firstname':'John', 'lastname':'Huang'}
r = requests.post(
    # this url is the "Action" of the form, not necessary the same as the web page url
    "http://pythonscraping.com/pages/files/processing.php",
    data = params
)
print(r.text)


### submitting files or images
# url: http://pythonscraping/pages/files/form2.html
# <form action="processing2.php" method="post" enctype="multipart/form-data">
#  Submit a jpg, png, or gif: <input type="file" name="uploadFile"><br>
#  <input type="submit" value="Upload File">
# </form>
import requests

files = {'uploadFile': open('./editors.csv', 'rb')}
r = requests.post(
    'http://pythonscraping.com/pages/files/processing2.php', 
    files=files)
print(r.text)