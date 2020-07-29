# encoding:utf-8


'''
处理上个case运行返回的body体，作为下个case运行的输入body体
'''

import readExcel
import json

#从停止录制接口返回body中获取sessionId
def deal_StopRecordingReaponseData(caseDirName1,caseDirName2,xls_name,sheet_name,case_name):

    caseBodyList = readExcel.readExcel().get_xls(caseDirName1,caseDirName2,xls_name,sheet_name)
    #print('caseBodyList is:',caseBodyList)
    for i in caseBodyList:
        if i[0] == case_name:
            body = i[1]
    #print('body is: ',body)

    body = json.loads(body)
    sessionId = body['sessionId']
    print('sessionId is: ',sessionId)
    return sessionId



deal_StopRecordingReaponseData('testCase','casedata','recordingVods_casedata.xlsx','responseData','test_StopRecording001')