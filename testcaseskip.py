# encoding:utf-8
'''
Unittest跳过用例：
@unittest.skip(reason) ， 直接跳过被装饰的用例 ，reason用于填写跳过用例的原因
@unittest.skipIf(condition, reason) ， condition 如果为真，跳过被装饰的用例，reason用于填写跳过用例的原因
@unittest.skipUnless(condition, reason) ， condition如果为假，跳过被装饰的用例，reason用于填写跳过用例的原因
'''

import unittest

class SkipExample(unittest.TestCase):

    @unittest.skip('用例一无条件跳过')
    def test_case_one(self):
        print('..用例一...')

    @unittest.skipIf( 2>1 , '条件为true，用例二跳过')
    def test_case_two(self):
        print('..用例二...')

    @unittest.skipUnless( 3<2 ,'条件为false,用例三条跳过')
    def test_case_three(self):
        print('..用例三...')


if __name__ == '__main__':
    unittest.main(verbosity = 2)