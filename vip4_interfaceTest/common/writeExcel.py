#coding:utf-8
import xlrd
import xlwt
from xlutils.copy import copy

class writeExcel(object):

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
