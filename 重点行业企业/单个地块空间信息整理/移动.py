# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-26
# -----------------------
import os
import shutil
data_path = r'C:\Users\65680\Desktop\不等于一'
arrat_path = r'C:\Users\65680\Desktop\cie_3'


def calc(path):
    temp_path = path
    while True:
        if len(os.listdir(temp_path)) == 1:
            temp_path = os.path.join(temp_path, os.listdir(temp_path)[0])
        if len(os.listdir(temp_path)) == 0:
            os.removedirs(temp_path)
        else:
            break
    return temp_path

count_number = 0

for one_dir in [os.path.join(data_path, i) for i in os.listdir(data_path)]:
    move_path = calc(one_dir)
    shutil.move(move_path, arrat_path)
    print(one_dir)
    count_number += 1

print(count_number)
