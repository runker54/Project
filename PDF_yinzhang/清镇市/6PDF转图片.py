# CODING:UTF-8
# pdf 文件列表

import fitz
import os

pdf_dir = []


def get_file(adress_):
    for roots, dirs, files in os.walk(adress_):
        for docuname in files:
            if os.path.splitext(docuname)[1] == '.pdf':  # 目录下包含.pdf的文件
                pdf_dir.append(os.path.join(roots, docuname))
    print(len(pdf_dir))
    print(pdf_dir)


def conver_img(p):
    for pdf in pdf_dir:
        doc = fitz.open(pdf)
        print(doc)
        # pdf_name = os.path.splitext(pdf)[0]
        pdf_name = str(pdf)[str(pdf).rfind('\\') + 1:str(pdf).rfind('.')]
        try:
            os.makedirs(os.path.join(p, pdf_name))
        except OSError:
            pass
        for pg in range(doc.pageCount):
            page = doc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为n，这将为我们生成分辨率提高n^2倍的图像。
            zoom_x = 4.0
            zoom_y = 4.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            # pm.writePNG('%s/%s%s.png' % (out_path, pdf_name + '_', pg + 1))
            pm.writePNG(os.path.join(os.path.join(p, pdf_name), pdf_name + '_'+str(pg + 1))+'.png')
            print(pdf)


# 拆分好的pdf位置
out_path = r'E:\需盖章处理\拆分后'
sss = r"E:\需盖章处理\大方县台账PDF"  # PDF所在路径
get_file(sss)
conver_img(out_path)
