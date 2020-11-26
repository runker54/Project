# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)	 # �ؿ����
outputgeodatabase = arcpy.GetParameterAsText(1)  # ���·��

zdmc = "����һ����"

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

arcpy.SetProgressorLabel("�ֶμ���...")
arcpy.CalculateField_management(lPolygon, zdmc, "[DKBM]=[�ؿ����]", "PYTHON_9.3")

arcpy.Select_analysis(lPolygon, outputfile,"{0}=0".format(zdmc))


