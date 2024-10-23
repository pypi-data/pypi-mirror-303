import urllib.request
import ssl
import json
import certifi

def get_request(url:str):
    context = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(url=url, context=context) as response:
        content = response.read()
    return content.decode('utf-8')






# json_data = json.loads(data)
# print(data)

# with open('html3.txt', 'w') as file:
#     file.write(data)