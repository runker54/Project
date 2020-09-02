# import arcpy
# import os
# arcpy.env.workspace = r"E:/����DOM3"
# base = "3147.5-36406.5DOM.tif"
# out_coor_system = arcpy.Describe(base).spatialReference
# dataType = arcpy.Describe(base).DataType
# #piexl_type = arcpy.Describe(base).pixelType
# #cellwidth = arcpy.Describe(base).meanCellWidth
# bandcount = arcpy.Describe(base).bandCount
# arcpy.CheckOutExtension("Spatial")
# rasters = []
# for ras in arcpy.ListRasters("*.tif"):
#     rasters.append(ras)
# ras_list = ";".join(rasters)
# print(ras_list)
#
# outFolder = r"C:/Users/Administrator/Desktop/out"
#
# arcpy.MosaicToNewRaster_management(ras_list,outFolder,"test.tif",out_coor_system,"16_BIT_SIGNED","",bandcount,"LAST","FIRST")

