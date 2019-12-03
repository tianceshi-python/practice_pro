# encoding:utf-8

'''
scope="module"

fixture为module时，在当前.py脚本里面所有用例开始前只执行一次。
'''

import  pytest

@pytest.fixture(scope='module')
def test1():
    b = '男'
    print('\n传出了%s， 且在当前py文件下执行一次！！！' % b)
    return b


def test3(test1):
    name = 'leo'
    print('找到name')
    assert test1 == name


class Testcase:
    def test4(self,test1):
        sex = '男'
        print('找到sex')
        assert test1 == sex


if __name__ =='__main__':
    pytest.main(['-s', 'test_fixture_scopeMoudle.py'])                  #显示 print内容
    #pytest.main(['-v', 'test_fixture_scopeMoudle.py'])
    #pytest.main(['-q', 'test_fixture_scopeMoudle.py'])