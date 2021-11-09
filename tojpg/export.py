# -*- coding: utf-8 -*
import os
import time
import arcpy
import sys
import os

reload(sys)
sys.setdefaultencoding("utf-8")

layer_list = []

mxd = arcpy.mapping.MapDocument(r"./to.mxd")
layers = arcpy.mapping.ListLayers(mxd)
polygons_1 = layers[0]
title = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[0]
rows = arcpy.da.SearchCursor(polygons_1, ["编码", "ZLDWMC"])

for row in rows:
    layer_list.append(row)
chatss = list(set(layer_list))

def to_jpg():
    # for unique in uniques:
    for one_c in chatss:
        start = time.time()
        print('正在导出：% s' % one_c[0])
        polygons_1.definitionQuery = "编码='%s'" % one_c[0]
        mxd.activeDataFrame.extent = polygons_1.getExtent()
        df = arcpy.mapping.ListDataFrames(mxd)[0]
        if df.scale < 200:
            df.scale = 200
        else:
            df.scale = df.scale * 1.05
        title.text = "石阡县%s%s"%(one_c[1],one_c[0])
        # 导出图片
        try:
            os.makedirs(r"./pictures/%s" % one_c[0])
        except:
            pass
        arcpy.mapping.ExportToJPEG(mxd, r"./pictures/%s/%s" % (one_c[0], one_c[0]),
                                   resolution=300)

        end_time = time.time() - start
        print("time:{:.1f}s".format(end_time))


def main():
    to_jpg()

if __name__ == '__main__':
    main()
