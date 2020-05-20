# encoding:utf-8

# -*- coding: UTF-8 -*-
import sys
sys.path.append('../')

import requests
from urllib.parse import urlparse
import re
import hashlib
import base64
import urllib
import hmac
import json

class Get_signature_url(object):
    def __init__(self,method,req_url,req_data,token):
        self.method = method
        self.req_url = req_url
        self.req_data = req_data
        self.token = token

    def parse_url(self):
        test1 = urllib.parse.urlparse(self.req_url)
        #去无值参数
        self.url = test1.scheme +'://'+test1.netloc + test1.path + '?' + urllib.parse.urlencode(urllib.parse.parse_qsl(test1.query))
        ttt = urllib.parse.parse_qs(test1.query)
        newdict = dict((x,ttt[x][0]) for x in ttt.keys())
        newdict_sort = sorted(newdict.items(), key=lambda e:e[0])
        new_query = urllib.parse.urlencode(newdict_sort)
        #适配wss
        if test1.scheme=='wss':
            API = re.split('/external/', test1.path)
        else:
            API = re.split('/v\d+/', test1.path)
        return API, new_query

    def hash_body(self):
        data_to_send = self.req_data[0:100]
        hash = hashlib.sha256()
        hash.update(data_to_send.encode("utf-8"))
        body = hash.digest()
        body_base64 = base64.b64encode(body)
        return body_base64

    def get_list(self):
        body_b64_temp = self.hash_body()
        body_b64 = body_b64_temp.decode()
        parse_url_reult = self.parse_url()
        parse_url_reult[0][1]
        ls = [self.method, parse_url_reult[0][1], parse_url_reult[1], body_b64]
        llist = '\n'.join(str(s) for s in ls if s not in ['NONE','NULL'])
        return llist

    def get_signature(self):
        llist = self.get_list()
        Hmac_sha256 = hmac.new(bytes(self.token, 'utf-8'), bytes(llist, 'utf-8'), digestmod=hashlib.sha256).digest()
        signature = urllib.parse.quote_plus(base64.b64encode(bytes(Hmac_sha256)))
        return signature

    def get_url(self):
        signature = self.get_signature()
        last_url = self.url + '&signature='+signature
        return last_url



# m = Meeting("20941037", "9005565260")
# print("token:                "+m.config.meeting_enterprise_token)
# print("extid:                "+m.config.meeting_ext_id)
# print("enterpriseid          "+m.config.meeting_enterprise_id)


# method = 'PUT'
# url = "http://cloud.xylink.com/api/rest/external/v1/conferenceControl/invitation?enterpriseId=1b1784bd484f734122a80915002a977681312f3e"
# data = {"callNumber": "9005565260", "deviceList": [{"number": "20941037"}]}
# token = "11db8813c2d616aac96c0e8c8ef409f13f8f229bde1ce88503db5eb22081f8df"
# headers_json = {'content-type': 'application/json', 'Connection': 'close'}
#
#
# res = requests_sig(method, url, data, token, verify=False, headers=headers_json)
# print(res.url)
# print(res.status_code)
# print(res.reason)

# enterpriseId="6d9cb3bc7556dd97467aabae448f037737a0ef7b"
# device_id="27311621"
# dial_num="9005151318"
# device_type="7"

# token="5d8e3d1ff6bd69a2c26bbfca361e7595d740bab8d8ff556529a4b687a95a00ef"
# jdata = ''
# print(jdata)
# url = " https://cloud.xylink.com/api/rest/external/v1/miniprogram/token?enterpriseId=6d9cb3bc7556dd97467aabae448f037737a0ef7b"
# testpre = Get_signature_url('PUT', url, jdata, token)
# sig = testpre.get_signature()
# print("123123123123123123")
# print(sig)


# print("---------------------------right try--------------------------------")
# header = {'Content-Type': 'application/json'}
# url = "https://cloud.xylink.com/api/rest/external/v1/conferenceControl/9005151318/disconnect?enterpriseId=6d9cb3bc7556dd97467aabae448f037737a0ef7b&signature=4VgT5FZxroE8DAzw%2FRrta7l%2BPj9EW7SwxFJt9tVNOsA%3D"
# res = requests.put(url=url,data=jdata,headers=header)
# print(res.url)
# print(res.status_code)
# print(res.text)
# class meetingreminders(unittest.TestCase):
#     @classmethod
#     def setUpClass(self):
#         self.enterpriseId = "62e1a68bda1c0d63e7a4921094664842d4971c7d"
#         self.ip = "dev.xylink.com"
#         self.token = "27eb0041c1a4a45eecc70967baad2f5b66fdb707d1ce3bfaf2a6adc3d2620059"
#         self.headers_json = {'content-type': 'application/json','Connection':'close'}

#     def test_querry_reminders(self):
#         start_time = (int(time.time()) + 110) * 1000
#         end_time = start_time + 600000
#         end_time2 = end_time + 100000
#         url_meetingreminders_creat = 'https://' + self.ip + conf_meetingreminders_creat[
#             'uri'] + '?enterpriseId=' + self.enterpriseId

#         data = {
#             "title": "小欣红月录制测试预约会议室",
#             "startTime": start_time,
#             "endTime": end_time,
#             "address": "发生发生",
#             "details": "第三个是德国阿萨的公司的给",
#             "autoInvite": 1,
#             "meetingRoomType": 2,
#             "autoRecord": 1,
#             "enableOffLineRecord": 1,
#             "offlineTranscodePriority": "high"
#         }
#         data["participants"] = ['18777777777']
#         data["password"] = ""
#         data["conferenceControlPassword"] = "123456"
#         data["conferenceNumber"] = "9005806947"

#         a=requests_sig(conf_meetingreminders_creat['method'], url_meetingreminders_creat, data,
#                                               self.token, verify=False, headers=self.headers_json)
#         print(a.status_code)
#         print(a.url)
#         import pdb
#         pdb.set_trace()


# if __name__ == '__main__':
#     unittest.main()