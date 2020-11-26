# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)	 # �ؿ����
lPoint = arcpy.GetParameterAsText(1)	 # �ؿ���
outputgeodatabase = arcpy.GetParameterAsText(2)  # ���·��

outputfile = "�����31"
midFile = "mid31"
midFile2 = "mid31_2"
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

arcpy.SetProgressorLabel("�������������λ...")
arcpy.Select_analysis(lPoint, midFile,"LXDM = '21' OR LXDM = '22' OR LXDM = '23' OR LXDM = '24' OR LXDM = '20'  OR LXDM = '25' OR LXDM = '26' OR LXDM = '27' OR LXDM = '28' OR LXDM = '29' OR LXDM = '41' OR LXDM = '42'")

arcpy.SetProgressorLabel("�ռ�����...")
arcpy.SpatialJoin_analysis(midFile,lPolygon, midFile2, match_option="INTERSECTS")

arcpy.Select_analysis(midFile2, outputfile,"DKBM_1 IS NOT NULL")
arcpy.Select_analysis(midFile2, outputfile,"DKBM = DKBM_1")

arcpy.SetProgressorLabel("������ʱ����...")
arcpy.Delete_management(midFile)
arcpy.Delete_management(midFile2)

