# encoding:utf-8
import readExcel
import readConfig
import json
import common.signature
import requests
import common.logPrintClass   #导入打印log的模块

class conferenceControlClass():
    def __init__(self,logPath,header,enterpriseId,token):
        #self.method = method
        self.header = header
        self.enterpriseId = enterpriseId
        self.token = token

        #实例化log打印类
        self.logPath = logPath
        self.log = common.logPrintClass.Log(self.logPath)


    #邀请入会
    def invitation(self,base_url,meeting_room,device_num):
        self.log.info('邀请入会请求 start....')

        #获取签名的req_url=invite_url
        invite_url = base_url + self.enterpriseId
        data = {
            "callNumber": meeting_room,
            "deviceList": [{"number": device_num}]}
        jdata = json.dumps(data)
        print(header.items())
        #获取该接口的数字签名
        obj = common.signature.Get_signature_url(method=str.upper("put"), req_url=invite_url, req_data=jdata, token=self.token)
        signaturePra =obj.get_signature()
        #print('signaturePra is :',signaturePra)

        #邀请入会的请求url地址
        invite_last_url = invite_url + '&signature=' + signaturePra
        print('invite_last_url is:',invite_last_url)
        res = requests.put(invite_last_url, data=jdata, headers=header)

        self.log.debug('res_url is:' + res.url)
        self.log.debug('status_code is:' + str(res.status_code))
        self.log.debug('res.text is:' + res.text)

        print('status_code is:\n',res.status_code)
        print('res_url is:\n',res.url)
        print('res.text is:\n',res.text)
        return res.status_code,res.text





if __name__ == '__main__':


    #邀请入会
    header = readConfig.ReadConfig().get_header('header')
    enterpriseId = readConfig.ReadConfig().get_enterprise('enterpriseId')
    token = readConfig.ReadConfig().get_enterprise('token')
    logPath = readConfig.ReadConfig().get_LogPath('LogPath')
    print('LogPath is:', logPath)

    #5.23修改了获取base_url的表名称
    base_url_list = readExcel.readExcel().get_xls('testCase','casedata','conferenceControl_casedate.xlsx','base_urll')
    #print('header is:', header.items())

    #print('enterpriseId is:',enterpriseId)
    #print('token is:',token)
    #print('base_url_list is:',base_url_list)
    for i in base_url_list:
        if i[0] == 'invitation':
            base_url = i[1]
            # print('base_url is:',base_url)
    #print('base_url is:',base_url)
    obj = conferenceControlClass(logPath,header,enterpriseId,token)
    obj.invitation(base_url,meeting_room = '9005853980',device_num = '20853543')

