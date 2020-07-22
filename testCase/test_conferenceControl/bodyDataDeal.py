# encoding:utf-8

'''
处理上个case运行返回的body体，作为下个case运行的输入body体
'''


import readExcel
import json


#从查询会议接口返回body中获取踢出会议的请求消息体
def deal_QueryMeetingStatusReaponseData(caseDirName1,caseDirName2,xls_name,sheet_name,case_name):

    caseBodyList = readExcel.readExcel().get_xls(caseDirName1,caseDirName2,xls_name,sheet_name)
    #print('caseBodyList is:',caseBodyList)
    for i in caseBodyList:
        if i[0] == case_name:
            body = i[1]
    #print('body is: ',body)

    deviceStatusList = json.loads(body)['deviceStatusList']
    #print('deviceStatusList is: ', deviceStatusList)
    participantNumberList = []
    dive_data = []
    if deviceStatusList is None:
        pass
    else:
        for i in deviceStatusList:
            value = (i['device'])
            participantNumber = i['device']["participantNumber"]
            del value['participantId']
            del value['externalUserId']
            dive_data.append(value)
            #print('value is: ', value)
            participantNumberList.append(participantNumber)


    data = json.dumps(dive_data)
    #print('data is: ', data)
    #print('participantNumberList is: ',participantNumberList)
    return data,participantNumberList



deal_QueryMeetingStatusReaponseData('testCase','casedata','conferenceControl_casedate.xlsx','responseData','test_QueryMeetingStatus001')