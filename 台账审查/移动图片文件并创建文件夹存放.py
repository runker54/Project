# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-27
# -----------------------
import os
import shutil
import re
from tqdm import tqdm

source_path = r'F:\错误图片'  # 存放散乱图片的文件夹位置
array_path = r'F:\0安全利用台账\0清镇市台账\清镇市导台账需要\清镇市图片_整理后'  # 整理后存放的位置
count_number = 0
error_number = 0
for roots, dirs, files in os.walk(source_path):
    for one_pictures in tqdm(files):
        if one_pictures.endswith('jpg'):

            move_source_path = os.path.join(roots, one_pictures)
            try:
                copy_name = re.findall(r'\d{12}', one_pictures)[0]
                move_array_path = os.path.join(array_path, copy_name)
            except:
                pass
            move_array_path1 = os.path.join(move_source_path, one_pictures)
            try:
                os.makedirs(move_array_path)
            except:
                pass
            shutil.copy(move_source_path, move_array_path)
            count_number += 1

print(f'共移动图片{count_number}张！')
print(f'错误图片{error_number}张！')
