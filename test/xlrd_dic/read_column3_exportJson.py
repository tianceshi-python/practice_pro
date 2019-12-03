# encoding:utf-8
# encoding:utf-8
import xlrd
import json
from datetime  import datetime
from xlrd import xldate_as_tuple

'''
path = 'C:\python_project\practice_pro\test\toapi_dic'
file_name = '\lemo.xlsx'
'''


'''
python读取excel中单元格的内容返回的有5种类型:
ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
'''

# 打开excel文件，创建一个workbook对象,book对象也就是lemo.xlsx文件,表含有sheet名
worksheet = xlrd.open_workbook(r'C:\python_project\practice_pro\test\toapi_dic\lemo.xlsx')
sheetnames = worksheet.sheet_names()     #获取表中的各个sheet名称
print(sheetnames)
for sheetname in sheetnames:
    sheet = worksheet.sheet_by_name(sheetname)     #按照sheet名称获取sheet对象
    rows = sheet.nrows     #获取行数
    clos = sheet.ncols    #获取列数
    all_content = {}
    for i in range(rows):
        crmid = ''
        for j in range(clos):
            cell = sheet.cell_value(i,j)     #第i行第j列数据
            ctype = sheet.cell(i,j).ctype     #将数据类型转换成表格的数据类型
            if j == 0:
                try:
                    id = int(cell)     #以第一列做键值
                except ValueError as e:
                    id = cell
                all_content[id] = []

            if ctype == 3:      #若是数据类型为日期类型，则将日期转换成固定的方式
                date = datetime(*xldate_as_tuple(cell,0))
                cell = date.strftime('%Y-%n-%d')
            elif ctype == 2 and cell % 1 == 0:  #如果是整形
                cell = int(cell)

        all_content[id].append(cell)

        res = json.dumps(all_content)
        with open('test.txt','a') as f:
            f.write(res)          #为啥输出到文件呢，因为数据太多的时候print打印不出来
        print(res)


