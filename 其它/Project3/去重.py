# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-10-22
# -------------------------------------------------------------------------------
import xlrd
import time
import xlwt
one_path = r'C:\Users\65680\Desktop\DFX\DFX_20201022_dissolve.xls'
work_book = xlrd.open_workbook(one_path)
old_sheet = work_book.sheet_by_index(2)
rows = old_sheet.nrows
cols = old_sheet.ncols

new_work_book = xlwt.Workbook('utf-8')
new_sheet = new_work_book.add_sheet("Fine")
for one_mes in range(1, rows):
    dkbm = old_sheet.cell_value(one_mes, 0)
    one_cell_value = []
    one_cell_value_text=''
    for cv_1 in range(1, cols):
        one_cell_value.append(old_sheet.cell_value(one_mes, cv_1))
    one_cell_value = list(set(one_cell_value))
    for ix in one_cell_value:
        one_cell_value_text += ix+" "
    one_cell_value_text.strip()
    new_sheet.write(one_mes, 0, dkbm)
    new_sheet.write(one_mes, 1, one_cell_value_text)
new_work_book.save(r'C:\Users\65680\Desktop\DFX\2020年.xls')


