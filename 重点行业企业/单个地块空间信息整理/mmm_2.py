# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-26
# -----------------------
import os
import shutil
data_path = r'C:\Users\65680\Desktop\auoty2'

hack = r'C:\Users\65680\Desktop\autoys'
one_dk_list = [os.path.join(data_path, i) for i in os.listdir(data_path)]
print(one_dk_list)
for one_dk in one_dk_list:
    if len(os.listdir(one_dk)) == 0:
        os.removedirs(one_dk)
    else:
        print(one_dk)
        move_path = os.path.join(one_dk, os.listdir(one_dk)[0])
        shutil.move(move_path, hack)
