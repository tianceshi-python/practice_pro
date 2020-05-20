# encoding:utf-8
'''
/**
 * 仿LISP字符串运算
 * LISP语言唯一的语法就是括号要配对。
 * 形如 (OP P1 P2 …)，括号内元素由单个空格分割。
 * 其中第一个元素OP为操作符，后续元素均为其参数，参数个数取决于操作符类型
 * 注意：参数 P1, P2 也有可能是另外一个嵌套的 (OP P1 P2 …)
 * 当前OP类型为add/sub/mul/div(全小写)，分别代表整数的加减乘除法。
 * 其中add/mul 参数个数为2个以上，sub/div参数个数为2个
 * 举例
 * -输入：(mul 3 -7)输出：-21
 * 输入：(add 1 2) 输出：3
 * 输入：(sub (mul 2 4) (div 9 3)) 输出 ：5
 * 输入：(sub (mul 2 (add 1 2 (sub 4 1))) (div 9 (div 9, 3))) 输出 9
 * 输入：(div 1 0) 输出：error
 */
'''
import re


#利用正则表达式，定义从输入的LISP字符串中，获取所有能计算的(OP P1 P2）表达式，OP是确切的计算符，P1  P2是确切的数字
def spiltStr(string):
    pattern = r'\S{3}\s\d+[\s\d+]{2,}'
    result = re.findall(pattern,string)
    #print( "result",result)
    return result

def replaceResult(string,lisp_list):
    print('replaceResult string is: ',string)
    print('replaceResult lisp_list is: ', lisp_list)
    for i in lisp_list:
        print(i)
        operator_result = lisp_op(i)
        # 给获取的lisp加上左右括号
        i = '(' + i + ')'
        #print(i)
        #除法运算的除数是0，则给string赋值error
        if operator_result == 'error':
            string = 'error'
        else:
            string = string.replace(i, operator_result)   # 将已经计算出结果的lisp表达式用结果替代
        print('str_result:', string)
    return string



def lisp_op(string):
    #获取字符串的前三个字符，即操作数
    operator = string[:3]
    # 获取需要计算的P1和P2值
    pattern = r'\d+'
    # 将所有的操作数放在一个列表中
    operatorP_list = re.findall(pattern, string)

    print(operatorP_list)

    if operator == 'add':
        operator_result = add(operatorP_list)
    elif operator == 'sub':
        operator_result = sub(operatorP_list)
    elif operator == 'mul':
        operator_result = mul(operatorP_list)
    elif operator == 'div':
        operator_result = div(operatorP_list)
    return operator_result


#定义加、减、乘、除的计算方法

def add(num_list):
    sum_num = int(num_list[0])
    num_list = num_list[1:]
    for i in num_list:
        sum_num = sum_num + int(i)
    return str(sum_num)

def sub(num_list):
    sub = int(num_list[0])
    num_list = num_list[1:]
    for i in num_list:
         sub = sub - int(i)
    return str(sub)


def mul(num_list):
    return str(int(num_list[0]) * int(num_list[1]))

def div(num_list):
    if int(num_list[1]) == 0:
        print('error')
        return 'error'
    else:
        return str(float(num_list[0]) / float(num_list[1]))



def lisp(string):
    while (string.partition('(')[-1]).find('(') != -1:
        result_list = spiltStr(string)
        string = replaceResult(string,result_list)
        print('string',string)
        if string == 'error':
            print('error')
            break

    '''
    else:
        lisp(string)
    #return string
    '''


if __name__ == '__main__':
    string = input('请输入需要计算的LISP:\n')
    lisp(string)