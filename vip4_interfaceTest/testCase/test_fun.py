#coding=utf-8

from testCase.myfun import add,multi
import unittest

class myTest(unittest.TestCase):

    def setUp(self):
        print('执行setup方法')

    def tearDown(self):
        print('执行tearDown方法')

    def test_add(self):
        result = add(1,2)
        self.assertEqual(add(1,2),3)

    def test_mul(self):
        self.assertEqual(multi(1,2),2)

if __name__ == '__main__':
    #suite =unittest.TestSuite()
    unittest.main