# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)	 # �ؿ����
lPoint = arcpy.GetParameterAsText(1)	 # �ؿ���
outputgeodatabase = arcpy.GetParameterAsText(2)  # ���·��

outputfile = "�����28"
midFile = "mid28"
midFile2 = "mid28_2"
zdmc = "����һ��"

arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

arcpy.SetProgressorLabel("�����ص������λ...")
arcpy.Select_analysis(lPoint, midFile,"LXDM = '11' OR LXDM = '12' OR LXDM = '13' OR LXDM = '14' OR LXDM = '10'")

arcpy.SetProgressorLabel("�ռ�����...")
arcpy.SpatialJoin_analysis(midFile,lPolygon, midFile2, match_option="INTERSECTS")

try:
	arcpy.DeleteField_management(midFile2, [zdmc])
except Exception as err:
	print(err)

try:
	arcpy.AddField_management(midFile2, zdmc, "String")
except Exception as err:
	print(err)

arcpy.CalculateField_management(midFile2, zdmc, "[DKBM]=[DKBM_1]")

arcpy.Select_analysis(midFile2, outputfile,"{0}='0'".format(zdmc))

arcpy.SetProgressorLabel("������ʱ����...")
arcpy.Delete_management(midFile)
arcpy.Delete_management(midFile2)

