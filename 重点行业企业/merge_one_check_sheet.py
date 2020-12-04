# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-27
# -----------------------
import pandas
import os

sheet_path = r'C:\Users\65680\Desktop\检查结果'
sheet_list = [os.path.join(sheet_path, one_sheet) for one_sheet in os.listdir(sheet_path)]
stram_list = [pandas.read_excel(read_sheet) for read_sheet in sheet_list]

stram_text = pandas.concat(stram_list)

stram_text.to_excel(r'C:\Users\65680\Desktop\贵州省合并表.xls', index_label=False)
