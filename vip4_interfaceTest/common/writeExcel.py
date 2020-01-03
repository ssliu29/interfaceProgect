#coding:utf-8
import xlrd

class writeExcel(object):

    def __init__(self,result,status):
        print('将实际结果和执行状态写入excel')
        pass

    def write(self, openpyxl):
       outwb = openpyxl.Workbook()  #打开一个将写的文件
       outws = outwb.creat_sheet(index=0) #在将写的文件中创建sheet
       for row in range(1,70000):
           for col in range(1,4):
               outws.cell(row,col).value = row * 2   #写文件
            print(row)
        saveExcel = "D:\\python_project\vip4_interfaceTest\testReport\test.xlsx"
       outwb.save(saveExcel)     #保存文件
