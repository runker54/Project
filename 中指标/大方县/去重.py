# coding: utf-8
"""
xls行列限制内模板
"""
import xlwt
import xlrd

data_path = r"E:\台账\织金县\ZJX20200724EXCEL-导表.xls"

work_book = xlrd.open_workbook(data_path)
old_sheet = work_book.sheet_by_index(1)
rows = old_sheet.nrows
columns = old_sheet.ncols
new_workbook = xlwt.Workbook()
ws = new_workbook.add_sheet('Data')
for _row in range(1, rows):
    bm = old_sheet.row(_row)[0].value
    cs_list = []
    cs = ''
    for _col in range(1, columns):
        cs = old_sheet.row(_row)[_col].value
        cs_list.append(cs)
        cs_list = list(set(cs_list))
        for _cs in cs_list:
            _cs = str(_cs) + ' '
            cs += str(_cs)
    ws.write(_row, 0, bm)
    ws.write(_row, 1, cs)
new_workbook.save(r'C:\Users\65680\Desktop\T2019.xls')

# """
# 超过xls行列限制模板
# """
#
# import openpyxl
#
# data_path = r"C:\Users\65680\Desktop\HZX2020年作物.xlsx"
#
# work_book = openpyxl.load_workbook(data_path)
# old_sheet = work_book['2020作物']
# rows = old_sheet.max_row
# columns = old_sheet.max_column
#
# new_workbook = openpyxl.Workbook()
# ws = new_workbook.create_sheet('DATA', 0)
# for _row in range(2, rows):
#     bm = old_sheet.cell(_row, 1).value
#     print(bm)
#     cs_list = []
#     cs = ''
#     for _col in range(2, columns):
#         cs1 = old_sheet.cell(_row, _col).value
#         cs_list.append(cs1)
#     cs_list = list(set(cs_list))
#     for _cs in cs_list:
#         if _cs is not None:
#             key = " " + _cs + "、"
#             cs += key
#             cs.strip(' ')
#         else:
#             pass
#     ws.cell(_row, 1).value = bm
#     ws.cell(_row, 2).value = cs
# new_workbook.save(r'C:\Users\65680\Desktop\HZX20201.xlsx')
