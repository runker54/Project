# coding:utf-8

import xlrd
import xlwt
import os


path = r'C:\Users\65680\Desktop\TK'    # 目录所在位置
path_list = []
for roots, dirs, files in os.walk(path):
    for file in files:
        if file[-3:].lower() == 'xls':
            ck = os.path.join(roots, file)
            path_list.append(ck)
r = 1
new_work_book = xlwt.Workbook(encoding='utf-8')
ws = new_work_book.add_sheet('Data')
for _d in path_list:
    if _d[-3:].lower() == 'xls':
        print(f'{_d}')
    old_book = xlrd.open_workbook(_d)
    old_sheet = old_book.sheet_by_index(0)
    rows = old_sheet.nrows
    columns = old_sheet.ncols
    for abstrat_row in range(4, rows - 1, 2):
        title = old_sheet.row(abstrat_row)[:5]
        abstrat_2019 = old_sheet.row(abstrat_row)[6:34]
        abstrat_2020 = old_sheet.row(abstrat_row + 1)[6:34]
        neirong = title + abstrat_2019 + abstrat_2020
        print(neirong)
        for _row in range(len(neirong)):
            ws.write(r, _row, neirong[_row].value)
        r += 1

new_work_book.save(r'C:\Users\65680\Desktop\云玲街道.xls')






