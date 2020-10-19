# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-09-29
# -------------------------------------------------------------------------------
import os
import shutil
import xlrd
import time

diaocha_Sheet_path = r"G:\金沙县台账\document文档\金沙县PDF"
pingmian_pictures_path = r"G:\金沙县台账\document文档\金沙县图片"
total_sheet_path = r"G:\金沙县台账\document文档\JSX_20200925_dissolve.xls"
file_ZZ_path = r"G:\金沙县台账\document文档\3金沙县文件佐证资料"
output_path = r"G:\JSXDZTZ"
work_book = xlrd.open_workbook(total_sheet_path)
work_sheet = work_book.sheet_by_index(1)
total_message_list = []
xz_list = []
cz_list = []
# 收集所有地块信息
for one_dk_number_row in range(1, work_sheet.nrows):
    total_message_list.append(work_sheet.row(one_dk_number_row))
    xz_list.append(work_sheet.row(one_dk_number_row)[2].value)
xz_list = list(set(xz_list))
# 遍历乡镇输出
for one_xz in xz_list:
    one_xz_list = list(filter(lambda x: x[2].value == one_xz,
                              total_message_list))
    # 创建乡镇文件夹
    xz_dir = os.path.join(output_path, one_xz)
    os.makedirs(xz_dir)
    pass