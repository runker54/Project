# coding:utf-8
import arcpy.da
import xlrd
data_path = r'E:\台账\织金县\织金县20200814验证\织金县.gdb\T无措施数据_确权_预处理'
with arcpy.da.UpdateCursor(data_path, ['BSBM', 'CQCS', '玉米19年', '玉米20年', '水稻19年', '水稻20年', '主要作物19年', '主要作物20年', '周边环境', '水稻19年面积', '水稻20年面积', '玉米19年面积', '玉米20年面积', 'MJ_MU_QQ']) as currsor:
    for row in currsor:
        if row[2] != "":
            row[11] = row[13]
        else:
            row[11] = 0
        if row[3] != "":
            row[12] = row[13]
        else:
            row[12] = 0
        if row[4] != "":
            row[9] = row[13]
        else:
            row[9] = 0
        if row[5] != "":
            row[10] = row[13]
        else:
            row[10] = 0
        currsor.updateRow(row)