# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-26
# -----------------------
import os
import shutil

source_path = r'C:\Users\65680\Desktop\单个地块文件夹'
arraty_path = r'C:\Users\65680\Desktop\aurth'  # 等于一的位置
no_arraty_path = r'C:\Users\65680\Desktop\auoty'  # 不等于一的位置
one_qx_dir_list = [os.path.join(source_path, i) for i in os.listdir(source_path)]
for one_qx in one_qx_dir_list:
    one_qx_list = [os.path.join(one_qx, x) for x in os.listdir(one_qx)]
    for one_dk in one_qx_list:
        length = len(os.listdir(one_dk))  # 等于一的情况
        if length == 1:
            shutil.move(one_dk, arraty_path)
        else:
            shutil.move(one_dk, no_arraty_path)
