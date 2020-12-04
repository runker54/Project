#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-12-04
# Author:Runker54
# -----------------------

from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader

# cx_list = {'安乐彝族仡佬族乡': 16, '八堡彝族苗族乡': 8, '百纳彝族乡': 15, '达溪镇': 9, '东关乡': 12, '果瓦乡': 9, '核桃彝族白族乡': 11, '红旗街道办事处': 3,
#            '黄泥塘镇': 4, '黄泥彝族苗族满族乡': 20, '理化苗族彝族乡': 11, '六龙镇': 20, '绿塘乡': 7, '马场镇': 6, '猫场镇': 15, '慕俄格古城街道办事处': 4,
#            '牛场苗族彝族乡': 6, '瓢井镇': 15, '普底彝族苗族白族乡': 3, '三元彝族苗族白族乡': 17, '沙厂彝族乡': 3, '双山镇': 10, '顺德街道办事处': 5, '文阁乡': 7,
#            '响水白族彝族仡佬族乡': 12, '星宿苗族彝族仡佬族乡': 11, '兴隆苗族乡': 6, '羊场镇': 6, '雨冲乡': 7, '长石镇': 22, '竹园彝族苗族乡': 8, '对江镇': 8,
#            '凤山彝族蒙古族乡': 9, '大山苗族彝族乡': 13, '鼎新彝族苗族乡 ': 9}
# cx_list = {'亚鱼乡': 11, '皂角坪街道办事处': 9, '朱家场镇': 19, '大龙镇': 37, '新店镇': 17}
cx_list = {'田坪镇': 36, '平溪街道办事处': 2}
# cx_list = {'新店镇': 17}
for one_xz in cx_list:
    quxian = '玉屏县'
    name = one_xz
    skip = cx_list[one_xz]  # 页面间隔值
    index_text = r'C:\Users\65680\Desktop\%s页码\%s.txt' % (quxian, name)  # 具有页码索引的txt
    pdf_path = r'C:\Users\65680\Desktop\%sPDF\%s.pdf' % (quxian, name)  # 需加盖印章的PDF
    mark_pdf = r'C:\Users\65680\Desktop\制作好\%s.pdf' % quxian  # 水印PDF
    out_stream = r'E:\%s盖章后保存\%s.pdf' % (quxian, name)


    # 构建查询列表

    def calc_index(*args):
        """传入具有页码的文本文件位置，返回各个调查表所在的页码列表，各元素类型为字符串型"""
        calc_stream = open(*args).readlines()
        calc_stream_list = [str(int(one_line.split('\t')[1].strip()) + skip - 1) for one_line in calc_stream]
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
