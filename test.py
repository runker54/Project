# # coding:utf-8
# # """
# # import arcpy
# # data_path = r'C:\Users\65680\Documents\ArcGIS\Packages\Visualize_temporal_data_d0c5bf\p12\visualize_temporal_data.gdb\test_point_Identity_quxian_xiangzhen_cun'
# # fileds = arcpy.ListFields(data_path)
# # for filed in fileds:
# #     filed_name = filed.name
# #     if filed_name not in ['OBJECTID', 'Shape', '年度', '样点类型', '样点编码', '省', '市', '县', '乡镇', '村', '经度', '纬度']:
# #         arcpy.DeleteField_management(data_path, filed_name)
# #     else:
# #         print(filed_name)
# # """
#
# # import arcpy
# # import math
# import numpy as np
#
# # arcpy.env.overwriteOutput = True
# # arcpy.env.workspace = r"C:\Users\65680\Desktop\test"
# # arcpy.CreateFileGDB_management(out_folder_path=r"C:\Users\65680\Desktop\test", out_name="test_gdb")
# # workspace = r"C:\Users\65680\Desktop\test\test_gdb.gdb"
# # arcpy.env.workspace = workspace
#
# # """
# # arcpy.CreateFeatureclass_management(workspace, "test_featureclass", "POINT", has_z="ENABLED")
# # element = "test_featureclass"
# # arcpy.AddField_management(element, "NUMBER", field_type="TEXT", field_length=255)
# # with arcpy.da.InsertCursor(element, ["SHAPE@X", "SHAPE@Y", "SHAPE@Z", "NUMBER"]) as cursor:
# #     for key_hash in range(1000):
# #         number = str(key_hash+1)
# #         x = np.random.uniform(106.000000, 110.000000)
# #         y = np.random.uniform(24.000000, 28.000000)
# #         z = np.random.randint(850, 2800)
# #         cursor.insertRow((x, y, z, number))
# # print("done!")
# # """
# # 3个环的组成点集合
# # points1 = [[0, 0], [0, 10], [10, 10], [10, 0], [0, 0]]
# # points2 = [[2, 2], [2, 8], [8, 8], [8, 2], [2, 2]]
# # points3 = [[4, 4], [4, 6], [6, 6], [6, 4], [4, 4]]
# #
# # # 3个环的Array对象
# # ring1 = arcpy.Array([arcpy.Point(*p) for p in points1])
# # ring2 = arcpy.Array([arcpy.Point(*p) for p in points2])
# # ring3 = arcpy.Array([arcpy.Point(*p) for p in points3])
# #
# # # 创建features列表，用于存放要素，在内存
# # features = []
# # # 通过Array组成的Array创建Polygon对象
# # # 将Polygon要素添加到features列表
# # features.append(arcpy.Polygon(arcpy.Array([ring1, ring2, ring3])))
# #
# # # 调用复制要素工具，将内存中的features列表创建为shapefile
# # # arcpy.CopyFeatures_management(features, r"C:\Users\65680\Desktop\test\test_gdb.gdb\test_polygon")
# # arcpy.FeatureClassToFeatureClass_conversion(features, workspace, "cake")
# # a = [[7], [9], [10], [5], [8], [4], [2], [1], [6], [3], [7], [9], [10], [5], [8], [4], [2]]
# # b = [[5], [2], [2], [1], [3], [2], [1], [9], [9], [4], [0], [5], [0], [3], [8], [2], [5]]
# # print('\033[4m'+"gslkjk")..
# # old_bianma = [str(520111210000+x) for x in range(1, 10000)]
# # dice_1 = {"0": "B", "1": "J", "2": "K", "3": "L", "4": "S", "5": "R",
# #           "6": "C", "7": "G", "8": "Y", "9": "Z", }
# # dice_2 = {"0": "Q", "1": "D", "2": "T", "3": "P", "4": "N", "5": "F",
# #           "6": "A", "7": "H", "8": "E", "9": "X", }
# # new_bianma = []
# # for one_key in old_bianma:
# #     no_change = one_key[2:6]
# #     is_change = one_key[-4:]
# #     change_sum = sum([int(_x) for _x in is_change])
# #     is_change_sum = str(change_sum)[-1]
# #     is_change_1 = dice_1[is_change[0]]
# #     is_change_2 = str(int(is_change[1])+int(change_sum))[-1]
# #     is_change_3 = dice_1[is_change[2]]
# #     is_change_4 = dice_1[is_change[3]]
# #     is_change_zz = dice_2[is_change_sum]
# #     # change_key = "520000"+is_change_1+is_change_2+is_change_3+is_change_4+is_change_zz
# #     change_key = "21"+no_change+is_change_1+is_change_2+is_change_3+is_change_4+is_change_zz
# #     new_bianma.append(change_key)
# #     print(one_key+",", change_key)
# # print(new_bianma)
# # print(len(old_bianma))
# # print(len(new_bianma))
# # check_bianma = list(set(new_bianma))
# # print(len(check_bianma))
#
# # a = 0
# # def calc():
# #     global a
# #     s = 520304210000
# #     if a == 0:
# #         a+=1
# #         s = 520304210000+a
# #     else:
# #        a+=1
# #        s+=a
# #     return str(s)+"-"+"T"
# #
# # print(calc())
# # print(calc())
# # print(calc())
# # print(calc())
# # print(calc())
# # print(calc())
#
#
# import xlrd
# import xlwt
#
# # sheet_path = r'C:\Users\65680\Desktop\重点行业企业质控.xls'
# # write_book = xlwt.Workbook("utf-8")
# # write_sheet = write_book.add_sheet("data_merge")
# # work_sheet = xlrd.open_workbook(sheet_path)
# # n_sheet = work_sheet.nsheets
# # r = 1
# # for n in range(n_sheet):
# #     read_sheet = work_sheet.sheet_by_index(n)
# #     rows = read_sheet.nrows
# #     cols = read_sheet.ncols
# #
# #     for one_row in range(1,rows):
# #         for one_col in range(cols):
# #             write_sheet.write(r, one_col, read_sheet.cell(one_row, one_col).value)
# #         r += 1
# #     write_book.save(r'C:\Users\65680\Desktop\重点行业企业质控_merge.xls')
# sheet_path = r'C:\Users\65680\Desktop\重点行业企业质控_merge.xls'
# write_book = xlwt.Workbook("utf-8")
# write_sheet = write_book.add_sheet("data_merge")
# work_sheet = xlrd.open_workbook(sheet_path)
# read_sheet = work_sheet.sheet_by_index(0)
# rows = read_sheet.nrows
# cols = read_sheet.ncols
# for one_row in range(rows):
#     for one_col in range(cols):
#         s = str(read_sheet.cell(one_row, one_col).value).strip()
#         if one_col !=5 and one_col!=6:
#             try:
#                 s = str(int(read_sheet.cell(one_row, one_col).value)).strip()
#             except:
#                 s = str(read_sheet.cell(one_row, one_col).value).strip()
#         else:
#             s = str(read_sheet.cell(one_row, one_col).value).strip()
#         write_sheet.write(one_row, one_col, s)
# write_book.save(r'C:\Users\65680\Desktop\重点行业企业质控_merge111.xls')

# import random
# list1 = ['佛山', '南宁', '北海', '杭州', '南昌', '厦门', '温州']
# a = random.choice(list1)
# print(a)
# a = 0
# def acc():
#     global a
#     result = 0
#     if a == 0:
#         result = 5226330001 + a
#         a += 1
#     else:
#         result = 5226330001 + a
#         a += 1
#     return str(result)[:6] + "-" + "RHDC"+"-"+str(result)[-4:]
# import random
# def calc(x):
#     data_dict = {
#         "友团村": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
#         "干团村": [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
#         "腊全村": [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
#         "腊水村": [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
#         "宰门村": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]}
#     result = random.choice(data_dict[x])
#     result_s = "2021年8月%s" % str(result)
#     return result_s
# for sys in range(5):
#     in_list = []
#     for i in range(10000):
#         a = calc("干团村")
#         in_list.append(a)
#     c = list(set(in_list))
#     gailv_dict = {}
#     for one_cahe in c:
#         count_number = in_list.count(one_cahe)
#         gailv_dict[one_cahe] = (count_number/10000)*100
#     print(gailv_dict)
# from PIL import Image
#
# in_path = r"C:\Users\65680\Desktop\A.png"
# out_path = r"C:\Users\65680\Desktop\AB.png"
# img = Image.open(in_path)
# new_w = 60
# new_h = 30
# out_img = img.resize((new_w, new_h), Image.ANTIALIAS)
# out_img.save(out_path)

# lil = [1,2,3,4,5,6,7]
# r = 0
# for i in lil:
#     lil.remove(lil[r])
#     r+=1
#     print(lil)
# print(lil)
# import random
# list = [random.randint(1,3) for _i in range(10)]
# print(list)
# c = {"1":"111","2":"222"}
# print(c[1])
# a = 0
# def calc():
#     global a
#     a+=1
#     result = "522633-RHDC-"+str(10000+a)[1:]
#     return result
# print(calc())
# print(calc())
# print(calc())
# print(calc())
# print(calc())
# print(calc())
#
# # name_dict = {"干团村":["潘新红","15085224882"], "友团村":["吴家海","15185653391"], "腊全村":["梁忠清","18212340115"], "腊水村":["梁丰维","13885534154"], "宰门村":["梁支书","13985823043"]}
# # def calc(x):
# #     result = name_dict[x][0]
# #     return result
#
#
# name_dict = {u"干团村":[u"潘新红","15085224882"], u"友团村":[u"吴家海","15185653391"], u"腊全村":[u"梁忠清","18212340115"],u"腊水村":[u"梁丰维","13885534154"],u"宰门村":[u"梁支书","13985823043"]}
# def calc(x):
#     result = name_dict[x][0]
#     return result
# print(calc("友团村"))
import os

rc = r"C:\Users\65680\Desktop\CCC.txt"
cc = r"C:\Users\65680\Desktop\CYCX"
test = open(rc)
text = test.readlines()
for one_dir in text:
    one_dir = one_dir.strip()
    os.makedirs(os.path.join(cc,one_dir))