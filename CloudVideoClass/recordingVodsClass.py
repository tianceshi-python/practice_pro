# encoding:utf-8
import readExcel
import readConfig
import json
import common.signature
import requests
import time

import common.logPrintClass


class recordingVodsClass():
    def __init__(self,logPath, header, enterpriseId,token):
        self.header = header
        self.enterpriseId = enterpriseId
        self.token = token
        self.logPath = logPath

        self.log = common.logPrintClass.Log(self.logPath)


    #开始录制
    def start_recording(self,base_url,meetingRoomNumber):
        self.log.info('开始录制请求 start....')
        #获取数字签名的url
        start_recording_base_url = base_url + meetingRoomNumber + '/start?enterpriseId=' + self.enterpriseId
        jdata = ''

        print('start_recording_base_url is:',start_recording_base_url)

        #获取数字签名
        obj = common.signature.Get_signature_url(method=str.upper("get"), req_url=start_recording_base_url, req_data=jdata,
                                                 token=self.token)
        signaturePra = obj.get_signature()

        #开始录制API接口请求的url
        start_recording_last_url = start_recording_base_url + '&signature=' + signaturePra

        res = requests.get(start_recording_last_url,data=jdata, headers=self.header)

        self.log.debug('res_url is:' + res.url)
        self.log.debug('status_code is:' + str(res.status_code))
        self.log.debug('res.text is:' + res.text)

        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text

    # 结束录制
    def stop_recording(self,base_url,meetingRoomNumber):
        self.log.info('结束录制请求 start....')

        # 获取数字签名的url
        stop_recording_base_url = base_url + meetingRoomNumber + '/stopWithSessionId?enterpriseId=' + self.enterpriseId
        jdata = ''

        print('stop_recording_base_url is:',stop_recording_base_url)

        # 获取数字签名
        obj = common.signature.Get_signature_url(method=str.upper("get"), req_url=stop_recording_base_url,
                                                 req_data=jdata,token=self.token)
        signaturePra = obj.get_signature()

        # 停止录制API接口请求的url
        stop_recording_last_url = stop_recording_base_url + '&signature=' + signaturePra
        res = requests.get(stop_recording_last_url,data=jdata, headers=self.header)

        self.log.debug('res_url is:' + res.url)
        self.log.debug('status_code is:' + str(res.status_code))
        self.log.debug('res.text is:' + res.text)

        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text

    #根据sessionId获取视频的下载链接
    def get_vodsDownloadurl(self,base_url,sessionId):
        self.log.info('根据sessionId获取视频的下载链接请求 start....')

        # 获取数字签名的url
        get_vodsDownloadurl_base_url = base_url + sessionId + '/downloadurl?enterpriseId=' + self.enterpriseId
        jdata = ''
        print('get_vodsDownloadurl_base_url is:',get_vodsDownloadurl_base_url)

        #获取数字签名
        obj = common.signature.Get_signature_url(method=str.upper("get"), req_url=get_vodsDownloadurl_base_url,
                                                 req_data=jdata,token=self.token)
        signaturePra = obj.get_signature()

        #根据sessionId获取视频的下载链接请求的API url
        get_vodsDownloadurl_last_url = get_vodsDownloadurl_base_url + '&signature=' + signaturePra

        res = requests.get(get_vodsDownloadurl_last_url,data=jdata, headers=self.header)

        self.log.debug('res_url is:' + res.url)
        self.log.debug('status_code is:' + str(res.status_code))
        self.log.debug('res.text is:' + res.text)

        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text

    #按云会议号分页获取视频列表
    def get_vodsList_accordMeetingroom(self,base_url,startTime,endTime,meetingRoomNumber,pageIndex,pageSize):
        self.log.info('按云会议号分页获取视频列表请求 start....')

        # 获取数字签名的url
        get_vodsList_accordMeetingroom_base_url = base_url + meetingRoomNumber + '/vods/page?enterpriseId=' + self.enterpriseId + '&startTime=' + str(startTime) + '&endTime=' + str(endTime) + '&pageIndex=' + str(pageIndex) + '&pageSize=' + str(pageSize)
        print('get_vodsList_accordMeetingroom_base_url is:',get_vodsList_accordMeetingroom_base_url)
        jdata = ''

        # 获取数字签名
        obj = common.signature.Get_signature_url(method=str.upper("get"), req_url=get_vodsList_accordMeetingroom_base_url,
                                                 req_data=jdata, token=self.token)
        signaturePra = obj.get_signature()

        get_vodsList_accordMeetingroom_last_url = get_vodsList_accordMeetingroom_base_url + '&signature=' + signaturePra
        res = requests.get(get_vodsList_accordMeetingroom_last_url,data=jdata, headers=self.header)

        self.log.debug('res_url is:' + res.url)
        self.log.debug('status_code is:' + str(res.status_code))
        self.log.debug('res.text is:' + res.text)

        print('status_code is:\n', res.status_code)
        print('res_url is:\n', res.url)
        print('res.text is:\n', res.text)
        return res.status_code, res.text






if  __name__ == '__main__':
    header = readConfig.ReadConfig().get_header('header')
    enterpriseId = readConfig.ReadConfig().get_enterprise('enterpriseId')
    token = readConfig.ReadConfig().get_enterprise('token')
    print('enterpriseId is:', enterpriseId)
    print('token is:', token)
    print('header is:', header)

    logPath = readConfig.ReadConfig().get_LogPath('LogPath')
    print('LogPath is:', logPath)

    '''
    # 开始录制
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'recordingVods_casedata.xlsx',
                                                  'base_url')

    # print('ModifyMeetingInfo_base_url_list is:', ModifyMeetingInfo_base_url_list)
    for i in base_url_list:
        if i[0] == 'start_recording':
            base_url = i[1]
            print('base_url is:', base_url)

    obj = recordingVodsClass(header,enterpriseId,token)
    obj.start_recording(base_url,'9005853980')

    time.sleep(50)

    #结束录制
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'recordingVods_casedata.xlsx',
                                                  'base_url')

    # print('ModifyMeetingInfo_base_url_list is:', ModifyMeetingInfo_base_url_list)
    for i in base_url_list:
        if i[0] == 'stop_recording':
            base_url = i[1]
            print('base_url is:', base_url)

    obj = recordingVodsClass(header, enterpriseId, token)
    obj.stop_recording(base_url, '9005853980')
    '''

    '''
    #根据sessionId获取视频的下载链接
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'recordingVods_casedata.xlsx',
                                                  'base_url')

    # print('ModifyMeetingInfo_base_url_list is:', ModifyMeetingInfo_base_url_list)
    for i in base_url_list:
        if i[0] == 'get_vodsDownloadurl':
            base_url = i[1]
            print('base_url is:', base_url)

    sessionId = "9005853980@CONFNO_1155637587202_1155637587202_0_normal_764541198384"
    obj = recordingVodsClass(header, enterpriseId, token)
    obj.get_vodsDownloadurl(base_url, sessionId)
    '''

    #按云会议号分页获取视频列表
    base_url_list = readExcel.readExcel().get_xls('testCase', 'casedata', 'recordingVods_casedata.xlsx',
                                                  'base_url')

    # print('ModifyMeetingInfo_base_url_list is:', ModifyMeetingInfo_base_url_list)
    for i in base_url_list:
        if i[0] == 'get_vodsList_accordMeetingroom':
            base_url = i[1]
            print('base_url is:', base_url)

    obj = recordingVodsClass(logPath,header, enterpriseId, token)
    obj.get_vodsList_accordMeetingroom(base_url,startTime =1470452566000,endTime =1470452566000,meetingRoomNumber ='9005853980',pageIndex =0,pageSize=20  )

