#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2021-11-09
# Author:Runker54
# ----------------------
import os
import paramiko
import openpyxl

data_path = r"C:\Users\65680\Desktop\样品采集名单\地址表格20211129.xlsx"
local_dir = r"C:\Users\65680\Desktop\样品采集名单"
USERNAME = ""
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
            provice = wb[f"A{one_row}"].value  # 省
            city = wb[f"B{one_row}"].value  # 市
            county = wb[f"C{one_row}"].value  # 区县
            project = wb[f"D{one_row}"].value  # 项目名称
            town = wb[f"E{one_row}"].value  # 乡镇
            village = wb[f"F{one_row}"].value  # 村
            path_value = wb[f"G{one_row}"].value  # 路径
            adres_value = wb[f"H{one_row}"].value  # 方位
            key_value = wb[f"I{one_row}"].value  # 编码
            local_dir_path = os.path.join(local_dir, "%s/%s/%s/%s/%s/%s/%s" % (
            provice, city, county, project, town, village, key_value))  # 图片本地存放文件夹
            if os.path.exists(local_dir_path):
                pass
            else:
                os.makedirs(local_dir_path)
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
