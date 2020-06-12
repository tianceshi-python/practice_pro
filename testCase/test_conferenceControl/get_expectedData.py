# encoding:utf-8

'''
获取case执行后预期的比对数据
'''
import re
import readExcel
import pytest

class Get_conferenceControl_expectedData:


    #@pytest.fixture()
    def get_QueryMeetingStatus_expectedData(self,ExcelName,sheetName,testName):
        # 从excel中读取参数
        expectedData_List = readExcel.readExcel().get_xls('testCase', 'casedata', ExcelName,
                                                      sheetName)
        print('expectedData_List is: ', expectedData_List)
        # 从表中读取相应case那一行的数据

        for i in expectedData_List:
            if i[0] == testName:
                expectedData = i
                print('expectedData is: ',expectedData)

        # 从case那一行的数据中获取云会议室号码
        pattern = r'expected_code.*'
        for i in expectedData:
            code_list = re.findall(pattern, i)
            if len(code_list) != 0:
                code = str(code_list).split(':')[-1][:-2]
                print('code is:', code)
                return code


if __name__ == '__main__':
    Get_conferenceControl_expectedData().get_QueryMeetingStatus_expectedData(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'result',testName = 'test_QueryMeetingStatus001')