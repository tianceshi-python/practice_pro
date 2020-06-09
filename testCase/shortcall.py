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




    def shortcase(self):

        #从excel中读取参数
        get_parameterObj = get_parameter.get_parameter()
        callNumber = get_parameterObj.get_resBodyPara(ExcelName ='conferenceControl_casedate.xlsx',sheetName = 'data',Para = 'callNumber')[1]
        callNumber = str(int(callNumber))
        deviceNum_list = get_parameterObj.get_resBodyPara(ExcelName ='conferenceControl_casedate.xlsx',sheetName = 'data',Para = 'device_number')
        InvitationBase_url = get_parameterObj.get_baseUrl(ExcelName = 'conferenceControl_casedate.xlsx',sheetName = 'base_urll',apiName = 'Invitation')
        print('callNumber_list is: ',callNumber)
        print('InvitationBase_url is: ',InvitationBase_url)
        #print('deviceNum_list is:',deviceNum_list[1:])
        deviceList = []
        for i in deviceNum_list[1:]:
            devicedic=  {'number': str(int(i))}
            deviceList.append(devicedic)
        print('deviceList is: ',deviceList)


        conferenceControlObj = conferenceControlClass.conferenceControlClass(self.header, self.enterpriseId, self.token)
        code,body = conferenceControlObj.Invitation(InvitationBase_url,callNumber,deviceList)
        print('code is: ',code)
        print('body is: ',body)





if __name__ == '__main__':
    shortcall = shortcall()
    shortcall.shortcase()