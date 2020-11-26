# coding:utf-8
import os
import time

data_path = r'D:\重点行业企业资料\520000贵州省数据（入库后随系统及时更新，保持数据与系统同步）\520000贵州省单个地块空间信息（20200805）\图片'
list1 = []
for roots, dirs, files in os.walk(data_path):
    for fiel in files:
        x = fiel[6]
        pp_path = os.path.join(roots, fiel)
        if x == '6':
            os.remove(pp_path)
