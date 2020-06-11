# encoding:utf-8
# @Time    : 2020/6/9
# @Author  : xueyan
# @File    : Email.py


"""
封装发送邮件的方法
"""

import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import common.logPrintClass

class SendMail:
    def __init__(self):
        self.log = common.logPrintClass.Log()