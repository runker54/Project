# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-09-03
# -------------------------------------------------------------------------------
import xlrd
import xlwt
import os
document_path = r"E:\台账\金沙县\台账\最终审核通过"
# 遍历文档路径下的所有xls文件
file_list = []
new_work_book = xlwt.Workbook(encoding='utf-8')
new_work_sheet = new_work_book.add_sheet("Data")
r = 1  # 开始行
for roots, dirs, files in os.walk(document_path):
    for file in files:
        if "附件" in file and file.endswith('xls'):
            file_list.append(file)
            one_file_path = os.path.join(roots, file)
            one_work_book = xlrd.open_workbook(one_file_path)
            one_work_sheet = one_work_book.sheet_by_index(1)
            rows = one_work_sheet.nrows
            columns = one_work_sheet.ncols
            # print(f"行：{rows}\n列：{columns}")
            for one_row in range(1, rows):
                for columns_ in range(columns):
                    cell_value = one_work_sheet.row(one_row)[columns_].value
                    new_work_sheet.write(r, columns_, cell_value)
                r += 1
new_work_book.save(r"C:\Users\65680\Desktop\金沙县.xls")