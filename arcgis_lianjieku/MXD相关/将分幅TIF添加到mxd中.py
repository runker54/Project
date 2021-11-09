#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-12-25
# Author:Runker54
# -----------------------
import os
import os.path
import arcpy

rootdir = u"d:\标准分幅5万DOM"
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
for parent, dirnames, filenames in os.walk(rootdir):
    for dirname in dirnames:
        arcpy.mapping.AddLayer(df, arcpy.mapping.Layer(rootdir + u"\\" + dirname + "\\" + dirname + u"DOM.tif"),
                               "BOTTOM")

tifLy = arcpy.mapping.ListLayers(mxd)[0]
# 此处手动修改第一个图层的样式，然后将这个图层的样式扩展到其他的图层
for i in range(1, len(arcpy.mapping.ListLayers(mxd))):
    arcpy.mapping.UpdateLayer(df, arcpy.mapping.ListLayers(mxd)[i], tifLy, True)

content = raw_input("input:")


