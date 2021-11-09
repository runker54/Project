#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-12-11
# Author:Runker54
# -----------------------
from tqdm import tqdm
import win32com.client as win32
from docx import Document
from docx.shared import Pt
from docx.enum.section import WD_ORIENTATION, WD_SECTION_START
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx import shared
from docx.shared import RGBColor
import time
import re
import os

quxian = '金沙县'
temp = r'F:\%s\temp' % quxian  # 过程数据
merge = r'F:\%s\merge' % quxian   # 保存位置

files1 = []
for roots, dirs, files in os.walk(merge):
    for file in files:
        if file.endswith('docx') and '$' not in file:
            files1.append(os.path.join(roots, file))
        else:
            pass

word1 = win32.gencache.EnsureDispatch('Word.Application')
# 非可视化运行
word1.Visible = True
output = word1.Documents.Add()  # 新建合并后空白文档
for one_col in files1:
    print(one_col)
    output.Application.Selection.Range.InsertFile(one_col)  # 拼接文档
output.SaveAs(r'%s\%s.docx' % (merge, quxian))  # 保存
output.Close()
word1.Quit()
