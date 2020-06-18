# encoding:utf-8

import pytest
import readConfig
from  common import logPrintClass,Shell
import pytest
import allure


if __name__ == "__main__":

    log = logPrintClass.Log()
    shell = Shell.Shell()
    xml_report_path = readConfig.ReadConfig().xml_report_path
    html_report_path = readConfig.ReadConfig().html_report_path
    print('xml_report_path is: ',xml_report_path)
    print('html_report_path is:',html_report_path)

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
