# encoding:utf-8
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
import time

#自动发送邮件
def send_email(new_report):
    #读取测试报告中的内容作为邮件的内容
    with open(new_report,'r',encoding='utf8') as f:
        mail_body = f.read()
    #print('mail_body is: ',mail_body)
    #发件人地址
    from_addr = 'tianxueyan@xylink.com'
    #收件人地址
    to_addr = 'zhangmingyue@xylink.com,1192923936@qq.com'
    #发送邮箱的服务器地址
    mail_server = 'smtp.exmail.qq.com'
    #邮件的标题
    subject = 'API自动化测试报告'
    #发件人的邮箱地址
    username = 'tianxueyan@xylink.com'
    password = 'Tian100405125'
    #邮箱的内容和标题
    message = MIMEText(mail_body,'html','utf8')
    message['Subject'] = Header(subject,charset='utf8')
    #发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(mail_server)
    smtp.login(username,password)
    smtp.sendmail(from_addr,to_addr.split(','),message.as_string())
    smtp.quit()

#获取最新报告的地址
def acquire_report_address(reports_address,report_name):
    #测试报告文件夹中的所有文件加入到列表
    test_reports_list = os.listdir(reports_address)
    print('test_reports_list is: ',test_reports_list)

    #最新的测试报告的地址
    the_last_report_address = os.path.join(reports_address,report_name)
    return the_last_report_address


if __name__ == '__main__':
    reports_address = r'C:\python_project\practice_pro\report_dic\html'
    report_name = 'index.html'
    reportAddress = acquire_report_address(reports_address,report_name)
    print('reportAddress is: ',reportAddress)

    send_email(reportAddress)


    '''
    # 生成测试报告并发送邮件
    #测试报告文件夹地址
    test_reports_address = 'C:\python_project\practice_pro\report_dic\html'
    #测试用例的文件夹地址
    test_cases_dir = r'F:\python_selenium\soft_test_selenium2.0\test_cases'
    #获取所有的测试用例
    test_cases = unittest.defaultTestLoader.discover(test_cases_dir,pattern='*.py')
    #获取当前时间
    now = datetime.now().strftime('%Y%m%d%H%MM%f')
    #生成以当前时间命名的测试报告文件名
    test_report_name = r'{}\report_{}.html'.format(test_reports_address,datetime.now().strftime('%Y%m%d%H%M%f'))
    #生成以当前时间命名的测试报告文件
    file_report = open(test_report_name,'w',encoding='utf8')
    #生成html形式的报告
    runner = HTMLTestRunner(stream=file_report,title='测试报告',description='QQ登录测试报告结果：')
    #运行
    runner.run(test_cases)
    #关闭打开的测试报告文件
    file_report.close()

    time.sleep(5)
    #查找最新生成的测试报告地址
    new_report_addr = acquire_report_address(test_reports_address)
    #自动发送邮件
    send_email(new_report_addr)
    '''