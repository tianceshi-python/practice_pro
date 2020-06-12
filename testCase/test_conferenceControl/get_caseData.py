# encoding:utf-8
'''
获取case执行需要的data数据
'''


import readExcel
import readConfig
import pytest
import re
from common import logPrintClass

class Get_conferenceControl_caseData:

    def __init__(self):
        self.log = logPrintClass.Log()

    def get_QueryMeetingStatus_data(self,ExcelName,sheetName,testName,getdata):


        # 从excel中读取参数
        caseData_List = readExcel.readExcel().get_xls('testCase', 'casedata', ExcelName,
                                                          sheetName)
        #print('caseData_List is: ', caseData_List)
        #从表中读取相应case那一行的数据

        for i in caseData_List:
            if i[0] == testName:
                caseData = i
                #print('caseData is: ',caseData)


        #从case那一行的数据中获取云会议室号码
        pattern = getdata + '.*'
        print('pattern is: ',pattern)
        for i in caseData:
            callNumber = re.findall(pattern,i)
            if len(callNumber) != 0:
                callNumberStr = str(callNumber).split(':')[-1][:-2]
                print('callNumberStr is:',callNumberStr)
                return callNumberStr





if __name__ == '__main__':
    obj = Get_conferenceControl_caseData()
    obj.get_QueryMeetingStatus_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'test_data',testName = 'test_QueryMeetingStatus001',getdata = 'callNumber')
    obj.get_QueryMeetingStatus_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'result',testName = 'test_QueryMeetingStatus001',getdata = 'expected_code')
    obj.get_QueryMeetingStatus_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'test_data',testName = 'test_Invitation001',getdata = 'device_number')