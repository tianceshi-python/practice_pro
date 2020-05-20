# encoding:utf-8
import re

def cal_len(string):
    str_list = string.split(' ')
    print(str_list)
    return len(str_list[-1])




if __name__ == '__main__':
    string = input('请输入字符串：')

    compile = r'^[a-zA-Z\s]{0,5000}$'
    #p = re.compile(compile_str)
    #print('string is :',string)
    if len(string) < 5000:
        print('string is :', string)
        print(re.match(compile,string))
        if re.match(compile,string):
            print('输入合格：',string)
            len_str = cal_len(string)
            print('len_str is:',len_str)
        else:
            print ('输入只能是字母或空格，请重新输入!')
    else:
        print ('输入不得超过5000个字符，请重新输入!')