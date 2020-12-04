#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2020/11/26
from PIL import Image
import fitz
import os
import random
import time
from tqdm import trange, tqdm

xcec = '安乐'
index_text = r'C:\Users\65680\Desktop\%s.txt' % xcec  # 具有页码索引的txt
# picture_adress = r'C:\Users\65680\Desktop\%s' % xcec  # 拆分好的图片所在的位置
picture_adress = r'C:\Users\65680\Desktop\%s' % xcec  # 拆分好的图片所在的位置
mask_logo = r'C:\Users\65680\Desktop\大方县农业农村局.png'  # 印章所在位置
pdf_name = r'C:\Users\65680\Desktop\last\大坝场镇.pdf'  # 加盖印章后存储的pdf路径及名称


# 页码间隔 page_skip = ?
# 印章参数（x = 291, y = 279）


# 获取需要加盖印章的图片地址
def calc_index(*args):
    """传入具有页码的文本文件位置，返回各个调查表所在的页码列表，各元素类型为字符串型"""
    calc_stream = open(*args).readlines()
    calc_stream_list = [str(int(one_line.split(' ')[1].strip()) + 16) for one_line in calc_stream]
    return calc_stream_list


# 加盖印章
def mask_picture_logo(p1, p2, p3, p4):
    """对符合条件的图片加盖印章，参数需传入图片所在路径及两个类型的盖章坐标['pictrres_adress','x1,y1','x2,y2']"""
    # 所有图片的地址列表
    picture_list = [os.path.join(p1, one_pictures) for one_pictures in os.listdir(p1) if one_pictures.endswith('png')]
    for one_mask_pictures in tqdm(picture_list):
        # 得到图片对应的编号 index_number_str
        index_number_str = str(int(one_mask_pictures[one_mask_pictures.rfind('_') + 1:one_mask_pictures.rfind('.')]))
        # 判断该图片的编号是否在需要加盖印章的列表内
        if index_number_str in calc_index(index_text):
            # 调查表图片对应地址
            survey_sheet_path = one_mask_pictures
            # 情况说明表对应地址
            # instructions_path = picture_list[picture_list.index(survey_sheet_path) + 1]
            # 平面布置图所在位置
            surafy_path = picture_list[picture_list.index(survey_sheet_path) + 2]
            # print("裁剪平面布置图")
            # cut_picture(surafy_path)
            # print(survey_sheet_path, instructions_path, surafy_path)
            # 对调查表和情况说明表盖章输出
            cass_pictures = Image.open(survey_sheet_path).convert('RGB')  # 调查表
            # cass_pictures1 = Image.open(instructions_path).convert('RGB')  # 情况说明表
            mask_logo = Image.open(p2)
            # mask_logo = mask_logo.transpose(Image.ROTATE_90)
            layer_deep = Image.new('RGBA', cass_pictures.size, (0, 0, 0, 0))  # 调查表
            # layer_deep1 = Image.new('RGBA', cass_pictures1.size, (0, 0, 0, 0))  # 情况说明表
            layer_deep.paste(mask_logo, p3)  # 调查表
            # layer_deep1.paste(mask_logo, p4)  # 情况说明表
            merge_pictures = Image.composite(layer_deep, cass_pictures, layer_deep)  # 调查表
            # merge_pictures1 = Image.composite(layer_deep1, cass_pictures1, layer_deep1)  # 情况说明表
            merge_pictures.save(survey_sheet_path)  # 覆盖调查表
            # merge_pictures1.save(instructions_path)  # 覆盖情况说明表


def cut_picture(cut_photo):
    """裁剪图例"""
    cut_im = Image.open(cut_photo)
    x1 = 240
    y1 = 210
    x, y = cut_im.size
    w = x - 200
    h = y - 110
    region = cut_im.crop((x1, y1, w, h))
    region.save(cut_photo)


# 合并处理后的图片为pdf
def png_to_pdf(s1, s2):
    img_list = []
    png_list = os.listdir(s1)
    png_list.sort()
    pdf = Image.open(os.path.join(s1, png_list[0]))  # 创建一个image对象
    png_list.pop(0)
    # 合并图片为pdf
    for n in png_list:
        img = Image.open(os.path.join(s1, n))
        img_list.append(img)
    pdf.save(s2, "PDF", save_all=True, resolution=300.0, append_images=img_list)


print(f'{"正在加盖印章"}')
mask_picture_logo(picture_adress, mask_logo, (220, 200), (977, 1402))
