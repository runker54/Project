# CODING:UTF-8
# pdf 文件列表

import fitz
import os
import time
import re

pdf_dir = []


def get_file(adress_):
    for roots, dirs, files in os.walk(adress_):
        for file in files:
            if os.path.splitext(file)[1] == '.pdf':  # 目录下包含.pdf的文件
                pdf_dir.append(os.path.join(roots, file))
    print(len(pdf_dir))

def conver_img():
    for pdf in pdf_dir:
        doc = fitz.open(pdf)
        pdf_name = os.path.splitext(pdf)[0]
        su_name = re.findall(r'5\d{11}', str(pdf_name))[0]
        for pg in range(doc.pageCount):
            page = doc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            if os.path.exists('%s%s.jpg' % (out_path, su_name)):
                print("图片已存在")
            else:
                pm.writePNG('%s/%s.jpg' % (out_path, su_name))
                print(pdf)
# 拆分好的pdf位置
out_path = r"C:\Users\65680\Desktop\大方图片"
sss = r"E:\台账\大方县\大方县导出资料\DFX_PDF"
get_file(sss)
conver_img()