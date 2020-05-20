# encoding:utf-8

#参数动态化
import readConfig
import json
from common import signature

readconfig = readConfig.ReadConfig()

class geturlParams(): #定义一个方法，将从配置文件中读取的进行拼接
    def get_Url(self,api_classification,other_para,data,method):
        #基本url = baseurl + api类型 + 其他接口参数 + enterpriseId=XXX
        new_url = readconfig.get_requstes('baseurl')+ readconfig.get_apiClassification(api_classification) + other_para + 'enterpriseId='+readconfig.get_enterprise('enterpriseId')
        jdata = json.dumps(data)
        token = readconfig.get_enterprise('token')
        obj = signature.Get_signature_url(method= str.upper(method), req_url=new_url, req_data=jdata, token=token)
        signature_para = obj.get_signature()
        last_url = new_url + '&signature=' + signature_para
        return last_url


if __name__ == '__main__':
    api_classification = 'conferenceControl'
    other_para = '/invitation?'
    data = {
        "callNumber": 9016934130,
        "deviceList": [{"number": 127367}]}
    method = 'put'
    requests_url = geturlParams().get_Url(api_classification,other_para,data,method)
    print(requests_url)
