# encoding:utf-8
import pandas as pd

#读取指定的单行，数据会存在列表里面
df = pd.read_excel('lemo.xlsx')    #默认读取第一个表单
data = df.iloc[0].values          #读取第一行的数据
print('读取指定行的数据：\n{0}'.format(data))

data = df.iloc[1].values
print('读取指定行的数据：\n{0}'.format(data))

data = df.iloc[2].values
print('读取指定行的数据：\n{0}'.format(data))

data = df.iloc[3].values
print('读取指定行的数据：\n{0}'.format(data))