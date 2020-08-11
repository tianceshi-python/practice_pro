# encoding:utf-8


from CloudVideoClass import recordingVodsClass
import pytest
from common import Assert,get_parameter,logPrintClass
import readConfig,writeExcel
from testCase import get_testCaseData


import allure

allure.feature('Test_get_vodsListAccordMeetingroom')
class Test_get_vodsListAccordMeetingroom:

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
        self.get_vodsList_accordMeetingroom_base_url = get_parameter.get_parameter().get_baseUrl(
            ExcelName='recordingVods_casedata.xlsx', sheetName='base_url', apiName='get_vodsList_accordMeetingroom')
        #print('get_vodsList_accordMeetingroom_base_url is: ', self.get_vodsList_accordMeetingroom_base_url)

        # 实例化获取case data对象
        self.get_caseDataObj = get_testCaseData.Get_caseData()

        # 实例化断言对象
        self.assertObj = Assert.Assertions()

        # 实例化writeExcel对象
        self.writeExcelObj = writeExcel.writeExcel('testCase', 'casedata', 'recordingVods_casedata.xlsx')

    @pytest.mark.run(order=4)
    @pytest.mark.RecordingAndVods
    @allure.story('test_get_vodsListAccordMeetingroom')
    @allure.title('test_get_vodsListAccordMeetingroom001')
    def test_get_vodsListAccordMeetingroom001(self):
        '''
        function:按云会议号分页获取视频列表
        :return:
        '''

        print('test_get_vodsListAccordMeetingroom001 starting......')
        self.log.debug('test_get_vodsListAccordMeetingroom001 starting......')

        #获取接口请求输入数据
        startTime = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                          sheetName='test_data',
                                                          testName='test_get_vodsListAccordMeetingroom001', getdata='startTime')

        endTime = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                          sheetName='test_data',
                                                          testName='test_get_vodsListAccordMeetingroom001', getdata='endTime')

        meetingRoomNumber = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                          sheetName='test_data',
                                                          testName='test_get_vodsListAccordMeetingroom001', getdata='meetingRoomNumber')

        pageIndex = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                          sheetName='test_data',
                                                          testName='test_get_vodsListAccordMeetingroom001', getdata='pageIndex')

        pageSize = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                          sheetName='test_data',
                                                          testName='test_get_vodsListAccordMeetingroom001', getdata='pageSize')

        # 获取期望返回码excepectCode
        excepectCode = self.get_caseDataObj.get_data(ExcelName='recordingVods_casedata.xlsx',
                                                     sheetName='ExpectedResult', testName='test_get_vodsListAccordMeetingroom001',
                                                     getdata='expected_code')

        print('startTime is: ',startTime)
        print('endTime is: ',endTime)
        print('meetingRoomNumber is: ',meetingRoomNumber)
        print('pageIndex is: ',pageIndex)
        print('pageSize is: ',pageSize)
        print('get_vodsList_accordMeetingroom_base_url is: ',self.get_vodsList_accordMeetingroom_base_url)
        print('excepectCode is: ',excepectCode)

        self.log.debug('startTime is: ' + startTime)
        self.log.debug('endTime is: ' + endTime)
        self.log.debug('meetingRoomNumber is: ' + meetingRoomNumber)
        self.log.debug('pageIndex is: ' + pageIndex)
        self.log.debug('pageSize is: ' + pageSize)
        self.log.debug('get_vodsList_accordMeetingroom_base_url is: ' + self.get_vodsList_accordMeetingroom_base_url)
        self.log.debug('excepectCode is: ' + excepectCode)

        #添加附件信息到allure报告中
        allure.attach('startTime is: ',startTime)
        allure.attach('endTime is: ',endTime)
        allure.attach('meetingRoomNumber is: ',meetingRoomNumber)
        allure.attach('pageIndex is: ',pageIndex)
        allure.attach('pageSize is: ',pageSize)
        allure.attach('get_vodsList_accordMeetingroom_base_url is: ',self.get_vodsList_accordMeetingroom_base_url)
        allure.attach('excepectCode is: ',excepectCode)



        #调取按云会议号分页获取视频列表接口
        code, body = self.recordingVodsObj.get_vodsList_accordMeetingroom(self.get_vodsList_accordMeetingroom_base_url, startTime =startTime,endTime =endTime,meetingRoomNumber =meetingRoomNumber,pageIndex =pageIndex,pageSize=pageSize)
        print('code is: ', code)
        print('body is', body)

        allure.attach('responseCode is: ', code)
        allure.attach('responseBody is: ', body)

        self.log.debug('responseCode is: '+  str(code))
        self.log.debug('responseBody is: '+ body)

        self.writeExcelObj.write_xml(sheet_name='responseData', case_name='get_vodsListAccordMeetingroom001', message=body)

        # 断言
        # 判断请求返回码是否与预期的一致
        self.assertObj.assert_code(code, excepectCode)

        self.log.debug('get_vodsListAccordMeetingroom001 end......')
        print('get_vodsListAccordMeetingroom001 end......')