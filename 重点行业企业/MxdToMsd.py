# This Python file uses the following encoding: utf-8
import os, sys
import arcpy
inMxdFilePath = sys.argv[1]
inLayers = sys.argv[2]
outMsdFilePath = sys.argv[3]
mxd = arcpy.mapping.MapDocument(inMxdFilePath)
df = arcpy.mapping.ListDataFrames(mxd, inLayers)[0]
arcpy.mapping.ConvertToMSD(mxd, outMsdFilePath, df, "NORMAL", "NORMAL")
del mxd, inMxdFilePath, outMsdFilePath, inLayers