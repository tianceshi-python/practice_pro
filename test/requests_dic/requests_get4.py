# encoding:utf-8
import requests
import json

response = requests.get('https://github.com/favicon.ico')
print(type(response.text),type(response.content))
print('.................................')
print(response.text)
print('.................................')
print(response.content)