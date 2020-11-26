# coding:utf-8
import arcpy
import os
import time
data_path = r'C:\Users\ols\Desktop\借力调查地块信息汇总\借力调查地块'
file_list = os.listdir(data_path)
for one_file_dir in file_list:
    work_space = os.path.join(data_path, one_file_dir)
    arcpy.env.workspace = work_space
    gs_file = arcpy.ListFeatureClasses()
    print(gs_file)
    print(one_file_dir)
    # try:
    #     arcpy.AddField_management(in_table=gs_file[0], field_name="DKBM", field_type="TEXT", field_length=50)
    # except:
    #     print('点DKBM字段已存在')
    #     arcpy.DeleteField_management(in_table=gs_file[0], drop_field="DKBM")
    #     arcpy.AddField_management(in_table=gs_file[0], field_name="DKBM", field_type="TEXT", field_length=50)
    #     print("添加成功")
    # try:
    #     arcpy.AddField_management(in_table=gs_file[0], field_name="BZ", field_type="TEXT", field_length=255)
    # except:
    #     print('点BZ已存在')
    #     arcpy.DeleteField_management(in_table=gs_file[0], drop_field="BZ")
    #     arcpy.AddField_management(in_table=gs_file[0], field_name="BZ", field_type="TEXT", field_length=255)
    #     print("添加成功")
    # try:
    #     arcpy.AddField_management(in_table=gs_file[1], field_name="DKBM", field_type="TEXT", field_length=50)
    # except:
    #     print('面DKBM已存在')
    #     arcpy.DeleteField_management(in_table=gs_file[1], drop_field="DKBM")
    #     arcpy.AddField_management(in_table=gs_file[1], field_name="DKBM", field_type="TEXT", field_length=50)
    #     print("添加成功")
    # try:
    #     arcpy.AddField_management(in_table=gs_file[0], field_name="LXDM", field_type="TEXT", field_length=5)
    # except:
    #     print('点LXDM已存在')
    #     arcpy.DeleteField_management(in_table=gs_file[0], drop_field="LXDM")
    #     arcpy.AddField_management(in_table=gs_file[0], field_name="LXDM", field_type="TEXT", field_length=5)
    #     print("添加成功")
    # try:
    #     arcpy.AddField_management(in_table=gs_file[1], field_name="BZ", field_type="TEXT", field_length=255)
    # except:
    #     print('面BZ已存在')
    #     arcpy.DeleteField_management(in_table=gs_file[1], drop_field="BZ")
    #     arcpy.AddField_management(in_table=gs_file[1], field_name="BZ", field_type="TEXT", field_length=255)
    #     print("添加成功")
    # arcpy.CalculateField_management(in_table=gs_file[0], field="DKBM", expression=one_file_dir)
    # arcpy.CalculateField_management(in_table=gs_file[1], field="DKBM", expression=one_file_dir)
    try:
        arcpy.DeleteField_management(in_table=gs_file[1], drop_field="LXDM")
    except:
        print('删除失败')
    arcpy.CalculateField_management(in_table=gs_file[0], field="LXDM", expression="!name!")
