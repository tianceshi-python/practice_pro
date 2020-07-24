# encoding:utf-8

# @Time    : 2020/6/12
# @Author  : xueyan
# @File    : test_conferenceControl_Querymeetingstatus.py

'''
setup和teardown操作

setup，在测试函数或类之前执行，完成准备工作，例如数据库链接、测试数据、打开文件等
teardown，在测试函数或类之后执行，完成收尾工作，例如断开数据库链接、回收内存资源等
备注：也可以通过在fixture函数中通过yield实现setup和teardown功能

'''


from CloudVideoClass import conferenceControlClass
import pytest
from common import Assert,get_parameter,logPrintClass
import readConfig
from testCase import get_testCaseData


import allure
import json
import time
import writeExcel


'''
主持会议--根据云会议室号查看当前会议全体成员的会议状态接口测试

'''


@allure.feature('Test_conferenceControl_QueryMeetingStatus')     #Feature: 主要功能模块--一级标签
class Test_conferenceControl_QueryMeetingStatus:

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
        self.QueryMeetingStatus_base_url = get_parameter.get_parameter().get_baseUrl(
            ExcelName='conferenceControl_casedate.xlsx', sheetName='base_url', apiName='Querymeetingstatus')
        #print('QueryMeetingStatus_base_url is: ', self.QueryMeetingStatus_base_url)

        # 实例化获取case data
        self.get_caseDataObj = get_testCaseData.Get_caseData()

        # 实例化断言对象
        self.assertObj = Assert.Assertions()

        #实例化writeExcel对象
        self.writeExcelObj = writeExcel.writeExcel('testCase','casedata','conferenceControl_casedate.xlsx')

    @pytest.mark.run(order=1)       #调整测试用例的执行顺序，放在第一个位置执行
    @pytest.mark.conferenceControl_test
    @allure.story('test_QueryMeetingStatus')         #story:子功能模块--二级标签
    @allure.title('test_QueryMeetingStatus001')     #title:标注用例标题
    def test_QueryMeetingStatus001(self):

        '''
        用例描述：根据云会议室号查看当前会议全体成员的会议状态，查询的室企业云会议室号
        '''
        self.log.debug('test_QueryMeetingStatus001 start......')
        print('test_QueryMeetingStatus001 start......')
        #获取云会议室callNumber
        callNumber = self.get_caseDataObj.get_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'test_data',testName = 'test_QueryMeetingStatus001',getdata = 'callNumber')
        #获取期望返回码excepectCode
        excepectCode = self.get_caseDataObj.get_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'ExpectedResult',testName = 'test_QueryMeetingStatus001',getdata = 'expected_code')
        #获取期望的比对信息excepectMsg
        excepectMsg = self.get_caseDataObj.get_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'ExpectedResult',testName = 'test_QueryMeetingStatus001',getdata = 'expected_msg')


        self.log.debug('test_QueryMeetingStatus001 requsts data is:' + callNumber)
        print('callNumber is: ',callNumber)
        print('excepectCode is: ',excepectCode)
        print('excepectMsg is:',excepectMsg)


        # 向测试报告中输入请求参数和基本url
        allure.attach('callNumber is: ',callNumber)
        allure.attach('QueryMeetingStatus_base_url is: ',self.QueryMeetingStatus_base_url)

        code,body = self.conferenceControlObj.QueryMeetingStatus(self.QueryMeetingStatus_base_url,callNumber)
        print('code is: ',code)
        print('body is',body)

        #断言
        #判断请求返回码是否与预期的一致
        self.assertObj.assert_code(code,excepectCode)
        #判断预期的云会议室名称是否在返回的body中
        self.assertObj.assert_in_text(body,excepectMsg)

        self.writeExcelObj.write_xml(sheet_name = 'responseData',case_name = 'test_QueryMeetingStatus001', message = body)

        # 向测试报告中输入请求返回状态码和消息体
        allure.attach('请求返回状态码code is:',code)
        allure.attach('查询的会议全体成员状态',json.dumps(body))

        #time.sleep(5)

        self.log.debug('test_QueryMeetingStatus001 end......')
        print('test_QueryMeetingStatus001 end......')






if __name__ == '__main__':
    obj = Test_conferenceControl_QueryMeetingStatus()
    obj.test_QueryMeetingStatus001()





