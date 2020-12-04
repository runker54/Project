#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2020/11/26

from PIL import Image

# imageSrc = Image.open(r"C:\Users\65680\Desktop\last\大坝场镇_页面_0002.png")
# logo = Image.open(r'C:\Users\65680\Desktop\logo3.png')
#
# logo_mask = logo.convert("L").point(lambda x: min(x, 40))
# logo.putalpha(logo_mask)
# imageSrc.paste(logo, (216, 171), mask=logo)
# imageSrc.save(r'C:\Users\65680\Desktop\logo1.png')

cass_pictures1 = Image.open(r"C:\Users\65680\Desktop\安乐彝族仡佬族乡_70.png")  # 调查表
mask_logo = Image.open(r'C:\Users\65680\Desktop\大方县农业农村局3.png')
layer_deep1 = Image.new('RGBA', cass_pictures1.size, (0, 0, 0, 0))  # 情况说明表
layer_deep1.paste(mask_logo, (500, 500))  # 情况说明表
merge_pictures1 = Image.composite(layer_deep1, cass_pictures1, layer_deep1)  # 情况说明表
merge_pictures1.save(r'C:\Users\65680\Desktop\logo53.png')  # 覆盖情况说明表
