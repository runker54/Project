# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-26
# -----------------------
import os
data_path = r'C:\Users\65680\Desktop\none'
dir_list = [os.path.join(data_path, i) for i in os.listdir(data_path)]
for one_dir in dir_list:
    if len(os.listdir(one_dir)) == 0:
        os.removedirs(one_dir)
        print(one_dir)
