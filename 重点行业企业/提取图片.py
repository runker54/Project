# coding:utf-8
import os
import shutil

data_path = r'E:\空间信息成果集成\520000贵州省单个地块空间信息'
out_path = r'C:\Users\ols\Desktop\截图'
for roots, dirs, files in os.walk(data_path):
    for file in files:
        if file.endswith('jpg'):
            if file[6] == '6':
                picture_path = os.path.join(roots, file)
                out_path_dir = os.path.join(out_path, file)
                shutil.copyfile(picture_path, out_path_dir)