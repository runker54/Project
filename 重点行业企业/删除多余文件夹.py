# coding:utf-8
import xlrd
import os
import time
import shutil
sheet_path = r'C:\Users\ols\Desktop\shanchu.xls'
dir_path = r'C:\Users\ols\Desktop\单个地块位置'
work_book = xlrd.open_workbook(sheet_path)
ws = work_book.sheet_by_index(0)
data_list = []
rows = ws.nrows
for one_row in range(rows):
    data_list.append(ws.cell_value(one_row, 0))
for roots, dirs, files in os.walk(dir_path):
    for one_dir in dirs:
        if one_dir not in data_list:
            dir_name_path = os.path.join(roots, one_dir)
            shutil.rmtree(dir_name_path)