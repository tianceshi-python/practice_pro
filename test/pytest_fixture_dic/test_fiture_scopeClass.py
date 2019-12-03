# encoding:utf-8
'''
scope="class"

fixture为class级别的时候，如果一个class里面有多个用例，都调用了此fixture，那么此fixture只在此class里所有用例开始前执行一次。
'''

import pytest


@pytest.fixture(scope='class')
def test1():
    b = '男'
    print('\n传出了%s，且只有在class里面所有用例开始前执行一次！！！！'%b)
    return b


class Testcase:
    def test3(self,test1):
        name = 'leo'
        print('找到name')
        assert test1 == name

    def test4(self,test1):
        sex = '男'
        print('找到sex')
        assert test1 == sex


if __name__ =='__main__':
    #pytest.main(['-s', 'test_fixture_scopeClass.py'])                  #显示 print内容
    pytest.main(['-v', 'test_fixture_scopeClass.py'])
    #pytest.main(['-q', 'test_fixture_scopeClass.py'])
