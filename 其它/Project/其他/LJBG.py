# # coding: utf-8
#
# import arcpy
# import xlrd
#
# sheel_path = ur'C:/Users/Administrator/Desktop/表2.xls'
# work_book = xlrd.open_workbook(sheel_path)
# sheel = work_book.sheet_by_index(0)
#
# gis_data = ur'E:/0质量类别划分台账建立/台账数据/T清镇市台账数据（编号老）.gdb/无措施数据_确权_连接种植表'
#
# currsor = arcpy.da.UpdateCursor(gis_data, ['BSBM', '水稻19年', '水稻20年', '玉米19年', '玉米20年', 'CQCS', '现状', '现状面积', '周边环境'])
#
# dict1 = {}
# for _i in range(1, sheel.nrows):
#     dict1[sheel.row(_i)[0].value] = _i
#
# for row in currsor:
#     try:
#         row2 = dict1[row[0]]
#         row1 = sheel.row(row2)
#         row[5] = row1[6].value
#         row[1] = row1[1].value
#         row[2] = row1[2].value
#         row[3] = row1[3].value
#         row[4] = row1[4].value
#         row[6] = row1[9].value
#         row[7] = row1[8].value
#         row[8] = row1[5].value
#         print(row1[0].value)
#         currsor.updateRow(row)
#     except:
#         pass