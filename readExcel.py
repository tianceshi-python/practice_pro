# encoding:utf-8

import os
import getpathInfo   #导入自已定义的内部类，该类返回项目的绝对路径

#调用读取Excel的第三方库
from xlrd import open_workbook

#拿到项目的绝对路径
path = getpathInfo.get_Path()

class readExcel():
    def get_xls(self,xls_name,sheet_name):
        cls = []

        xlsPath = os.path.join(path,"testFile",'case',xls_name)
        file =open_workbook(xlsPath)   #打开用例的excel
        #sheet = file.sheets()[0]    #通过索引顺序获取表

        #print(sheet_name)
        sheet = file.sheet_by_name(sheet_name)   #通过名称获取表

        #sheet = file.sheet_by_index(0)

        #获取这个sheet的内容行数
        nrows = sheet.nrows

        for i in range(nrows):  #根据行数循环
            if sheet.row_values(i)[0] != u'case_name':  #判断将表的第一行排除，第一行不是case
                cls.append(sheet.row_values(i))
        return cls


if __name__ == '__main__':
    print(readExcel().get_xls('userCase.xlsx','MeetRoomCase'))
    print(readExcel().get_xls('userCase.xlsx','MeetRoomCase')[0][1])
    print(readExcel().get_xls('userCase.xlsx','MeetRoomCase')[1][2])
