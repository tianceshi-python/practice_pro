# encoding:utf-8

'''
开始于方法始末（在类中）
setup_method
teardown_method
'''

'''
执行结果： setup_class --》 setup_method -->test1 -->teardown_method --》setup_method --> test_add（）--》teardown_method --> teardown_class
'''
import pytest

class Testmethod(object):

    def setup_class(self):
        print('\nsetup_class:每个类之前运行一次')

    def teardown_class(self):
        print('teardown_class:每个类之后执行一次')

    def setup_method(self):
        print('\nsetup_method:每个方法之前运行一次')

    def teardown_method(self):
        print('teardown_method:每个方法之后运行一次')

    def add(self, a, b):
        print('这是加法运算')
        return a + b

    def test_01(self):
        print('正在执行test1')
        x = 'hello'
        assert 'h' in x

    def test_02(self):
        print('正在执行test2')
        assert self.add(3, 4) == 7

if __name__ == '__main__':
    pytest.main(['-s', 'test_SetupTeardown_method.py'])

