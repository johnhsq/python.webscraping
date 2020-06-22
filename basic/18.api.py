# https://realpython.com/python-requests/


# An API defines a standardized syntax that allows one piece of software to communicate with another piece of software

# use ip-api.com to get physical address of an IP
import requests

### Simple API call
ip="50.78.253.58"
service="http://ip-api.com/json/"
url = service+ip

response = requests.get(url)
if response:
    print('Success!')
    #response.encoding = 'utf-8'
    #print(response.headers)
    print(response.headers['Content-Type'])
    #print(response.content)
    print(response.json())
else:
    print('An error has occurred.')

print("="*100)
### API call with parameters
# params as a dict
params={'q': 'requests+language:python'}
# params as a list of tuple
# params=[('q', 'requests+language:python')]
# params as bytes
# params=b'q=requests+language:python'
# request headers
headers={'Accept': 'application/vnd.github.v3.text-match+json'}
response = requests.get(
    'https://api.github.com/search/repositories',
    params=params,
    headers=headers,
)

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  
print(f'Repository description: {repository["description"]}') 
print(f'Text matches: {repository["text_matches"]}')