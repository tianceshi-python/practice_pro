# encoding:utf-8

'''
在类之前和之后执行一次
setup_class
teardown_class
'''
import pytest

class Testclass(object):

    def setup_class(self):
        print('\nsetup_class：每个类之前运行一次')


    def teardown_class(self):
        print('teardown_class:每个类之后执行一次')

    def add(self,a,b):
        print('这是加法运算')
        return a + b

    def test_01(self):
        print('正在执行test1')
        x = 'hello'
        assert  'h' in x


    def test_02(self):
        print('正在执行test2')
        assert self.add(3,4) == 7




if __name__ == '__main__':
    pytest.main(['-s','test_SetupTeardown_class.py'])


