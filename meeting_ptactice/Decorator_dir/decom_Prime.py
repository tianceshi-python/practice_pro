# encoding:utf-8

'''
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
最后一个数后面也要有空格

详细描述：
函数接口说明：
public String getResult(long ulDataInput)

输入参数：
long ulDataInput：输入的正整数

返回值：
String
'''


def decom_Prime(num):
    prime_list = []
    temp = 2
    if num == 2:
        prime_list.append(num)
        print('2的质数是它本身')
    else:
        while num >= 2:
            if num % temp == 0:
                prime_list.append(str(temp))
                num = num / temp
            else:
                temp = temp + 1

    prime_list.sort(reverse=True)
    prime_str = ' '.join(prime_list) + ' '
    return prime_str


num = input('请输入正整数：')
num = int(num)
print(decom_Prime(num))

