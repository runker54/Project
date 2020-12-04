# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-10-02
# -------------------------------------------------------------------------------

from PIL import Image
import os
import time


def cut_image(path, out_Path, x, y, w, h):
    for roots, dirs, files in os.walk(path):
        for file in files:
            if file.endswith("jpg"):
                old_picture = os.path.join(roots, file)
                im = Image.open(old_picture)
                # 图片的宽度和高度
                # 进行上下颠倒
                # out = im.transpose(Image.FLIP_TOP_BOTTOM)
                # 进行左右颠倒
                # out = out.transpose(Image.FLIP_LEFT_RIGHT)
                # 进行旋转90
                # im = im.transpose(Image.ROTATE_90)
                # 进行旋转180
                # out = im.transpose(Image.ROTATE_180)
                # 进行旋转270
                # out = im.transpose(Image.ROTATE_270)
                # 将图片重新设置尺寸
                # out = out.resize((1280, 720))
                img_size = im.size
                print(type(img_size))
                width = img_size[0]
                height = img_size[1]
                if width > height:
                    im = im.transpose(Image.ROTATE_90)
                else:
                    pass
                print("图片" + old_picture + " 图片宽度和高度分别是{}".format(img_size))
                '''
                裁剪：传入一个元组作为参数
                元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，裁剪框宽度w，裁剪框高度h）
                '''
                region = im.crop((x, y, x + w, y + h))
                new_name = os.path.join(out_Path, file)
                region.save(new_name)


in_path = r"F:\kaiyang\KYX_PDF"  # 需裁剪图片的路径
out_path = r"E:\xye\0开阳县台账\cut"   # 裁剪后的图片存储路径
cut_image(in_path, out_path, 70, 95, 1033, 1448)  # 输入四个参数
