# encoding:utf-8

def dup_removal(str):
    list1 = list(str)   #set()是列表的操作函数，需要将字符串转换成列表形式在操作
    print(list1)
    list1 = list(set(str))
    return list1

def dup_count(str):
    a = {}
    for i in str:
        a[i] = str.count(i)
    return a


data = [1,2,1,1,1,2,2,2,2,3,4,4,4,4,5,5,6,6,6,6,8]
str = r'11112245799655444333333333222222111'
print(dup_removal(str))
print('每个数字重复显示的个数：',dup_count(str))