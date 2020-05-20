# encoding:utf-8
def string_sort(num):
    num = int(num)
    list_str = []
    while num > 0:
        string = input('请输入一个字符串：\n')
        if len(string) <= 100 and string.isalpha() == True:
            list_str.append(string)
            num = num - 1
        else:
            print('请重新输入一个字符串！！')

    list_str.sort()
    return list_str


num = input()
list_str = string_sort(num)
for i in list_str:
    print(i)
    #print('\n')