#coding = utf-8

import  unittest
from ddt import ddt,data,unpack
from common.resdExcel import getExcelData

'''
1.导入目标模块或包
2.调用resdExcel模块，获取测试数据
3.根据测试数据，调用对应的接口方法，完成接口请求
4.获取实际结果
5.将实际结果与预期结果进行比对
6.将接口执行状态写入exce
'''
@ddt
class MyCase(object):

    #2.调用resdExcel模块，获取测试数据
    def getData(self):
        data = getExcelData
        test_data = data.assembleData()
        print(test_data)
        return test_data

    @ddt
    @data()
    @unpack
    def test_request(self,id,url,name,method,param,expect):
        print('')

    def __init__(self):
        pass

    def send_request(self):
        pass