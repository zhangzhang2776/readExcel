'''
Created on 2018年9月11日

@author: my
'''
#coding=utf-8
'''
Created on 2018年9月10日

@author: my
'''
import xlrd
import operator

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
rowvalue = table.row_values(1)
#获取一列的数值，例如第6列
col_values = table.col_values(1)
#获取一个单元格的数值，例如第5行第6列
cell_value = table.cell(1,1).value
sql='('
sql1='('
sql2='('
sql3='('
sql5='( SELECT '
sql6='( SELECT '
sql7='( SELECT '
sql8='( SELECT '
count=0
count1=0
count2=0
count3=0

for i in range(1,nrows):
    cell_value = table.cell(i,2).value.strip()
    #print(cell_value)
    cell_value1=table.cell(i,0).value
    cell_value2=table.cell(i,1).value
    if('INPATIENT_MEDICAL_RECORD' in cell_value):                
        sql+=cell_value1+','
        sql5+=cell_value2+','+'\n'
        count+=1
    if('GENERAL_OPERATION_RECORDS' in cell_value):
        sql1+=cell_value1+','
        sql6+=cell_value2+','+'\n'
        count1+=1
    if('DIAGNOSIS' in cell_value):
        if('and' in cell_value2):
            cell_value2_1=cell_value2.split('and')
            #print(cell_value2_1[1])
            #print(cell_value2_1[0])
            #print('case when '+cell_value2_1[1] +' then '+cell_value2_1[0]+' end,')
            #cell_value2='( select '+cell_value2.replace('and', 'from  DIAGNOSIS where')+')'
            cell_value2='case when '+cell_value2_1[1] +' then '+cell_value2_1[0]+' end'
        sql2+=cell_value1+','
        sql7+=cell_value2+','+'\n'
        count2+=1
    if(operator.eq('PATIENT',cell_value)):
        sql3+=cell_value1+','
        sql8+=cell_value2+','+'\n'
        count3+=1

#关联查询
print('insert into HQMS' + sql+')'+'\n'+'values'+sql5+'  FROM INPATIENT_MEDICAL_RECORD, DIAGNOSIS,GENERAL_OPERATION_RECORDS, PATIENT '+'\n'
 'WHERE PATIENT.PATIENT_DOMAIN_ID =  INPATIENT_MEDICAL_RECORD.PATIENT_DOMAIN_ID'+
  ' AND PATIENT.PATIENT_LOCAL_ID = INPATIENT_MEDICAL_RECORD.PATIENT_LOCAL_ID'+
  ' AND PATIENT.OUTPATIENT_NO = DIAGNOSIS.OUTPATIENT_NO'+
  ' AND PATIENT.PATIENT_DOMAIN_ID = GENERAL_OPERATION_RECORDS.PATIENT_DOMAIN_ID'+
   'AND PATIENT.PATIENT_LOCAL_ID =  GENERAL_OPERATION_RECORDS.PATIENT_LOCAL_ID' +'\n')
print('insert into HQMS' + sql1+')'+'\n'+'values'+sql6+'  FROM INPATIENT_MEDICAL_RECORD, DIAGNOSIS,GENERAL_OPERATION_RECORDS, PATIENT '+'\n'
 'WHERE PATIENT.PATIENT_DOMAIN_ID =  INPATIENT_MEDICAL_RECORD.PATIENT_DOMAIN_ID'+
  ' AND PATIENT.PATIENT_LOCAL_ID = INPATIENT_MEDICAL_RECORD.PATIENT_LOCAL_ID'+
  ' AND PATIENT.OUTPATIENT_NO = DIAGNOSIS.OUTPATIENT_NO'+
  ' AND PATIENT.PATIENT_DOMAIN_ID = GENERAL_OPERATION_RECORDS.PATIENT_DOMAIN_ID'+
   'AND PATIENT.PATIENT_LOCAL_ID =  GENERAL_OPERATION_RECORDS.PATIENT_LOCAL_ID' +'\n')
print('insert into HQMS' + sql2+')'+'\n'+'values'+sql7+' FROM INPATIENT_MEDICAL_RECORD, DIAGNOSIS,GENERAL_OPERATION_RECORDS, PATIENT '+'\n'
 'WHERE PATIENT.PATIENT_DOMAIN_ID =  INPATIENT_MEDICAL_RECORD.PATIENT_DOMAIN_ID'+
  ' AND PATIENT.PATIENT_LOCAL_ID = INPATIENT_MEDICAL_RECORD.PATIENT_LOCAL_ID'+
  ' AND PATIENT.OUTPATIENT_NO = DIAGNOSIS.OUTPATIENT_NO'+
  ' AND PATIENT.PATIENT_DOMAIN_ID = GENERAL_OPERATION_RECORDS.PATIENT_DOMAIN_ID'+
   'AND PATIENT.PATIENT_LOCAL_ID =  GENERAL_OPERATION_RECORDS.PATIENT_LOCAL_ID' +'\n')
print('insert into HQMS' + sql3+')'+'\n'+'values'+sql8+' FROM INPATIENT_MEDICAL_RECORD, DIAGNOSIS,GENERAL_OPERATION_RECORDS, PATIENT '+'\n'
 'WHERE PATIENT.PATIENT_DOMAIN_ID =  INPATIENT_MEDICAL_RECORD.PATIENT_DOMAIN_ID'+
  ' AND PATIENT.PATIENT_LOCAL_ID = INPATIENT_MEDICAL_RECORD.PATIENT_LOCAL_ID'+
  ' AND PATIENT.OUTPATIENT_NO = DIAGNOSIS.OUTPATIENT_NO'+
  ' AND PATIENT.PATIENT_DOMAIN_ID = GENERAL_OPERATION_RECORDS.PATIENT_DOMAIN_ID'+
   'AND PATIENT.PATIENT_LOCAL_ID =  GENERAL_OPERATION_RECORDS.PATIENT_LOCAL_ID' +'\n')

# 
# print(count)
# print('\n')
# print(count1)
# print('\n')
# print(count2)
# print('\n')
# print(count3)

