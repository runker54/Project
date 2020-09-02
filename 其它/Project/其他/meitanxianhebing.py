# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-08-30
# -------------------------------------------------------------------------------
import os
import xlrd
import xlwt

data_path = r'C:\Users\65680\Desktop\湄潭县'

dir_list = os.listdir(data_path)
merge_sheet = xlwt.Workbook(encoding='utf-8')
merge_ws = merge_sheet.add_sheet("织金县_合并")
r = 1
for roots, dirs, files in os.walk(data_path):
    for file in files:
        if file[-3:].lower() == "xls":
            xls_path = os.path.join(roots, file)
            work_book = xlrd.open_workbook(xls_path)
            sheet_ = work_book.sheet_by_index(0)
            rows = sheet_.nrows
            columns = sheet_.ncols
            print("%s----%s++++++%s" % (xls_path, rows, sheet_.cell(1, 0).value))
            for row in range(5, rows - 1):
                for col in range(columns):
                    dkbm = sheet_.row(row)[0].value
                    print(dkbm)
                    merge_ws.write(r, col, sheet_.row(row)[col].value)
                r = r + 1
merge_sheet.save(r'C:\Users\65680\Desktop\湄潭县合并.xls')
