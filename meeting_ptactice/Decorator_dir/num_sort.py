# encoding:utf-8

def oprater(string):
    str_list = string.split(',')
    result = []
    for i in str_list:
        if i not in result:
            result.append(i)
        else:
            pass
    return result.sort()



n = input('请输入需要排序的个数')
inputArray = input()