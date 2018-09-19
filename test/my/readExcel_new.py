#coding=utf-8
'''
Created on 2018年9月10日

@author: my
'''
import xlrd
#from my.readExcel_1 import cell_value

#路径前加 r，读取的文件路径
file_path = r'E:/t.xlsx'
#文件路径的中文转码
#file_path = file_path.encode('utf-8')
#获取数据
data = xlrd.open_workbook(file_path)
#获取sheet
table = data.sheet_by_name('Sheet1')
#获取总行数
nrows = table.nrows
#获取总列数
#ncols = table.ncols
#获取一行的数值，例如第5行
# rowvalue = table.row_values(1)
# #获取一列的数值，例如第6列
# col_values = table.col_values(1)
#获取一个单元格的数值，例如第5行第6列
#cell_value = table.cell(1,1).value
cell_value=''

for i in range(1,nrows,2):
    cell_value += table.cell(i,0).value+'\n'
print(cell_value)
print('\n')
