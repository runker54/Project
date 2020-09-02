# coding:utf-8
# import xlrd
# import openpyxl
# import os
# import time


# path1 = r'E:\台账\赫章县\数据对比-2020.07.07修改后\已经处理核对后-2020.07.08\TP.2'    # 目录所在位置
# dir_list = os.listdir(path1)
# for dir_1 in dir_list:
#     WB = openpyxl.Workbook()
#     ws = WB.active
#     path_list = []
#     path = os.path.join(path1, dir_1)
#     for roots, dirs, files in os.walk(path):
#         for file in files:
#             if file[-3:].lower() == 'xls':
#                 ck = os.path.join(roots, file)
#                 path_list.append(ck)
#     path_list = list(set(path_list))
#     print(len(path_list))
#     r = 0
#     for _d in path_list:
#         if _d[-3:].lower() == 'xls':
#             print(f'{_d}')
#             work = xlrd.open_workbook(_d)
#             sheet = work.sheet_by_index(0)
#             rows = sheet.nrows
#             columns = sheet.ncols
#             for _r in range(5, rows-1):
#                 for _c in range(columns):
#                     cell_v = sheet.cell_value(_r, _c)
#                     ws.cell(_r+r, _c+1, cell_v)
#             r = r+rows
#     WB.save(r'C:\Users\65680\Desktop\HZX\{}.xls'.format(dir_1))   # 保存文件名


