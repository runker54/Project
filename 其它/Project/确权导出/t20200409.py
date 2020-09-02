# coding:utf-8
import arcpy
import xlrd
import xlwt
import pydoc
from arcpy import env


data = "E:/Space.gdb/评价单元对应农用地图层_无机5综合_52_Project"
cyjgtz_data = "E:/0清镇台账措施数据/产业结构调整/2018产业结构调整/清镇农业产业结构.mdb/清镇市农业产业"
vall = "E:/0清镇台账措施数据/产业结构调整/2018产业结构调整/清镇农业产业结构.mdb/ccc"
# arcpy.CopyFeatures_management(cyjgtz_data, vall, "", "0", "0", "0")

# fileds = arcpy.ListFields(vall)
# fileds_list = []
# for filename in fileds:
#     name = filename.name
#     if name !='XMMC' or name !='SJYSSZ':
#         fileds_list.append(name)
#     else:
#         continue
# print(fileds_list)



