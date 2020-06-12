# encoding:utf-8
# @Time    :2020.6.4
# @Author  :tian
# @File    :Assert.py
'''
获取case执行的数据
'''

import readExcel
import readConfig
import common.logPrintClass
import re


class get_parameter:
    def __init__(self):
        # 初始化log
        self.log = common.logPrintClass.Log()

    #获取基本参数header，enterpriseId，token
    def get_basicParam(self):
        header = readConfig.ReadConfig().get_header('header')
        enterpriseId = readConfig.ReadConfig().get_enterprise('enterpriseId')
        token = readConfig.ReadConfig().get_enterprise('token')

        self.log.info('header is: ' + header)
        self.log.info('enterpriseId is: ' + enterpriseId)
        self.log.info('token is: ' + token)


        return header,enterpriseId,token


    #从casedata的excel表种获取API请求的base_url
    def get_baseUrl(self,ExcelName,sheetName,apiName):
        base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', ExcelName,
                                                      sheetName)

        # print('ModifyMeetingInfo_base_url_list is:', ModifyMeetingInfo_base_url_list)
        for i in base_url_list:
            if i[0] == apiName:
                base_url = i[1]
                #print('base_url is:', base_url)

        return base_url






if __name__ == '__main__':

    para = get_parameter()
    print('apiName is: ' + para.get_baseUrl(ExcelName = 'conferenceControl_casedate.xlsx',sheetName = 'base_url',apiName = 'Invitation'))


