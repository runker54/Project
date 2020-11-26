# coding:utf-8
import os
import shutil
import re
import time

in_path = r"C:\Users\ols\Desktop\借力地块更新"
out_path = r'C:\Users\ols\Desktop\out_path'
for roots, dirs, files in os.walk(in_path):
    for one_file in files:
        number_id = re.findall('\d+?', str(one_file))
        print(number_id)
        x = len(number_id)
        number_text = re.findall(r"\d{%d}" % x, str(one_file))[0]
        old_path = os.path.join(roots, one_file)   # 原文件位置
        print(number_text)
        new_dir_adress = os.path.join(out_path, number_text)  # 新文件夹
        try:
            os.mkdir(new_dir_adress)
        except:
            pass
        new_name = ''
        if '点' in one_file:
            new_name = number_text + 'point' + one_file[-4:]
        else:
            new_name = number_text + 'polygon' + one_file[-4:]
        new_path = os.path.join(new_dir_adress, new_name)
        shutil.copyfile(old_path, new_path)

