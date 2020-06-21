# encoding:utf-8

import pytest
import readConfig
from  common import logPrintClass,Shell
import pytest
import allure
from common import EmailSend
import getpathInfo
import os

if __name__ == "__main__":

    log = logPrintClass.Log()
    shell = Shell.Shell()
    xml_report_path = readConfig.ReadConfig().xml_report_path
    html_report_path = readConfig.ReadConfig().html_report_path
    print('xml_report_path is: ',xml_report_path)
    print('html_report_path is:',html_report_path)

    reports_address = os.path.join(getpathInfo.get_Path(),r'\report_dic\html')
    print('reports_address',reports_address)
    report_name = 'index.html'

    #定义测试集
    args = ['-s', '-q','-m=conferenceControl_test', '--alluredir', xml_report_path]
    pytest.main(args)

    #cmd1 = 'cd %s'%xml_report_path
    #shell.into_xmlDirPath(cmd1)

    #allure generate xml_report_path -o html_report_path - -clean
    cmd = 'allure generate %s -o %s --clean' %(xml_report_path, html_report_path)

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise

    #report_addr = EmailSend.acquire_report_address(reports_address,report_name)
    #EmailSend.send_email(report_addr)
