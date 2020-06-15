# encoding:utf-8

# @Time    : 2020/6/14
# @Author  : xueyan
# @File    : test_conferenceControl_Invitation.py

from common import Assert,get_parameter,logPrintClass,geturlParams
from CloudVideoClass import conferenceControlClass
import readConfig
from testCase import get_testCaseData

import pytest




class Test_conferenceControl_Invitation():

    def setup_class(self):
        # 实例化log打印对象
        self.log = logPrintClass.Log()
        print('类前面打印！！')



    @pytest.fixture(scope='function')
    def setup_function(self):
        print('函数前打印！！！！')

        # 获取基本数据header，enterpriseId，token
        self.header = readConfig.ReadConfig().get_header('header')
        self.enterpriseId = readConfig.ReadConfig().get_enterprise('enterpriseId')
        self.token = readConfig.ReadConfig().get_enterprise('token')
        
        
        # 实例化会控对象
        self.conferenceControlObj = conferenceControlClass.conferenceControlClass(self.header, self.enterpriseId,self.token)




        # 获取接口的基本base_url
        self.Invitation_base_url = get_parameter.get_parameter().get_baseUrl(
            ExcelName='conferenceControl_casedate.xlsx', sheetName='base_url', apiName='Invitation')
        # print('QueryMeetingStatus_base_url is: ', self.QueryMeetingStatus_base_url)

        # 实例化获取case data
        self.get_caseDataObj = get_testCaseData.Get_caseData()

        # 实例化断言对象
        self.assertObj = Assert.Assertions()

    def test_Invitation001(self,setup_function):

        self.log.debug('test_Invitation001 start......')
        print('test_Invitation001 start......')

        #获取云会议室号码callNumber
        callNumber =self.get_caseDataObj.get_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'test_data',testName = 'test_Invitation001',getdata = 'callNumber')
        print('callNumber is: ',callNumber)

        #获取被邀请的终端或者软终端号码device_number
        device_number = self.get_caseDataObj.get_data(ExcelName= 'conferenceControl_casedate.xlsx',sheetName = 'test_data',testName = 'test_Invitation001',getdata = 'device_number')
        #print('device_number is:',device_number)
        device_number_list = device_number.split(',')
        #print('device_number_list is: ',device_number_list)
        device_numberlist = []
        for i in device_number_list:
            if i != ' ':
                i = "{'number':'" + str(i) + "'}"
                device_numberlist.append(i)
        print('device_numberlist is: ',device_numberlist)


        # 获取期望返回码excepectCode
        excepectCode = self.get_caseDataObj.get_data(ExcelName='conferenceControl_casedate.xlsx', sheetName='result',
                                                     testName='test_Invitation001', getdata='expected_code')
        print('excepectCode is: ',excepectCode)

        self.log.debug('test_Invitation001 requsts callNumber data is:' + callNumber)
        self.log.debug('test_Invitation001 requsts device_number is:' + device_number)
        code, body = self.conferenceControlObj.Invitation(self.Invitation_base_url, callNumber,device_numberlist)
        print('code is: ', code)
        print('body is', body)

        # 断言
        # 判断请求返回码是否与预期的一致
        self.assertObj.assert_code(code, excepectCode)

        self.log.debug('test_Invitation001 end......')
        print('test_Invitation001 end......')




if __name__ == "__main__":
    try:
        pytest.main(['-s', '-q',])#测试当前文件夹以test开头的py文件
    except:
        print('pytest运行失败')
