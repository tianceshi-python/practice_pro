# encoding:utf-8

import CloudVideoClass.conferenceControlClass
import pytest
import  common.logPrintClass
import readConfig
import common.get_parameter
import common.Assert
import testCase.test_conferenceControl.get_caseData


'''
主持会议--根据云会议室号查看当前会议全体成员的会议状态接口测试

'''

class Test_conferenceControl:
    def __init__(self):
        self.log = common.logPrintClass.Log()

    def setup_class(self):
        print('类前面打印！！')

        #获取基本数据header，enterpriseId，token
        self.header = readConfig.ReadConfig().get_header('header')
        self.enterpriseId = readConfig.ReadConfig().get_enterprise('enterpriseId')
        self.token = readConfig.ReadConfig().get_enterprise('token')

    def setup_function(self):
        print('函数前打印！！！！')

        #实例化接口对象实例化
        self.conferenceControlObj = CloudVideoClass.conferenceControlClass.conferenceControlClass(self.header,self.enterpriseId,self.token)

        #实例化获取case data实例化
        self.get_caseDataObj = testCase.test_conferenceControl.get_caseData.Get_conferenceControl_caseData()

        #获取接口的基本base_url
        self.QueryMeetingStatus_base_url = common.get_parameter.get_parameter.get_baseUrl(ExcelName = 'conferenceControl_casedate.xlsx',sheetName = 'base_url',apiName = 'Querymeetingstatus')
        print('QueryMeetingStatus_base_url is: ',self.QueryMeetingStatus_base_url)


    def test_QueryMeetingStatus001(self):

        #获取云会议室callNumber
        callNumber = self.get_caseDataObj.get_QueryMeetingStatus_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'test_data',testName = 'test_QueryMeetingStatus001')
        print('callNumber is: '+ callNumber)
        responsedata = list(self.conferenceControlObj.QueryMeetingStatus(self.QueryMeetingStatus_base_url,callNumber))
        code = responsedata[0]
        msg = responsedata[1]
        assert code == 200
        assert
        print("test_addCategory_0000001 is:", )

    if __name__ == "__main__":
        pytest.main(['-s', r''])

