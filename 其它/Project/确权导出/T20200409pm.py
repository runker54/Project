# coding: utf-8
import arcpy
import arcpy.da
import os
import xlwt
import xlrd

# 成果数据所在位置
workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('name', cell_overwrite_ok=True)

layersdata = "E:/Space.gdb/成果数据_1"
# fileds = arcpy.ListFields(layersdata)
# fileds_list = []
# for ID in fileds:
#     fileds_list.append(ID.name)
# new_list = fileds_list[2:-2]
# print(new_list)
# 创建游标遍历图层
with arcpy.da.SearchCursor(layersdata, ['LBBM', 'FXZQMC', 'TXZQMC', 'XZQMC', 'ZLLB', 'CQCS', 'ZXLON', 'ZXLAT','SUM_MJ_MU']) as cursor:
    # 创建空列表接受信息
    data_list = []
    for row in cursor:
        data_list.append(row)
# 读取信息
workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('data', cell_overwrite_ok=True)
r = 0
c = 0
title_list = ['LBBM', 'FXZQMC', 'TXZQMC', 'XZQMC', 'ZLLB', 'CQCS', 'ZXLON', 'ZXLAT','SUM_MJ_MU']
# 写入题头
for message in data_list:
    if r == 0:
        for title in title_list:
            data1 = str(title)
            sheet.write(r, c, data1)
            c += 1
    else:
        for sheet_data in message:
            data2 = str(sheet_data)
            sheet.write(r, c, data2)
            c += 1
    c = 0
    r += 1

workbook.save("12345.xls")
