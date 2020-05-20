# encoding:utf-8
'''
python 全排列combinations和permutations函数
combinations方法重点在组合，permutations方法重在排列
还有就是，combinations和permutations返回的是对象地址，原因是在python3里面，返回值已经不再是list,而是iterators（迭代器）, 所以想要使用，只用将iterator 转换成list 即可， 还有其他一些函数返回的也是一个对象，需要list转换，比如 list(map())等 。

'''

import itertools

def num_line1(str):
    list_num = list(str)
    list_num01 = list(itertools.combinations(list_num,4))
    return list_num01


def num_line2(str):
    list_num = list(str)
    list_num02 = list(itertools.permutations(list_num,3))
    return list_num02


if __name__ == '__main__':
    num_str = input('请输入多个不同的数字字符:')
    print(num_line1(num_str))
    sub_str = input('请输入不同的字母:')
    print(num_line2(sub_str))