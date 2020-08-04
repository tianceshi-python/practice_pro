# encoding:utf-8

from CloudVideoClass import recordingVodsClass
import pytest
from common import Assert,get_parameter,logPrintClass
import readConfig,writeExcel
from testCase import get_testCaseData


import allure

class Test_get_vodsListEnterpriseOneDay:

    @classmethod  # 类中所有的用例只会执行一次
    def setup_class(cls):
        # 实例化log打印对象
        cls.log = logPrintClass.Log()
        print('类前面打印！！')

    def setup_method(self, methond):
        print('函数前打印！！！！')

        # 获取基本数据header，enterpriseId，token
        self.header = readConfig.ReadConfig().get_header('header')
        self.enterpriseId = readConfig.ReadConfig().get_enterprise('enterpriseId')
        self.token = readConfig.ReadConfig().get_enterprise('token')

        # 实例化录制视频对象
        self.recordingVodsObj = recordingVodsClass.recordingVodsClass(self.header, self.enterpriseId,
                                                                      self.token)

        # 获取接口的基本base_url
        self.get_vodsList_enterpriseOneDay_base_url = get_parameter.get_parameter().get_baseUrl(
            ExcelName='recordingVods_casedata.xlsx', sheetName='base_url', apiName='get_vodsList_enterpriseOneDay')
        # print('get_vodsList_enterpriseOneDay_base_url is: ', self.get_vodsList_enterpriseOneDay_base_url)

        self.log.debug('get_vodsList_enterpriseOneDay_base_url is: ' + self.get_vodsList_enterpriseOneDay_base_url)

        # 实例化获取case data对象
        self.get_caseDataObj = get_testCaseData.Get_caseData()

        # 实例化断言对象
        self.assertObj = Assert.Assertions()

        # 实例化writeExcel对象
        self.writeExcelObj = writeExcel.writeExcel('testCase', 'casedata', 'recordingVods_casedata.xlsx')


    def test_get_vodsListEccordDeviceNum001(self):
        '''
        function:分页查询企业一天内的视频列表
        :return:
        '''

        # 获取接口请求输入数据
        startTime = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                  sheetName='test_data',
                                                  testName='test_get_vodsListEccordDeviceNum001', getdata='startTime')

        endTime = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                sheetName='test_data',
                                                testName='test_get_vodsListEccordDeviceNum001', getdata='endTime')


        pageIndex = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                  sheetName='test_data',
                                                  testName='test_get_vodsListEccordDeviceNum001', getdata='pageIndex')

        pageSize = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                 sheetName='test_data',
                                                 testName='test_get_vodsListEccordDeviceNum001', getdata='pageSize')

        # 获取期望返回码excepectCode
        excepectCode = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                     sheetName='ExpectedResult',
                                                     testName='test_get_vodsListEccordDeviceNum001',
                                                     getdata='expected_code')

        # 获取期望返回码message
        excepectMessage = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                        sheetName='ExpectedResult',
                                                        testName='test_get_vodsListEccordDeviceNum001',
                                                        getdata='excepect_message')

        print('startTime is: ', startTime)
        print('endTime is: ', endTime)
        print('pageIndex is: ', pageIndex)
        print('pageSize is: ', pageSize)

        print('excepectCode is: ', excepectCode)
        print('excepectMessage is: ', excepectMessage)

        code, body = self.recordingVodsObj.get_vodsList_enterpriseOneDay(self.get_vodsList_enterpriseOneDay_base_url,
                                                                        startTime=startTime, endTime=endTime, pageIndex=pageIndex,
                                                                        pageSize=pageSize)
        print('code is: ', code)
        print('body is: ', body)
