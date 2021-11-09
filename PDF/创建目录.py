#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-12-09
# Author:Runker54
# -----------------------
import fitz

doc = fitz.open(r'C:\Users\65680\Desktop\组合 1.pdf')

# 获取目录
toc = doc.getToC()

# 目录内容
tocs = [
    # [目录level，标题，页码]
    [1, '宣言和原则', 1],
    [2, '价值观', 1],
    [2, '原则', 2],
]

for t in tocs:
    toc.append(t)

doc.setToC(toc)
doc.save(r'C:\Users\65680\Desktop\组合111.pdf')