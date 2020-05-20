# encoding:utf-8

def hello(fn):      #用来做回调的函数
    def wrapper():
        print('hello,%s'%fn.__name__)
        fn()
        print('goodbye,%s'%fn.__name__)
    return wrapper       #decorator必需得返回了一个函数出来给func



@hello
def foo():
    print('i im foo')


foo()     #foo= hello(foo)   就是把一个函数当参数传到另一个函数中，然后再回调

'''
1、把decorator这个函数的返回值赋值回了原来的func;
2、decorator必需得返回了一个函数出来给func
'''


def funk(fn):
    print('funk %s!'%fn.__name__[::-1].upper())

@funk
def wfg():
    pass