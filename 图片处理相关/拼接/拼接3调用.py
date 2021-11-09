#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2021-01-25
# Author:Runker54
# -----------------------
from 拼接3 import Stitcher
import cv2
import os
# 读取拼接图片

data_path = r'C:\Users\65680\Desktop\test'
data_list = [os.path.join(data_path, x_) for x_ in os.listdir(data_path)]
length_path = len(data_list)

# imageA = cv2.imread(r"C:\Users\65680\Desktop\test\1.jpg")
# imageB = cv2.imread(r"C:\Users\65680\Desktop\test\2.jpg")
imageA_path = data_list[0]

stitcher = Stitcher()
for one_pic in range(1):
    imageB_path = data_list[one_pic]
    imageA = cv2.imread(imageA_path)
    imageB = cv2.imread(imageB_path)
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
    imageA_path = os.path.join(data_path, "result.jpg")
    cv2.imwrite(imageA_path, result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite(r"C:\Users\65680\Desktop\test\5.jpg", result)

# 把图片拼接成全景图
# 显示所有图片
# cv2.imshow("Image A", imageA)
# cv2.imshow("Image B", imageB)
# cv2.imshow("Keypoint Matches", vis)
# cv2.imshow("Result", result)



