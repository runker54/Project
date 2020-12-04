# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-26
# -----------------------
import xlrd
import os
import shutil

sheet_path = r'C:\Users\65680\Desktop\1.区县2018年代码.xls'
data_path = r'C:\Users\65680\Desktop\none'
data_path1 = r'C:\Users\65680\Desktop\cie_33'

read_book = xlrd.open_workbook(sheet_path)
read_sheet = read_book.sheet_by_index(0)
sz_dict = {}
qx_dict = {}
for one_row in range(1, read_sheet.nrows):
    sz_dict[str(int(read_sheet.row(one_row)[1].value))] = read_sheet.row(one_row)[0].value  # 市州字典
    qx_dict[str(int(read_sheet.row(one_row)[3].value))] = read_sheet.row(one_row)[2].value  # 区县字典
for one_dir in os.listdir(data_path):
    dir_source_path = os.path.join(data_path, one_dir)
    sz_name = one_dir[:4]  # 市州索引
    qx_name = one_dir[:6]  # 区县索引
    source_dir = os.path.join(os.path.join(data_path1, sz_name + sz_dict[sz_name]), qx_name + qx_dict[qx_name])  # 目标文件夹
    shutil.move(dir_source_path, source_dir)
    print(f"file {one_dir} move done!")
