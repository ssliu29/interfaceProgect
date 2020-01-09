import unittest
import HTMLTestRunner

from test_fun import myTest

suite = unittest.TestSuite()
suite.addTest(myTest('test_add'))

filename = "./test.html"

fp = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='单元测试报告',description='这是描叙')

runner.run(suite)

fp.close()

# discover = unittest.defaultTestLoader.discover('D:\python_project\vip4_interfaceTest\testCase\test_fun.py', pattern='test_fun*.fun',
#                                                top_level_dir=None)
# print('--discover', discover)
# runner = unittest.TextTestRunner()
# runner.run(discover)