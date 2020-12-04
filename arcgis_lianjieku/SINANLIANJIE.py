# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-10-29
# -------------------------------------------------------------------------------
# coding:utf-8
import arcpy.da
import xlrd
data_path = r'F:\思南.gdb\T思南县消除中段1027_111_连接'
sheet_path = r'C:\Users\65680\Desktop\思南县表格.xls'
work_book = xlrd.open_workbook(sheet_path)
for i in [0]:
    ws = work_book.sheet_by_index(i)
    rows = ws.nrows
    print("*****************************************")
    print(rows)
    cx_dict = {}
    for row_1 in range(1, rows):
        key = str(ws.row(row_1)[0].value).strip()
        cx_dict[key] = row_1
    print(cx_dict)
    with arcpy.da.UpdateCursor(data_path,
                               ['ob', '主要作物19年', '主要作物20年']) as currsor:
        ic = 0
        for row in currsor:
            try:
                print('-----')
                print(row[0])
                print(row[1])
                print(row[2])

                row_temp = cx_dict[row[0]]
                row_sheet = ws.row(row_temp)
                print(row_sheet[0].value)
                print('+++++')
                # row[1] = row_sheet[1].value  # CQCS
                # row[2] = row_sheet[2].value  # 玉米19
                # row[3] = row_sheet[3].value  # 玉米20
                # row[4] = row_sheet[4].value  # 水稻19
                # row[5] = row_sheet[5].value  # 水稻20
                row[1] = str(row_sheet[1].value)  # 主要19
                row[2] = str(row_sheet[2].value)  # 主要20
                # row[8] = row_sheet[6].value  # 周边环境
                # mj = row_sheet[12].value       # 地块面积
                # if row_sheet[4].value != "":
                #     row[9] = row[13]
                # else:
                #     row[9] = 0
                # if row_sheet[5].value != "":
                #     row[10] = row[13]
                # else:
                #     row[10] = 0
                # if row_sheet[2].value != "":
                #     row[11] = row[13]
                # else:
                #     row[11] = 0
                # if row_sheet[3].value != "":
                #     row[12] = row[13]
                # else:
                #     row[12] = 0
                currsor.updateRow(row)
                ic += 1
            except:
                print("该%s未在表中" % row[0])
    print("9999999999999999999999999999999999999999999")
    print(ic)
