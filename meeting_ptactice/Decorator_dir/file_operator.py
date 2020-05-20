# encoding:utf-8
import os


path =r'C:\Users\Administrator\Desktop\log搜索.txt'

with open(path,'r',encoding='UTF-8') as f :
    f_lines = f.readlines()     #按行读取文件
    list1 = []
    for line in f_lines:
        list1 = list(line)
        print(list1)
        if line !='\n' or '':
            #line = line[::-1]
            list1.reverse()     #reverse()该方法没有返回值，但是会对列表的元素进行反向排序。
            list1 = ''.join(list1)    #将列表转换成字符串
            print(list1)
        print('该行为空，不需要进行操作')
    f.close()