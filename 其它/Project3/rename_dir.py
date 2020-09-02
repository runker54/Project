# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-08-31
# -------------------------------------------------------------------------------
import os

data_path = r"C:\Users\65680\Desktop\织金县--图斑"
dir_list = os.listdir(data_path)
print(dir_list)
for roots, dirs, files in os.walk(data_path):
    for dir in dirs:
        old_dir = os.path.join(roots, dir)
        new_dir = os.path.join(roots, str(dir) + "--台账表格")
        os.rename(old_dir, new_dir)

