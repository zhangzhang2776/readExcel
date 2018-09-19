#coding=utf-8
'''
Created on 2018年9月10日

@author: my
'''
import xlrd
#from my.readExcel_1 import cell_value

#路径前加 r，读取的文件路径
file_path = r'E:/HQMS.xlsx'
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
# #获取一个单元格的数值，例如第5行第6列
# cell_value = table.cell(1,1).value
sql='('
sql1='('
sql2=''
for i in range(1,nrows-1):
    cell_value = table.cell(i,0).value
    sql+=cell_value+','
    cell_value1=table.cell(i,1).value.replace('\n','')
    cell_value2=table.cell(i,2).value
    if(cell_value1==''):
        cell_value1='\'\''
    if('and' in cell_value1):
        #cell_value1='(select '+cell_value1.replace('and', 'from '+cell_value1+' where')+')'
        cell_value2_1=cell_value1.split('and')      
        cell_value1='case when '+cell_value2_1[1] +' then '+cell_value2_1[0]+' end '
    sql1+=cell_value1+' '+cell_value+','+'\n'
print('insert into hqms'+sql+table.cell(i+1,0).value+')'+'\n'+'values'+'\n'+'select'+sql1+table.cell(i+1,1).value+' '+table.cell(i+1,0).value+')'+'\n'+'  FROM INPATIENT_MEDICAL_RECORD, DIAGNOSIS,GENERAL_OPERATION_RECORDS, PATIENT '+'\n'
 'WHERE PATIENT.PATIENT_DOMAIN_ID =  INPATIENT_MEDICAL_RECORD.PATIENT_DOMAIN_ID'+
  ' AND PATIENT.PATIENT_LOCAL_ID = INPATIENT_MEDICAL_RECORD.PATIENT_LOCAL_ID'+
  ' AND PATIENT.OUTPATIENT_NO = DIAGNOSIS.OUTPATIENT_NO'+
  ' AND PATIENT.PATIENT_DOMAIN_ID = GENERAL_OPERATION_RECORDS.PATIENT_DOMAIN_ID'+
   'AND PATIENT.PATIENT_LOCAL_ID =  GENERAL_OPERATION_RECORDS.PATIENT_LOCAL_ID' +'\n')
print('\n')
#print(sql1)
    #print('insert into hqms ('+cell_value+','+')' )
    #print(cell_value)
    
    


#print(nrows)
#print(ncols)
#print(rowvalue)
#print(col_values)