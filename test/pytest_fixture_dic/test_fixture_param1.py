# encoding:utf-8

import pytest

@pytest.fixture()
def test1():
    a = 'leo'
    b = '123456'
    print('传出a,b的值')
    return (a,b)


def test2(test1):
    u = test1[0]
    p = test1[1]
    assert  u == 'leo'
    assert p == '123456'


if __name__ == '__main__':
    #pytest.main(['-v', 'test_fixture_param1.py'])
    pytest.main(['-s', 'test_fixture_param1.py'])