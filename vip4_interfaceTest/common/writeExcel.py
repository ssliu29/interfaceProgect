#coding:utf-8
import xlrd
import xlwt
from xlutils.copy import copy
import  os

class writeExcel(object):
    '''
        def __init__(self):
            mybook = self.xlrd.open_Workbook()  # 打开一个将写的文件
            #复制目标对象
            self.wb = copy(mybook)
            #获取目标sheet页
            self.ws =self.wb.get_sheet(2)

        def addWriteExcel(self,id, realt,status):
            self.ws.write(id,2,realt)
            self.ws.write(id,3,status)
            self.wb.save(r'../testData/data.xls')     #保存文件

    '''

    dir = 'testData'
    excel_dir = os.path.dirname(os.getcwd()) + "\\" + dir
    excel_dir = os.getcwd() + "\\" + dir
    print('excel_dir',excel_dir)
    rb = xlrd.open_workbook(excel_dir + '\\' + 'data.xls')
    #rs = rb.sheet_by_index(2)
    wb = copy(rb)
    #通过get_sheet()获取的sheet有write（）方法
    ws = wb.get_sheet(2)

    def writeData(self,id,real,status):
        try:
            print('写入')
            #根据id写入对应的实际结果和接口测试状态
            self.ws.write(id,2,real)
            self.ws.write(id,3,status)
            self.ws.save(self.excel_dir + '\\' + 'data.xls')
        except Exception as msg:
            print(msg)




