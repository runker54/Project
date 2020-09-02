# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-08-31
# -------------------------------------------------------------------------------
import xlrd
import xlwt

data_path = r"C:\Users\65680\Desktop\ZZZ\ZJX20200831-1.xls"
cuncun_path = r"C:\Users\65680\Desktop\表"
read_sheet = xlrd.open_workbook(data_path)
r_ws = read_sheet.sheet_by_index(0)
r_rows = r_ws.nrows
r_colunms = r_ws.ncols
sheet_value = []  # 总数据表
xz = []  # 乡镇列表
title_list = []
for cooo in range(r_colunms):
    title_list.append(r_ws.row(0)[cooo].value)
for one_row in range(1, r_rows):
    row_value = []
    xz.append(r_ws.row(one_row)[2].value)
    for one_col in range(r_colunms):
        one_cell_value = r_ws.row(one_row)[one_col].value
        row_value.append(one_cell_value)
    sheet_value.append(row_value)
    xz = list(set(xz))
print(f"{xz}共有{len(xz)}个")

for one_xz in xz:
    r = 1  # 开始行
    xz_value_list = list(filter(lambda x: x[2] == one_xz, sheet_value))
    print(xz_value_list)
    work_book = xlwt.Workbook(encoding="utf-8")
    ws = work_book.add_sheet(f"{str(one_xz)}")
    for title_key in range(len(title_list)):
        ws.write(0, title_key, title_list[title_key])
    for one_message in xz_value_list:
        for one_cell in range(len(one_message)):
            ws.write(r, one_cell, one_message[one_cell])
        r += 1
    work_book.save("%s/%s--台账汇总表.xls" % (cuncun_path, one_xz))
