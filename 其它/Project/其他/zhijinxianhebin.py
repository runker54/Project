# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-08-29
# -------------------------------------------------------------------------------
import os
import xlrd
import xlwt
import time
data_path = r'C:\Users\65680\Desktop\桂果镇'

dir_list = os.listdir(data_path)
merge_sheet = xlwt.Workbook(encoding='utf-8')
merge_ws = merge_sheet.add_sheet("织金县_合并")
r = 1
for roots, dirs, files in os.walk(data_path):
    for file in files:
        if file[-3:].lower()=="xls":
            xls_path = os.path.join(roots, file)
            work_book = xlrd.open_workbook(xls_path)
            sheet_ = work_book.sheet_by_index(0)
            rows = sheet_.nrows
            columns = sheet_.ncols
            print("%s----%s++++++%s" % (xls_path, rows, sheet_.cell(1, 0).value))
            for row in range(1, rows):
                dkbm = sheet_.row(row)[0].value
                print(dkbm)
                qx = sheet_.row(row)[1].value
                xz = sheet_.row(row)[2].value
                xzc = sheet_.row(row)[3].value
                cqcs = sheet_.row(row)[4].value
                z19 = sheet_.row(row)[5].value
                z20 = sheet_.row(row)[6].value
                zbhj = sheet_.row(row)[7].value
                mj = sheet_.row(row)[8].value
                merge_ws.write(r, 0, dkbm)
                merge_ws.write(r, 1, qx)
                merge_ws.write(r, 2, xz)
                merge_ws.write(r, 3, xzc)
                merge_ws.write(r, 4, cqcs)
                merge_ws.write(r, 5, z19)
                merge_ws.write(r, 6, z20)
                merge_ws.write(r, 7, zbhj)
                merge_ws.write(r, 8, mj)
                r = r + 1
merge_sheet.save(r'C:\Users\65680\Desktop\织金县合并2.xls')
