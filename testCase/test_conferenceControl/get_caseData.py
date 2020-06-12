# encoding:utf-8
'''
获取case执行需要的data数据
'''


import readExcel
import readConfig
import pytest
import re

class Get_conferenceControl_caseData():


    @pytest.fixture()
    def get_QueryMeetingStatus_data(self,ExcelName,sheetName,testName):


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
        pattern = r'callNumber.*'
        for i in caseData:
            callNumber = re.findall(pattern,i)
            if len(callNumber) != 0:
                callNumberStr = str(callNumber).split(':')[-1][:-2]
                print('callNumberStr is:',callNumberStr)
                return callNumberStr





if __name__ == '__main__':
    Get_conferenceControl_caseData.get_QueryMeetingStatus_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'test_data',testName = 'test_QueryMeetingStatus001')