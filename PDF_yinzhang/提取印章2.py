#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2020/11/26
import cv2
import numpy as np

np.set_printoptions(threshold=np.inf)
image=cv2.imread(r'C:\Users\65680\Desktop\p1.png')

hue_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
low_range = np.array([150, 103, 100])
high_range = np.array([180, 255, 255])
th = cv2.inRange(hue_image, low_range, high_range)
index1 = th == 255

img = np.zeros(image.shape, np.uint8)
img[:, :] = (255, 255, 255)
img[index1] = image[index1]#(0,0,255)
cv2.imshow('original_img', image)
cv2.imwrite('original_img.png', image)
cv2.imshow('extract_img', img)
cv2.imwrite('extract_img.png', img)
