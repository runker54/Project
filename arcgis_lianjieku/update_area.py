# coding:utf-8
import arcpy.da
import xlrd
data_path = r'G:\台账\种植表汇总统计\大方县\消除部件\test.gdb\T大方县20200811_无措施'
with arcpy.da.UpdateCursor(data_path, ['LBBM', 'CQCS', '玉米19年', '玉米20年', '水稻19年', '水稻20年', '主要作物19年', '主要作物20年', '周边环境', '水稻19年面积', '水稻20年面积', '玉米19年面积', '玉米20年面积', 'MJ_MU']) as currsor:
    for row in currsor:
        if str(row[2]).strip(" ") != "":
            row[11] = row[13]
        else:
            row[11] = 0
        if str(row[3]).strip(" ") != "":
            row[12] = row[13]
        else:
            row[12] = 0
        if str(row[4]).strip(" ") != "":
            row[9] = row[13]
        else:
            row[9] = 0
        if str(row[5]).strip(" ") != "":
            row[10] = row[13]
        else:
            row[10] = 0
        print(row[13])
        currsor.updateRow(row)
