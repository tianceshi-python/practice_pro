# encoding:utf-8

'''
要求：
　　1. 不能依赖库函数直接实现此功能，需使用基础的数据结构实现
　　2. 时间复杂度 O(n)
思路：

　　1. 用字典存储每个字符在字符串中出现的次数
　　2. 列表是有序的，用来存储字符的出现先后
　　3. 最后，从前向后遍历列表，找出第一个出现次数为1的字符，即为符合条件的字符
'''


def find_str(string):
    str_dic = {}   #字典键设置为字符，值为其出现的次数
    str_ls = []    #将字符串中字符顺序存入列表
    for i in string:
        if i not in str_dic.keys():
            str_dic[i] = 1
            str_ls.append(i)
        else:
            str_dic[i] += 1
    print('str_dic:',str_dic)
    print('str_ls:',str_ls)

    for j in str_ls:
        if str_dic[j] == 1:
            print('查询的符合字典结果的数据是:',j)
            return j         #查找字典中出现次数为1，并且返回排在最前面的字符
        else:
            pass
    return ('没有符合的数据!!')



if __name__ == '__main__':
    string = input('请输入需要操作的字符串:\n')
    print('result is :',find_str(string))