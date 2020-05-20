# encoding:utf-8
import requests
import json
import time

#######################################################
# 配置文件
from common.signature import Get_signature_url

enterpriseId = "2bc382f16515877abf19ba8bbf9d5e215fe7bf12"
token = "a3ee00129513ec79fc4d1d0f8c82d202d3f1183d79ebaefc4eee8749996e1052"
device_num = "18710881114"
device_id = "21548116"
device_type = "5"
meeting_room="9005814904"
#######################################################
header = {"Content-Type": "application/json"}


count = 0

while True:
    # 邀请入会
    invite_url = "https://sdk.xylink.com/api/rest/external/v1/conferenceControl/invitation?enterpriseId="+enterpriseId
    data = {
    "callNumber": meeting_room,
    "deviceList":[{"number":device_num}]}
    jdata = json.dumps(data)
    obj = Get_signature_url(method=str.upper("put"), req_url=invite_url, req_data=jdata, token=token)
    invite_last_url = obj.get_url()
    res = requests.put(invite_last_url,data=jdata,headers=header)
    print(res.status_code)
    print(res.url)
    print(res.text)

    time.sleep(5)

    # 录制
    recording_url = "https://sdk.xylink.com/api/rest/external/v1/meeting/recording/"+meeting_room+"/start?enterpriseId="+enterpriseId
    jdata=""
    obj = Get_signature_url(method=str.upper("get"), req_url=recording_url, req_data=jdata, token=token)
    recording_last_url = obj.get_url()
    res = requests.get(recording_last_url,data=jdata,headers=header)
    print(res.status_code)
    print(res.url)
    print(res.text)

    time.sleep(5)

    # 停止录制
    recording_url = "https://sdk.xylink.com/api/rest/external/v2/meeting/recording/"+meeting_room+"/stopWithSessionId?enterpriseId="+enterpriseId
    jdata=""
    obj = Get_signature_url(method=str.upper("get"), req_url=recording_url, req_data=jdata, token=token)
    recording_last_url = obj.get_url()
    res = requests.get(recording_last_url,data=jdata,headers=header)
    print(res.status_code)
    print(res.url)
    print(res.text)

    time.sleep(3)



    # 退会
    kick_url ="https://sdk.xylink.com/api/rest/external/v1/conferenceControl/"+meeting_room+"/disconnect?enterpriseId="+enterpriseId
    data=[{"id":device_id,"type":device_type}]
    jdata = json.dumps(data)
    obj = Get_signature_url(method=str.upper("put"), req_url=kick_url, req_data=jdata, token=token)
    kick_last_url = obj.get_url()
    res = requests.put(kick_last_url,data=jdata,headers=header)
    print(res.status_code)
    print(res.url)
    print(res.text)

    time.sleep(5)
    count += 1
    print('*' * 15)
    print("第", end="")
    print(count, end="")
    print("次")
    print('*' * 15)
