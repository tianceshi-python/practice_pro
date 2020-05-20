# encoding:utf-8
'''
利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法.
'''

def trim1(s):
    if s[:1] == ' ':
        s = s[1:]
    if s[-1:] == ' ':
        s = s[:-1]
    return s


def trim2(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


if __name__ == '__main__':
    s1 = ' l '
    s2 = 'y jik ooo  '
    print(s1)
    print(trim1(s1))
    print(s2)
    print(trim2(s2))




