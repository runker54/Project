#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2021-01-27
# Author:Runker54
# -----------------------
import arcpy

# data_ = r'E:\资料\贵州省底图\底图.gdb\test_point'
data_ = r'E:\资料\贵州省底图\底图.gdb\test_point_Identity'
fileds = arcpy.ListFields(data_)
print(fileds)


# with arcpy.da.UpdateCursor(data_, ['SHAPE@X', 'SHAPE@Y', '经度', '纬度']) as cursor:
#     for row in cursor:
#         row[3] = row[1]
#         print(row[2], row[3])
#         cursor.updateRow(row)