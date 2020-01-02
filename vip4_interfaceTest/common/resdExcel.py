#coding = utf-8

import xlrd  #1.导入读取excel的包

class getExcelData(object):

    def __init__(self):
        #2.打开Excel文件
        readbook = xlrd.open_workbook(r'..\testData\data.xls')     #运用相对路径的好处是在其他地方执行时不会出现找不到文件的情况
        #print(readbook)
        #3.获取Excel，定位文件的sheet页
        self.urlsheet = readbook.sheet_by_name('urlSheet')       #为什么要加self,实例化类的时候调用可以直接拿到
        # 4.定位行和列
        self.urlNum = self.urlsheet.nrows
        self.paramsheet = readbook.sheet_by_name('paramSheet')
        self.paramNum = self.paramsheet.nrows
        self.assertsheet = readbook.sheet_by_name('assertSheet')
        self.assertNum = self.paramsheet.nrows

    #5.读取sheet页内部的数据
    def getSheetData(self,num,sheetName):
        data = []
        for i in range(1, num):
            urldata = sheetName.row_values(i)
            data.append(urldata)
        return data

    #6.组装数据
    def assembleData(self):
    #调用获取sheet页数据的方法，分别拿到3个sheet页里面的数据
        urlList = self.getSheetData(self.urlNum,self.urlsheet)
        paramList = self.getSheetData(self.urlNum,self.paramsheet)
        assertList = self.getSheetData(self.urlNum,self.assertsheet)
        dataList = []
        #分别取出所有sheet页的第一行数据，进行组装
        for i in range(len(urlList)):
            new_urlList = urlList[i]            #取出URLList中的(第一个元素) 第一行
            #print(urlList[i])
            new_paramList = paramList[i][1:]     #取出paramList中的第一个元素 (第一行) 中除第一个元素之外的所有元素
            new_assertList = assertList[i][1:]   #取出assertList中的第一个元素 (第一行) 中除第一个元素之外的所有元素
            new_urlList.append(new_paramList)    #将新的paramList和assertList分别追加进new_urlList中
            new_urlList.append(new_assertList)
            dataList.append(new_urlList)

        return dataList

if __name__=='__main__':       #好处是被别的方法调用时，不会执行内部的方法
    getData = getExcelData()
    print(getData.assembleData())

