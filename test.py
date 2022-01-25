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
# import os
#
# rc = r"C:\Users\65680\Desktop\CCC.txt"
# cc = r"C:\Users\65680\Desktop\CYCX"
# test = open(rc)
# text = test.readlines()
# for one_dir in text:
#     one_dir = one_dir.strip()
#     os.makedirs(os.path.join(cc,one_dir))
# dict_c = {u"果朗铁": u"0.1kg/亩", u"美鑫隆": u"0.3kg/亩", u"降镉灵": u"0.5L/亩"}
#
#
# def calc(x):
#     s = dict_c[x]
#     return s
#
# dict_c = {u"含磷型土壤调理剂": u"150kg/亩", u"改性天然矿物材料": u"200kg/亩", u"凹凸棒土壤调理剂": u"160kg/亩", u"楚戈土壤调理剂": u"150kg/亩", u"天象土壤调理剂": u"200kg/亩"}
# print(calc("果朗铁"))
# 含量
# dict_c = {u"商品有机肥": u"有机质≥45%，N+P2O5+K2O≥5%", u"硅钙肥": u"SiO2≥30%，CaO≥35%，P2O5≥2%", u"硫酸钾肥": u"水溶性K2O大于等于52%，Cl≤1%，S≥17.5%", u"巨能螯合氮肥": u"硫铵态氮≥26%"}
#
#
# def calc(x):
#     try:
#         s = dict_c[x]
#     except:
#         s = "-"
#     return s
# print(calc(""))
# 每亩用量
# dict_c = {u"美鑫隆": u"Mn≥5%，Zn≥5%",
#           u"降镉灵": u"Si≥85g/L",
#           u"喷喷富": u"Si≥100g/L"}

#
# def calc(x):
#     try:
#         s = dict_c[x]
#     except:
#         s = "-"
#     return s
# # print(calc(""))
# # 钝化剂成分
dict_c = {u"果朗铁": u"有机硅",
          u"降镉灵": u"EDDHA-Fe",
          u"美鑫隆": u"Mn,Zn"}
dict_c = {u"果朗铁": u"10%",
          u"降镉灵": u"Si≥85g/L",
          u"美鑫隆": u"Mn≥5%，Zn≥5%"}
dict_c = {u"果朗铁": u"0.1kg/亩",
          u"降镉灵": u"0.5L/亩",
          u"美鑫隆": u"0.3kg/亩"}
dict_c = {u"果朗铁": u"施用节点：拔节期-齐穗期；施用方式：无人机喷施",
          u"降镉灵": u"施用节点：拔节期、抽穗期；施用方式：无人机喷施",
          u"美鑫隆": u"施用节点：抽穗期、齐穗期；施用方式：无人机喷施"}
dict_c = {u"硅钙肥": u"二氧化硅、氧化钙",
          u"巨能螯合氮肥": u"硫铵态氮",
          u"有机肥": u"有机质、N、P",
          u"硫酸钾肥": u"N、P2O5、K2O、S"}
dict_c = {u"硅钙肥": u"SiO2≥30%，CaO≥35%，P2O5≥2%",
          u"巨能螯合氮肥": u"硫铵态氮≥26%",
          u"有机肥": u"有机质≥45%，N+P2O5+K2O≥5%",
          u"硫酸钾肥": u"水溶性K2O大于等于52%，Cl≤1%，S≥17.5%"}
dict_c = {u"硅钙肥": u"15kg/亩",
          u"巨能螯合氮肥": u"15kg/亩",
          u"有机肥": u"100kg/亩",
          u"硫酸钾肥": u"15kg/亩"}

dict_c = {u"含磷型土壤调理剂": u"Ca3(P04)2",
          u"凹凸棒土壤调理剂": u"镁硅酸盐",
          u"天象土壤调理剂": u"CaO≥25%,SiO2≥10%,MgO≥5%,K2O≥2%",
          u"改性天然矿物材料": u"CaCo3≥60%"}

dict_c = {u"含磷型土壤调理剂": u"施用节点：秧苗移栽前一周；施用方式：人工施撒",
          u"凹凸棒土壤调理剂": u"施用节点：秧苗移栽前一周；施用方式：人工施撒",
          u"天象土壤调理剂": u"施用节点：秧苗移栽前一周；施用方式：人工施撒",
          u"改性天然矿物材料": u"施用节点：秧苗移栽前一周；施用方式：人工施撒"}

dict_c = {u"含磷型土壤调理剂": u"150kg/亩",
          u"凹凸棒土壤调理剂": u"160kg/亩",
          u"天象土壤调理剂": u"150kg/亩",
          u"改性天然矿物材料": u"200kg/亩"}
dict_c = {u"果朗铁": u"0.1kg/亩",
          u"降镉灵": u"0.5L/亩",
          u"美鑫隆": u"0.3kg/亩"}


def calc(x):
    try:
        s = dict_c[x]
    except:
        s = "-"
    return s


# print(calc(""))
# 农产品限值字典
def calc_value(value):
    try:
        value = float(value)
    except:
        value = 0
    return value


#
# import os
# import PIL
#
# data_path_y = r"E:\pic_path\水稻地块"  # 地块
# data_put_path = r"E:\pic_path\水稻地块_压缩后"  # 地块压缩后

# from PIL import Image
#
#
# def transfer(infile, outfile):
#     im = Image.open(infile)
#     x, y = im.size
#     x, y = int(x / (x * 0.0007)), int(y / (y * 0.0007))
#     print(x, y)
#     reim = im.resize((x, y))
#     reim.save(outfile, dpi=(96, 96))  ##200.0,200.0分别为想要设定的dpi值
#
#
# if __name__ == '__main__':
#     r = 1
#     for one_pic in os.listdir(data_path_y):
#         one_pic_name = os.path.join(data_path_y, one_pic)
#
#         infil = one_pic_name
#         outfile = os.path.join(data_put_path, f"水稻{r}.jpg")
#         transfer(infil, outfile)
#         r += 1
# import random
# a = random.randint(0,999)
# print(a)
# import plotly as py
# import plotly.figure_factory as ff
# pyplt = py.offline.plot
#
# df = [dict(Task="叶面调控", Start='2019-01-01', Finish='2019-02-02', Resource='Complete'),
#       dict(Task="优化施肥", Start='2019-02-15', Finish='2019-03-15', Resource='Incomplete'),
#       dict(Task="原位钝化", Start='2019-01-17', Finish='2019-02-17', Resource='Not Started'),
#       dict(Task="项目4", Start='2019-01-17', Finish='2019-02-17', Resource='Complete'),
#       dict(Task="项目5", Start='2019-03-10', Finish='2019-03-20', Resource='Not Started'),
#       dict(Task="项目6", Start='2019-04-01', Finish='2019-04-20', Resource='Not Started'),
#       dict(Task="项目7", Start='2019-05-18', Finish='2019-06-18', Resource='Not Started'),
#       dict(Task="项目8", Start='2019-01-14', Finish='2019-03-14', Resource='Complete')]
#
# colors = {'Not Started': 'rgb(220, 0, 0)',
#           'Incomplete': (1, 0.9, 0.16),
#           'Complete': 'rgb(0, 255, 100)'}
#
# fig = ff.create_gantt(df, colors=colors, index_col='Resource', group_tasks=True)
# pyplt(fig,r"C:\Users\65680\Desktop\xls.jpg")
# import numpy as np
# import pandas as pd
# import time
# path = r"C:\Users\65680\Desktop\AAAAAA\cumcm2011A附件_数据.xls"
# s1 = pd.read_excel(path, sheet_name="附件1")
# s2 = pd.read_excel(path, sheet_name="附件2")
# s3 = pd.read_excel(path, sheet_name="附件3")   # 读入一个文件中的三个表
# s1 = s1.values     # 转化为数值形式
# s2 = s2.values
# s3 = s3.values
# s1 = pd.DataFrame(s1)   # 转化为dataframe形式
# s2 = pd.DataFrame(s2)
# s3 = pd.DataFrame(s3)
# # print(s1)
# s1 = s1.iloc[2:, 0:5]
# s2 = s2.iloc[2:, 0:9]
# s3 = s3.iloc[2:, :]     # 去掉表头等不需要的部分，如表一的右边
# # print(s1,'\n')
# # print(s2,'\n')
# # print(s3,'\n')
#
# l = []  # 标准差列表
# for c in range(1, 9):  # 将各元素标准差放到列表
#     a = s2.iloc[:, c].std()
#     l.append(a)
#     # print(a, '\n')
#
# p = []  # 均值列表
# for c in range(1, 9):  # 各元素均值放到列表
#     a = s2.iloc[:, c].mean()
#     p.append(a)
#
# for c in range(0, 8):
#     themin = p[c] - 2 * l[c]
#     themax = p[c] + 2 * l[c]
#     print(themin, '  ', themax)
#     s2 = s2[(s2.iloc[:, c + 1] >= themin) & (s2.iloc[:, c + 1] <= themax)]  # 选出符合的行
#     print(s2)
#     print('\n', s2.shape[0], '\n')
# ID = pd.DataFrame(s2.iloc[:, 0])   # 表二0列单独成表
# print(ID)
# s1 = pd.merge(s1, ID, how="inner", right_on=0, left_on=0)    # 找出表一0列在表二0列的行，merge，join，constack进行拼接
# print(s1)
# path = r"C:/Users/65680/Desktop/AAAAAA/"  # 保存
# s1.to_excel(path+"sheet1.xlsx")
# s2.to_excel(path+"sheet2.xlsx")
# s3.to_excel(path+"sheet3.xlsx")
# -*- coding:UTF-8 -*-
# coding=utf-8
# from __future__ import print_function, absolute_import
# from gm.api import *
# """
# Dual Thrust是一个趋势跟踪系统
# 计算前N天的最高价－收盘价和收盘价－最低价。然后取这2N个价差的最大值，乘以k值。把结果称为触发值。
# 在今天的开盘，记录开盘价，然后在价格超过上轨（开盘＋触发值）时马上买入，或者价格低于下轨（开盘－触发值）时马上卖空。
# 没有明确止损。这个系统是反转系统，也就是说，如果在价格超过（开盘＋触发值）时手头有空单，则平空开多。
# 同理，如果在价格低于（开盘－触发值）时手上有多单，则平多开空。
# 选用了SHFE的rb2010 在2020-02-07 15:00:00 到 2020-04-15 15:00:00' 进行回测。
# 注意：
# 1：为回测方便，本策略使用了on_bar的一分钟来计算，实盘中可能需要使用on_tick。
# 2：实盘中，如果在收盘的那一根bar或tick触发交易信号，需要自行处理，实盘可能不会成交
# """
#
#
# # 策略中必须有init方法
# def init(context):
#     # 设置要进行回测的合约（可以在掘金终端的仿真交易中查询标的代码）
#     context.symbol = 'SHFE.rb2010'  # 订阅&交易标的, 此处订阅的是上期所的螺纹钢 2010
#     # 设置参数
#     context.N = 5
#     context.k1 = 0.2
#     context.k2 = 0.2
#     # 获取当前时间
#     time = context.now.strftime('%H:%M:%S')
#     # 如果策略执行时间点是交易时间段，则直接执行algo定义buy_line和sell_line，以防直接进入on_bar()导致context.buy_line和context.sell_line未定义
#     if '09:00:00' < time < '15:00:00' or '21:00:00' < time < '23:00:00':
#         algo(context)
#     # 如果是交易时间段，等到开盘时间确保进入algo()
#     schedule(schedule_func=algo, date_rule='1d', time_rule='09:00:00')
#     schedule(schedule_func=algo, date_rule='1d', time_rule='21:00:00')
#     # 只需要最新价，所以只需要订阅一个, 如果用tick，次数太多，用一分钟线代替
#     subscribe(symbols=context.symbol, frequency='60s', count=1)
#
#
# def algo(context):
#     # 取历史数据
#     data = history_n(symbol=context.symbol, frequency='1d', end_time=context.now,
#                      fields='symbol,open,high,low,close', count=context.N + 1, df=True)
#     # 取开盘价
#     # 回测模式下，开盘价可以直接用history_n取到
#     if context.mode == 2:
#         # 获取当天的开盘价
#         current_open = data['open'].loc[context.N]
#         # 去掉当天的实时数据
#         data.drop(context.N, inplace=True)
#     # 如果是实时模式，开盘价需要用current取到
#     else:
#         # 获取当天的开盘价
#         current_open = current(context.symbol)[0]['open']
#     # 计算Dual Thrust 的上下轨
#     HH = data['high'].max()
#     HC = data['close'].max()
#     LC = data['close'].min()
#     LL = data['low'].min()
#     range = max(HH - LC, HC - LL)
#     context.buy_line = current_open + range * context.k1  # 上轨
#     context.sell_line = current_open - range * context.k2  # 下轨
#
#
# def on_bar(context, bars):
#     # 取出订阅的这一分钟的bar
#     bar = bars[0]
#     # 取出买卖线
#     buy_line = context.buy_line
#     sell_line = context.sell_line
#     # 获取现有持仓
#     position_long = context.account().position(symbol=context.symbol, side=PositionSide_Long)
#     position_short = context.account().position(symbol=context.symbol, side=PositionSide_Short)
#     # 交易逻辑部分
#     # 如果超过range的上界
#     if bar.close > buy_line:
#         if position_long:  # 已经持有多仓，直接返回
#             return
#         elif position_short:  # 已经持有空仓，平仓再做多。
#             order_volume(symbol=context.symbol, volume=1, side=OrderSide_Buy,
#                          order_type=OrderType_Market, position_effect=PositionEffect_Close)
#             print('市价单平空仓', context.symbol)
#             order_volume(symbol=context.symbol, volume=1, side=OrderSide_Buy,
#                          order_type=OrderType_Market, position_effect=PositionEffect_Open)
#             print('市价单开多仓', context.symbol)
#         else:  # 没有持仓时，市价开多。
#             order_volume(symbol=context.symbol, volume=1, side=OrderSide_Buy,
#                          order_type=OrderType_Market, position_effect=PositionEffect_Open)
#             print('市价单开多仓', context.symbol)
#     # 如果低于range的下界
#     elif bar.close < sell_line:
#         if position_long:  # 已经持有多仓， 平多再开空。
#             order_volume(symbol=context.symbol, volume=1, side=OrderSide_Sell,
#                          order_type=OrderType_Market, position_effect=PositionEffect_Close)
#             print('市价单平多仓', context.symbol)
#             order_volume(symbol=context.symbol, volume=1, side=OrderSide_Sell,
#                          order_type=OrderType_Market, position_effect=PositionEffect_Open)
#             print('市价单开空仓', context.symbol)
#         elif position_short:  # 已经持有空仓，直接返回。
#             return
#         else:  # 没有持仓，直接开空
#             order_volume(symbol=context.symbol, volume=1, side=OrderSide_Sell,
#                          order_type=OrderType_Market, position_effect=PositionEffect_Open)
#             print('市价单开空仓', context.symbol)
#
#
# if __name__ == '__main__':
#     '''
#         strategy_id策略ID,由系统生成
#         filename文件名,请与本文件名保持一致
#         mode实时模式:MODE_LIVE回测模式:MODE_BACKTEST
#         token绑定计算机的ID,可在系统设置-密钥管理中生成
#         backtest_start_time回测开始时间
#         backtest_end_time回测结束时间
#         backtest_adjust股票复权方式不复权:ADJUST_NONE前复权:ADJUST_PREV后复权:ADJUST_POST
#         backtest_initial_cash回测初始资金
#         backtest_commission_ratio回测佣金比例
#         backtest_slippage_ratio回测滑点比例
#     '''
#     run(strategy_id='strategy_id',
#         filename='main.py',
#         mode=MODE_BACKTEST,
#         token='token_id',
#         backtest_start_time='2020-02-07 15:00:00',
#         backtest_end_time='2020-04-15 15:00:00',
#         backtest_initial_cash=30000,
#         backtest_commission_ratio=0.0001,
#         backtest_slippage_ratio=0.0001)
# a = 1
# b = 1
# if a ==1:
#     print("sdfsf")
# if b == 1:
#     print("kskggg")
# import requests
# import lxml.etree as le
# from functools import reduce
#
# global herf_g
#
# # requests标准格式
# content = requests.get(
#     url='https://support.hbfile.net/hc/zh-cn',
#     headers={
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
#     }
# ).content
#
# # 将首个网址爬出，保存源文件
# with open('huobia.html', 'wb') as f:
#     f.write(content)
#
# with open('huobia.html', 'rb') as l:
#     content = l.read()
#
# # 把源文件中的二级目标网址通过xpath取出
# contentx = le.HTML(content)
#
# hrefs = contentx.xpath("//ul[@class='article-list promoted-articles']//a/@href")
#
# with open("href.html", 'w') as u:  ###################################
#     for i in hrefs:
#         u.write(i + '\n')
#
# with open('href_duibi.html', 'r') as w:
#     href_g = w.readlines()
#
# print(href_g)
# print("href_g is", href_g[0])
# print("hrefs  is", hrefs[0])
#
# print("用==判断是否一致：", href_g[0].strip() == hrefs[0].strip())
# print("用is判断是否一致：", href_g[0] is hrefs[0])
#
#
# def isint(x):
#     if isinstance(x, int):
#         print("int")
#     if isinstance(x, str):
#         print("str")
#     if isinstance(x, list):
#         print("list")
#
#
# isint(href_g[0])
# isint(hrefs[0])
#
# # 判断是否相同，如果有更新的话，执行。只爬取最新的一个公告
# if href_g[0].strip() != hrefs[0].strip():
#     url = 'https://support.hbfile.net/' + hrefs[0]
#     print("如果无更新，不会打印此行\n", url)  # 如果上面未更新就不会有这一步
#     detail_content = requests.get(
#         url=url,
#         headers={
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
#         }
#
#     ).content
#
#     with open("shouye_list.html", 'wb') as f:
#         f.write(detail_content)
#
#     with open("shouye_list.html", 'rb') as l:
#         contentx = l.read()
#
#     contenty = le.HTML(contentx)
#
#     content_huobi = contenty.xpath("//div[@class='article-body']//p/text()")
#     # title=contenty.xpath("")
#
#     with open('huobi_download/new_01.html', 'w', encoding='utf-8') as x:
#         for i in content_huobi:
#             x.write(i + '\n')
#     # x.write(str(content_huobi))
#
#     with open('href.html', 'r') as l:
#         content_cd = l.read()
#     with open('href_duibi.html', 'w') as l:
#         l.write(content_cd)
# import time
# list_1 = ["I", "J", "K", "L", "M", "N"]
# for _x in list_1:
#     str1 = f"=countif({_x}:{_x},1)"
#     str2 = f"=countif({_x}:{_x},2)"
#     str3 = f"=countif({_x}:{_x},3)"
#     print(str1+" "+str2+" "+str3)
# import openpyxl
# import random
#
# work_path = r"C:\Users\65680\Desktop\calc.xlsx"
# work_book = openpyxl.load_workbook(work_path)
# ws = work_book.active
# rows = ws.max_row
#
# for one_row in range(1, rows + 1):
#     n = random.randint(1, 100)
#     b = random.randint(2, 20) * 0.01
#     print(n, b)
#     if n % 2 == 0:
#         if b >= 0.05:
#             ws[f"B{one_row}"].value = ws[f"A{one_row}"].value + ws[f"A{one_row}"].value * b
#         else:
#             ws[f"B{one_row}"].value = ws[f"A{one_row}"].value - ws[f"A{one_row}"].value * b
#     else:
#         if b >= 0.05:
#             ws[f"B{one_row}"].value = ws[f"A{one_row}"].value - ws[f"A{one_row}"].value * b
#         else:
#             ws[f"B{one_row}"].value = ws[f"A{one_row}"].value + ws[f"A{one_row}"].value * b
# work_book.save(r"C:\Users\65680\Desktop\calcww.xlsx")
# coding:utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#
# data = {
#     'China': [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2500],
#     'America': [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100],
#     'Britain': [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],
#     "Russia": [800, 1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
# }
# df = pd.DataFrame(data)
#
# # df.plot.box(title="Consumer spending in each country", vert=False)
# df.plot.box(title="CD")
#
# plt.grid(linestyle="--", alpha=0.3)
# plt.show()
# import random
# print(random.randint(1,1000))
# pp_dict = {}
# pp_dict["1"] = 5
# print(pp_dict)
a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 6]
c = a + b
for number, key in enumerate(c):
    print(number)
