# encoding:utf-8

# @Time    : 2020/7/17
# @Author  : xueyan
# @File    : test_conferenceControl_Kickoutmeeting.py


from CloudVideoClass import conferenceControlClass
import pytest
from common import Assert,get_parameter,logPrintClass
import readConfig
from testCase import get_testCaseData
from testCase.test_conferenceControl import bodyDataDeal


import allure
import json
import time

@allure.feature('Test_conferenceControl_Kickoutmeeting')     #Feature: 主要功能模块--一级标签
class Test_conferenceControl_Kickoutmeeting:

    @classmethod  # 类中所有的用例只会执行一次
    def setup_class(cls):
        # 实例化log打印对象
        cls.log = logPrintClass.Log()
        print('类前面打印！！')

    #@pytest.fixture(scope = 'function')
    def setup_method(self,methond):

        print('函数前打印！！！！')

        # 获取基本数据header，enterpriseId，token
        self.header = readConfig.ReadConfig().get_header('header')
        self.enterpriseId = readConfig.ReadConfig().get_enterprise('enterpriseId')
        self.token = readConfig.ReadConfig().get_enterprise('token')

        #实例化会控对象
        self.conferenceControlObj = conferenceControlClass.conferenceControlClass(self.header, self.enterpriseId,
                                                                                  self.token)

        # 获取接口的基本base_url
        self.kickoutmeeting_base_url = get_parameter.get_parameter().get_baseUrl(
            ExcelName='conferenceControl_casedate.xlsx', sheetName='base_url', apiName='kickoutmeeting_url')
        print('kickoutmeeting_base_url is: ', self.kickoutmeeting_base_url)

        # 实例化获取case data
        self.get_caseDataObj = get_testCaseData.Get_caseData()

        # 实例化断言对象
        self.assertObj = Assert.Assertions()

    @pytest.mark.run(order=3)  # 调整测试用例的执行顺序，放在第一个位置执行
    @pytest.mark.conferenceControl_Kickoutmeeting
    @allure.story('test_Kickoutmeeting')  # story:子功能模块--二级标签
    @allure.title('test_Kickoutmeeting001')  # title:标注用例标题
    def test_Kickoutmeeting001(self):

        '''
        :param setup_method: 在会议过程中，从会议中删除一个或多个与会人员
        :return:
        '''
        self.log.debug('test_Kickoutmeeting001 start......')
        print('test_Kickoutmeeting001 start......')

        # 获取云会议室callNumber
        callNumber = self.get_caseDataObj.get_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'test_data',testName = 'test_Kickoutmeeting001',getdata = 'callNumber')
        # 获取期望返回码excepectCode
        excepectCode = self.get_caseDataObj.get_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'ExpectedResult',testName = 'test_Kickoutmeeting001',getdata = 'expected_code')

        #获取body消息体
        bodyList = bodyDataDeal.get_Kickoutmeeting_requstData('testCase','casedata','conferenceControl_casedate.xlsx','responseData','test_QueryMeetingStatus001')
        bodyList = json.loads(bodyList)
        print('bodyList is: ', bodyList)

        request_bodyList = bodyList[0]      #将查询会议信息中的第一个参会人员提出会议
        print('request_bodyList type is:', type(request_bodyList))
        print('callNumber is: ', callNumber)
        print('excepectCode is: ', excepectCode)

        #request_bodyList = request_bodyList
        print('request_bodyList type is: ', type(request_bodyList))
        print('request_bodyList  is: ', request_bodyList)

        code,body= self.conferenceControlObj.Kickoutmeeting(self.kickoutmeeting_base_url,callNumber,[request_bodyList])
        print('code is: ', code)
        #print('body is', body)

        # 断言
        # 判断请求返回码是否与预期的一致
        self.assertObj.assert_code(code, excepectCode)

        self.log.debug('test_Kickoutmeeting001 end......')
        print('test_Kickoutmeeting001 end......')



if __name__ == '__main__':
    obj = Test_conferenceControl_Kickoutmeeting()
    obj.test_Kickoutmeeting001()






