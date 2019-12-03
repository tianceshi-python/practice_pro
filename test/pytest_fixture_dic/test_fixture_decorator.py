# encoding:utf-8

'''
调用fixture的三种方式:
第一种是每个函数前声明;
第二种是封装在类里，类里的每个成员函数声明;
第三种是封装在类里在前声明

3种不同方式的运行结果都是一样
'''

import pytest


@pytest.fixture()
def before():
    print(' \nbefore each test')


#第一种是每个函数前声明;
@pytest.mark.usefixtures("before")
def test_1(before):
    print('test_1()')

@pytest.mark.usefixtures("before")
def test_2(before):
    print('test_2()')

#第二种是封装在类里，类里的每个成员函数声明;
class Test1:

    @pytest.mark.usefixtures("before")
    def test_3(self):
        print("test_1()")

    @pytest.mark.usefixtures("before")
    def test_4(self):
        print('test_2()')

#第三种是封装在类里在前声明
@pytest.mark.usefixtures("before")
class Test2:

    def test_5(self):
        print('test_1()')

    def test_6(self):
        print('test_2()')

if __name__ == '__main__':
    #pytest.main(['-v','test_fixture_decorator.py'])
    pytest.main(['-s', 'test_fixture_decorator.py'])