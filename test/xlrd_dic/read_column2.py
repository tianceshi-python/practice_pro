# encoding:utf-8

'''
读取excel指定的列
介绍了使用 xlrd 模块，读取指定坐标的单元格，以及循环整个表格。

还没有介绍如何读取指定的列。
'''
import pandas as pd
import xlrd

'''
#读取指定的多行多列值：
df = pd.read_excel('lemo.xlsx')
data = df.iloc[[1,2]].values   #读取第0行和第一行的title和data值


print('读取指定行指定列的数据是：\n{0}'.format(data))
'''

# 打开excel文件，创建一个workbook对象,book对象也就是lemo.xlsx文件,表含有sheet名
rbook = xlrd.open_workbook('lemo.xlsx')
#sheets方法返回对象列表,[<xlrd.sheet.Sheet object at 0x103f147f0>]
rbook.sheets()
# xls默认有3个工作簿,Sheet1,Sheet2
rsheet = rbook.sheet_by_index(0)    #取第一个工作簿

#循环工作簿的所有行
for row in rsheet.get_rows():
    title_column = row[1]   #title所在的列
    title_value = title_column.value   #title值
    if title_column != 'title':    #排除第一行
        data_column = row[2]     #data所在列
        data_value = data_column.value

        #打印
        print('title:',title_value,'data:',data_value)

