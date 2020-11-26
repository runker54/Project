# coding:utf-8
import arcpy
import os
import time
data_path = r'C:\Users\ols\Desktop\借力调查地块信息汇总\借力调查地块'
file_list = os.listdir(data_path)
point_list = []
polygon_list = []
for one_file_adress in file_list:
    file_adress = os.path.join(data_path, one_file_adress)
    arcpy.env.workspace = os.path.join(data_path, one_file_adress)
    shp = arcpy.ListFeatureClasses()
    print(shp)
    point_list.append(os.path.join(file_adress, shp[0]))
    polygon_list.append(os.path.join(file_adress, shp[1]))
print(polygon_list)
print(point_list)
point_out_path = os.path.join(data_path, '借力地块_merge_point.shp')
polygon_out_path = os.path.join(data_path, '借力地块_merge_polygon.shp')
arcpy.Merge_management(inputs=point_list, output=point_out_path)
arcpy.Merge_management(inputs=polygon_list, output=polygon_out_path)
