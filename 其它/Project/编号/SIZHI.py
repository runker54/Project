# coding:utf-8
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


def auto(w):
    x = w.extent.xmin
    y = w.extent.ymin
    z = w.extent.xmax
    p = w.extent.ymax
    min_x_6 = round(x, 6)
    if len(str(min_x_6)) != 10:
        min_x_6 = str(min_x_6) + "0" * (10 - len((str(min_x_6))))

    min_y_6 = round(y, 6)
    if len(str(min_y_6)) != 9:
        min_y_6 = str(min_y_6) + "0" * (9 - len((str(min_y_6))))

    max_x_6 = round(z, 6)
    if len(str(max_x_6)) != 10:
        max_x_6 = str(max_x_6) + "0" * (10 - len((str(max_x_6))))

    max_y_6 = round(p, 6)
    if len(str(max_y_6)) != 9:
        max_y_6 = str(max_y_6) + "0" * (9 - len((str(max_y_6))))

    s_text = "经度（%s-%s）, 纬度（%s-%s）" % (min_x_6, max_x_6, min_y_6, max_y_6)
    return s_text