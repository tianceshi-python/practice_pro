# encoding:utf-8

'''
fixture 返回值:
如果你的fixture需要配置一些数据，读个文件，或者连接一个数据库，那么你可以让fixture返回这些数据或资源。

如何带参数:
fixture还可以带参数，可以把参数赋值给params，默认是None。
对于param里面的每个值，fixture都会去调用执行一次，就像执行for循环一样把params里的值遍历一次
'''

import pytest

@pytest.fixture(params=[1, 2, 3])
def test_data(request):
    return request.param


def test_one_2(test_data):
    print('test_data:%s' %test_data)
    assert test_data != 2

if __name__ == '__main__':
    pytest.main(['-v','test_fixture_param.py'])
    #pytest.main(['-s', 'test_fixtureSam1.py'])
