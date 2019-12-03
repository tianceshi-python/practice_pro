# encoding:utf-8

import requests

response =requests.get('http://httpbin.org/get?name=germey&age=22')
print(response.text)