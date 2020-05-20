# encoding:utf-8

'''
题目描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述:
连续输入字符串(输入2次,每个字符串长度小于100)

输出描述:
输出到长度为8的新字符串数组
'''


def printStr(string):
    if len(string) > 8:
        while (len(string) > 8):
            str1 = string[:8]
            print(str1)
            string = string[8:]

        str1 = string + '0' * (8 - len(string))
        print(str1)

    else:
        for i in range(len(string),8):
            string = string + '0'
        print(string)


string1 = input('请输入string1：\n')
string2 = input('请输入string2：\n')
printStr(string1)
printStr(string2)
