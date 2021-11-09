# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-09-08
# -------------------------------------------------------------------------------
from fpdf import FPDF
from PIL import Image
import os
import time


def makePdf(pdfFileName, listPages):
    """图片转PDF"""
    maxw_list = []
    maxh_list = []
    for one_p in listPages:
        cover = Image.open(one_p)
        width, height = cover.size
        maxh_list.append(height)
        maxw_list.append(width)
    try:
        width_m = max(maxw_list)
        height_m = max(maxh_list)
    except:
        width_m = 2339
        height_m = 1654
    pdf = FPDF(unit="pt", format=[width_m, height_m])
    for page in listPages:
        pdf.add_page()
        pdf.image(page, 0, 0)
    pdf.output(pdfFileName, "F")


f_path = r'F:\out'
f_list = os.listdir(f_path)
pp = r'F:\calc'
for one_dir in f_list:
    print(one_dir)
    pictures_path = os.path.join(f_path, one_dir)
    out_path = os.path.join(f_path, one_dir + ".pdf")
    if os.path.exists(os.path.join(pp, one_dir + ".pdf")):
        print("文件已创建")
    else:
        pictures_list = []
        for roots, dirs, files in os.walk(pictures_path):
            for one_picture in files:
                if str(one_picture).endswith("jpg" or "png"):
                    sizzz = Image.open(os.path.join(roots, one_picture))
                    width, height = sizzz.size
                    if width < height:
                        pass
                    else:
                        ak = sizzz.transpose(Image.ROTATE_90)
                        ak.save(os.path.join(roots, one_picture))
                    one_picture_path = os.path.join(roots, one_picture)
                    pictures_list.append(one_picture_path)
        makePdf(out_path, pictures_list)
