# coding:utf-8
import re
import os
import time
import shutil
import xlrd
import xlwt
from aip import AipOcr
APP_ID = '11383764'
API_KEY = 'gwKFpUvbjQw0doKB6eMPNI1a'
SECRET_KEY = '0ELuilEhYzpvvYGiGS91fmCr1tDxx2XO'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 调查表路径
dc_sheet = r"C:\Users\65680\Desktop\1\调查表"
# 种植情况调查表路径
zw_sheet = r"C:\Users\65680\Desktop\1\种植情况调查表"
# 文件资料路径
wjzl_adress = r"C:\Users\65680\Desktop\1\文件资料"
# 最终文件存储路径
cc_adress = r"C:\Users\65680\Desktop\新店镇"
# 图片位置
picture_adress = r"E:\新店镇台账\衙院村安全利用类\耕地调查表"
path_list = os.listdir(picture_adress)
start_time = time.time()
# 构造措施查询字典
cs_dict = {}
xz_dict = {}
zllb_dict = {}
sheet_path = r"C:\Users\65680\Desktop\1\清镇市导表20200721.xls"
sheet_ = xlrd.open_workbook(sheet_path)
ws = sheet_.sheet_by_index(0)
nrows = ws.nrows
# 将无法识别的文件写入记录
work_book = xlwt.Workbook()
ws1 = work_book.add_sheet("Data")
for one_row in range(1, nrows):
    s = ""
    dkbm = ws.row(one_row)[0].value
    xz = ws.row(one_row)[3].value
    zllb = ws.row(one_row)[6].value
    xz_dict[dkbm] = xz
    zllb_dict[dkbm] = zllb
    if ws.row(one_row)[12].value != "":
        s += "F"
    if ws.row(one_row)[14].value != "":
        s += "H"
    if ws.row(one_row)[18].value != "":
        s += "L"
    if ws.row(one_row)[21].value != "":
        s += "O"
    cs_dict[dkbm] = s
# 图片识别编码并命名
r = 1
for one_picture in path_list:
    if one_picture[-3:].lower() == "jpg":
        picture = os.path.join(picture_adress, one_picture)
        print(picture)
        with open(picture, 'rb') as fp:
            photo = fp.read()
            photo_recognition = client.basicAccurate(photo)  # 高精度版
            result = photo_recognition['words_result']
            print(str(result))
            name = re.findall("520181\d\d\d\d\d\d", str(result))
        if len(name) == 0:
            ws1.write(r, 1, one_picture)
            r += 1
            print("%s识别失败" % one_picture)
        else:
            print(name[0])
            file_adress = os.path.join(cc_adress, name[0])
            newname = os.path.join(picture_adress, str(name[0]) + ".jpg")
            os.rename(picture, newname)
            # 创建单个文件文件夹
            os.mkdir(os.path.join(cc_adress, name[0]))
            # 创建作物调查表文件夹
            os.mkdir(os.path.join(file_adress, "种植情况调查表"))
            # 移入调查图片
            shutil.copyfile(newname, os.path.join(os.path.join(cc_adress, name[0]), str(name[0]) + ".jpg"))
            # 移入作物调查表
            zzqkdcb_adress = os.path.join(file_adress, "种植情况调查表")
            zzqkdcbzl_adress = os.path.join(wjzl_adress, "种植情况调查表")
            source_pathzw = os.path.abspath(zzqkdcbzl_adress)  # 种植情况调查表文件夹
            target_pathzw = os.path.abspath(zzqkdcb_adress)  # 目标文件夹
            if not os.path.exists(target_pathzw):
                # 如果目标路径不存在原文件夹的话就创建
                os.makedirs(target_pathzw)
            if os.path.exists(source_pathzw):
                # 如果目标路径存在原文件夹的话就先删除
                shutil.rmtree(target_pathzw)
            shutil.copytree(source_pathzw, target_pathzw)
            # 输出该地块措施
            all_cs = cs_dict[name[0]]
            print("该地块包含措施%s" % all_cs)
            # 判断措施深翻耕
            if "F" in all_cs:
                os.mkdir(os.path.join(file_adress, "深翻耕"))
                sfg_adress = os.path.join(file_adress, "深翻耕")
                sfgzl_adress = os.path.join(wjzl_adress, "深翻耕")
                source_path = os.path.abspath(sfgzl_adress) # 深翻耕文件夹
                target_path = os.path.abspath(sfg_adress) # 目标文件夹
                if not os.path.exists(target_path):
                    # 如果目标路径不存在原文件夹的话就创建
                    os.makedirs(target_path)
                if os.path.exists(source_path):
                    # 如果目标路径存在原文件夹的话就先删除
                    shutil.rmtree(target_path)
                shutil.copytree(source_path, target_path)
            # 判断措施优化施肥
            if "H" in all_cs:
                os.mkdir(os.path.join(file_adress, "清镇市犁倭镇2020测土配方施肥项目实施方案"))
                yhsf_adress = os.path.join(file_adress, "清镇市犁倭镇2020测土配方施肥项目实施方案")
                yhsfzl_adress = os.path.join(wjzl_adress, "清镇市犁倭镇2020测土配方施肥项目实施方案")
                source_path = os.path.abspath(yhsfzl_adress) # 优化施肥文件夹
                target_path = os.path.abspath(yhsf_adress) # 目标文件夹
                if not os.path.exists(target_path):
                    # 如果目标路径不存在原文件夹的话就创建
                    os.makedirs(target_path)
                if os.path.exists(source_path):
                    # 如果目标路径存在原文件夹的话就先删除
                    shutil.rmtree(target_path)
                shutil.copytree(source_path, target_path)
            # 判断措施退耕还林
            if "L" in all_cs:
                os.mkdir(os.path.join(file_adress, "清镇市退耕还林文件"))
                tghl_adress = os.path.join(file_adress, "清镇市退耕还林文件")
                tghlzl_adress = os.path.join(wjzl_adress, "清镇市退耕还林文件")
                source_path = os.path.abspath(tghlzl_adress) # 退耕还林文件夹
                target_path = os.path.abspath(tghl_adress) # 目标文件夹
                if not os.path.exists(target_path):
                    # 如果目标路径不存在原文件夹的话就创建
                    os.makedirs(target_path)
                if os.path.exists(source_path):
                    # 如果目标路径存在原文件夹的话就先删除
                    shutil.rmtree(target_path)
                shutil.copytree(source_path, target_path)
            # 判断措施退耕还林
            if "O" in all_cs:
                os.mkdir(os.path.join(file_adress, "2019年秋冬季和2020年种植结构调整工作实施方案"))
                os.mkdir(os.path.join(file_adress, "2020年农业产业结构调整实施方案"))
                os.mkdir(os.path.join(file_adress, "清镇市产业结构调整文件"))
                tghl_adress = os.path.join(file_adress, "清镇市产业结构调整文件")
                tghlzl_adress = os.path.join(wjzl_adress, "清镇市产业结构调整文件")
                tghl_adress1 = os.path.join(file_adress, "2020年农业产业结构调整实施方案")
                tghlzl_adress1 = os.path.join(wjzl_adress, "2020年农业产业结构调整实施方案")
                tghl_adress2 = os.path.join(file_adress, "2019年秋冬季和2020年种植结构调整工作实施方案")
                tghlzl_adress2 = os.path.join(wjzl_adress, "2019年秋冬季和2020年种植结构调整工作实施方案")
                source_path = os.path.abspath(tghlzl_adress) # zz文件夹
                target_path = os.path.abspath(tghl_adress) # 目标文件夹
                source_path1 = os.path.abspath(tghlzl_adress1) # zz文件夹
                target_path1= os.path.abspath(tghl_adress1) # 目标文件夹
                source_path2 = os.path.abspath(tghlzl_adress2) # zz文件夹
                target_path2 = os.path.abspath(tghl_adress2) # 目标文件夹

                if not os.path.exists(target_path):
                    os.makedirs(target_path)
                if os.path.exists(source_path):
                    shutil.rmtree(target_path)
                if not os.path.exists(target_path1):
                    os.makedirs(target_path1)
                if os.path.exists(source_path1):
                    shutil.rmtree(target_path1)
                if not os.path.exists(target_path2):
                    os.makedirs(target_path2)
                if os.path.exists(source_path2):
                    shutil.rmtree(target_path2)
                shutil.copytree(source_path, target_path)
                shutil.copytree(source_path1, target_path1)
                shutil.copytree(source_path2, target_path2)
xzmc = xz_dict[name[0]]
work_book.save(r"C:\Users\65680\Desktop\存储位置\%s识别失败名单.xls" % xzmc)