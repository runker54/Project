#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-11-28
# Author:Runker54
# -----------------------
import os
import time
import cv2
from PIL import Image
test_pictures = r'C:\Users\65680\Desktop\test.png'
test_p = cv2.imread(test_pictures)
def rotation(image, angle, center=None, scale=1.0):
    # 获取图像尺寸
    (h, w) = image.shape[:2]
    # 若未指定旋转中心，则将图像中心设为旋转中心
    if center is None:
        center = (w / 2, h / 2)
    # 执行旋转
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    # 返回旋转后的图像
    return rotated
cv2.imwrite(r'C:\Users\65680\Desktop\test1.png',rotation(test_p,12))