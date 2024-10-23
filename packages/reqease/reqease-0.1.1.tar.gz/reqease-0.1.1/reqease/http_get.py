import urllib.request
import ssl
import certifi
from dataclasses import dataclass
import json

@dataclass
class Response:
    status_code:int
    headers:list
    body_bytes: bytes
    body_str:str

def get(url:str) -> Response:
    context = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(url=url, context=context) as response:
        body_bytes = response.read()
        return Response(response.getcode(),
                        response.getheaders(),
                        body_bytes,
                        body_bytes.decode('utf-8'))

def save_to_file(url:str, file_path:str) -> None:
    response = get(url)
    with open(file_path,'w') as file:
        file.write(response.body_str)

def loads_to_json(url:str):
    response = get(url)
    json_object = json.loads(response.body_str)
    return json_object