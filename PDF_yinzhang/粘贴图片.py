# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-27
# -----------------------
from PIL import Image
from tqdm import tqdm
import time
cass_pictures = Image.open(r'C:\Users\65680\Desktop\2.png')
cass_pictures = cass_pictures.convert("RGBA")
mask_logo = Image.open(r'C:\Users\65680\Desktop\logo.png')
layer_deep = Image.new('RGBA', cass_pictures.size, (0, 0, 0, 0))  # 调查表
layer_deep.paste(mask_logo, (233, 233))  # 调查表
merge_pictures = Image.composite(layer_deep, cass_pictures, layer_deep)  # 调查表
merge_pictures.save(r'C:\Users\65680\Desktop\text.png')  # 覆盖情况说明表


