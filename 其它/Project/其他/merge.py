import arcpy

arcpy.env.workspace = r"C:/Users/Administrator/Desktop/cpb"

shaps = arcpy.ListFeatureClasses()

arcpy.Merge_management(shaps, "AAAA.shp")