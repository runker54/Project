# # coding: utf-8
# # import arcpy
# import sys
#
# default_encoding = 'utf-8'
#
# # if sys.getdefaultencoding() != default_encoding:
# #     reload(sys)
#     sys.setdefaultencoding(default_encoding)

# data = r'E:/T清镇市台账数据.gdb/T无措施数据_确权_严格管控类'
# row_list = []
# zu_list = []
# cm_list = []
# xz_list = []
# cursor = arcpy.da.SearchCursor(data, ["LBBM", "地块编码", "XZQMC", "地域名称", "承包方名称", "地块名称", "MJ_MU_QQ", "TXZQMC"])
# for row in cursor:
#     txz_qmc = row[7]
#     lb_bm = row[0]
#     dk_bm = row[1]
#     xz_qmc = row[2]
#     cb_nh_xm = row[4]
#     dk_mc = row[5]
#     mjm = round(row[6], 3)
#     # lens = len(xz_qmc) + 10
#     # zm = row[3][lens:]
#     zm = row[3]
#     bm = str(zm)
#     try:
#         zm_index = bm.index('村')
#         zm = bm[zm_index+3:]
#     except:
#         zm = zm
#     list1 = [txz_qmc, lb_bm, dk_bm, xz_qmc, zm, cb_nh_xm, dk_mc, mjm]
#     row_list.append(list1)
#     zu_list.append(zm)  # 组列表
#     cm_list.append(xz_qmc)  # 村列表
#     xz_list.append(txz_qmc)  # 乡镇列表
# cu_list = list(set(cm_list))  # 列表化集合
# bu_list = list(set(zu_list))  # 列表化集合
# pz_list = list(set(xz_list))  # 列表化集合
# x_list = [pz_list, cu_list, bu_list]  # 信息列表  用于下一个for循环索引
# print(zu_list)
# for one in zu_list:
#     print(one)


# def pd(x):
#     if x == "其他林地" or x == "其他草地" or x == "其他园地" or x == "乔木林地" or x == "竹林地" or x == "茶园" or x == "灌木用地" or x == "果园":
#         s = "K"
#     elif x == "":
#         s = x
#     else:
#         s = "L"
#     return s
#
#
# print(pd("领地"))

# import xlwt
# import os
# import shutil
#
# workbook = xlwt.Workbook(encoding='utf-8')
# ws = workbook.add_sheet(sheetname='Data', cell_overwrite_ok=True)
# # ws = workbook.add_font(font='黑体')
#
# ws.write(1, 1, 'book')
# #
# # ws.write_merge()
# #
# # workbook.save('tkk.xls')
# #
# # shutil.move()
# # os.times()
# print os.times()
# # print os.renames()
# row = ['倭','','','贵州砷会计划公开数据发生纠纷类似的空间']
# zm = row[3]
# print zm
# zm.index('会')
# zm = zm[zm.index('会'):]
# print zm
#
# key_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','VIP','FH','']
# list1 = ['520121003017', '开阳县', '城关镇', '城关镇城西村', '106.982552', '27.08025576', '安全利用类', '', '0.617788196',
#          'L','9.687963888']
# value_list = []
# for key in key_list:
#     try:
#         bh = list1.index(key)
#         lvalue = list1[bh+1]
#     except:
#         lvalue = ''
#     value_list.append(lvalue)
# print(value_list)


# coding:utf-8
import sys

# default_encoding = 'utf-8'
# if sys.getdefaultencoding() != default_encoding:
#     reload(sys)
#     sys.setdefaultencoding(default_encoding)


def auto(x):
    min_x = x.extent.xmin
    max_x = x.extent.xmax
    min_y = x.extent.ymin
    max_y = x.extent.ymax
    min_x_6 = round(min_x, 6)
    min_y_6 = round(min_y, 6)
    max_x_6 = round(max_x, 6)
    max_y_6 = round(max_y, 6)
    s_text = "经度（%s-%s),纬度（%s-%s）" % (min_x_6, max_x_6, min_y_6, max_y_6)
    return s_text


# coding:utf-8

import sys

# default_encoding = 'utf-8'
# if sys.getdefaultencoding() != default_encoding:
#     reload(sys)
#     sys.setdefaultencoding(default_encoding)

def auto(w):
    x = w.extent.xmin
    y = w.extent.ymin
    z = w.extent.xmax
    p = w.extent.ymax
    min_x_6 = round(x, 6)
    if len(str(min_x_6)) != 10:
        min_x_6 = str(min_x_6) + "0" * (10 - len((str(min_x_6))))

    min_y_6 = round(y, 6)
    if len(str(min_y_6)) != 9:
        min_y_6 = str(min_y_6) + "0" * (9 - len((str(min_y_6))))

    max_x_6 = round(z, 6)
    if len(str(max_x_6)) != 10:
        max_x_6 = str(max_x_6) + "0" * (10 - len((str(max_x_6))))

    max_y_6 = round(p, 6)
    if len(str(max_y_6)) != 9:
        max_y_6 = str(max_y_6) + "0" * (9 - len((str(max_y_6))))

    s_text = "经度（%s-%s）, 纬度（%s-%s）" % (min_x_6, max_x_6, min_y_6, max_y_6)
    return s_text

# k = '风华社区在这里'
# if '区' in k:
#     zm = k.index('区')
#     print zm
# else:
#     print "no"
