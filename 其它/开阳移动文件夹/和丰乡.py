# coding:utf-8
import os
import re
import shutil
import time
sourece_path = r'F:\开阳台账-扫描\宅吉乡'
picture_path = r'F:\开阳县耕地安全利用类别划分图斑'
picture_dict = {}  # 图片路径字典
picture_name_dict = {}  # 图片名称字典
for proots, pdirs, pfiles in os.walk(picture_path):
    for pfile in pfiles:
        pname = re.findall(r'520121\d{6}', pfile)[0]
        pname_path = os.path.join(proots, pfile)
        picture_dict[pname] = pname_path
        picture_name_dict[pname] = pfile
print(picture_name_dict)
print(picture_dict)
for roots, dirs, files in os.walk(sourece_path):
    for file in files:
        if file[:6] == '520121':
            file_name = file[:12]
            make_dir = os.path.join(roots, file_name)  # 单个地块文件夹
            try:
                os.makedirs(make_dir)
            except:
                '文件夹已存在'
            try:
                old_path = os.path.join(roots, file)  # 调查表pdf
                new_path = os.path.join(make_dir, file)  # 调查表移动终点
                # picture_in_path = picture_dict[file_name]  # 图片原路径
                # picture_out_path = os.path.join(make_dir, picture_name_dict[file_name])  # 图片输出路径
                shutil.move(old_path, new_path)
                # shutil.copyfile(picture_in_path, picture_out_path)
            except:
                print(file_name)
time.sleep(5)
for roots1, dirs1, files1 in os.walk(sourece_path):
    for file11 in files1:
        if file11[:6] == '520121':
            file_name1 = file11[:12]
            try:
                picture_in_path = picture_dict[file_name1]
                picture_out_path = os.path.join(roots1, picture_name_dict[file_name1])
                shutil.copyfile(picture_in_path, picture_out_path)
            except:
                print(file_name1)
