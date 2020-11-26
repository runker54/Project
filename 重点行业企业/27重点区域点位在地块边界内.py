# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)	 # �ؿ����
lPoint = arcpy.GetParameterAsText(1)	 # �ؿ���
outputgeodatabase = arcpy.GetParameterAsText(2)  # ���·��

outputfile = "�����27"
midFile = "mid27"
midFile2 = "mid27_2"
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

arcpy.SetProgressorLabel("�����ص������λ...")
arcpy.Select_analysis(lPoint, midFile,"LXDM = '11' OR LXDM = '12' OR LXDM = '13' OR LXDM = '14' OR LXDM = '10'")

arcpy.SetProgressorLabel("�ռ�����...")
arcpy.SpatialJoin_analysis(midFile,lPolygon, midFile2, match_option="INTERSECTS")

arcpy.Select_analysis(midFile2, outputfile,"DKBM_1 IS NULL")

arcpy.SetProgressorLabel("������ʱ����...")
arcpy.Delete_management(midFile)
arcpy.Delete_management(midFile2)

