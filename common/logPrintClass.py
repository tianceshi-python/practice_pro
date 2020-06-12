# encoding:utf-8

import logging
import time
import os
import readConfig
import getpass


# 定义要创建的目录
def mkdir():
    user_name = getpass.getuser()  # 获取当前用户名
    path = 'C:\\Users\\' + user_name + '\\AppData\\Roaming\\autoTestLog'
    #print('path is:', path)
    #判断路径是否存在
    #存在 True
    #不存在 False
    isExists = os.path.exists(path)

    #判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 如果不存在则创建目录
        os.makedirs(path)
        print('path创建成功：',path)
    else:
        print( path +'  目录已经存在')
    return path




#写log类
class Log():
    def __init__(self):
        path = mkdir()
        self.logname = path + '\\' +'autoTestLog' +  time.strftime('%Y-%m-%d') + '.log'



    def printconsole(self,level, message):
        #创建一个logger
        logger = logging.getLogger('mylogger')
        logger.setLevel(logging.DEBUG)

        #创建一个handler,用于写入到日志文件
        fh = logging.FileHandler(self.logname,encoding="utf-8",mode="a")
        fh.setLevel(logging.DEBUG)

        '''
        #再创建一个handler，用于输出到控制台
        ch = logging.FileHandler(encoding="utf-8")
        ch.setLevel(logging.DEBUG)
        '''

        #定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        #ch.setFormatter(formatter)

        #给logger添加handler
        logger.addHandler(fh)
        #logger.addHandler(ch)

        #记录一条日志
        if level == 'info':
            logger.info(message)
        if level == 'debug':
            logger.debug(message)
        if level == 'warning':
            logger.warning(message)
        if level == 'error':
            logger.error(message)
        #logger.removeHandler(ch)
        logger.removeHandler(fh)



    def debug(self,message):
        self.printconsole('debug',message)

    def info(self,message):
        self.printconsole('info',message)

    def warning(self,message):
        self.printconsole('warning',message)

    def error(self,message):
        self.printconsole('error',message)



if __name__ == '__main__':

    log = Log()
    log.info('info msg1000013333')
    log.debug('debug msg')
    log.warning('warning msg')
    log.error('error msg')