# coding: utf-8
import xlrd
import xlwt
xls_path = r'C:\Users\65680\Desktop\湄潭县\复兴镇\复兴镇图斑祥查\复兴镇大桥村\520328000134-2.xls'
old_xls = xlrd.open_workbook(xls_path)
old_ws = old_xls.sheet_by_index(0)
columns = old_ws.ncols
rows = old_ws.nrows
dkbm = old_ws.cell_value(5, 0)
xzqmc = old_ws.name
zmj = old_ws.cell_value(rows-1, 2)
