# coding:utf-8
import os
import shutil
import re
import time
data_path = r'E:\毛云乡'
picture_path = r'E:\毛云乡平面布置图'
picture_dict = {}
name_dict = {}
for roots, dirs, files in os.walk(picture_path):
    for file in files:
        name_key = re.findall(r'520121\d{6}', file)[0]
        picture_adress = os.path.join(roots, file)
        picture_dict[name_key] = picture_adress
        name_dict[name_key] = file

for roots, dirs, files in os.walk(data_path):
    for file in files:
        if file[:6] == '520121':
            name = file[:12]
            make_dir = os.path.join(roots, name)  # 地块文件夹
            # try:
            #     os.makedirs(make_dir)
            # except:
            #     print('文件夹已存在')
            # old_path = os.path.join(roots, file)
            # new_path = os.path.join(make_dir,file)
            # shutil.move(old_path, new_path)
            try:
                old_path = picture_dict[name]
                new_path = os.path.join(make_dir, name_dict[name])
                shutil.rmtree(new_path)
                # shutil.copyfile(old_path,new_path)
            except:
                print(name)