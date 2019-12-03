# encoding:utf-8
'''
post  简单使用方法
'''
import  requests
import json


data = {'name':'germey','age':22}
response = requests.post('http://httpbin.org/post',data = data)
print(response.text)
print('*****************************')
print(response.json())