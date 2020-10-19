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
	print(listPages[0])

	cover = Image.open(listPages[0])
	print(cover)
	width, height = cover.size
	pdf = FPDF(unit = "pt", format = [width, height])
	for page in listPages:
		pdf.add_page()
		pdf.image(page, 0, 0)
	pdf.output(pdfFileName, "F")
pictures_path = r"C:\Users\65680\Desktop\picture_test"
pictures_list = []
for roots, dirs, files in os.walk(pictures_path):
	for one_picture in files:
		if str(one_picture).endswith("jpg"):
			one_picture_path = os.path.join(roots, one_picture)
			pictures_list.append(one_picture_path)
makePdf(r"C:\Users\65680\Desktop\picture_test\resualt.pdf", pictures_list)







