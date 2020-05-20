# encoding:utf-8
'''
问题：给定一个字符串，找出其中出现次数最多的字母？
拓展：如果出现次数一样的字母，按照字母顺序就输出第一个
思路： 利用collections 工具中的Counter,对列表中元素出现的频率进行排序。 Counter返回值是一个按元素出现频率降序排列的Counter对象，它是字典的子类，因此可以使用字典的方法
'''

from collections import Counter

def get_max_char_collec(string):
    count = Counter(string)
    # 以为count现在是一个对象，利用他的属性--count.values()取出其中的值
    count_list = list(count.values())
    max_value = max(count_list)
    max_list = []
    for k, v in count.items():
        if v == max_value:
            max_list.append(k)
    # max_list = sorted(max_list) #加这个排序的原因是，如果你找到 两个或两个以上的具有相同的频率的字母， 返回那个先出现在字母表中的字母
    # return max_list[0]
    return max_list



def get_max_char(string):
    can = ''  # 可以看做存放元素的变量
    count = 0  # 用来判断次数
    for i in range(len(string)):
        if count == 0:
            can = string[i]
            count += 1
        elif string[i] == can:
            count += 1
        else:
            count -= 1
    return (can)

def get_max_char_dic(string):
    str_dic = {}
    str_ls = []
    for i in string:
        if i not in str_dic.keys():
            str_dic[i] = 1
            str_ls.append(i)
        else:
            str_dic[i] += 1

    return str_dic,str_ls



if __name__ == '__main__':
    string = input('请输入需要计算个数的字符串：\n')
    #print('出现次数最多的字串是get_max_char：',get_max_char(string))
    #print('出现次数最多的字串是get_max_char_collec:',get_max_char_collec(string))

    str_dic,str_ls = get_max_char_dic(string)

    print('str_dic:',str_dic)    #记录每个字符出现的次数，字符是键，字符次数是值
    print('str_ls:',str_ls)

    sum_ls = list(str_dic.values())    #将每个字符出现的次数组成一个列表，以便统计列表中的最大值
    print('sum_ls',sum_ls)

    max_str = max(sum_ls)     #获取字符串中字符出现的最大次数

    for i in str_dic:
        if max_str == str_dic[i]:     #出现次数一样的字母，按照字母顺序就输出第一个
            print('出现次数最多的字串是get_max_char_dic:',i )     #
            break


