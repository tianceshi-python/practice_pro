# encoding:utf-8

# @Time    : 2020/6/14
# @Author  : xueyan
# @File    : test_conferenceControl_Invitation.py

from common import Assert,get_parameter,logPrintClass,geturlParams
from CloudVideoClass import conferenceControlClass
import readConfig
from testCase import get_testCaseData

import pytest
import allure
import time


@allure.feature('邀请入会：Test_conferenceControl_Invitation')           #Allure特性-feature：每一个大的功能模块可以定义为一个feature,代码如下
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

    @pytest.mark.run(order=2)         #调整测试用例的执行顺序，放在第二位执行
    @pytest.mark.conferenceControl_test
    @allure.story('test_Invitation001')           #Allure特性-story：大功能下的一个子功能
    @allure.title('test_Invitation001')
    def test_Invitation001(self,setup_function):


        '''
        用例描述：邀请入会，同时邀请硬件和软终端入会
        :param setup_function:
        :return:
        '''
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
                i ={"number":i}
                device_numberlist.append(i)
        print('device_numberlist is: ',device_numberlist)


        # 获取期望返回码excepectCode
        excepectCode = self.get_caseDataObj.get_data(ExcelName='conferenceControl_casedate.xlsx', sheetName='result',
                                                     testName='test_Invitation001', getdata='expected_code')
        print('excepectCode is: ',excepectCode)

        self.log.debug('test_Invitation001 requsts callNumber data is:' + callNumber)
        self.log.debug('test_Invitation001 requsts device_number is:' + device_number)

        #Allure特性 - attach：增加附加信息或图片
        # 向测试报告中输入请求参数和基本url
        allure.attach('callNumber is: ', callNumber)
        allure.attach('device_numberlist is: ',device_numberlist)
        allure.attach('Invitation_base_url is: ', self.Invitation_base_url)


        code, body = self.conferenceControlObj.Invitation(self.Invitation_base_url, callNumber,device_numberlist)
        print('code is: ', code)
        print('body is', body)

        # 断言
        # 判断请求返回码是否与预期的一致
        self.assertObj.assert_code(code, excepectCode)

        # 向测试报告中输入请求返回状态码和消息体
        allure.attach('请求返回状态码code is:', code)


        time.sleep(5)
        self.log.debug('test_Invitation001 end......')
        print('test_Invitation001 end......')




if __name__ == "__main__":
    try:
        pytest.main(['-s', '-q',])#测试当前文件夹以test开头的py文件
    except:
        print('pytest运行失败')
