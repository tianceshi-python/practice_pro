# encoding:utf-8


from CloudVideoClass import recordingVodsClass
import pytest
from common import Assert,get_parameter,logPrintClass
import readConfig,writeExcel
from testCase import get_testCaseData


import allure


@allure.feature('Test_get_vodsListAccordDeviceNum')
class Test_get_vodsListAccordDeviceNum:

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
        self.get_vodsList_accordDeviceNum_base_url = get_parameter.get_parameter().get_baseUrl(
            ExcelName='recordingVods_casedata.xlsx', sheetName='base_url', apiName='get_vodsList_accordDeviceNum')
        #print('get_vodsList_accordDeviceNum_base_url is: ', self.get_vodsList_accordDeviceNum_base_url)

        self.log.debug('get_vodsList_accordDeviceNum_base_url is: '+ self.get_vodsList_accordDeviceNum_base_url)

        # 实例化获取case data对象
        self.get_caseDataObj = get_testCaseData.Get_caseData()

        # 实例化断言对象
        self.assertObj = Assert.Assertions()

        # 实例化writeExcel对象
        self.writeExcelObj = writeExcel.writeExcel('testCase', 'casedata', 'recordingVods_casedata.xlsx')

    @pytest.mark.run(order=5)
    @pytest.mark.RecordingAndVods
    @allure.story('test_get_vodsListAccordDeviceNum')
    @allure.title('test_get_vodsListAccordDeviceNum001')
    def test_get_vodsListAccordDeviceNum001(self):

        '''
        function:按小鱼号分页获取视频列表
        :return:
        '''

        self.log.debug('test_get_vodsListAccordDeviceNum001 starting ......')
        print('test_get_vodsListAccordDeviceNum001 starting ......')

        # 获取接口请求输入数据
        startTime = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                  sheetName='test_data',
                                                  testName='test_get_vodsListAccordDeviceNum001', getdata='startTime')

        endTime = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                sheetName='test_data',
                                                testName='test_get_vodsListAccordDeviceNum001', getdata='endTime')

        nemoNumber = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                          sheetName='test_data',
                                                          testName='test_get_vodsListAccordDeviceNum001',
                                                          getdata='nemoNumber')

        pageIndex = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                  sheetName='test_data',
                                                  testName='test_get_vodsListAccordDeviceNum001', getdata='pageIndex')

        pageSize = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                 sheetName='test_data',
                                                 testName='test_get_vodsListAccordDeviceNum001', getdata='pageSize')

        # 获取期望返回码excepectCode
        excepectCode = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                     sheetName='ExpectedResult',
                                                     testName='test_get_vodsListAccordDeviceNum001',
                                                     getdata='expected_code')

        # 获取期望返回码message
        excepectMessage = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                     sheetName='ExpectedResult',
                                                     testName='test_get_vodsListAccordDeviceNum001',
                                                     getdata='excepect_message')

        print('startTime is: ',startTime)
        print('endTime is: ',endTime)
        print('nemoNumber is: ',nemoNumber)
        print('pageIndex is: ',pageIndex)
        print('pageSize is: ',pageSize)
        print('excepectCode is: ',excepectCode)
        print('excepectMessage is: ', excepectMessage)

        self.log.debug('startTime is: ' + startTime)
        self.log.debug('endTime is: '+ endTime)
        self.log.debug('nemoNumber is: '+ nemoNumber)
        self.log.debug('pageIndex is: '+ pageIndex)
        self.log.debug('pageSize is: '+ pageSize)
        self.log.debug('excepectCode is: '+ excepectCode)
        self.log.debug('excepectMessage is: '+ excepectMessage)

        # 添加附件信息到allure报告中
        allure.attach('startTime is: ', startTime)
        allure.attach('endTime is: ', endTime)
        allure.attach('nemoNumber is: ', nemoNumber)
        allure.attach('pageIndex is: ', pageIndex)
        allure.attach('pageSize is: ', pageSize)
        allure.attach('excepectCode is: ', excepectCode)
        allure.attach('excepectMessage is: ', excepectMessage)

        code,body = self.recordingVodsObj.get_vodsList_accordDeviceNum(self.get_vodsList_accordDeviceNum_base_url,startTime =startTime,endTime =endTime,nemoNumber =nemoNumber,pageIndex =pageIndex,pageSize=pageSize)
        print('code is: ',code)
        print('body is: ',body)

        allure.attach('responseCode is: ', code)
        allure.attach('responseBody is: ', body)

        self.log.debug('responseCode is: ' + str(code))
        self.log.debug('responseBody is: ' + body)

        self.writeExcelObj.write_xml(sheet_name='responseData', case_name='test_get_vodsListAccordDeviceNum001',
                                     message=body)

        # 断言
        # 判断请求返回码是否与预期的一致
        self.assertObj.assert_code(code, excepectCode)
        self.assertObj.assert_in_text(body,excepectMessage)

        self.log.debug('test_get_vodsListAccordDeviceNum001 end......')
        print('test_get_vodsListAccordDeviceNum001 end......')