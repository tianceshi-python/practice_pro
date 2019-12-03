# encoding:utf-8

'''
使用 Requests 模块，上传文件也是如此简单的，文件的类型会自动进行处理
'''

import requests
files = {'file':open('cokie.txt','rb')}
response = requests.post('http://httpbin.org/post',files =files )
print(response.text)