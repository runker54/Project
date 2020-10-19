# coding:utf-8
# import os
# rename_path = r"C:\Users\65680\Desktop\BT_XCTP\佐证图片"
# list_dir = os.listdir(rename_path)
# for one_dir in list_dir:
#     old_dir = os.path.join(rename_path, one_dir)
#     new_dir = os.path.join(rename_path, "520328000"+str(one_dir))
#     os.rename(old_dir, new_dir)
#     print(f"{old_dir}已更名为{new_dir}")
import os
import shutil
import re
import time
import xlwt
# work_book = xlwt.Workbook('utf-8')
# work_sheet = work_book.add_sheet("data")
# data_path = r'G:\1台账导出文档基础资料\思南县台账\思南县调查表\思南县调查表cut'
# r = 1
# for roots, dirs, files in os.walk(data_path):
#     for file in files:
#         file_name = file[:12]
#         work_sheet.write(r,0,file_name)
#         r+=1
#         print(file_name)
# work_book.save(r'C:\Users\65680\Desktop\新建文件夹\对比.xls')
i = 1
list1 = []
while True:
    i += 1
    list1.append(i)
    print(i)
