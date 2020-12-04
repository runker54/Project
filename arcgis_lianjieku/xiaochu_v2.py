# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-10-23
# -------------------------------------------------------------------------------
import arcpy
import time

arcpy.env.workspace = r"C:\Users\65680\Documents\ArcGIS\Projects\MyProject\MyProject.gdb"

lbbm_list = []
with arcpy.da.SearchCursor("recursion_one_eye", ["LBBM"]) as currsor:
    for row in currsor:
        lbbm_list.append(row[0])
lbbm_list = list(set(lbbm_list))
layers_1 = arcpy.MakeFeatureLayer_management("recursion_one_eye", "testlyr")  # 创建总视图
# 个数统计
total_count = len(lbbm_list)
count_total = 0

i = 0
for one_elimte in lbbm_list:
    start_time = time.time()
    arcpy.env.overwriteOutput = True
    # print(one_elimte)
    query = '\"LBBM\"=\'%s\' AND \"Shape_Area\" < 100' % one_elimte
    if i % 2 == 0:
        nice = "testB"
        good = "testA"
    else:
        nice = "testA"
        good = "testB"
    if i == 0:
        arcpy.SelectLayerByAttribute_management(layers_1, 'NEW_SELECTION', query)
        arcpy.Eliminate_management(layers_1, "testA", "LENGTH", '\"LBBM\" <> \'%s\'' % one_elimte)  # 存储为A
    else:
        layers_2 = arcpy.MakeFeatureLayer_management("%s" % nice, "testlyr")  # 利用A创建视图
        arcpy.SelectLayerByAttribute_management(layers_2, 'NEW_SELECTION', query)
        arcpy.Eliminate_management(layers_2, "%s" % good, "LENGTH", '\"LBBM\" <> \'%s\'' % one_elimte)  # 利用A存储为B
    count_total += 1
    i += 1
    end_time = time.time()
    print(f"{one_elimte}消除成功,已消除{count_total}个，剩余{total_count - count_total}个，"
          f"共{total_count}个,单个耗时{end_time-start_time}秒")