# encoding:utf-8

import os
import getpathInfo   #导入自已定义的内部类，该类返回项目的绝对路径

#调用读取Excel的第三方库
from xlrd import open_workbook
import xlrd,xlwt


#拿到项目的绝对路径
path = getpathInfo.get_Path()

class writeExcel:



    def write_xml(self,caseDirName1,caseDirName2,xls_name,sheet_name,case_name,ncol,message):

        xlsPath = os.path.join(path, caseDirName1, caseDirName2, xls_name)
        #file = Workbook(encoding = 'utf-8')  # 打开用例的excel
        file = open_workbook(xlsPath)  # 打开用例的excel
        sheet = file.sheet_by_name(sheet_name)  # 通过名称获取表
        # 获取这个sheet的内容行数
        nrows = sheet.nrows

        for i in range(nrows):
            if sheet.row_values(i)[0] == case_name:  #判断每行的第一个内容是否和case名称相同
                print('case name is: ',sheet.row_values(i)[0])
                sheet.write(i,int(ncol),message)                  #在指定case名称的指定列存入数据

       #file.save(file)



if  __name__ == "__main__":
    obj = writeExcel()
    obj.write_xml('testCase','casedata','conferenceControl_casedate.xlsx','responseData',case_name = 'test_QueryMeetingStatus001', ncol= '1',message = '1234566789')