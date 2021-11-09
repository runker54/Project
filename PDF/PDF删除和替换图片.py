#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-12-13
# Author:Runker54
# -----------------------
pdf = '紫兴社区服务中心.pdf'
import fitz
import os

doc = fitz.open(pdf)
imgcount = 0
for page in doc:
    picture_list = page.getImageList()
    print(picture_list)
    for pic in picture_list:
        # pi = fitz.Pixmap(doc, pic[0])
        # pi.writePNG("%s.png" % imgcount)
        # imgcount+=1
        doc._deleteObject(pic[0])
        rect = fitz.Rect(40, 40, 100, 100)
        page.insertImage(rect, '冯三镇.jpg')

doc.save('删除后.pdf')
