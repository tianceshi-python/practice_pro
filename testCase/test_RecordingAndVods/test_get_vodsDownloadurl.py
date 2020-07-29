# encoding:utf-8

from CloudVideoClass import recordingVodsClass
import pytest
from common import Assert,get_parameter,logPrintClass
import readConfig,writeExcel
from testCase import get_testCaseData
from testCase.test_RecordingAndVods import RecordingAndVods_BodyDataDeal



import allure

@allure.feature('Test_get_vodsDownloadurl')
class Test_get_vodsDownloadurl:
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
        self.get_vodsDownloadurl_base_url = get_parameter.get_parameter().get_baseUrl(
            ExcelName='recordingVods_casedata.xlsx', sheetName='base_url', apiName='get_vodsDownloadurl')
        # print('get_vodsDownloadurl_base_url is: ', self.get_vodsDownloadurl_base_url)

        # 实例化获取case data对象
        self.get_caseDataObj = get_testCaseData.Get_caseData()

        # 实例化断言对象
        self.assertObj = Assert.Assertions()


        #实例化writeExcel对象
        self.writeExcelObj = writeExcel.writeExcel('testCase','casedata','recordingVods_casedata.xlsx')



    @pytest.mark.run(order=3)
    @pytest.mark.RecordingAndVods
    @allure.story('test_get_vodsDownloadurl')
    @allure.title('test_get_vodsDownloadurl001')
    def test_get_vodsDownloadurl001(self):
        '''
        用例描述： 开始录制视频
        '''

        self.log.debug('test_StopRecording001 starting......')
        print('test_StopRecording001 starting......')

        # 获取sessionId
        sessionId = RecordingAndVods_BodyDataDeal.deal_StopRecordingReaponseData('testCase','casedata','recordingVods_casedata.xlsx','responseData','test_StopRecording001')
        # 获取期望返回码excepectCode
        excepectCode = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                     sheetName='ExpectedResult', testName='test_StopRecording001',
                                                     getdata='expected_code')


        print('sessionId is: ',sessionId)
        print('excepectCode is: ',excepectCode)

        # 添加附件信息到allure报告中
        allure.attach('sessionId is: ', sessionId)
        allure.attach('excepectCode is: ', excepectCode)
        allure.attach('stop_recording_base_url is: ', self.get_vodsDownloadurl_base_url)

        self.log.debug('sessionId is: ' + sessionId)
        self.log.debug('excepectCode is: ' + excepectCode)
        self.log.debug('stop_recording_base_url is: ' + self.get_vodsDownloadurl_base_url)

        # 调取踢出会议接口，将指定的参会人员踢出会议
        code, body = self.recordingVodsObj.get_vodsDownloadurl(self.get_vodsDownloadurl_base_url, sessionId)
        print('code is: ', code)
        print('body is', body)

        self.writeExcelObj.write_xml(sheet_name = 'responseData',case_name = 'test_get_vodsDownloadurl001', message = body)

        allure.attach('responseCode is: ', str(code))
        self.log.debug('responseCode is: ' + str(code))

        # 断言
        # 判断请求返回码是否与预期的一致
        self.assertObj.assert_code(code, excepectCode)

        self.log.debug('test_get_vodsDownloadurl001 end......')
        print('test_get_vodsDownloadurl001 end......')
