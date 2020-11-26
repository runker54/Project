﻿# Name: CreateVectorTilePackage.py
# Description: Find all the maps in the project and
#   create a vector tile package for each map
# import system modules
import os
import arcpy

#set environment settings
arcpy.env.overwriteOutput = True


inMxdFilePath = sys.argv[1]
outFilePath = sys.argv[2]
tilingSchemeFile = sys.argv[3]

# Loop through the project, find all the maps, and
#   create a vector tile package for each map,
#   using the same name as the map
# 注意：此方法的最大和最小比例需根据最终数据生成的切片方案进行配置
arcpy.CreateVectorTilePackage_management(inMxdFilePath, outFilePath, "EXISTING", tilingSchemeFile, "INDEXED", 8000000, 1953.125)              