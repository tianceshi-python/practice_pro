# encoding:utf-8
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from datetime import datetime
import time
import readConfig



#自动发送邮件
def send_email(mail_body):

    mailObj = readConfig.ReadConfig()
    print('mail meg is: ', mailObj.get_mail('from_name'))

    #发件人地址
    from_addr = mailObj.get_mail('from_addr')
    #收件人地址
    to_addr =  mailObj.get_mail('to_addr')
    #print('to_addr is: ', to_addr)
    #发送邮箱的服务器地址
    mail_server = mailObj.get_mail('mail_server')
    #邮件的标题
    subject = mailObj.get_mail('subject')
    #发件人的邮箱地址
    username = mailObj.get_mail('username')
    password = mailObj.get_mail('password')

    # 发件人、收件人名称、抄送人名称
    from_name = mailObj.get_mail('from_name')
    to_name = mailObj.get_mail('to_name')

    # 构造一个MIMEMultipart对象代表邮件本身
    msg = MIMEMultipart()

    #邮箱的内容和标题以及发件人和收件人
    msg.attach(MIMEText(mail_body, _subtype='html', _charset='utf-8'))



    msg['From'] = Header(from_name, 'utf-8')    #发件人名称转码
    msg['To'] = Header(to_name, 'utf-8')             #收件人名称转码
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
    #print('mail_body is: ', mail_body)
    return mail_body

if __name__ == '__main__':
    reports_address = r'C:\python_project\practice_pro\report_dic\html'
    report_name = 'address.html'
    mail_body = acquire_report_ToMailbody(reports_address,report_name)
    #print('mail_body is: ', mail_body)

    send_email(mail_body)