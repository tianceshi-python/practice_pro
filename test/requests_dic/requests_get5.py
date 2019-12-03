# encoding:utf-8

import requests
import  json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}


response = requests.get('https://www.zhihu.com/explore',headers = headers)
print(response.text)