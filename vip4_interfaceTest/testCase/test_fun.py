#coding=utf-8

from testCase.myfun import add,multi
import unittest

class myTest(unittest.TestCase):

    def setUp(self):
        print('执行setup方法')

    def tearDown(self):
        print('执行tearDown方法')

    def test_add(self):
        self.assertEqual(add(1,2),3)

    def test_mul(self):
        self.assertEqual(multi(1,2),2)

if __name__ == '__main__':
    # 默认加载所有的test开头的方法到测试套件，如果想自定义运行的方法则需要通过手动添加的方式
    unittest.main


    # 手动添加：1.实例化测试套件类
    suite = unittest.TestSuite()
    # 2.调用addTest方法向测试套件中添加测试方法（类名.方法名---方法后面不要加括号）
    suite.addTest(myTest.test_add())

    print('suite', suite)
    # 运行测试套件：1.实例化测试运行类
    runner = unittest.TextTestRunner()
    # 2.运行测试套件
    runner.run(suite)