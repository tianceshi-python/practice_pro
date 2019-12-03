# encoding:utf-8
'''
当需要cookie时，直接调用response.cookie:(response为请求后的返回值)
'''

import requests

response = requests.get('https://www.baidu.com')
print(response.cookies)
print('************************')
for key,value in response.cookies.items():
    print(key + '=' + value)