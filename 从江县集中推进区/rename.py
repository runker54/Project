#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2021-10-09
# Author:Runker54
# -----------------------
import os
import openpyxl
import shutil
import time

word_path = r'C:\Users\65680\Desktop\ccc'
new_path = r'C:\Users\65680\Desktop\ddd'
b = open(r'C:\Users\65680\Desktop\rrr.txt')
text = b.readlines()
cc_list = os.listdir(word_path)

for one_word in cc_list:
    old_name = os.path.join(word_path, one_word)
    print(old_name)
    id = one_word.find("_")
    id2 = one_word.find(".")
    print(one_word)
    id_number = one_word[id+1:id2]
    print(id_number)
    time.sleep(1)
    new_name = os.path.join(new_path, str(text[int(id_number)-1]).strip() + ".docx")
    # os.rename(os.path.join(word_path, one_word), os.path.join(new_path, str(text[r]) + ".docx"))
    # os.rename(old_name,new_name)
    shutil.move(old_name,new_name)

