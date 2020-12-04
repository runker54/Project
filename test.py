# coding:utf-8
# import os
# import shutil

# rename_path = r"F:\1台账导出文档基础资料\湄潭县台账\湄潭县图片\耕地种植照片"
# adress = r"F:\1台账导出文档基础资料\湄潭县台账\湄潭县图片\耕地种植照片"
# for roots, dirs, files in os.walk(rename_path):
#     for file in files:
#         dir_name = '520328000'+file
#         dir_name_text = dir_name[:12]
#         old_name_adress = os.path.join(roots, file)
#         dir_name_adress = os.path.join(adress, dir_name_text)
#         new_name_adress = os.path.join(dir_name_adress, dir_name)
#         try:
#             os.makedirs(dir_name_adress)
#         except:
#             print('文件夹已存在')
#         shutil.copyfile(old_name_adress, new_name_adress)
# data_path = r'C:\Users\65680\Desktop\temp_dir'
# list_dir = os.listdir(data_path)
# for one_dir in list_dir:
#     os.rename(os.path.join(data_path, one_dir), os.path.join(data_path, '520328000' + one_dir))
# value_list = {'品种调整': 1, '石灰调节': 2, '水分调控': 3}
# sum_total = ''
# for one_mess in value_list:
#     sum_total+=one_mess
# print(sum_total)

# coding:utf-8
# def auto_calc(x):
#     ee = x.extent.xmin
#     ew = x.extent.xmax
#     nn = x.extent.ymin
#     nm = x.extent.ymax
#     text = "东经："+str(round(ee, 6))+"-"+str(round(ew, 6))+","+"北纬："+str(round(nn, 6))+"-"+str(round(nm, 6))
#     return text
import os
# import shutil
#
# source_path = r'C:\Users\65680\Desktop\新建文件夹 (2)'
# array_path = r'C:\Users\65680\Desktop\新建文件夹 (3)'
# count_number = 0
# for roots, dirs, files in os.walk(source_path):
#     for one_pictures in files:
#         copy_path = os.path.join(roots, one_pictures)  # 图片所在路径
#         # 建立文件夹
#         temp_dirname = one_pictures[:13]  # 获取编码
#         temp_dir = os.path.join(array_path, temp_dirname)
#         # 创建文件夹
#         try:
#             os.makedirs(temp_dir)
#         except:
#             print('文件夹已存在')
#         # 复制文件
#         paste_path = os.path.join(temp_dir, one_pictures)
#         # 复制
#         shutil.move(copy_path, paste_path)
#         count_number += 1
# print(count_number)
# for ipx in range(0,708, 300):
#     print(ipx)
# import random
# x = round(random.random(), 2)
# print(x)
from PIL import Image

# im = Image.open(r"C:\Users\65680\Desktop\犁倭镇_页面_5703.png")
# print(im.size)
# x, y = im.size
# print(x)
# x1 = 240
# y1 = 210
# w = x - 200
# h = y - 110
# print(w, h)
# cut = im.crop((x1, y1, w, h))
# cut.save(r"C:\Users\65680\Desktop\暗流镇111.png")
skip = 16
def calc_index(*args):
    """传入具有页码的文本文件位置，返回各个调查表所在的页码列表，各元素类型为字符串型"""
    calc_stream = open(*args).readlines()
    calc_stream_list = [str(int(one_line.split('\t')[1].strip()) + skip - 1) for one_line in calc_stream]
    return calc_stream_list
print(calc_index(r'C:\Users\65680\Desktop\玉屏县页码\朱家场镇.txt' ))
