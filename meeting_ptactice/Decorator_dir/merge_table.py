# encoding:utf-8
'''
题目描述
数据表记录包含表索引和数值（int范围的整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出描述:
输出合并后的键值对（多行）
'''


def add_key_value(num_key):
    key_values_dic= {}
    num_key = int(num_key)
    key_values = input('请输入键值对的索引index和值value，之间用空格隔开：\n')
    key_values_list = key_values.split(' ')
    key_values_dic[key_values_list[0]] = key_values_list[-1]
    num_key = num_key -1
    while num_key > 0:
        key_values = input('请输入键值对的索引index和值value，之间用空格隔开：\n')
        key_values_list = key_values.split(' ')
        print('key_values_list is :',key_values_list)
        #key_values_dic[key_values_list[0]] = key_values_dic[key_values_list[-1]]
        if  key_values_list[0] in key_values_dic.keys():
            key_values_dic[key_values_list[0]] = str(int(key_values_dic[key_values_list[0]]) + int(key_values_list[-1]))
        else :
            key_values_dic[key_values_list[0]] = key_values_list[-1]
            #print('key_values_dic[key_values_list[0]] is :', key_values_dic[key_values_list[0]])

        num_key = num_key - 1


    return key_values_dic









num_key = input('请输入键值对个数：\n')

print('结果是：',add_key_value(num_key))