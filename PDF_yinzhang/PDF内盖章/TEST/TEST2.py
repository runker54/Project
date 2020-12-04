#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-12-03
# Author:Runker54
# -----------------------
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader

index_text = r'C:\Users\65680\Desktop\安乐.txt'  # 具有页码索引的txt
pdf_path = r'C:\Users\65680\Desktop\安乐彝族仡佬族乡.pdf'  # 需加盖印章的PDF
mark_pdf = r'C:\Users\65680\Desktop\大方县.pdf'  # 水印PDF
out_stream = r'C:\Users\65680\Desktop\安乐彝族仡佬族乡_盖章.pdf'
skip = 16  # 页面间隔值
#  构建查询列表


def calc_index(*args):
    """传入具有页码的文本文件位置，返回各个调查表所在的页码列表，各元素类型为字符串型"""
    calc_stream = open(*args).readlines()
    calc_stream_list = [str(int(one_line.split(' ')[1].strip()) + skip-1) for one_line in calc_stream]
    return calc_stream_list


search_list = calc_index(index_text)

# Create the watermark from an image
# c = canvas.Canvas('PDF内盖章.pdf')

xAxis = 0
yAxis = 0
width = 0
height = 0
requiredPage = 28
# actualPage = requiredPage - 1

# Draw the image at x, y. I positioned the x,y to be where i like here
# c.drawImage(r'C:\Users\65680\Desktop\大方县农业农村局1.png', xAxis, yAxis, width, height)

# Add some custom text for good measure
# c.drawString(15, 720,"Hello World")
# c.save()

# Get the watermark file you just created
watermark = PdfFileReader(open(mark_pdf, "rb"))

# Get our files ready
output_file = PdfFileWriter()
input_file = PdfFileReader(open(pdf_path, "rb"))

# Number of pages in input document
page_count = input_file.getNumPages()
print(page_count)

# Go through all the input file pages to add a watermark to them
for page_number in range(page_count):
    print(page_number)
    # print 'Watermarking page {} of {}'.format(page_number, page_count)
    # merge the watermark with the page
    input_page = input_file.getPage(page_number)
    # if page_number == actualPage:
    if str(page_number) in search_list:
        # print(type(page_number))
        # print(page_number)
        input_page.mergePage(watermark.getPage(0))
    # add page from input file to output document
    output_file.addPage(input_page)

# finally, write "output" to document-output.pdf
with open(out_stream, "wb") as outputStream:
    output_file.write(outputStream)
