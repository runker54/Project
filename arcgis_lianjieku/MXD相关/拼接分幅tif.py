#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-12-25
# Author:Runker54
# -----------------------
import os
import os.path
import arcpy
rootdir = r''
arcpy.env.workspace = rootdir
lst=[]
for parent,dirnames,filenames in os.walk(rootdir):
    for dirname in dirnames:
        lst.append(dirname+"\\"+dirname+"DOM.tif")
imgs=";".join(lst)
arcpy.MosaicToNewRaster_management(imgs, 'D:\\Mosaic2New','landnew.tif','',"8_BIT_UNSIGNED", "", "3", "LAST","FIRST")
content = raw_input("input:")