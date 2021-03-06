# encoding:utf-8

import os
import configparser
import getpathInfo


path = getpathInfo.get_Path() #调用实例化，返回当前文件的绝对路径
config_path = os.path.join(path, 'config.ini')   #在path路径下再加一级，

'''
在对配置文件进行读写操作前，我们需要先进行以下两个操作：
1、实例化configParser对象
2、读取config.ini文件
'''



class ReadConfig():

    # 实例化ConfigParser对象
    config = configparser.ConfigParser()
    # 读取配置文件
    config.read(config_path, 'utf-8')

    def get_enterprise(self, name):
        value = self.config.get('ENTERPRISE', name)
        return value
    def get_device(self, name):
        value = self.config.get('DEVICE', name)
        return value
    def get_metting_room(self, name):
        value = self.config.get('METTING_ROOM', name)
        return value
    def get_requstes(self,name):
        value = self.config.get('REQUEST', name)
        return value
    def get_apiClassification(self,name):
        value = self.config.get('APICLASSIFICATION', name)
        return value
    def get_email(self, name):
        value = self.config.get('EMAIL', name)
        return value


if __name__ == '__main__':
    print ('企业的token信息为',ReadConfig().get_enterprise('token'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off'))

