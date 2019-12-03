# encoding:utf-8

'''
需求2：有些用例不能在预发布环境或者生产环境运行，怎么跳过该用例
'''

'''
小结:
1、从上面的例子可以了解，如何通过sys.argv传入环境参数，虽然上文是用百度首页作为例子，但同时引出，我们在做自动化测试时候，实现一套代码多环境运行思路

2、命令行带参数启动脚本，在Unittest中，可以实现不同的测试环境可以跳过用例
'''

from selenium import webdriver
from sys import argv
from time import sleep
import unittest

URL = argv[-1]
print('argv[-1]:',URL)

class TestEvn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @unittest.skipIf(URL !='https://www.baidu.com', '条件为true，用例二跳过')
    def test_load_page(self):
        self.driver.get(URL)
        sleep(10)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestEvn('test_load_page'))
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suit)
