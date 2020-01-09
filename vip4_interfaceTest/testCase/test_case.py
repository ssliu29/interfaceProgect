#coding = utf-8

import unittest
from ddt import ddt,data,unpack
from common.readExcel import getExcelData
from common.writeExcel import writeExcel
from common.configHttp import ConfigHttp

'''
1.导入目标模块或包
2.调用resdExcel模块，获取测试数据
3.根据测试数据，调用对应的接口方法，完成接口请求
4.获取实际结果
5.将实际结果与预期结果进行比对
6.将接口执行状态写入excel
'''

# 2.调用resdExcel模块，获取测试数据
excelData = getExcelData()
test_data = excelData.assembleData()
print(test_data)

#调用confighttp内部方法
result =ConfigHttp()
#print(result)

#实例化writeExcel类
writeData = writeExcel()

@ddt
class MyTestCase(unittest.TestCase):

    @ddt
    @data(*test_data)
    @unpack
    def test_request(self,id,url,name,method,param,expect):
        #3.根据测试数据，调用对应的接口方法，完成接口请求
        if method == 'get' or method =='GET':
            # #请求get方法
            # 4.获取实际结果
            resultdata =result.get(url,param)
            self.assertEqual(str(resultdata),str(expect))
            #使用try-except接受异常，来判断断言是否成功
            try:
                self.assertEqual(str(resultdata),str(expect))
                status = "成功"
            except AssertionError as msg:
                print(msg)
                status = "失败"

        elif method == 'post' or method =='POST':
            #请求post方法
            # 4.获取实际结果
            resultdata = result.post(url,param)
            # 5.将实际结果与预期结果进行比对
            self.assertEqual(str(resultdata),expect)
            try:
                self.assertEqual(str(resultdata),str(expect))
                status = "Fail"
            except AssertionError as msg:
                print(msg)
                status ="Fail"

        elif method == 'put' or method =='PUT':
            #请求post方法
            pass
        elif method == 'delete' or method =='DELETE':
            #请求post方法
            pass

        #6.将接口执行状态写入excel
        writeData.addWriteExcel(id,resultdata,status)


if __name__ == '__main__':
    unittest.main()
    # mycase = MyTestCase()
    # mycase.test_request()

