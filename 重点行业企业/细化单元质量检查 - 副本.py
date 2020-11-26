# Name: CreateVectorTilePackage.py
# Description: Find all the maps in the project and
#   create a vector tile package for each map
# import system modules
import os
import sys
# sys.path.append(r'C:\Program Files (x86)\ArcGIS\Desktop10.5\arcpy')
import numpy
import arcpy

#set environment settings
arcpy.env.overwriteOutput = True
outputPath = "C://Tilepackages//"

# Loop through the project, find all the maps, and
#   create a vector tile package for each map,
#   using the same name as the map
mxd = arcpy.mapping.MapDocument("C:/city.mxd")
arcpy.CreateVectorTilePackage_management(mxd, outputPath + 'citty.vtpk', "EXISTING ", "", "INDEXED", 295828763.795777, 564.248588)