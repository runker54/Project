# coding:utf-8
import os
import shutil
import re
import time
source_path = r'E:\金中镇\金中镇'
pdf_path = r'E:\金中镇\PDF'
source_list = []
for roots, dirs, files in os.walk(source_path):
    for one_file in files:
        if one_file.endswith('pdf') and one_file[:6] == '520121':
            old_path = os.path.join(roots, one_file)
            new_path = os.path.join(pdf_path, one_file)
            try:
                shutil.copyfile(new_path, old_path)
            except:
                print('编码不一致')