# encoding:utf-8
'''
如何使用sys.argv:
1、sys.argv 是一个数组 第一个元素是程序本身路径
2、sys.argv 实现从程序外部向程序传递参数。
'''


'''
小结：
1、sys.argv 实现从程序外部向程序传递参数
2、传入的第一个参数为脚本文件名
3、传入程序的每一个参数以空格 隔开
4、传入程序的参数均以字符串的类型存储，命令行中不需要加引号
'''

from sys import argv

print('arge是一个数组:',argv)
