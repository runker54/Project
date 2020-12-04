# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       Runker54
# Date:         2020-09-10
# -------------------------------------------------------------------------------
from fpdf import FPDF
from PIL import Image
import time
import os

folder = r"C:\Users\65680\Desktop\merge\大坝场镇"     # 需转换成PDF的图片路径
out_path = r"C:\Users\65680\Desktop\merge"  # 生成后的PDF输出路径

xz_list = os.listdir(folder)
for one_xz in xz_list:
    start_time = time.time()
    pdf = FPDF()
    imagelist = []
    for dirpath, dirnames, filenames in os.walk(os.path.join(folder, one_xz)):
        for filename in [f for f in filenames if f.endswith(".png")]:
            full_path = os.path.join(dirpath, filename)
            imagelist.append(full_path)

    for i in range(0, len(imagelist)):
        im1 = Image.open(imagelist[i])
        width, height = im1.size
        if width > height:
            im2 = im1.transpose(Image.ROTATE_270)
            os.remove(imagelist[i])
            im2.save(imagelist[i])
    for image in imagelist:
        pdf.add_page()
        pdf.image(image, 0, 0, 210, 297)
    print(one_xz)
    pdf.output(os.path.join(out_path, (str(one_xz)+'.pdf')), "F")
    end_time = time.time()
    print(f"{one_xz}已完成，共{len(imagelist)}张,耗时{(end_time-start_time):.6f}秒")

