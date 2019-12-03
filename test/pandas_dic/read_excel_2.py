# encoding:utf-8

import pandas as pd

'''
读取Excel文件的两种方式:
'''
#方法二：通过指定表单名的方式来读取
df = pd.read_excel("lemo.xlsx",sheet_name='student')    #可以通过sheet_name来指定读取的表单
data = df.head()       #默认读取前5行数据
print("获取到的所有值是:\n{0}".format(data))      #格式化输出