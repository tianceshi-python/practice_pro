# encoding:utf-8
import json
import pytest
from common.configHttp import RunMain
from common import geturlParams
import urllib.parse
import readExcel



url = geturlParams.geturlParams().get_Url('invitation?')
invite_xls = readExcel.readExcel().get_xls('userCase.xlsx','MeetRoomCase')

class testUserLogin:
    def setParameters(self,case_name,parh,query,method):
        '''
        set params
        :param case_name:
        :param parh:
        :param query:
        :param method:
        :return:
        '''

        self.case_name = str(case_name)
        self.path = str(parh)
        self.query = str(query)
        self.methond = str(method)

    def description(self):
        '''
        test report description
        :return:
        '''

        self.case_name

    @classmethod
    def setup_class(self,cls):
        print(self.case_name + '测试开始前准备')

    def test01case(self):
        case01_data = readExcel().get_xls('userCase.xlsx','invitation')[1]
        case01_case_name = case01_data[0]
        case01_deviceNum = case01_data[1]
        case01_method = case01_data[2]
        print(case01_case_name,case01_deviceNum,case01_method)
        self.checkResult(case01_case_name,case01_deviceNum,case01_method)

    def teardown_class(self,cls):
        print('测试结束，输出log完结\n\n')

    def checkResult(self,case_name,device_num,method):
        '''
        check test result
        :return:
        '''
        url1 = geturlParams().get_Url('invitation?',device_num)
        data1 =dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(url1)))
        info = RunMain.run_main(self.methond.url.data1)
        ss = json.loads(info)
        if self.case_name == 'pc/mac':
            assert ss['code'] == 200
        if self.case_name == 'app':
            assert ss['code'] == 200
        if self.case_name == 'ne60':
            assert ss['code'] == 200

