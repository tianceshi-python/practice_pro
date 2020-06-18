# encoding:utf-8
# @Time    : 2020/6/17 下午15:42
# @Author  : xueyan
# @File    : Shell.py


"""
封装执行shell语句方法
"""

import subprocess
import allure

'''
subprocess.Popen 详解：https://www.cnblogs.com/zhoug2020/p/5079407.html

用subprocess这个模块来产生子进程,并连接到子进程的标准输入/输出/错误中去，还可以得到子进程的返回值。
subprocess.Popen
subprocess模块定义了一个类： Popen
class subprocess.Popen( args,
      bufsize=0,
      executable=None,
      stdin=None,
      stdout=None,
      stderr=None,
      preexec_fn=None,
      close_fds=False,
      shell=False,
      cwd=None,
      env=None,
      universal_newlines=False,
      startupinfo=None,
      creationflags=0)
      
args:
args参数。可以是一个字符串，可以是一个包含程序参数的列表。要执行的程序一般就是这个列表的第一项，或者是字符串本身。
subprocess.Popen(["cat","test.txt"])
当shell=True时，如果arg是个字符串，就使用shell来解释执行这个字符串。如果args是个列表，则第一项被视为命令，
其余的都视为是给shell本身的参数。也就是说，等效于：
subprocess.Popen(['/bin/sh', '-c', args[0], args[1], ...])


subprocess.PIPE
一个可以被用于Popen的stdin 、stdout 和stderr 3个参数的特输值，表示需要创建一个新的管道。


communicate参数是标准输入，返回标准输出和标准出错

'''

class Shell:


    @staticmethod
    def invoke(cmd):
        print('cmd is: ',cmd)
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o