#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2021-11-17
# Author:Runker54
# ----------------------
import arcpy
import time

arcpy.env.workspace = r"C:\Users\65680\Desktop\temp_path\test.gdb"
arcpy.env.overwriteOutput = True
cahea = r"C:\Users\65680\Desktop\temp_path\test.gdb\附件3"
caheb = r"C:\Users\65680\Desktop\temp_path\test.gdb\贯洞镇"
data_base = arcpy.Identity_analysis(in_features=cahea, identity_features=caheb,
                                    out_feature_class=r"C:\Users\65680\Desktop\temp_path\test.gdb\附件3_identity")
arcpy.AddField_management(in_table=data_base, field_name="Ob_number", field_type="String")
arcpy.CalculateField_management(data_base, "Ob_number", "!OBJECTID!", "PYTHON_9.3")
lbbm_list = []
with arcpy.da.SearchCursor(data_base, ["LBBM", "Ob_number", "编码"]) as currsor:
    for row in currsor:
        if len(row[0]) < 2:
            lbbm_list.append(row[2])
print(lbbm_list)

lbbm_list = list(set(lbbm_list))

layers_1 = arcpy.MakeFeatureLayer_management(data_base, "testlyr")  # 创建总视图

# # 个数统计

total_count = len(lbbm_list)
count_total = 0
i = 0
for one_elimte in lbbm_list:
    start_time = time.time()
    arcpy.env.overwriteOutput = True
    query = u'\"编码\"=\'%s\' AND \"LBBM\" = \'\'' % one_elimte
    if i % 2 == 0:
        nice = "testB"
        good = "testA"
    else:
        nice = "testA"
        good = "testB"
    if i == 0:
        arcpy.SelectLayerByAttribute_management(layers_1, 'NEW_SELECTION', query)
        arcpy.Eliminate_management(layers_1, "testA", "LENGTH", u'\"编码\" <> \'%s\'' % one_elimte)  # 存储为A
    else:
        layers_2 = arcpy.MakeFeatureLayer_management("%s" % nice, "testlyr")  # 利用A创建视图
        arcpy.SelectLayerByAttribute_management(layers_2, 'NEW_SELECTION', query)
        arcpy.Eliminate_management(layers_2, "%s" % good, "LENGTH", u'\"编码\" <> \'%s\'' % one_elimte)  # 利用A存储为B
    count_total += 1
    i += 1
    end_time = time.time()
    # print(f"{one_elimte}消除成功,已消除{count_total}个，剩余{total_count - count_total}个，"
    #       f"共{total_count}个,单个耗时{end_time - start_time}秒")
    print ("{}消除成功，已消除{}个，剩余{}个，共{}个，单个耗时{}秒".format(one_elimte, count_total, (total_count - count_total), total_count,
                                                     (end_time - start_time)))
