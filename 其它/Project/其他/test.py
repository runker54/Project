# -*- coding: utf-8*
import sys

import arcpy

default_encoding = 'utf-8'

if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
# path_new = r'E:/纳雍县台账数据/纳雍县'
#
# # for roots, dirs, files in os.walk(path_new):
# # #     for one_file in files:
# # #         infc = os.path.join(roots, one_file)
# # #         if infc
# # #         print(infc)
# #
# arcpy.env.workspace = path_new
# shps = arcpy.ListFeatureClasses()


# for shp in shps:
#     name = shp[:-4]
#     print(name)
#     arcpy.AddField_management(shp, 'ZM', 'text')
#     arcpy.CalculateField_management(shp, 'ZM', '"' + name + '"')
#     try:
#         arcpy.DeleteField_management(shp, 'LJH')
#     except:
#         pass


# list_1 = [1, 1, 1, 1, 4, 4, 4, 4, 7, 7, 7, 7, 9, 10, 10]
# set_list = list(set(list_1))
#
# for one_list in set_list:
#     print(one_list)
    # list_2 = filter(lambda x: x == one_list)
    #
    # print(list_2)
# data = r"E:/Space.gdb/T无措施数据_确权"
#
# cursor = arcpy.UpdateCursor(data, ['LBBM', '标识编码'])
# row_list = []
# for row in cursor:
#     row_list.append(row)
# row_list.sort(row_list[0])
# print(row_list)
# set_list = list(set(row_list))
# for id_1 in set_list:
#     shuliang = row_list.count(id_1)
#     print(shuliang)

l = ['123', '453245', '2345t2']
l[1] = l[1][len(l[0]):]
print(l)