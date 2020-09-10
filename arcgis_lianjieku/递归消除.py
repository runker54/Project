# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-09-05
# -------------------------------------------------------------------------------
import arcpy
import time

arcpy.env.workspace = r"C:\Users\65680\Desktop\TEST\TEST.gdb"

lbbm_list = []
with arcpy.da.SearchCursor("test", ["LBBM"]) as currsor:
    for row in currsor:
        lbbm_list.append(row[0])
lbbm_list = list(set(lbbm_list))
layers_1 = arcpy.MakeFeatureLayer_management("test", "testlyr")  # 创建总视图
for one_elimte in lbbm_list:
    arcpy.env.overwriteOutput = True
    print(one_elimte)
    query = '\"LBBM\"=\'%s\' AND \"Shape_Area\" < 100' % one_elimte
    arcpy.SelectLayerByAttribute_management(layers_1, 'NEW_SELECTION', query)
    arcpy.Eliminate_management(layers_1, "testA", "LENGTH", '\"LBBM\" <> \'%s\'' % one_elimte)  # 存储为A
    layers_1 = arcpy.MakeFeatureLayer_management("testA", "testlyr")    # 利用A创建视图
    try:
        arcpy.Delete_management("testB")  # 删除B
    except:
        print("NONE")
    arcpy.SelectLayerByAttribute_management(layers_1, 'NEW_SELECTION', query)
    arcpy.Eliminate_management(layers_1, "testB", "LENGTH", '\"LBBM\" <> \'%s\'' % one_elimte)  # 利用A存储为B
    layers_1 = arcpy.MakeFeatureLayer_management("testB", "testlyr")  # 利用B创建视图
    arcpy.Delete_management("testA")  # 删除A
    print(f"{one_elimte}消除成功")




