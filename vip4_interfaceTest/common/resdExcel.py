#coding = utf-8

import xlrd  #1.导入读取excel的包


#2.打开Excel文件
readbook = xlrd.open_workbook(r'D:\python_project\vip4_interfaceTest\testData\data.xls')
#print(readbook)
#3.获取Excel，定位文件的sheet页
#urlsheet = readbook.sheet_by_index(1)            #方法一：根据下标定位sheet页，索引的方式从0开始
#urlsheet = readbook.sheet_by_name('urlSheet')    #方法二：根据name定位sheet页

urlsheet = readbook.sheet_by_name('urlSheet')
urllineNum = urlsheet.nrows
paramsheet = readbook.sheet_by_name('paramSheet')
paramlineNum = paramsheet.nrows
assertsheet = readbook.sheet_by_name('assertSheet')
assertlineNum = paramsheet.nrows

#4.定位行和列
'''
urllineNum = urlsheet.nrows    #获取循环的次数
for i in range(1,urllineNum):
    urldata = urlsheet.row_values(i)
    print(urldata)

paramlineNum = paramsheet.nrows
for j in range(1,paramlineNum):
    paramdata = paramsheet.row_values(j)
    print(paramdata)

assertlineNum = paramsheet.nrows
for k in range(1,assertlineNum):
    assertdata = assertsheet.row_values(k)
    print(assertdata)
'''

def getSheetData(num,sheetName):
    data = []
    for i in range(1, num):
        urldata = sheetName.row_values(i)
        data.append(urldata)
    return data

urlsheetData = getSheetData(urllineNum , urlsheet)
paramsheetData = getSheetData(paramlineNum , paramsheet)
assertsheetData = getSheetData(assertlineNum , assertsheet)
print(urlsheetData)
# tepData = list(zip(urlsheetData,paramsheetData))
# data = list(zip(tepData,assertsheetData))
# print(data)

a = [[11,12,13],[14,15,16]]
b = [[21,22,23],[24,25,26]]
for n,m in a:
    c =[]
    
print(c)