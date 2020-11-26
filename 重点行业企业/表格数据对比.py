# coding:utf-8
import xlrd
import xlwt
import os

data_path = r'C:\Users\ols\Desktop\现有数据对比.xls'
out_path = r'C:\Users\ols\Desktop\异同比较'
work_book = xlrd.open_workbook(data_path)
work_sheet = work_book.sheet_by_index(0)
print(work_sheet.name)
rows = work_sheet.nrows
kjk_list = []
sjk_list = []
new_work_book = xlwt.Workbook('utf-8')
new_ws = new_work_book.add_sheet(work_sheet.name)
for one_row in range(1, rows):
    kjk = work_sheet.row(one_row)[0].value
    sjk = work_sheet.row(one_row)[1].value
    kjk_list.append(kjk)
    sjk_list.append(sjk)
dif_list = set(kjk_list) ^ set(sjk_list)
for row_c, one_dif in enumerate(dif_list):
    new_ws.write(row_c, 0, one_dif)
new_work_book.save(os.path.join(out_path, work_sheet.name + '.xls'))
