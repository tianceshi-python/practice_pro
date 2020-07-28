# encoding:utf-8

from CloudVideoClass import recordingVodsClass
import pytest
from common import Assert,get_parameter,logPrintClass
import readConfig
from testCase import get_testCaseData
import time



import allure


@allure.feature('Test_StartRecording')
class Test_StartRecording:
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
        self.start_recording_base_url = get_parameter.get_parameter().get_baseUrl(
            ExcelName='recordingVods_casedata.xlsx', sheetName='base_url', apiName='start_recording')
        # print('start_recording_base_url is: ', self.start_recording_base_url)

        # 实例化获取case data对象
        self.get_caseDataObj = get_testCaseData.Get_caseData()

        # 实例化断言对象
        self.assertObj = Assert.Assertions()

    @pytest.mark.run(order=1)
    @pytest.mark.RecordingAndVods
    @allure.story('test_StartRecording')
    @allure.title('test_StartRecording001')
    def test_StartRecording001(self):
        '''
        用例描述： 开始录制视频
        '''

        self.log.debug('test_StartRecording001 starting......')
        print('test_StartRecording001 starting......')

        # 获取云会议室callNumber
        meetingRoomNumber = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx', sheetName='test_data',
                                                   testName='test_StartRecording001', getdata='meetingRoomNumber')
        # 获取期望返回码excepectCode
        excepectCode = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                     sheetName='ExpectedResult', testName='test_StartRecording001',
                                                     getdata='expected_code')


        print('meetingRoomNumber is: ',meetingRoomNumber)
        print('excepectCode is: ',excepectCode)

        #添加附件信息到allure报告中
        allure.attach('meetingRoomNumber is: ',meetingRoomNumber)
        allure.attach('excepectCode is: ',excepectCode)
        allure.attach('start_recording_base_url is: ',self.start_recording_base_url)

        self.log.debug('meetingRoomNumber is: '+ meetingRoomNumber)
        self.log.debug('excepectCode is: '+ excepectCode)
        self.log.debug('start_recording_base_url is: '+ self.start_recording_base_url)

        # 调取踢出会议接口，将指定的参会人员踢出会议
        code, body = self.recordingVodsObj.start_recording(self.start_recording_base_url, meetingRoomNumber)
        print('code is: ', code)
        #print('body is', body)

        allure.attach('responseCode is: ', str(code))
        self.log.debug('responseCode is: '+ str(code))

        # 断言
        # 判断请求返回码是否与预期的一致
        self.assertObj.assert_code(code, excepectCode)

        time.sleep(5)       #录制后持续5s
        self.log.debug('test_StartRecording001 end......')
        print('test_StartRecording001 end......')
