# encoding:utf-8
'''
response属性
'''

import requests
import json

response = requests.get('http://httpbin.org/get')
print(type(response.status_code),response.status_code)
print(type(response.headers),response.headers)
print(type(response.cookies),response.cookies)
print(type(response.url),response.url)
print(type(response.history),response.history)
