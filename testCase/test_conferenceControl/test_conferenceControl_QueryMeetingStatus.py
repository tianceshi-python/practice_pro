# encoding:utf-8

# @Time    : 2020/6/12
# @Author  : xueyan
# @File    : test_conferenceControl_Querymeetingstatus.py

from CloudVideoClass import conferenceControlClass
import pytest
from common import Assert,logPrintClass,get_parameter
import readConfig
from testCase import get_testCaseData



'''
主持会议--根据云会议室号查看当前会议全体成员的会议状态接口测试

'''

class Test_conferenceControl_QueryMeetingStatus:

    def setup_class(self):
        #实例化log打印对象
        self.log = logPrintClass.Log()
        print('类前面打印！！')

    @pytest.fixture(scope = 'function')
    def setup_function(self):
        print('函数前打印！！！！')
        # 获取基本数据header，enterpriseId，token
        self.header = readConfig.ReadConfig().get_header('header')
        self.enterpriseId = readConfig.ReadConfig().get_enterprise('enterpriseId')
        self.token = readConfig.ReadConfig().get_enterprise('token')

        #实例化会控对象
        self.conferenceControlObj = conferenceControlClass.conferenceControlClass(self.header, self.enterpriseId,
                                                                                  self.token)

        # 获取接口的基本base_url
        self.QueryMeetingStatus_base_url = get_parameter.get_parameter().get_baseUrl(
            ExcelName='conferenceControl_casedate.xlsx', sheetName='base_url', apiName='Querymeetingstatus')
        #print('QueryMeetingStatus_base_url is: ', self.QueryMeetingStatus_base_url)

        # 实例化获取case data
        self.get_caseDataObj = get_testCaseData.Get_caseData()

        # 实例化断言对象
        self.assertObj = Assert.Assertions()


    def test_QueryMeetingStatus001(self,setup_function):


        self.log.debug('test_QueryMeetingStatus001 start......')
        print('test_QueryMeetingStatus001 start......')
        #获取云会议室callNumber
        callNumber = self.get_caseDataObj.get_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'test_data',testName = 'test_QueryMeetingStatus001',getdata = 'callNumber')
        #获取期望返回码excepectCode
        excepectCode = self.get_caseDataObj.get_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'result',testName = 'test_QueryMeetingStatus001',getdata = 'expected_code')
        #获取期望的比对信息excepectMsg
        excepectMsg = self.get_caseDataObj.get_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'result',testName = 'test_QueryMeetingStatus001',getdata = 'expected_msg')


        self.log.debug('test_QueryMeetingStatus001 requsts data is:' + callNumber)
        print('callNumber is: ',callNumber)
        print('excepectCode is: ',excepectCode)
        print('excepectMsg is:',excepectMsg)

        code,body = self.conferenceControlObj.QueryMeetingStatus(self.QueryMeetingStatus_base_url,callNumber)
        print('code is: ',code)
        print('body is',body)

        #断言
        #判断请求返回码是否与预期的一致
        self.assertObj.assert_code(code,excepectCode)
        #判断预期的云会议室名称是否在返回的body中
        self.assertObj.assert_in_text(body,excepectMsg)

        self.log.debug('test_QueryMeetingStatus001 end......')
        print('test_QueryMeetingStatus001 end......')




