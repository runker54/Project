# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-09-03
# -------------------------------------------------------------------------------
import arcpy
import xlrd
data_path = r"E:\台账\织金县\织金县20200814验证\调度表.gdb\point"  # 地理数据路径
lon_lat_path = r"C:\Users\65680\Desktop\新建 XLS 工作表.xls"

arcpy.AddField_management(data_path, "编号")
arrayCoordenades = []
read_work_book = xlrd.open_workbook(lon_lat_path)
read_work_sheet = read_work_book.sheet_by_index(0)
rows = read_work_sheet.nrows
for one_row in range(1, rows):
    lon_lat = read_work_sheet.row(one_row)[2].value, read_work_sheet.row(one_row)[3].value, read_work_sheet.row(one_row)[1].value
    arrayCoordenades.append(lon_lat)
with arcpy.da.InsertCursor(data_path, ["SHAPE@X", "SHAPE@Y", "编号"]) as cursor:
    for row in arrayCoordenades:
        print(row)
        cursor.insertRow(row)
