# encoding:utf-8
# @Time    :2020.6.4
# @Author  :tian
# @File    :Assert.py

'''
shortcall包括入会、发起录制、发起共享、停止共享、停止录制、退会
'''

import common.logPrintClass
from CloudVideoClass import conferenceControlClass,create_meetingClass,recordingVodsClass
import readConfig
from common import get_parameter
from common import Assert
import time




class shortcall:
    def __init__(self):
        #初始化log
        self.log = common.logPrintClass.Log()

        #获取基本参数header，enterpriseId，token
        self.header = readConfig.ReadConfig().get_header('header')
        self.enterpriseId = readConfig.ReadConfig().get_enterprise('enterpriseId')
        self.token = readConfig.ReadConfig().get_enterprise('token')

        # 实例化对象
        conferenceControlObj = conferenceControlClass.conferenceControlClass(self.header,self.enterpriseId,self.token)
        self.create_meetingObj = create_meetingClass.conferenceControlClass(self.header,self.enterpriseId,self.token)
        self.recordingVodsObj = recordingVodsClass.recordingVodsClass(self.header,self.enterpriseId,self.token)

        self.assertObj = common.Assert.Assertions()




    def shortcase(self):

        #从excel中读取参数
        get_parameterObj = get_parameter.get_parameter()
        callNumber = get_parameterObj.get_resBodyPara(ExcelName ='conferenceControl_casedate.xlsx',sheetName = 'data',Para = 'callNumber')[1]
        callNumber = str(int(callNumber))
        deviceNum_list = get_parameterObj.get_resBodyPara(ExcelName ='conferenceControl_casedate.xlsx',sheetName = 'data',Para = 'device_number')
        InvitationBase_url = get_parameterObj.get_baseUrl(ExcelName = 'conferenceControl_casedate.xlsx',sheetName = 'base_urll',apiName = 'Invitation')
        start_recording_url = get_parameterObj.get_baseUrl(ExcelName='recordingVods_casedata.xlsx',
                                                          sheetName='base_url', apiName='start_recording')
        stop_recording_url = get_parameterObj.get_baseUrl(ExcelName='recordingVods_casedata.xlsx',
                                                          sheetName='base_url', apiName='stop_recording')
        Querymeetingstatus_url = get_parameterObj.get_baseUrl(ExcelName = 'conferenceControl_casedate.xlsx',sheetName = 'base_urll',apiName = 'Querymeetingstatus')
        Kickoutmeeting_url = get_parameterObj.get_baseUrl(ExcelName = 'conferenceControl_casedate.xlsx',sheetName = 'base_urll',apiName = 'kickoutmeeting_url')


        #print('callNumber_list is: ',callNumber)
        #print('deviceNum_list is:',deviceNum_list[1:])
        deviceList = []
        for i in deviceNum_list[1:]:
            devicedic=  {'number': str(int(i))}
            deviceList.append(devicedic)
        print('deviceList is: ',deviceList)


        conferenceControlObj = conferenceControlClass.conferenceControlClass(self.header, self.enterpriseId, self.token)
        recordingVodsObj = recordingVodsClass.recordingVodsClass(self.header, self.enterpriseId, self.token)


        code,body = conferenceControlObj.Invitation(InvitationBase_url,callNumber,deviceList)
        self.assertObj.assert_code(code, expected_code=200)
        print('已经通过！！！')
        time.sleep(5)

        code, body = conferenceControlObj.QueryMeetingStatus(Querymeetingstatus_url, callNumber)
        print('body is: ',body)
        self.assertObj.assert_code(code, expected_code=200)
        print('已经通过！！！')
        time.sleep(5)


        print('开始录制。。。。')
        code, bidy = recordingVodsObj.start_recording(start_recording_url, callNumber)
        print('start_recording code is: ', code)
        time.sleep(20)
        self.assertObj.assert_code(code, expected_code=200)

        print('停止录制。。。。')
        code, bidy = recordingVodsObj.stop_recording(stop_recording_url, callNumber)
        print('start_recording code is: ', code)
        time.sleep(20)
        self.assertObj.assert_code(code, expected_code=200)

        print('踢出会议！！！')











if __name__ == '__main__':
    shortcall = shortcall()
    shortcall.shortcase()