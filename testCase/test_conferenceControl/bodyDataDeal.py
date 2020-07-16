# encoding:utf-8

import readExcel
import json


#从查询会议接口返回body中获取踢出会议的请求消息体
def get_disconnect_requstData(caseDirName1,caseDirName2,xls_name,sheet_name,case_name):

    caseBodyList = readExcel.readExcel().get_xls(caseDirName1,caseDirName2,xls_name,sheet_name)
    print('caseBodyList is:',caseBodyList)
    for i in caseBodyList:
        if i[0] == case_name:
            body = i[1]
    print('body is: ',body)

    deviceStatusList = json.loads(body)['deviceStatusList']
    print('deviceStatusList is: ', deviceStatusList)
    data = []
    for i in deviceStatusList:
        value = (i['device'])
        del value['participantId']
        del value['externalUserId']
        data.append(value)
        #print('value is: ', value)

    data = json.dumps(data)
    print('data is: ', data)



get_disconnect_requstData('testCase','casedata','conferenceControl_casedate.xlsx','responseData','test_QueryMeetingStatus001')