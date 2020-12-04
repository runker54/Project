# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-27
# -----------------------
import fitz
import os
from PIL import Image


# 合并处理后的图片为pdf
def png2pdf(temp_adress, i):
    img_list = []
    png_list = os.listdir(temp_adress)
    png_list.sort()
    pdf = Image.open(os.path.join(temp_adress, png_list[0]))  # 创建一个image对象
    png_list.pop(0)
    # 合并图片为pdf
    for n in png_list:
        img = Image.open(os.path.join(temp_adress, n))
        img_list.append(img)
    pdf.save(i, "PDF", save_all=True, resolution=200.0, append_images=img_list)


# 对target_dir文件夹中的每一个pdf文件，循环执行操作
temp_dir = r'C:\Users\65680\Desktop\merge\大坝场镇'  # 图片所在路径
i = r'C:\Users\65680\Desktop\merge.pdf'  # 保存文件
png2pdf(temp_dir, i)
