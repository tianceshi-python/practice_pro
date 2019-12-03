#encoding:utf-8

# -*-coding:utf-8 -*-

import xlrd
import xlwt
from datetime import  date,datetime

def read_excel():
    #打开文件
    worksheet = xlrd.open_workbook(r'C:\python_project\practice_pro\test\toapi_dic\lemo.xlsx')

    #获取所有sheet
    print(worksheet.sheet_names())
    sheet1_name = worksheet.sheet_names()[0]      #获取第一个sheet名称
    print('获取sheet1的名称：',sheet1_name)
    sheet2_name = worksheet.sheet_names()[1]     #获取第2个sheet名称
    print('获取sheet2的名称：', sheet2_name)

    #根据索引或者表名称获取sheet内容
    sheet1 = worksheet.sheet_by_index(0)
    sheet2 = worksheet.sheet_by_name(sheet2_name)
    print('sheet1的内容：',sheet1)
    print('sheet2的内容：', sheet2)

    #sheet1的名称、行数、列数
    print('sheet1的名称:',sheet1.name)
    print('sheet1的行数:',sheet1.nrows)
    print('sheet1的列数:',sheet1.ncols)


    #获取整行和整列的值（数组）
    rows = sheet1.row_values(1)  #获取第2行数据
    cols = sheet1.col_values(2)  #获取第3列数据
    print(rows)
    print(cols)

    #获取单元格内容
    print('第1行第2列数据：',sheet1.cell(1,1).value)
    print('第1行第3列数据：', sheet1.cell(1,2).value)
    print('第1行第2列数据：', sheet1.cell_value(1,1))
    print('第1行第2列数据：', sheet1.row(1)[1])

    #获取单元格的数据类型
    print('单元格的数据类型是：',sheet1.cell(1,1).ctype)




if __name__ == '__main__':
    read_excel()
