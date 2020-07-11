# encoding:utf-8
from testCase.test_conferenceControl.test_conferenceControl_QueryMeetingStatus import Test_conferenceControl_QueryMeetingStatus
import pytest
import json


#从查询会议接口返回body中获取踢出会议的请求消息体
def get_disconnect_requstData():
    obj = Test_conferenceControl_QueryMeetingStatus()
    body = obj.test_QueryMeetingStatus001()
    print('body type is: ', type(body))
    deviceStatusList = json.loads(body)['deviceStatusList']
    print('deviceStatusList is: ', deviceStatusList)
    data = []
    for i in deviceStatusList:
        value = (i['device'])
        del value['participantId']
        del value['participantNumber']
        data.append(value)
        #print('value is: ', value)

    data = json.dumps(data)
    print('data is: ', data)



get_disconnect_requstData()