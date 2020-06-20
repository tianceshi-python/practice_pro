# encoding:utf-8
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from datetime import datetime
import time

#自动发送邮件
def send_email(mail_body):

    #发件人地址
    from_addr = 'tianxueyan@xylink.com'
    #收件人地址
    to_addr = '1192923936@qq.com,tianxueyan@xylink.com'
    #发送邮箱的服务器地址
    mail_server = 'smtp.exmail.qq.com'
    #邮件的标题
    subject = 'API自动化测试报告'
    #发件人的邮箱地址
    username = 'tianxueyan@xylink.com'
    password = 'Tian100405125'

    # 构造一个MIMEMultipart对象代表邮件本身
    msg = MIMEMultipart()

    #邮箱的内容和标题以及发件人和收件人
    msg.attach(MIMEText(mail_body, _subtype='html', _charset='utf-8'))

    msg['From'] = Header("自动化测试执行", 'utf-8')    #发件人名称转码
    msg['To'] = Header("xuyan", 'utf-8')             #收件人名称转码
    msg['Subject'] = Header(subject,'utf-8')         #邮件标题转码
    #发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(mail_server,'25')      # 25 为 SMTP 端口号
    smtp.login(username,password)
    smtp.sendmail(from_addr,to_addr.split(','),msg.as_string())      # as_string()把MIMEText对象变成str
    smtp.quit()

#获取最新报告
def acquire_report_ToMailbody(reports_address,report_name):
    #测试报告文件夹中的所有文件加入到列表
    #test_reports_list = os.listdir(reports_address)
    #print('test_reports_list is: ',test_reports_list)

    #最新的测试报告的地址
    the_last_report_address = os.path.join(reports_address,report_name)

    # 读取测试报告中的内容作为邮件的内容
    with open(the_last_report_address, 'r', encoding='utf-8') as f:
        mail_body = f.read()
    print('mail_body is: ', mail_body)
    return mail_body

if __name__ == '__main__':
    reports_address = r'C:\python_project\practice_pro\report_dic\html'
    report_name = 'index.html'
    mail_body = acquire_report_ToMailbody(reports_address,report_name)
    #print('mail_body is: ', mail_body)

    send_email(mail_body)


