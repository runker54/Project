# coding: utf-8
import arcpy
import arcpy.da
import os
import xlwt
import xlrd

# 成果数据所在位置
# workbook = xlwt.Workbook(encoding='utf-8')
# sheet = workbook.add_sheet('name', cell_overwrite_ok=True)

layersdata = ur"E:/Space.gdb/成果数据_1"

# 创建游标遍历图层
with arcpy.da.UpdateCursor(layersdata,
                        ['LBBM', 'FXZQMC', 'TXZQMC', 'XZQMC', 'ZLLB', 'CQCS', 'ZXLON', 'ZXLAT', 'SUM_MJ_MU']) as cursor:
    # 创建空列表接受信息

    for row in cursor:
        if row[5] == '':
            row[5] = "无措施"
        # print(row[6])
        # print(row[7])
        # print(row[8])
        row[6] = '%.6f' % row[6]
        row[7] = '%.6f' % row[7]
        row[8] = '%.1f' % row[8]
        # print(row[6])
        # print(row[7])
        # print(row[8])
        cursor.updateRow(row)
with arcpy.da.SearchCursor(layersdata,['LBBM', 'FXZQMC', 'TXZQMC', 'XZQMC', 'ZLLB', 'CQCS', 'ZXLON', 'ZXLAT', 'SUM_MJ_MU']) as cursor1:
    data_list = []
    for row in cursor:
        data_list.append(row)
# 读取信息
workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('data', cell_overwrite_ok=True)
r = 0
c = 0
title_list = ['LBBM', 'FXZQMC', 'TXZQMC', 'XZQMC', 'ZLLB', 'CQCS', 'ZXLON', 'ZXLAT', 'SUM_MJ_MU']
# 写入题头
for message in data_list:
    if r == 0:
        for title in title_list:
            sheet.write(r, c, title)
            c += 1
    else:
        for sheet_data in message:
            sheet.write(r, c, sheet_data)
            c += 1
    c = 0
    r += 1





workbook.save("123456.xls")

