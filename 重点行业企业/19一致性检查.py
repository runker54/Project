# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)	 # 地块面层
outputgeodatabase = arcpy.GetParameterAsText(1)  # 输出路径

zdmc = "编码一致性"

outputfile = "temp19"
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

try:
	arcpy.DeleteField_management(lPolygon, [zdmc])
except Exception as err:
	print(err)

try:
	arcpy.AddField_management(lPolygon, zdmc, "String")
except Exception as err:
	print(err)

arcpy.SetProgressorLabel("字段计算...")
arcpy.CalculateField_management(lPolygon, zdmc, "[DKBM]=[地块编码]", "PYTHON_9.3")

arcpy.Select_analysis(lPolygon, outputfile,"{0}=0".format(zdmc))


