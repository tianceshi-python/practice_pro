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

@allure.feature('Test_conferenceControl_Kickoutmeeting')     #allure.Feature: 主要功能模块--一级标签
class Test_conferenceControl_Kickoutmeeting:

    @classmethod  # 类中所有的用例只会执行一次
    def setup_class(cls):
        # 实例化log打印对象
        cls.log = logPrintClass.Log()
        print('类前面打印！！')

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
        #print('kickoutmeeting_base_url is: ', self.kickoutmeeting_base_url)

        # 实例化获取case data
        self.get_caseDataObj = get_testCaseData.Get_caseData()

        # 实例化断言对象
        self.assertObj = Assert.Assertions()

    @pytest.mark.run(order=3)  # 调整测试用例的执行顺序，放在第一个位置执行
    @pytest.mark.conferenceControl_test
    @allure.story('test_Kickoutmeeting')  # story:子功能模块--二级标签
    @allure.title('test_Kickoutmeeting001')  # title:标注用例标题
    def test_Kickoutmeeting001(self):

        '''
        用例描述： 在会议过程中，从会议中删除一个或多个与会人员
        '''
        self.log.debug('test_Kickoutmeeting001 start......')
        print('test_Kickoutmeeting001 start......')

        # 获取云会议室callNumber
        callNumber = self.get_caseDataObj.get_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'test_data',testName = 'test_Kickoutmeeting001',getdata = 'callNumber')
        # 获取期望返回码excepectCode
        excepectCode = self.get_caseDataObj.get_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'ExpectedResult',testName = 'test_Kickoutmeeting001',getdata = 'expected_code')

        #获取请求的body消息体bodystr
        bodystr,participantNumberList = bodyDataDeal.deal_QueryMeetingStatusReaponseData('testCase','casedata','conferenceControl_casedate.xlsx','responseData','test_QueryMeetingStatus001')

        # 将字符串类型转换成json格式
        bodyList = json.loads(bodystr)
        #print('bodyList is: ', bodyList)
        if len(bodyList) != 0:
            request_bodyList = bodyList[0]      #将查询会议信息中的第一个参会人员踢出会议
            #print('request_bodyList type is:', type(request_bodyList))

            print('callNumber is: ', callNumber)
            print('excepectCode is: ', excepectCode)
            print('request_bodyList  is: ', [request_bodyList])

            # 将请求信息在报告中展示
            allure.attach('excepectCode is: ',excepectCode)
            allure.attach('callNumber is: ',callNumber)
            allure.attach('excepectCode is: ',excepectCode)
            allure.attach('kickoutmeeting_base_url is: ',self.kickoutmeeting_base_url)
            allure.attach('request_bodyList is: ',[request_bodyList])

            self.log.debug('test_Kickoutmeeting001excepectCode is: ' + excepectCode)
            self.log.debug('test_Kickoutmeeting001 callNumber is: ' + callNumber)
            self.log.debug('test_Kickoutmeeting001 excepectCode is: ' + excepectCode)
            self.log.debug('test_Kickoutmeeting001 kickoutmeeting_base_url is: ' + self.kickoutmeeting_base_url)
            self.log.debug('test_Kickoutmeeting001 request_bodyList is: '+ str([request_bodyList]))

            #调取踢出会议接口，将指定的参会人员踢出会议
            code,body= self.conferenceControlObj.Kickoutmeeting(self.kickoutmeeting_base_url,callNumber,[request_bodyList])
            print('code is: ', code)
            #print('body is', body)

            allure.attach('请求返回的状态码 is: ',code)

            # 断言
            # 判断请求返回码是否与预期的一致
            self.assertObj.assert_code(code, excepectCode)
        else:
            print('会议已经结束，没有参会人员，无法执行踢人接口，请重新组会！！！！')

        self.log.debug('test_Kickoutmeeting001 end......')
        print('test_Kickoutmeeting001 end......')



if __name__ == '__main__':
    obj = Test_conferenceControl_Kickoutmeeting()
    obj.test_Kickoutmeeting001()






