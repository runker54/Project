#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 修改透明背景为白色
from PIL import Image
import cv2
def transparence2white(img):
    sp = img.shape  # 获取图片维度
    width = sp[0]  # 宽度
    height = sp[1]  # 高度
    for yh in range(height):
        for xw in range(width):
            color_d = img[xw, yh]  # 遍历图像每一个点，获取到每个点4通道的颜色数据
            if (color_d[3] == 255):  # 最后一个通道为透明度，如果其值为0，即图像是透明
                img[xw, yh] = [0, 0, 0, 0]  # 则将当前点的颜色设置为白色，且图像设置为不透明
    return img

img = cv2.imread(r'C:\Users\65680\Desktop\logo.png', -1)  # 读取图片。-1将图片透明度传入，数据由RGB的3通道变成4通道
img = transparence2white(img)  # 将图片传入，改变背景色后，返回
cv2.imwrite(r'C:\Users\65680\Desktop\logo22p.png', img)  # 保存图片，文件名自定义，也可以覆盖原文件
