# encoding:utf-8

'''
自动化测试项目中如何一套代码多套环境运行
需求1：一套代码可以测试多个环境，不希望每次测试不同环境的时候都要去改代码里面的URL，希望把代码里面的URL参数化
'''

from selenium import webdriver
from sys import argv
from time import sleep
import unittest

class TestEvn(unittest.TestCase):

    def setUp(self):
        self.url = argv[-1]
        print(self.url)
        self.driver = webdriver.Chrome()

    def test_load_page(self):
        self.driver.get(self.url)
        sleep(10)

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestEvn('test_load_page'))
    runner = unittest.TextTestRunner()
    runner.run(suit)



