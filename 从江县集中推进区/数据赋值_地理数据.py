#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2021-10-08
# Author:Runker54
# -----------------------
import arcpy
import xlrd

data_path = r'C:\Users\65680\Desktop\从江县集中推进区赋值\集中推进区图块.gdb\确权地块20210901'
sheet_path = r'C:\Users\65680\Desktop\从江县信息更新.xls'
work_book = xlrd.open_workbook(sheet_path, encoding_override="utf-8")
work_sheet = work_book.sheet_by_index(0)
data_dict = {}
rows = work_sheet.nrows
cols = work_sheet.ncols
for one_row in range(1, rows):
    nonghu_ = work_sheet.cell_value(one_row, 2)
    zubie_ = work_sheet.cell_value(one_row, 1)
# with arcpy.da.UpdateCursor(data_path, ['id_number', '组', '种植农户']) as currsor:
with arcpy.da.UpdateCursor(data_path, ['组', '种植农户']) as currsor:
    for one_row in currsor:
        print(one_row[0], one_row[1],)
