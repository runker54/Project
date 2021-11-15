#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2021-11-09
# Author:Runker54
# ----------------------
import os
import paramiko
import openpyxl

data_path = r"D:\P_path\数据下载\dict1.xlsx"
local_dir = r"D:\dir"
USERNAME = "root"
PASSWORD = ""
HOST = ""
PORT = 22
work_b = openpyxl.load_workbook(data_path)
wb = work_b.active
rows = wb.max_row
adres_dict = {"east": "东", "south": "南", "west": "西", "north": "北", "gps": "GPS", "director": "负责人",
              "center": "中心点采样过程", "offset1": "偏移证明", "offset2": "偏移证明1", "other": "其它", "soilcenter": "中心点采样过程", }
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=HOST, username=USERNAME, password=PASSWORD)
trans = client.get_transport()
sftp = paramiko.SFTPClient.from_transport(trans)

while True:
    try:
        n = 1

        for one_row in range(2, rows + 1):
            key_value = wb[f"C{one_row}"].value  # 编码
            quxian_value = wb[f"M{one_row}"].value  # 区县
            local_dir_path_quxian = os.path.join(local_dir, quxian_value)  # 图片本地存放文件夹
            local_dir_path = os.path.join(local_dir_path_quxian, key_value)  # 图片本地存放文件夹
            adres_value = wb[f"E{one_row}"].value  # 方位
            if os.path.exists(local_dir_path):
                pass
            else:
                os.makedirs(local_dir_path)
            path_value = wb[f"D{one_row}"].value  # 路径
            path_value_path = str(path_value).replace("/files", "/mnt/uploaded_files")  # 服务器图片路径
            local_pic_name = key_value + "_" + adres_dict[adres_value] + ".jpg"  # 本地图片name
            local_pic_path = os.path.join(local_dir_path, local_pic_name)  # 本地图片绝对路径
            n += 1
            if os.path.exists(local_pic_path):
                print("文件已存在")
            else:
                sftp.get(path_value_path, local_pic_path)  # 数据下载
                print(f"{local_pic_name}图片下载已完成")
            print(f"共计{rows}张，已下载{n}张。")
    except:
        print("正在重连")
