#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2021-01-06
# Author:Runker54
# -----------------------
import arcpy
import mkl
import time

arcpy.env.workspace = r'C:\Users\65680\Desktop\数据处理\T清镇市.gdb'
data = 'qzs_rwsj'
filed = arcpy.ListFields(data)
for one_filed in filed:
    print(one_filed.name)
    print(str(one_filed.name).lower())
    if str(one_filed.name).lower() not in ["objectid", "shape", "shape_length", "shape_area"]:
        new_name1 = one_filed.name + "_temp"  # 重命名
        arcpy.AlterField_management(data, one_filed.name, new_field_name=new_name1,
                                    new_field_alias='', clear_field_alias=True)
        print("已添加空字段")
        time.sleep(0.1)
        new_name = one_filed.name.lower()
        arcpy.AddField_management(data, new_name, field_type="TEXT", field_length=255)   # 添加字段
        print("已添加新字段名")
        time.sleep(0.1)
        arcpy.CalculateField_management(data, new_name, expression="!{}!".format(new_name1))  # 计算字段
        print("已计算完成")
        time.sleep(0.1)
        arcpy.DeleteField_management(data, new_name1)
        print("已删除空字段")
        time.sleep(0.1)
    else:
        print("pass")
