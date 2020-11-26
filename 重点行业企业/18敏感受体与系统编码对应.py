# coding:utf-8
import arcpy.da
import xlrd

data_path = r'D:\重点行业企业资料\重点行业企业成果集成\520000贵州省.gdb\T520000贵州省points'
sheet_path = r'C:\Users\ols\Desktop\check\贵州省-总.xls'
data_list = []
sheet_list = []
work_book = xlrd.open_workbook(sheet_path)
work_sheet = work_book.sheet_by_index(0)
cols = work_sheet.ncols
col_index = 0
for one_col in range(cols):
    col_name = work_sheet.row(0)[one_col].value
    if col_name == '地块编码':
        col_index = one_col
rows = work_sheet.nrows
for one_row in range(1, rows):
    sheet_list.append(work_sheet.row(one_row)[col_index].value)

with arcpy.da.SearchCursor(data_path, ['DKBM']) as currsor:
    for ag_row in currsor:
        if ag_row[0][6] == '1' or ag_row[0][6] == '2' or ag_row[0][6] == '3' or ag_row[0][6] == '4':
            data_list.append(ag_row[0])
print(f"系统中地块数量{len(sheet_list)}个")
print(f"数据库中地块数量{len(data_list)}个")
chayi = set(sheet_list) ^ set(data_list)
print(chayi)
print(f"差异地块编码为{set(sheet_list) ^ set(data_list)}")
