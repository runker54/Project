# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       A
# Date:         2020-10-02
# -------------------------------------------------------------------------------
import sys
import time
from PyPDF2 import PdfFileReader, PdfFileWriter
from PIL import Image as pilImage
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
# from wand.image import Image
# =====================


class DelLogo_pdf(object):
    def __init__(self):
        # 原pdf文件名
        self.old_pdf_name = r"C:\Users\65680\Desktop\安洛苗族彝族满族乡大萝卜村520523006590-2.pdf"
        # 新pdf文件名
        self.new_pdf_name = r"C:\Users\65680\Desktop\new_noLogo.pdf"
        # pdf总页数
        self.pdf_total_pages = 0
        # 图片后缀
        self.image_suffix = ".jpg"
        # 图片精度
        self.resolution = 200
        # 宽度和高度 1654*2399
        # 距离图片左边界距离x， 距离图片上边界距离y，裁剪框宽度w，裁剪框高度h
        self.gx = 0
        self.gy = 120
        self.gw = 1417
        self.gh = 2009
        print("init ok")

    def run(self):
        # 1原pdf文件，按单页，存单页pdf文件，
        self.split_pdf(self.old_pdf_name)
        print("pdf_total_pages:", self.pdf_total_pages)
        # 2单页pdf文件，分别转为单个图片
        pages = 0
        while pages < self.pdf_total_pages:
            pdfFileName = "./tmp/" + str(pages) + ".pdf"
            imageFileName = "./tmp/" + str(pages) + self.image_suffix
            self.pdf_to_image(pdfFileName, imageFileName, self.resolution)
            pages += 1

        # 3图片切去logo, 并保存为新图片
        pages = 0
        while pages < self.pdf_total_pages:
            oldImageName = "./tmp/" + str(pages) + self.image_suffix
            newImageName = "./tmp/" + str(pages) + "_new" + self.image_suffix
            self.del_image_logo(oldImageName, newImageName, self.gx, self.gy, self.gw, self.gh)
            pages += 1

        # 4、单个新图片，转为单页pdf
        pages = 0
        while pages < self.pdf_total_pages:
            pdfName = "./tmp/" + str(pages) + "_new.pdf"
            imageName = "./tmp/" + str(pages) + "_new" + self.image_suffix
            self.image_to_pdf(imageName, pdfName)
            pages += 1

        # 5 合成
        infnList = []
        pages = 0
        while pages < self.pdf_total_pages:
            pdfName = "./tmp/" + str(pages) + "_new.pdf"
            infnList.append(pdfName)
            pages += 1

        self.merge_pdf(infnList, self.new_pdf_name)
        print("over.....")
        return

    # 1、原pdf文件，按单页，存单页pdf文件，
    def split_pdf(self, readFileName):
        print("原pdf文件，按单页，存单页pdf文件")
        # 获取一个 PdfFileReader 对象
        pdfReader = PdfFileReader(open(readFileName, 'rb'))
        # 获取 PDF 的页数
        pageCount = pdfReader.getNumPages()
        # self.pdf_total_pages = pageCount
        self.pdf_total_pages = pageCount
        print("原pdf文件总页数:", pageCount)
        pages = 0
        while pages < self.pdf_total_pages:
            # 返回一个 PageObject
            page = pdfReader.getPage(pages)
            # 获取一个 PdfFileWriter 对象
            pdfWriter = PdfFileWriter()
            # 将一个 PageObject 加入到 PdfFileWriter 中
            pdfWriter.addPage(page)
            writeFileName = "./tmp/" + str(pages) + ".pdf"
            # 输出到文件中
            pdfWriter.write(open(writeFileName, 'wb'))
            pages += 1

    # 2、单页pdf文件，分别转为单个图片；
    def pdf_to_image(self, pdfFileName, imageFileName, imgResolution):
        with Image(filename=pdfFileName, resolution=imgResolution) as img:
            with img.convert('png') as converted:
                converted.save(filename=imageFileName)

        print("pdf_to_image:", pdfFileName, imageFileName)

    # 3  图片切, 并保存为新图片。
    def del_image_logo(self, oldImageName, newImageName, x, y, w, h):
        im = pilImage.open(oldImageName)
        # 图片的宽度和高度
        img_size = im.size
        print("图片" + oldImageName + " 图片宽度和高度分别是{}".format(img_size))
        '''
        裁剪：传入一个元组作为参数
        元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，裁剪框宽度w，裁剪框高度h）
        '''
        region = im.crop((x, y, x + w, y + h))
        region.save(newImageName)

        # ==== 图片背景色设为白色
        im = pilImage.open(newImageName)
        x, y = im.size
        p = pilImage.new('RGBA', im.size, (255, 255, 255))
        p.paste(im, (0, 0, x, y), im)
        p.save(newImageName)

    # 4、单个新图片，转为单页pdf。
    def image_to_pdf(self, imageName, pdfName):
        print("image_to_pdf:", imageName, pdfName)
        (maxw, maxh) = pilImage.open(imageName).size
        c = canvas.Canvas(pdfName, pagesize=portrait((maxw, maxh)))
        c.drawImage(imageName, 0, 0, maxw, maxh)
        c.showPage()
        c.save()
    # 5、合成所有单页pdf，转为完整新pdf文件
    # infnList：单个pdf文件名数组。
    # outfn: 新pdf文件
    def merge_pdf(self, infnList, outfn):
        print("合成pdf:", infnList, outfn)
        pdf_output = PdfFileWriter()
        for infn in infnList:
            pdf_input = PdfFileReader(open(infn, 'rb'))
            # 获取 pdf 共用多少页
            page_count = pdf_input.getNumPages()
            # print(page_count)
            for i in range(page_count):
                pdf_output.addPage(pdf_input.getPage(i))
        pdf_output.write(open(outfn, 'wb'))


if __name__ == '__main__':
    localtime = time.asctime(time.localtime(time.time()))
    print("开始时间为 :", localtime)
    delLogo_pdf = DelLogo_pdf()
    delLogo_pdf.run()
    localtime = time.asctime(time.localtime(time.time()))
    print("结束时间为 :", localtime)

