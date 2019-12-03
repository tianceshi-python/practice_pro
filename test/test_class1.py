# encoding:utf-8

# content of test_class1.py
import pytest

class TestClassOne():
    def test_one(self):
        x = "this"
        #print('1...')
        assert  'h' in x

    def test_two(self):
        x = "hello"
        #print('2...')
        assert  hasattr(x , 'check')

class TestClassTwo():
    def test_one(self):
        x = "iphone"
        #print('3...')
        assert  'p' in x

    def test_two(self):
        x = "apple"
        #print('4...')
        assert  hasattr(x , 'check')

if __name__ == '__main__':
    pytest.main(['-s','test_class1.py'])