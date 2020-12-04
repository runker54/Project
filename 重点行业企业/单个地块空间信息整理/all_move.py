# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-26
# -----------------------
import os
import shutil

data_path = r'C:\Users\65680\Desktop\单个地块文件夹'
yi = r'C:\Users\65680\Desktop\一'
noyi = r'C:\Users\65680\Desktop\不等于一'
count_number = 0
dir_list = []
for roots, dirs, files in os.walk(data_path):
    for one_dir in dirs:
        if one_dir[:2] == '52':
            dir_list.append(os.path.join(roots, one_dir))
for one_ice in dir_list:
    try:
        if len(os.listdir(one_ice)) == 1:
            shutil.move(one_ice, yi)
        else:
            shutil.move(one_ice, noyi)
    except:
        print('父级时已移动')
