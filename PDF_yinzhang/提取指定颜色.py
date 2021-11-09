# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-27
# -----------------------

# tips:不能包含中文路径
import cv2
import matplotlib.pyplot as plt
from PIL import Image
imagepath = r'C:\Users\65680\Desktop\TAT.png'
# cass_pictures1 = Image.open(imagepath).convert('RGBA')
# cass_pictures1.save(r'C:\Users\65680\Desktop\P1.png')
image = cv2.imread(imagepath)

height, width, channel = image.shape
for i in range(height):
    for j in range(width):
        b, g, r = image[i, j]
        if (r - b) > 110 and (r - g) > 110:  # 对颜色进行判断，110->red
        # if (r - b) == 255 and (r - g) > 255:  # 对颜色进行判断，110->red
            b = 255
            g = 0
            r = 0
        else:
            b = 255
            g = 255
            r = 255

        image[i, j] = [r, g, b]
plt.figure(figsize=(20, 10))
plt.imshow(image)
plt.show()
cv2.imwrite(r'C:\Users\65680\Desktop\PH.png', image)
