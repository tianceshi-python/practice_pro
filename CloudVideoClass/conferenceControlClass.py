# encoding:utf-8
import readExcel
import readConfig
import json
import common.signature
import requests

class conferenceControlClass():
    def __init__(self,meeting_room,device_num):
        #self.method = method
        self.meeting_room = meeting_room
        self.device_num = device_num


    #邀请入会
    def invitation(self,header,enterpriseId,token,base_url):

        #获取签名的req_url=invite_url
        invite_url = base_url + enterpriseId
        data = {
            "callNumber": self.meeting_room,
            "deviceList": [{"number": self.device_num}]}
        jdata = json.dumps(data)
        print(header.items())
        #获取该接口的数字签名
        obj = common.signature.Get_signature_url(method=str.upper("put"), req_url=invite_url, req_data=jdata, token=token)
        signaturePra =obj.get_signature()
        #print('signaturePra is :',signaturePra)

        #邀请入会的请求url地址
        invite_last_url = base_url + enterpriseId + '&signature=' + signaturePra
        print('invite_last_url is:',invite_last_url)
        res = requests.put(invite_last_url, data=jdata, headers=header)
        print('status_code is:\n',res.status_code)
        print('res_url is:\n',res.url)
        print('res.text is:\n',res.text)
        return res.status_code,res.text





if __name__ == '__main__':


    #邀请入会
    header = readConfig.ReadConfig().get_header('header')
    enterpriseId = readConfig.ReadConfig().get_enterprise('enterpriseId')
    token = readConfig.ReadConfig().get_enterprise('token')

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
    obj = conferenceControlClass(meeting_room = '9005853980',device_num = '20853543')
    obj.invitation(header,enterpriseId,token,base_url)

