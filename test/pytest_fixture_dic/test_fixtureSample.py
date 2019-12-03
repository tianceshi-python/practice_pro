# encoding:utf-8
import pytest

@pytest.fixture()
def before():
    print(' \nbefore each test')

def test_1(before):
    print('test_1()')


def test_2(before):
    print('test_2()')
    assert 0



if __name__ == '__main__':
    #pytest.main(['-v','test_fixtureSample.py'])
    pytest.main(['-s', 'test_fixtureSample.py'])