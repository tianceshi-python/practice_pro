# encoding:utf-8
'''
题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

输入描述:
输入一个正浮点数值

输出描述:
输出该数值的近似整数值
'''


def calculate(num_str):
    #print(list(num_str))
    list_num = num_str.split('.')

    if int(list_num[-1]) >= 5:
        #print(int(list_num[0]) + 1)
        return int(list_num[0]) + 1
    else:
        return int(list_num[0])


num_str = input('请输入正浮点数：\n')
print('正浮点数的近似值：',calculate(num_str))