

# Time:2020/11/26
from PIL import Image
import cv2
cass_pictures = Image.open(r"C:\Users\65680\Desktop\test.jpg")
mask_logo = Image.open(r'C:\Users\65680\Desktop\logo.png')
layer_deep = Image.new('RGBA', cass_pictures.size, (0, 0, 0, 0))
layer_deep.paste(mask_logo, (230, 40))
merge_pictures = Image.composite(layer_deep, cass_pictures, layer_deep)
merge_pictures.save(r'C:\Users\65680\Desktop\end.png')
