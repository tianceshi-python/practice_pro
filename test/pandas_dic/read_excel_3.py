# encoding:utf-8
import pandas as pd

'''
读取Excel文件的两种方式:
'''
#方法三：通过表单索引来指定要访问的表单，0表示第一个表单
#也可以采用表单名和索引的双重方式来定位表单
#也可以同时定位多个表单，方式都罗列如下所示

'''
df = pd.read_excel("lemo.xlsx",sheet_name=['python',1])  
#df = pd.read_excel("lemo.xlsx",sheet_name=['python','student'])    #可以通过表单名同时指定多个
#df = pd.read_excel("lemo.xlsx",sheet_name=['python',1])    #可以用混合的方式来指定
df = pd.read_excel("lemo.xlsx",sheet_name=[0,1])     #可以用索引同时指定多个
data = df.values()    #获取所有的数据，注意这里不能用head()方法哦~
df = pd.read_excel("lemo.xlsx",sheet_name=['python',1])  
'''


df = pd.read_excel("lemo.xlsx",sheet_name=1)    #可以通过表单索引来指定读取的表单
data = df.values    #获取所有的数据，注意这里不能用head()方法哦~      它是类对象的一个属性，不是方法。

print("获取到的所有值是:\n{0}".format(data))      #格式化输出