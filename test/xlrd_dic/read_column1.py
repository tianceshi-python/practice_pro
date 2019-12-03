# encoding:utf-8
import xlrd

'''
path = 'C:\python_project\practice_pro\test\toapi_dic'
file_name = '\lemo.xlsx'
'''

worksheet = xlrd.open_workbook(r'C:\python_project\practice_pro\test\toapi_dic\lemo.xlsx')
sheetnames = worksheet.sheet_names()
print(sheetnames)
for sheetname in sheetnames:
    sheet = worksheet.sheet_by_name(sheetname)
    rows = sheet.nrows     #获取行数
    clos = sheet.ncols    #获取列数
    all_content = []
    for i in range(rows):
        cell = sheet.cell_value(i,2)     #这一行的第2列数据
        try:
            all_content.append(cell)
        except  ValueError  as e:
            pass

    print(all_content)
