# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)  # 地块面图层
outputgeodatabase = arcpy.GetParameterAsText(1)  # 输出路径

zdmc = "Mutilparts"
midFile = "mid26"
outputfile = "检查结果20"
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

arcpy.Select_analysis(lPolygon, midFile)
try:
    arcpy.DeleteField_management(midFile, [zdmc])
except Exception as err:
    print(err)

try:
    arcpy.AddField_management(midFile, zdmc, "String")
except Exception as err:
    print(err)

arcpy.SetProgressorLabel("字段计算...")
arcpy.CalculateField_management(midFile, zdmc, "!shape.ismultipart!", "PYTHON_9.3")

whereclause = "Mutilparts = 'TRUE'"
arcpy.Select_analysis(midFile, outputfile, whereclause)

arcpy.SetProgressorLabel("清理临时数据...")
# arcpy.DeleteField_management(midFile, [zdmc])
arcpy.Delete_management(midFile)
