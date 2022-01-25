#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2021-11-25
# Author:Runker54
# ----------------------
import os
import paramiko
import openpyxl

local_dir = r"E:\pic_path\玉米品种"
USERNAME = "root"
PASSWORD = "runker54.++"
HOST = "120.77.46.249"
PORT = 22
adres_dict = ["ZY002858", "ZY002668", "ZY001643", "ZJ002877", "SQ003325", "SQ003033", "SQ002673", "SQ000345",
              "QX003432", "QX003403", "QX002933", "QX000879", "QX000520", "MT003966", "MT000387", "MT000113",
              "LD004176", "LD000368", "JK007175", "JK007114", "JK006351", "JK006331", "JK001600", "JK000577",
              "DF002588", "522302217410", "522302216121", "522302216083", "522302215680", "522302214794"]
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=HOST, username=USERNAME, password=PASSWORD)
trans = client.get_transport()
sftp = paramiko.SFTPClient.from_transport(trans)
dir_path = r"C:\Users\65680\Desktop\样品采集名单\地址路径表.xlsx"
wb_a = openpyxl.load_workbook(dir_path)
ws_a = wb_a.active
rows = ws_a.max_row
dict_adress = {}
for one_row in range(2, rows):
    bianma = ws_a[f"F{one_row}"].value
    leixin = ws_a[f"H{one_row}"].value
    url = ws_a[f"G{one_row}"].value
    dict_adress[bianma + leixin] = url

cass_dict = {"ZY004226": "中浙优8号", "ZY003589": "天优华占", "ZY003559": "中优177", "ZY002858": "黔单988", "ZY002668": "好玉4号",
             "ZY001643": "黔兴7号", "ZY001015": "晶两优1206", "ZJ002877": "织金3号", "SQ005819": "中浙优10号", "SQ003325": "正大999",
             "SQ003033": "邦玉539", "SQ002673": "先玉1171", "SQ000345": "中单808", "QX003432": "贵农玉188", "QX003403": "安单3号",
             "QX002933": "靖丰8号", "QX000879": "盛农3号", "QX000520": "顺单7号", "MT003966": "正大99", "MT001230": "糯谷",
             "MT000387": "天池2号", "MT000113": "隆玉68", "LD006046": "无", "LD004176": "正大808", "LD001925": "泰优808",
             "LD000368": "东单808", "JK007175": "青青515", "JK007114": "西抗18", "JK006351": "中单", "JK006331": "新中玉",
             "JK005799": "川优3727", "JK002779": "得优3301", "JK001600": "青青500", "JK000577": "自留种", "JK000188": "中9优2号",
             "DF002588": "赫单4号", "522302217410": "亲瑞189", "522302216121": "隆白1号", "522302216083": "大天1号",
             "522302215680": "遵玉", "522302214794": "金玉999", "522302210031": "宜香优2115"
             }
while True:
    try:
        n = 1
        for one_row in adres_dict:
            one_row = str(one_row)
            key_value = one_row  # 编码
            local_dir_path_quxian = local_dir  # 图片本地存放文件夹
            path_value = dict_adress[one_row + "variety"]
            path_value_path = str(path_value).replace("/files", "/mnt/uploaded_files")  # 服务器图片路径
            local_pic_name = cass_dict[one_row] + ".jpg"  # 本地图片name
            local_pic_path = os.path.join(local_dir, local_pic_name)  # 本地图片绝对路径
            n += 1
            if os.path.exists(local_pic_path):
                print("文件已存在")
            else:
                sftp.get(path_value_path, local_pic_path)  # 数据下载
                print(f"{local_pic_name}图片下载已完成")
            print(f"共计{len(adres_dict)}张，已下载{n}张。")
    except:
        print("正在重连")
