#!/usr/bin/python
# -*- coding: gbk -*-
import xlrd,xlwt
from xlutils.copy import  copy
import sys


def t(obj):
    print type(obj)
filename = 'C:\\Users\\wushuang\\Desktop\\baby\\mk watch I\\2.xlsx'

to_filename = 'C:\\Users\\wushuang\\Desktop\\baby\\mk watch I\\1.xls'
style = xlwt.easyxf('font: underline single')

#ʹ�� xlutils ��xlrd���������ļ�copy��xlwt����д���ļ���
data = xlrd.open_workbook(filename)
table = data.sheet_by_index(0)
"""
for row_index in range(table.nrows):
    for col_index in range(table.ncols):
        print xlrd.cellname(row_index,col_index),'-',
        print table.cell(row_index,col_index).value
t(table)
"""
"""
��ȡ���к����е�ֵ�����飩
 ����
table.row_values(i)

table.col_values(i)

��ȡ����������
����
nrows = table.nrows

ncols = table.ncols

ѭ�����б�����
for i in range(nrows ):
    print table.row_values(i)

"""
wb = copy(data)
#print type(wb)
ws = wb.get_sheet(0)


for i in range(table.nrows):
    if i > 1:
        #print table.cell_value(i,0)
        tmp_value = table.cell_value(i,0)
        path = 'HYPERLINK("file:///C:\\Users\\wushuang\\Desktop\\baby\\mk watch I\\' + \
        str(i+1) + "\\" + '";"' + str(tmp_value) +'")'
        ws.write(
        i, 0,
        xlwt.Formula(path),
        style)


wb.save(to_filename)
