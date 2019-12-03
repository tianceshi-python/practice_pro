# encoding:utf-8

import requests
import json

data = {
    'name':'germey',
    'age':22
}

response =requests.get('http://httpbin.org/get',params=data)
print(response.text)
print('....................................')
print(response.json())
print('....................................')
print(json.loads(response.text))
print('....................................')
print(type(response.json()))