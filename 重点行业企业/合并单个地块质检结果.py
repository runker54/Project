# coding:utf-8
import xlwt
import xlrd
import os

sheet_path = r'C:\Users\ols\Desktop\检查结果'
write_work = xlwt.Workbook('utf-8')
write_sheet = write_work.add_sheet('merge_sheet', cell_overwrite_ok=True)
r = 1  # 开始行
for roots, dirs, files in os.walk(sheet_path):
    for one_file in files:
        print(one_file)
        read_work = xlrd.open_workbook(os.path.join(roots, one_file))
        read_sheet = read_work.sheet_by_index(0)
        rows = read_sheet.nrows
        cols = read_sheet.ncols
        # 写入title
        for one_col_title in range(cols):
            write_sheet.write(0, one_col_title, read_sheet.cell_value(0, one_col_title))
        for one_row in range(1, rows):
            for one_col in range(cols):
                write_sheet.write(r, one_col, read_sheet.cell_value(one_row, one_col))
            r += 1
write_work.save(r'C:\Users\ols\Desktop\sve\merge.xls')