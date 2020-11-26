# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)	 # �ؿ����
lPoint = arcpy.GetParameterAsText(1)	 # �ؿ���
outputgeodatabase = arcpy.GetParameterAsText(2)  # ���·��

outputfile = "�����33"
midFile_buffer = "mid33_buffer"
midFile_join = "mid33_join"
midFile3 = "mid33"
zdmc1 = "����״̬1"
zdmc2 = "����״̬2"
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

arcpy.SetProgressorLabel("����������...")
arcpy.Buffer_analysis(lPolygon, midFile_buffer, "1000 METERS")

arcpy.SetProgressorLabel("�������������...")
arcpy.Select_analysis(lPoint, midFile3, "LXDM = '21' OR LXDM = '22' OR LXDM = '23' OR LXDM = '24' OR LXDM = '20'  OR LXDM = '25' OR LXDM = '26' OR LXDM = '27' OR LXDM = '28' OR LXDM = '29' OR LXDM = '41' OR LXDM = '42'")

arcpy.SetProgressorLabel("�ռ�����...")
arcpy.SpatialJoin_analysis(midFile3, midFile_buffer, midFile_join, join_operation="JOIN_ONE_TO_MANY", match_option="INTERSECTS")

try:
	arcpy.DeleteField_management(midFile_join, [zdmc1, zdmc2])
except Exception as err:
	print(err)

try:
	arcpy.AddField_management(midFile_join, zdmc1, "String")
	arcpy.AddField_management(midFile_join, zdmc2, "String")
except Exception as err:
	print(err)

arcpy.SetProgressorLabel("�ֶμ���...")
arcpy.CalculateField_management(midFile_join, zdmc1, "Mid([DKBM],7,1)")
arcpy.CalculateField_management(midFile_join, zdmc2, "Mid([DKBM_1],7,1)")

arcpy.Select_analysis(midFile_join, outputfile, "DKBM_1 IS NOT NULL")
arcpy.SetProgressorLabel("������ʱ����...")
#arcpy.Delete_management(midFile)
#arcpy.Delete_management(midFile2)
#arcpy.Delete_management(midFile3)

