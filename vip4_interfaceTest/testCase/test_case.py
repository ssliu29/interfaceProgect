#coding = utf-8

import unittest,json
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
    def test_request(self , id ,url  ,method ,param ,expect):
        #3.根据测试数据，调用对应的接口方法，完成接口请求
        if method == 'get' or method =='GET':
            # #请求get方法
            # 4.获取实际结果
            resultdata =result.get(url,param)
            real = json.loads(resultdata)['errorCode']
            #使用try-except接受异常，来判断断言是否成功
            try:
                self.assertEqual(str(expect),str(real))
                status = "成功"
            except AssertionError as msg:
                print(msg)
                status = "失败"

        elif method == 'post' or method =='POST':
            #请求post方法
            # 4.获取实际结果
            resultdata = result.post(url,param)
            print(type(resultdata))
            real = json.loads(resultdata)['errorCode']
            try:
                # 5.将实际结果与预期结果进行比对
                self.assertEqual(str(expect),str(real))
                status = "Fail"
            except AssertionError as msg:
                print(msg)
                status ="Fail"
            finally:
                # 6.将接口执行状态写入excel
                if status == None:
                    writeData.writeData(id,real,'Success')
                else:
                    writeData.writeData(id,real,'Fail')


if __name__ == '__main__':
    unittest.main()    #运行所有的用例
    # mycase = MyTestCase()
    # mycase.test_request()

