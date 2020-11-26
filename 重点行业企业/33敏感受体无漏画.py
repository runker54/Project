# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)	 # �ؿ����
lPoint = arcpy.GetParameterAsText(1)	 # �ؿ���
outputgeodatabase = arcpy.GetParameterAsText(2)  # ���·��

outputfile = "�����33"
midFile = "mid33_buffer"
midFile2 = "mid33_join"
midFile3 = "mid33"
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

arcpy.SetProgressorLabel("����������...")
arcpy.Buffer_analysis(lPolygon, midFile, "1000 METERS")

arcpy.SetProgressorLabel("�������������...")
arcpy.Select_analysis(lPoint, midFile3, "LXDM = '21' OR LXDM = '22' OR LXDM = '23' OR LXDM = '24' OR LXDM = '20'  OR LXDM = '25' OR LXDM = '26' OR LXDM = '27' OR LXDM = '28' OR LXDM = '29' OR LXDM = '41' OR LXDM = '42'")

arcpy.SetProgressorLabel("�ռ�����...")
arcpy.SpatialJoin_analysis(midFile3 ,midFile, midFile2,join_operation="JOIN_ONE_TO_MANY", match_option="INTERSECTS")

#zdmc = "����һ��"
#try:
#	arcpy.DeleteField_management(midFile2, [zdmc])
#except Exception as err:
#	print(err)

#try:
#	arcpy.AddField_management(midFile2, zdmc, "Short")
#except Exception as err:
#	print(err)

#arcpy.SetProgressorLabel("�ֶμ���...")
#arcpy.CalculateField_management(midFile2, zdmc, "[DKBM] = [DKBM_1]")

#arcpy.Select_analysis(midFile2, outputfile,"{0}=0 OR {0} IS NULL".format(zdmc))
arcpy.Select_analysis(midFile2, outputfile, "DKBM_1 IS NOT NULL")
arcpy.SetProgressorLabel("������ʱ����...")
#arcpy.Delete_management(midFile)
#arcpy.Delete_management(midFile2)
#arcpy.Delete_management(midFile3)

