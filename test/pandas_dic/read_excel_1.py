# encoding:utf-8


'''
在利用pandas模块进行操作前，可以先引入这个模块
'''
import pandas as pd

'''
读取Excel文件的两种方式:
'''
#方法一：默认读取第一个表单
df = pd.read_excel("lemo.xlsx")
data = df.head()       #默认读取前5行数据
print("获取到的所有值是:\n{0}".format(data))      #格式化输出

