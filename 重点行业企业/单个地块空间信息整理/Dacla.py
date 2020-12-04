# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-26
# -----------------------
import os
import shutil
data_path = r'C:\Users\65680\Desktop\none'
for roots, dirs, files in os.walk(data_path):
    for file in files:
        print()
        file_source_path = os.path.join(roots, file)
        temp_name = file[:13]
        temp_dir = os.path.join(data_path, temp_name)
        shutil.move(file_source_path, temp_dir)
