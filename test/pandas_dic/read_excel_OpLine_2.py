# encoding:utf-8

import pandas as pd

#读取指定的多行，数据会存在嵌套的列表里面：

df = pd.read_excel('lemo.xlsx')    #默认读取第一个表单
data = df.iloc[[0,1]].values      #读取指定多行的话，就要在ix[]里面嵌套列表指定行数
print('读取指定的行数列表：\n{0}'.format(data))
print("读取的列表中第0个列表元素是：\n{0}".format(data[0]))
print("读取的列表中第1个列表元素是：\n{0}".format(data[1]))
print("正常登陆的用户名和密码是：\n{0}".format(data[0][2]))