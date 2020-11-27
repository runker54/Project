#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2020/11/26
# coding=utf-8
# author: echo
# date: 2020/04/03

import fitz
import os
from PIL import Image

target_dir = r'C:\Users\runke\Desktop\pdf_adress'
temp_dir = r'C:\Users\runke\Desktop\temp'
zhang_file = r'C:\Users\runke\Desktop\gongzhang\test.png'

# 把pdf分拆为一张张图片，保存在temp_dir文件夹中，并获得最后一张图片的页码
def get_lastpng_num(target_dir, temp_dir, i):
    target_file = os.path.join(target_dir, i)
    pdf_treat = fitz.open(target_file)  # 获得要处理的pdf文件

    # 把pdf文件转成png图片，并把每一张图片写入temp_dir文件夹中
    for page_num in range(pdf_treat.pageCount):
        page = pdf_treat[page_num]

        # 提高从pdf转换成图片的分辨率，如果不设置，分辨率太低
        zoom_x = 2.0
        zoom_y = 2.0
        transform = fitz.Matrix(zoom_x, zoom_y)
        png_from_page = page.getPixmap(matrix=transform, alpha = False)

        temp_file = os.path.join(temp_dir, (i + str(page_num) + '.png'))
        png_from_page.writePNG(temp_file)

    # 获得temp_dir文件夹中最后一张图片的页码
    return str(pdf_treat.pageCount - 1)

# 定位最后一张图片，和公章合并为一张图片
def merge_png(target_dir, temp_dir, i, zhang_file):
    # 拼接temp_dir文件夹中最后一张图片的路径
    temp_file_last = os.path.join(temp_dir, (i + get_lastpng_num(target_dir, temp_dir, i) + '.png'))

    # 接下来把pdf文件的最后一页，现在这一页已经是图片了，和公章的图片，合并为一张图片
    gongzhang = Image.open(zhang_file)
    kuan, gao = gongzhang.size
    print(kuan,gao)
    trans_gongzhang = gongzhang.resize((int(kuan*5), int(gao*5))) # 放大公章
    png_last = Image.open(temp_file_last)
    width, height = png_last.size
    print(width, height)
    # 公章是有透明像素的png图像，在使用paste()函数时，需要传入第三参数
    # 这个第三参数是“遮罩”Image对象，它的alpha值是有效的，但红绿蓝值被忽略，即只保留alpha透明度
    png_last.paste(trans_gongzhang, (round(width), round(height)), trans_gongzhang)
    png_last.save(temp_file_last)

# 合并处理后的图片为pdf
def png2pdf(temp_dir, i):
    img_list = []
    png_list = os.listdir(temp_dir)
    png_list.sort()
    pdf = Image.open(os.path.join(temp_dir, png_list[0])) # 创建一个image对象
    png_list.pop(0)

    # 合并图片为pdf
    for n in png_list:
        img = Image.open(os.path.join(temp_dir, n))
        img_list.append(img)
    pdf.save(i, "PDF", save_all = True, resolution = 200.0, append_images=img_list)

    # 图片合并成pdf后清空临时文件夹temp_dir，避免i循环时，照片被重复使用
    # 即，下次循环时，又会新拆分出图片，用新拆分的图片合并pdf
    # png_list = os.listdir(temp_dir)
    # for n in png_list:
    #     os.remove(os.path.join(temp_dir, n))

# 对target_dir文件夹中的每一个pdf文件，循环执行操作
for i in os.listdir(target_dir):
    merge_png(target_dir, temp_dir, i, zhang_file)
    png2pdf(temp_dir, i)