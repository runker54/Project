# coding: utf-8
import time

import xlrd
import xlwt

data_path = r'C:\Users\65680\Desktop\表-09 综合单价分析表2010.xls'
old_work = xlrd.open_workbook(data_path)
old_sheet = old_work.sheet_by_index(0)
rows = old_sheet.nrows
columns = old_sheet.ncols

new_work_book = xlwt.Workbook(encoding='utf-8')
ws = new_work_book.add_sheet('Data')
r = 1
for _r in range(2, rows, 11):
    xmbm = old_sheet.row(_r)[2].value
    debh = old_sheet.row(_r + 4)[0].value
    zmmc = old_sheet.row(_r + 4)[1].value
    dw = old_sheet.row(_r + 4)[2].value
    sl = old_sheet.row(_r + 4)[3].value
    rgf = old_sheet.row(_r + 4)[4].value
    clf = old_sheet.row(_r + 4)[5].value
    jxf = old_sheet.row(_r + 4)[6].value
    glf = old_sheet.row(_r + 4)[8].value
    lr = old_sheet.row(_r + 4)[13].value
    zhdj = old_sheet.row(_r + 7)[9].value
    list1 = [xmbm, debh, zmmc, dw, sl, rgf, clf, jxf, glf, lr, zhdj]
    for _x in range(len(list1)):
        ws.write(r, _x+1, list1[_x])
    r = r+1
new_work_book.save(r'C:\Users\65680\Desktop\xxx1.xls')