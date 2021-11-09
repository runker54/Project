# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-10-03
# -------------------------------------------------------------------------------
from PIL import Image
import os


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
                out = im.transpose(Image.ROTATE_90)
                # 进行旋转180
                # out = im.transpose(Image.ROTATE_180)
                # 进行旋转270
                # out = im.transpose(Image.ROTATE_270)
                # 将图片重新设置尺寸
                # out = out.resize((1280, 720))
                img_size = out.size
                print("图片" + old_picture + " 图片宽度和高度分别是{}".format(img_size))
                out.save(os.path.join(out_Path, file))


in_path = r"H:\picturesHZ1"   # 导出平面布置图所在路径
out_path = r"H:\picturesHZ1"  # 旋转后图片存储路径
cut_image(in_path, out_path, 84, 106, 1011, 1426)
