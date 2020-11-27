#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2020/11/26

from PIL import Image

imageSrc = Image.open(r"C:\Users\runke\Desktop\temp\组合 1.pdf1.png")
logo = Image.open(r'D:\PYCHARMFILES\PDF_yinzhang\img2.png')

logo_mask = logo.convert("L").point(lambda x: min(x, 500))
logo.putalpha(logo_mask)
imageSrc.paste(logo, (216, 171), mask=logo)
imageSrc.save('test1.jpg')
