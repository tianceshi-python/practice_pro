# encoding:utf-8

import readExcel
import readConfig
import json
import common.signature
import requests
import common.logPrintClass

class conferenceControlClass():
    def __init__(self,header,enterpriseId,token):
        self.header = header
        self.enterpriseId = enterpriseId
        self.token = token

        self.log = common.logPrintClass.Log()



    def create_meeting(self,base_url,**dictargs):  #字典ditargs存data数据

        self.log.info('创建云会议室号请求 start....')
        createmeet_url = base_url + self.enterpriseId
        print('createmeet_url is:',createmeet_url)
        data = dictargs
        print('data is:',data)
        jdata = json.dumps(data)

        #获取创建会议接口的数字签名
        obj = common.signature.Get_signature_url(method=str.upper("post"), req_url=createmeet_url, req_data=jdata,
                                                 token=self.token )
        signaturePra = obj.get_signature()
        print('signaturePra is:',signaturePra)
        #获取创建云会议室号的url地址
        createmeet_last_url = createmeet_url + '&signature=' + signaturePra
        print('createmeet_last_url is:',createmeet_last_url)
        res = requests.post(createmeet_last_url,data=jdata, headers=self.header)

        self.log.debug('res_url is:' + res.url)
        self.log.debug('status_code is:' + str(res.status_code))
        self.log.debug('res.text is:' + res.text)

        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text

    def QueryMeetingInfo(self,base_url,meetingRoomNumber,**dictargs):

        self.log.info('按云会议室号获取会议室信息请求 start....')
        meetingInfo_url = base_url + meetingRoomNumber + '?enterpriseId=' + self.enterpriseId
        jdata = ""

        obj = common.signature.Get_signature_url(method=str.upper('get'),req_url=meetingInfo_url,req_data =jdata,token=self.token)
        signaturePra = obj.get_signature()
        print('signaturePra is:',signaturePra)

        meetingInfo_last_url = meetingInfo_url + '&signature=' + signaturePra
        print('meetingInfo_last_url is:',meetingInfo_last_url)
        res = requests.get(meetingInfo_last_url,data=jdata,headers=self.header)

        self.log.debug('res_url is:' + res.url)
        self.log.debug('status_code is:' + str(res.status_code))
        self.log.debug('res.text is:' + res.text)

        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text

    def ModifyMeetingInfo(self,base_url,**dictargs):

        self.log.info('按云会议室号修改SDK云会议室信息请求 start....')

        data = dictargs
        print('data is:',data)

        ModifyMeetingInfo_url = base_url + data['meetingRoomNumber'] + '?enterpriseId=' + self.enterpriseId
        print('ModifyMeetingInfo_url is:',ModifyMeetingInfo_url)
        jdata = json.dumps(data)

        obj = common.signature.Get_signature_url(method=str.upper('put'), req_url=ModifyMeetingInfo_url, req_data=jdata,
                                                 token=self.token)
        signaturePra = obj.get_signature()
        print('signaturePra is:',signaturePra)

        ModifyMeetingInfo_last_url = ModifyMeetingInfo_url + '&signature=' + signaturePra

        res =requests.put(ModifyMeetingInfo_last_url,data =jdata,headers = self.header )

        self.log.debug('res_url is:' + res.url)
        self.log.debug('status_code is:' + str(res.status_code))
        self.log.debug('res.text is:' + res.text)

        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text

    def DeleMeetingInfo(self,base_url,meetingRoomNumber):

        self.log.info('按云会议室号删除SDK云会议室请求 start....')

        #获取签名的基本url
        DeleMeetingInfo_base_url = base_url + meetingRoomNumber + '?enterpriseId=' + self.enterpriseId
        jdata = ''

        obj = common.signature.Get_signature_url(method=str.upper('delete'), req_url=DeleMeetingInfo_base_url, req_data=jdata,
                                                 token=self.token)
        signaturePra = obj.get_signature()
        print('signaturePra is:', signaturePra)

        DeleMeetingInfo_last_url = DeleMeetingInfo_base_url + '&signature=' + signaturePra
        res = requests.delete(DeleMeetingInfo_last_url,data =jdata,headers = self.header)

        self.log.debug('res_url is:' + res.url)
        self.log.debug('status_code is:' + str(res.status_code))
        self.log.debug('res.text is:' + res.text)

        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text


    def QueryEnterpriseMeetingInfo(self,base_url,**dictargs):

        self.log.info('按云会议室类型查询企业下云会议室列表请求 start....')

        #获取请求数字签名的url
        QueryEnterpriseMeetingInfo_base_url= base_url + '?enterpriseId=' + self.enterpriseId
        print('QueryEnterpriseMeetingInfo_base_url is:',QueryEnterpriseMeetingInfo_base_url)

        data = dictargs
        print('data is:',data)
        jdata = json.dumps(data)
        obj = common.signature.Get_signature_url(method=str.upper('get'), req_url=QueryEnterpriseMeetingInfo_base_url,
                                                 req_data=jdata,token=self.token)
        signaturePra = obj.get_signature()
        print('signaturePra is:', signaturePra)

        QueryEnterpriseMeetingInfo_last_url = QueryEnterpriseMeetingInfo_base_url + '&signature=' + signaturePra
        res = requests.get(QueryEnterpriseMeetingInfo_last_url,data =jdata,headers = self.header)

        self.log.debug('res_url is:' + res.url)
        self.log.debug('status_code is:' + str(res.status_code))
        self.log.debug('res.text is:' + res.text)

        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text


    def QueryBatchMeetingInfo_inMeetingType(self,base_url,*tupmeetingroom):  # ’*tupmeetingroom‘ 表示非固定传参，可同时指定多个云会议室号码，传过来的所有参数打包元祖

        self.log.info('按云会议室号批量查询云会议室信息请求 start....')

        # 获取请求数字签名的url
        QueryBatchMeetingInfo_inMeetingType_base_url = base_url + '?enterpriseId=' + self.enterpriseId
        print('QueryBatchMeetingInfo_inMeetingType_base_url is:',QueryBatchMeetingInfo_inMeetingType_base_url)

        data = list(tupmeetingroom)
        print('data is:',data)
        jdata = json.dumps(data)
        obj = common.signature.Get_signature_url(method=str.upper('put'), req_url=QueryBatchMeetingInfo_inMeetingType_base_url,
                                                 req_data=jdata, token=self.token)
        signaturePra = obj.get_signature()
        print('signaturePra is:', signaturePra)

        QueryBatchMeetingInfo_inMeetingType_last_url = QueryBatchMeetingInfo_inMeetingType_base_url + '&signature=' + signaturePra
        res = requests.put(QueryBatchMeetingInfo_inMeetingType_last_url,data =jdata,headers = self.header)

        self.log.debug('res_url is:' + res.url)
        self.log.debug('status_code is:' + str(res.status_code))
        self.log.debug('res.text is:' + res.text)

        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text
















if __name__ == '__main__':
    header = readConfig.ReadConfig().get_header('header')
    enterpriseId = readConfig.ReadConfig().get_enterprise('enterpriseId')
    token = readConfig.ReadConfig().get_enterprise('token')
    print('enterpriseId is:',enterpriseId)
    print('token is:',token)
    print('header is:',header)

    #log = common.logPrintClass.Log()
    '''
    #创建云会议室号
    
    #获取create_meeting的base_url
    create_meetingbase_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'create_meeting_casedate.xlsx',
                                                                'base_urll')
    print('create_meetingbase_url_list is:',create_meetingbase_url_list)
    for i in create_meetingbase_url_list:
        if i[0] == 'create_meeting':
            base_url = i[1]
            print('base_url is:',base_url)
    
    obj = conferenceControlClass(logPath,header,enterpriseId,token)
    obj.create_meeting(base_url,meetingName = 'haha meetingroom')
    '''

    '''
    #按云会议室号获取会议室信息
    
    # 获取create_meeting的base_url
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'create_meeting_casedate.xlsx',
                                                                'base_urll')
    print('base_url_list is:', base_url_list)
    for i in base_url_list:
        if i[0] == 'QueryMeetingInfo':
            base_url = i[1]
            print('base_url is:', base_url)

    obj = conferenceControlClass(logPath,header, enterpriseId, token)
    obj.QueryMeetingInfo(base_url, meetingRoomNumber='9005853980')
    '''


    '''
    #按云会议室号修改SDK云会议室信息
    #注意：修改的云会议室号必须是SDK创建的云会议室
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'create_meeting_casedate.xlsx',
                                                                'base_urll')

    #print('ModifyMeetingInfo_base_url_list is:', ModifyMeetingInfo_base_url_list)
    for i in base_url_list:
        if i[0] == 'ModifyMeetingInfo':
            base_url = i[1]
            print('ModifyMeetingInfo_base_url is:', base_url)

    obj = conferenceControlClass(logPath,header, enterpriseId, token)
    obj.ModifyMeetingInfo(base_url, meetingRoomNumber='910063916161',autoMute = '1' )
    '''

    '''
    # 按云会议室号删除SDK云会议室
    #注意：删除的云会议室号必须是SDK创建的云会议室
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'create_meeting_casedate.xlsx',
                                                                'base_urll')
    for i in base_url_list:
        if i[0] == 'DeleMeetingInfo':
            base_url = i[1]
            print('DeleMeetingInfo_base_url is:', base_url)

    obj = conferenceControlClass(logPath,header, enterpriseId,token)
    obj.DeleMeetingInfo(base_url, meetingRoomNumber='910063916161')
    '''

    '''
    #按云会议室类型查询企业下云会议室列表
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'create_meeting_casedate.xlsx',
                                                  'base_urll')
    for i in base_url_list:
        if i[0] == 'QueryEnterpriseMeetingInfo':
            base_url = i[1]
            print('QueryEnterpriseMeetingInfo_base_url is:', base_url)

    obj = conferenceControlClass(logPath,header, enterpriseId, token)
    obj.QueryEnterpriseMeetingInfo(base_url, pageIndex =0,pageSize =20,type ='ENTERPRISE_CONFERENCE')
    '''

    #按云会议室号批量查询云会议室信息
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'create_meeting_casedate.xlsx',
                                                  'base_urll')
    for i in base_url_list:
        if i[0] == 'QueryBatchMeetingInfo_inMeetingType':
            base_url = i[1]
            print('QueryBatchMeetingInfo_inMeetingType_base_url is:', base_url)

    obj = conferenceControlClass(header, enterpriseId, token)
    obj.QueryBatchMeetingInfo_inMeetingType(base_url,"9016934130","9016934130","9016934130","9016934130","9016934130","9016934130")