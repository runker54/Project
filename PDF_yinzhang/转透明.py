#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2020/11/26
import PIL.Image as Image
import time

# 以第一个像素为准，相同色改为透明
def transparent_back(img):
    img = img.convert('RGBA')
    L, H = img.size
    # color_0 = (255, 255, 255, 255)  # 要替换的颜色
    for h in range(H):
        for l in range(L):
            dot = (l, h)
            color_1 = img.getpixel(dot)
            print(color_1)
            if (color_1[0] > 200 and color_1[1] > 200 and color_1[2] > 200 and color_1[3] > 200) or (color_1[0] < 50 and color_1[1] < 50 and color_1[2] < 50 and color_1[3] < 50):
                color_1 = color_1[:-1] + (0,)
                print(color_1)
                # time.sleep(3)
                img.putpixel(dot, color_1)
    return img


if __name__ == '__main__':
    img = Image.open(r'C:\Users\65680\Desktop\LC.png')
    img = transparent_back(img)
    img.save(r'C:\Users\65680\Desktop\P222.png')
