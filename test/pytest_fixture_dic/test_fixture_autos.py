# encoding:utf-8

'''
用autos调用fixture:
fixture decorator一个optional的参数是autouse, 默认设置为False。 当默认为False，就可以选择用上面两种方式来试用fixture。
当设置为True时，在一个session内的所有的test都会自动调用这个fixture。 权限大，责任也大，所以用该功能时也要谨慎小心。

fixture scope：session>module>class>function
function：每个test都运行，默认是function的scope(每一个函数或方法都会调用)
class：每个class的所有test只运行一次(每一个类调用一次，一个类中可以有多个方法)
module：每个module的所有test只运行一次(每一个.py文件调用一次，该文件内又有多个function和class)
session：每个session只运行一次(是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module)

比如你的所有test都需要连接同一个数据库，那可以设置为module，只需要连接一次数据库，对于module内的所有test，这样可以极大的提高运行效率。
'''

import  time
import pytest

@pytest.fixture(scope ='module',autouse=True)
def mod_header(request):
    print('\n---------------')
    print('module :%s' %request.module.__name__)
    print('---------------')

@pytest.fixture(scope="function", autouse=True)
def func_header(request):
    print('\n**********************')
    print('function : %s' % request.function.__name__)
    print('time : %s' % time.asctime())
    print('**********************')


def test_one():
    print('in test_one()')

def test_two():
    print('in test_two()')


if __name__ == '__main__':
    #pytest.main(['-v','test_fixture_autos.py'])
    pytest.main(['-s', 'test_fixtureSam1.py'])