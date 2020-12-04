# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-27
# -----------------------
import fitz
import os
import re
import xlrd
from PIL import Image
from tqdm import tqdm
import time

xy_name = '乐治镇'
text_path = r'F:\乐治镇\readtext.txt'
diaochabiao_path = r'F:\乐治镇\乐治镇表'
pingmianbuzhitu_path = r'F:\乐治镇\乐治镇图'

pdf_dir = []


def get_file(adress_):
    for roots, dirs, files in os.walk(adress_):
        for docuname in files:
            if os.path.splitext(docuname)[1] == '.pdf':  # 目录下包含.pdf的文件
                pdf_dir.append(os.path.join(roots, docuname))
    print(len(pdf_dir))


def conver_img():
    for pdf in pdf_dir:
        doc = fitz.open(pdf)
        pdf_name = os.path.splitext(pdf)[0]
        for pg in range(doc.pageCount):
            page = doc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为n，这将为我们生成分辨率提高n^2倍的图像。
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            pm.writePNG('%s%s.jpg' % (pdf_name, pg))
            print(pdf)


def calc_index(*args):
    """传入具有页码的文本文件位置，返回各个调查表所在的页码列表，各元素类型为字符串型"""
    calc_stream = open(*args).readlines()
    calc_stream_list = [one_line.split('\t')[2].strip() for one_line in calc_stream]
    return calc_stream_list


x = calc_index(text_path)

get_file(diaochabiao_path)
conver_img()

diaochabiao_pictures_dict = {}
for roots, dirs, files in os.walk(diaochabiao_path):
    for one_file in files:
        if one_file.endswith('jpg'):
            diaochabiao_key_name = re.findall(r'520525\d{6}', one_file)[0]
            diaochabiao_pictures_dict[diaochabiao_key_name] = os.path.join(roots, one_file)
print(len(diaochabiao_pictures_dict))

pingmianbuzhitu_pictures_dict = {}
for roots, dirs, files in os.walk(pingmianbuzhitu_path):
    for one_ppictures in files:
        if one_ppictures.endswith('jpg'):
            pingmianbuzhitu_key_name = re.findall(r'520525\d{6}', one_ppictures)[0]
            pingmianbuzhitu_pictures_dict[pingmianbuzhitu_key_name] = os.path.join(roots, one_ppictures)
print(len(pingmianbuzhitu_pictures_dict))
print(len(x))

# 创建一个image对象

img_list = []
one_ic = len(x)
pdf = Image.open(diaochabiao_pictures_dict[x[0]])
# for one_index in tqdm(x[one_ic-200:one_ic]):
for one_index in tqdm(x[0:len(x)]):
    img_list.append(Image.open(diaochabiao_pictures_dict[one_index]))
    img_list.append(Image.open(pingmianbuzhitu_pictures_dict[one_index]).transpose(Image.ROTATE_90))
pdf.save(r'F:\乐治镇\%s_%s.pdf' % (pingmianbuzhitu_path[pingmianbuzhitu_path.rfind('\\'):], one_ic),
         "PDF", save_all=True, resolution=200.0, append_images=img_list)
