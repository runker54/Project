# coding:utf-8
import os
data_path = r'C:\Users\ols\Desktop\借力调查地块信息汇总\借力调查地块'
file_list = os.listdir(data_path)
for one_dir in file_list:
    name = one_dir
    for one_file in os.listdir(os.path.join(data_path, one_dir)):
        print(name)
        name_path = os.path.join(data_path, one_dir)
        re_file_path = os.path.join(name_path, one_file)
        end_name = name + one_file[one_file.index('p'):]
        new_name_path = os.path.join(name_path, end_name)
        os.rename(re_file_path, new_name_path)
