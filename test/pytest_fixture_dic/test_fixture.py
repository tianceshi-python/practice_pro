# encoding:utf-8
import pytest

@pytest.fixture()
def test1():
    a = 'leo'
    return a


def test2(test1):
    assert test1 == 'leo'
    print('测试用纸执行完毕。。。。')


if __name__ == '__main__':
    pytest.main(['-v','test_fixture.py'])
    #pytest.main(['-s', 'test_fixture.py'])