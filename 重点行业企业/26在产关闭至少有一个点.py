# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)	 # �ؿ����
lPoint = arcpy.GetParameterAsText(1)	 # �ؿ�����
outputgeodatabase = arcpy.GetParameterAsText(2)  # ���·��

zdmc = "ZCJG"
midFile = "mid26"
midFile2 = "mid26_2"
outputfile = "�����26"
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

arcpy.Select_analysis(lPolygon, midFile2)
try:
	arcpy.DeleteField_management(midFile2, [zdmc])
except Exception as err:
	print(err)

try:
	arcpy.AddField_management(midFile2, zdmc, "String")
except Exception as err:
	print(err)

arcpy.SetProgressorLabel("�ֶμ���...")
arcpy.CalculateField_management(midFile2, zdmc, "Mid([DKBM],7,1)")
arcpy.Select_analysis(midFile2, midFile,"{0}='1' OR {0}='2'".format(zdmc))

arcpy.JoinField_management(midFile, "DKBM", lPoint, "DKBM", ["DKBM"])

arcpy.Select_analysis(midFile, outputfile,"DKBM_1 IS NULL")

#arcpy.DeleteField_management(lPolygon, [zdmc])
arcpy.Delete_management(midFile2)

