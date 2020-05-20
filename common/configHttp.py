# encoding:utf-8

'''
json模块dumps、loads、dump、load介绍

1.json.dumps()用于将dict类型的数据转成str

json.dumps()参数解释：常用参数解释
indent：应该是一个非负的整型，如果是0，或者为空，则一行显示数据；否则会换行且按照indent的数量显示前面的空白
sort_keys：将数据根据keys的值进行排序

2.json.loads():用于将str类型的数据转成dict

3.json.dump()用于将dict类型的数据转成str，并写入到json文件中

4.json.load()用于从json文件中读取数据
'''


import requests
import json
from common import geturlParams


class RunMain():

    def send_post(self,url,data):     #定义一个方法，传入需要的url,和data
        # 参数必须按照url、data顺序传入
        result = requests.post(url = url ,data = data).json()   #因为这里要封装post方法，所以这里的url和data值不能写死
        print(result)
        res = json.dumps(result, ensure_ascii= False,sort_keys= True,indent= 2)   #json.dumps()用于将dict类型的数据转成str
        return res

    def send_get(self,url,data):
        result = requests.get(url = url,params=data).json()
        res = json.dumps(result, ensure_ascii= False,sort_keys= True,indent= 2)
        return res

    def send_put(self,url,data):
        result = requests.put(url = url,params=data).json()
        res = json.dumps(result, ensure_ascii= False,sort_keys= True,indent= 2)
        return res

    def run_main(self,methond,url= None,data = None):   #定义一个run_main函数，通过传过来的methond来进行不同的get和post
        result = None
        if methond == 'post':
            result = self.send_post(url,data)
        if methond == 'put':
            result = self.send_put(url,data)
        elif methond == 'get':
            result = self.send_get(url,data)
        else:
            print("methond值错误！！！！")
        return result



if __name__ == '__main__':
    requests_url = geturlParams.geturlParams().get_Url('invitation?')
    result1 = RunMain().run_main('put',url= requests_url,data =None )
    print(result1)
