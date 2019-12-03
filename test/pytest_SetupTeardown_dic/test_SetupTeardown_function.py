# encoding:utf-8

'''
只对函数用例生效，不在类中
setup_function
teardown_function
'''


import pytest


def setup_function():
    print('\nsetup_function:每个方法之前执行')


def teardown_function():
    print('teardown_function:每个方法之后执行')


def test_01():
    print('正在执行test1')
    x = 'this'
    assert 'h' in x


def test_02():
    print('正在执行test2')
    x = 'hello'
    assert hasattr(x , 'hello')


def test_add():
    print('正在执行test_add')
    fruits = {"apple", "banana", "cherry"}
    fruits.add("orange")
    print(fruits)
    assert 'orange' in fruits


if __name__ == '__main__':
    pytest.main(['-s','test_SetupTeardown_function.py'])



