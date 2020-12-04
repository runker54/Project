#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-11-28
# Author:Runker54
# -----------------------
from PIL import Image
import os
import fitz
import fpdf
from fpdf import FPDF


def makePdf(pdfName, listimage):  # listPages，以列表形式传入，方便批量合成
    cover = Image.open(listimage[0])  # 以第一张的尺寸来定义这个PDF的尺寸大小，具体也可自己设置
    width, height = cover.size
    pdf = FPDF(unit="pt", format=[width, height])

    for page in listimage:
        pdf.add_page()
        pdf.image(page, 0, 0)

    pdf.output(pdfName, "F")
path_1 = r'C:\Users\65680\Desktop\新建文件夹'
makePdf(r'C:\Users\65680\Desktop\test.pdf', [os.path.join(path_1, x) for x in os.listdir(path_1)])
