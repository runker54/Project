# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)  # �ؿ���ͼ��
outputgeodatabase = arcpy.GetParameterAsText(1)  # ���·��

zdmc = "Mutilparts"
midFile = "mid26"
outputfile = "�����20"
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

arcpy.SetProgressorLabel("�ֶμ���...")
arcpy.CalculateField_management(midFile, zdmc, "!shape.ismultipart!", "PYTHON_9.3")

whereclause = "Mutilparts = 'TRUE'"
arcpy.Select_analysis(midFile, outputfile, whereclause)

arcpy.SetProgressorLabel("������ʱ����...")
# arcpy.DeleteField_management(midFile, [zdmc])
arcpy.Delete_management(midFile)
