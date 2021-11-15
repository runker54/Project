#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2021-11-09
# Author:Runker54
# ----------------------
import paramiko
import os
import paramiko
import openpyxl

data_path = r"C:\Users\65680\Desktop\dict.xlsx"
local_dir = r"F:\从江县2020年耕地生产障碍修复利用项目台账资料\12.联合攻关区集中推进区样品采集\从江县样品采集图片"
USERNAME = "root"
PASSWORD = ""
HOST = ""
PORT = 22
work_b = openpyxl.load_workbook(data_path)
wb = work_b["从江县"]
rows = wb.max_row
adres_dict = {"east": "东", "south": "南", "west": "西", "north": "北", "gps": "GPS", "director": "负责人",
              "center": "中心点采样过程", "offset1": "偏移证明", "offset2": "偏移证明1", "other": "其它", "soilcenter": "中心点采样过程", }
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=HOST, username=USERNAME, password=PASSWORD)
trans = client.get_transport()
sftp = paramiko.SFTPClient.from_transport(trans)
n = 0
for one_row in range(2, rows + 1):
    key_value = wb[f"C{one_row}"].value  # 编码
    local_dir_path = os.path.join(local_dir, key_value)  # 图片本地存放文件夹
    adres_value = wb[f"E{one_row}"].value  # 方位
    if os.path.exists(local_dir_path):
        pass
    else:
        os.makedirs(local_dir_path)
    path_value = wb[f"D{one_row}"].value  # 路径
    path_value_path = str(path_value).replace("/files", "/mnt/uploaded_files")  # 服务器图片路径
    local_pic_name = key_value + "_" + adres_dict[adres_value] + ".jpg"
    local_pic_path = os.path.join(local_dir_path, local_pic_name)
    n += 1
    if os.path.exists(local_pic_path):
        print("图片已存在")
    else:
        sftp.get(path_value_path, local_pic_path)
    print(f"已下载{n}/{rows},{local_pic_name}图片下载已完成")
