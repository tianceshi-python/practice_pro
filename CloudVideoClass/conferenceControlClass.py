# encoding:utf-8
import readExcel
import readConfig
import json
import common.signature
import requests
import time
import getpass
import common.logPrintClass   #导入打印log的模块

class conferenceControlClass():
    def __init__(self,logPath,header,enterpriseId,token):
        self.header = header
        self.enterpriseId = enterpriseId
        self.token = token

        #实例化log打印类
        self.logPath = logPath
        self.log = common.logPrintClass.Log(self.logPath)

    # 根据云会议室号查看当前会议全体成员的会议状态
    def QueryMeetingStatus(self, base_url, callNumber):
        meetingStatus_url = base_url + callNumber + '/meetingStatus?enterpriseId=' + self.enterpriseId
        jdata = ""
        print(meetingStatus_url)

        obj = common.signature.Get_signature_url(method=str.upper('get'), req_url=meetingStatus_url, req_data=jdata,
                                                 token=self.token)
        signaturePra = obj.get_signature()
        print('signaturePra is:', signaturePra)

        meetingStatus_last_url = meetingStatus_url + '&signature=' + signaturePra
        print('meetingStatus_last_url is:', meetingStatus_last_url)

        res = requests.get(meetingStatus_last_url, data=jdata, headers=self.header)
        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text

    # 邀请入会

    def Invitation(self, base_url, callNumber, deviceList):  # devicelist为列表参数：[{'number':'20734806'},{'number':'619827'}
        self.log.info('邀请入会请求 start....')

        # 获取签名的req_url=invite_url
        invite_url = base_url + self.enterpriseId
        data = {
        "callNumber": callNumber,
        "deviceList": deviceList}
        print(data)
        jdata = json.dumps(data)

        # 获取该接口的数字签名
        obj = common.signature.Get_signature_url(method=str.upper("put"), req_url=invite_url, req_data=jdata, token=self.token)
        signaturePra = obj.get_signature()
        print('signaturePra is :', signaturePra)

        # 邀请入会的请求url地址
        invite_last_url = invite_url + '&signature=' + signaturePra
        print('invite_last_url is:', invite_last_url)
        res = requests.put(invite_last_url, data=jdata, headers=self.header)

        self.log.debug('res_url is:' + res.url)
        self.log.debug('status_code is:' + str(res.status_code))
        self.log.debug('res.text is:' + res.text)

        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text


    # 踢出会议
    def Kickoutmeeting(self, base_url, callNumber, data):
        kickoutmeeting_url = base_url + callNumber + '/disconnect?enterpriseId=' + self.enterpriseId
        data = data
        # data数据格式如下
        # data = [{
        #     "id": id,
        #     "type": type,
        #     "participantNumber":"participantNumber"}
        #     ]
        print(data)
        jdata = json.dumps(data)

        # 获取该接口的数字签名
        obj = common.signature.Get_signature_url(method=str.upper("put"), req_url=kickoutmeeting_url, req_data=jdata,
                                                 token=self.token)
        signaturePra = obj.get_signature()
        print('signaturePra is :', signaturePra)

        # 踢出会议的请求url地址
        kickoutmeeting_url_last_url = kickoutmeeting_url + '&signature=' + signaturePra
        print('kickoutmeeting_url_last_url is:', kickoutmeeting_url_last_url)
        res = requests.put(kickoutmeeting_url_last_url, data=jdata, headers=self.header)
        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text


    # 设置主画面
    def Mainscreen(self, base_url, meetingRoomNumber, data):
        Mainscreen_url = base_url + meetingRoomNumber + '/mainImage?enterpriseId=' + self.enterpriseId
        data = data
        # data数据格式如下
        # data = [{
        #     "id": id,
        #     "type": type,
        #     "participantNumber":"participantNumber"}
        #     ]
        print(data)
        jdata = json.dumps(data)

        # 获取该接口的数字签名
        obj = common.signature.Get_signature_url(method=str.upper("put"), req_url=Mainscreen_url,
                                                 req_data=jdata,
                                                 token=self.token)
        signaturePra = obj.get_signature()
        print('signaturePra is :', signaturePra)

        # 设置主画面的请求url地址
        Mainscreen_url_last_url = Mainscreen_url + '&signature=' + signaturePra
        print('Mainscreen_url_last_url is:', Mainscreen_url_last_url)
        res = requests.put(Mainscreen_url_last_url, data=jdata, headers=self.header)
        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text


    # 禁言
    def Nospeaking(self, base_url, callNumber, data):
        Nospeaking_url = base_url + callNumber + '/mute?enterpriseId=' + self.enterpriseId + '&force=True'
        data = data
        # data数据格式如下
        # data = [{
        #     "id": id,
        #     "type": type,
        #     "participantNumber":"participantNumber"}
        #     ]
        print(data)
        jdata = json.dumps(data)

        # 获取该接口的数字签名
        obj = common.signature.Get_signature_url(method=str.upper("put"), req_url=Nospeaking_url,
                                                 req_data=jdata,
                                                 token=self.token)
        signaturePra = obj.get_signature()
        print('signaturePra is :', signaturePra)

        # 设置禁言的请求url地址
        Nospeaking_url_last_url = Nospeaking_url + '&signature=' + signaturePra
        print('Mainscreen_url_last_url is:', Nospeaking_url_last_url)
        res = requests.put(Nospeaking_url_last_url, data=jdata, headers=self.header)
        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text


    # 解除禁言
    def Allowspeaking(self, base_url, callNumber, data):
        Allowspeaking_url = base_url + callNumber + '/unmute?enterpriseId=' + self.enterpriseId
        data = data
        # data数据格式如下
        # data = [{
        #     "id": id,
        #     "type": type,
        #     "participantNumber":"participantNumber"}
        #     ]
        print(data)
        jdata = json.dumps(data)

        # 获取该接口的数字签名
        obj = common.signature.Get_signature_url(method=str.upper("put"), req_url=Allowspeaking_url,
                                                 req_data=jdata,
                                                 token=self.token)
        signaturePra = obj.get_signature()
        print('signaturePra is :', signaturePra)

        # 解除禁言的请求url地址
        Allowspeaking_url_last_url = Allowspeaking_url + '&signature=' + signaturePra
        print('Mainscreen_url_last_url is:', Allowspeaking_url_last_url)
        res = requests.put(Allowspeaking_url_last_url, data=jdata, headers=self.header)
        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text


    # 向终端发送字幕
    def Sendsubtitles(self, base_url, callNumber, *datas):
        Sendsubtitles_url = base_url + callNumber + '/meeting/subtitle?enterpriseId=' + self.enterpriseId
        data = datas
        # data数据格式
        # {
        #
        #     "content": "时尚大方",
        #     "targets":
        #         [
        #             {
        #                 "deviceId": 60784924,
        #                 "deviceType": 7
        #             }
        #         ]
        # }
        jdata = json.dumps(data)

        # 获取该接口的数字签名
        obj = common.signature.Get_signature_url(method=str.upper("put"), req_url=Sendsubtitles_url,
                                                 req_data=jdata,
                                                 token=self.token)
        signaturePra = obj.get_signature()
        print('signaturePra is :', signaturePra)

        # 向终端发送字幕的请求url地址
        Sendsubtitles_url_last_url = Sendsubtitles_url + '&signature=' + signaturePra
        print('Sendsubtitles_url_last_url is:', Sendsubtitles_url_last_url)
        res = requests.post(Sendsubtitles_url_last_url, data=jdata, headers=self.header)
        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text


    # 结束会议
    def Endmeeting(self, base_url, callNumber):
        Endmeeting_url = base_url + callNumber + '/end?enterpriseId=' + self.enterpriseId
        jdata = ""

        # 获取该接口的数字签名
        obj = common.signature.Get_signature_url(method=str.upper("put"), req_url=Endmeeting_url,
                                                 req_data=jdata,
                                                 token=self.token)
        signaturePra = obj.get_signature()
        print('signaturePra is :', signaturePra)

        # 结束会议的请求url地址
        Endmeeting_url_last_url = Endmeeting_url + '&signature=' + signaturePra
        print('Sendsubtitles_url_last_url is:', Endmeeting_url_last_url)
        res = requests.put(Endmeeting_url_last_url, data=jdata, headers=self.header)
        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text


if __name__ == '__main__':

    header = readConfig.ReadConfig().get_header('header')
    enterpriseId = readConfig.ReadConfig().get_enterprise('enterpriseId')
    token = readConfig.ReadConfig().get_enterprise('token')
    user_name = getpass.getuser()  # 获取当前用户名
    LogPath = 'C:\\Users\\' + user_name + '\\AppData\\Roaming\\autoTestLog'
    # logPath = readConfig.ReadConfig().get_LogPath('LogPath')
    print('LogPath is:', LogPath)

    '''
    #查询会议状态
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'conferenceControl_casedate.xlsx',
                                                  'base_urll')
    for i in base_url_list:
        if i[0] == 'Querymeetingstatus':
            base_url = i[1]
    print('base_url is:',base_url)

    obj = conferenceControlClass(enterpriseId,token,header)
    obj.QueryMeetingStatus('9005853980',base_url)
        '''

    # 邀请入会
    '''参数传入'''
    deviceList = []
    devicenumber1 = {'number': '20734806'}
    devicenumber2 = {'number': '619827'}
    devicenumber3 = {'number': '22481414'}
    deviceList.append(devicenumber1)
    deviceList.append(devicenumber2)
    deviceList.append(devicenumber3)

    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'conferenceControl_casedate.xlsx', 'base_urll')
    for i in base_url_list:
        if i[0] == 'Invitation':
            base_url = i[1]
    print('base_url is:', base_url)
    obj = conferenceControlClass(LogPath,header,enterpriseId,token)
    obj.Invitation(base_url, '9005853980', deviceList)

    time.sleep(10)

    # 查询会议状态
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'conferenceControl_casedate.xlsx',
                                                  'base_urll')
    for i in base_url_list:
        if i[0] == 'Querymeetingstatus':
            base_url = i[1]
    print('base_url is:', base_url)

    obj = conferenceControlClass(LogPath,header,enterpriseId,token)
    obj.QueryMeetingStatus(base_url, '9005853980')

    # 获取终端id/type等信息
    responsedata = list(obj.QueryMeetingStatus(base_url, '9005853980'))
    print(responsedata)
    # meetinginfo = json.loads(responsedata[1])
    # print(meetinginfo)
    deviceStatusList = json.loads(responsedata[1])["deviceStatusList"]
    print(len(deviceStatusList))
    data = []
    for i in range(len(deviceStatusList)):
        for k in deviceStatusList[i].keys():
            if k == 'device':
                value = deviceStatusList[i][k]
                del value['participantId']
                del value['externalUserId']
                print(value)
        data.append(value)
    print(data)

    # 踢出会议
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'conferenceControl_casedate.xlsx',
                                                  'base_urll')
    for i in base_url_list:
        if i[0] == 'Kickoutmeeting':
            base_url = i[1]
    print('base_url is:', base_url)

    obj = conferenceControlClass(LogPath,header,enterpriseId,token)
    obj.Kickoutmeeting(base_url, '9005853980', [data[0]])

    time.sleep(5)

    # 设置主画面
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'conferenceControl_casedate.xlsx',
                                                  'base_urll')
    for i in base_url_list:
        if i[0] == 'Mainscreen':
            base_url = i[1]
    print('base_url is:', base_url)

    obj = conferenceControlClass(LogPath,header,enterpriseId,token)
    obj.Mainscreen(base_url, '9005853980', data[1])

    time.sleep(5)

    # 禁言
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'conferenceControl_casedate.xlsx',
                                                  'base_urll')
    for i in base_url_list:
        if i[0] == 'Nospeaking':
            base_url = i[1]
    print('base_url is:', base_url)

    obj = conferenceControlClass(LogPath,header,enterpriseId,token)
    obj.Nospeaking(base_url, '9005853980', data)

    time.sleep(5)

    # 解除禁言
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'conferenceControl_casedate.xlsx',
                                                  'base_urll')
    for i in base_url_list:
        if i[0] == 'Allowspeaking':
            base_url = i[1]
    print('base_url is:', base_url)

    obj = conferenceControlClass(LogPath,header,enterpriseId,token)
    obj.Allowspeaking(base_url, '9005853980', data)

    time.sleep(5)

    # 向终端发送字幕
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'conferenceControl_casedate.xlsx',
                                                  'base_urll')
    for i in base_url_list:
        if i[0] == 'Sendsubtitles':
            base_url = i[1]
    print('base_url is:', base_url)

    datas = {"content": "测试test", "targets": [{"deviceId": 221123196, "deviceType": 8}]}

    obj = conferenceControlClass(LogPath,header,enterpriseId,token)
    obj.Sendsubtitles(base_url, '9005853980', *datas)

    time.sleep(10)

    # 结束会议
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'conferenceControl_casedate.xlsx',
                                                  'base_urll')
    for i in base_url_list:
        if i[0] == 'Endmeeting':
            base_url = i[1]
    # print('base_url is:',base_url)
    # print('base_url is:',base_url)
    obj = conferenceControlClass(LogPath, header, enterpriseId, token)
    obj.Endmeeting(base_url, meeting_room='9005853980', device_num='20853543')
    print('base_url is:', base_url)


