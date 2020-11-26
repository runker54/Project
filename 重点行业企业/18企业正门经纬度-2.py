# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)  # �ؿ����
lPoint = arcpy.GetParameterAsText(1)  # �ؿ���
outputgeodatabase = arcpy.GetParameterAsText(2)  # ���·��

outputfile = "�����18"
midFile_buffer = "mid18_buffer"
midFile_join = "mid18_join"
midFile18 = "mid18"
midFile18_2 = "mid18_2"
midFile18_3 = "mid18_3"
midFile19 = "mid19"
zdmc = "����״̬"
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

try:
    arcpy.Delete_management(midFile18)
except Exception as err:
    print(err)

arcpy.Select_analysis(lPolygon, midFile18)

arcpy.SetProgressorLabel("�ֶμ���...")
try:
    arcpy.DeleteField_management(midFile18, [zdmc])
except Exception as err:
    print(err)

try:
    arcpy.AddField_management(midFile18, zdmc, "String")
except Exception as err:
    print(err)

arcpy.CalculateField_management(midFile18, zdmc, "Mid([DKBM],7,1)")
arcpy.Select_analysis(midFile18, midFile18_2, "{0}='1' OR {0}='2' OR {0}='3'".format(zdmc))
arcpy.Delete_management(midFile18)

arcpy.SetProgressorLabel("����������...")
arcpy.Buffer_analysis(midFile18_2, midFile_buffer, "30 METERS")
arcpy.Delete_management(midFile18_2)

arcpy.SetProgressorLabel("�ռ�����...")
arcpy.SpatialJoin_analysis(midFile_buffer, lPoint, midFile_join, join_operation="JOIN_ONE_TO_MANY",
                           match_option="INTERSECTS")
arcpy.SpatialJoin_analysis(lPoint, midFile_buffer, midFile18_3, match_option="INTERSECTS")
arcpy.Select_analysis(midFile18_3, "���18�ؿ鷶Χ���", "DKBM IS NULL")
arcpy.Delete_management(midFile18_3)

zdmc = "����һ��"
try:
    arcpy.DeleteField_management(midFile_join, [zdmc])
except Exception as err:
    print(err)

try:
    arcpy.AddField_management(midFile_join, zdmc, "Short")
except Exception as err:
    print(err)

arcpy.SetProgressorLabel("�ֶμ���...")
arcpy.CalculateField_management(midFile_join, zdmc, "[DKBM] = [�ؿ����]")

# arcpy.Select_analysis(midFile2, outputfile,"�ؿ���� IS NULL")
# arcpy.Select_analysis(midFile2, midFile19,"�ؿ���� IS NOT NULL")
# arcpy.SetProgressorLabel("����19...")

arcpy.SetProgressorLabel("������...")
arcpy.Select_analysis(midFile_join, "�����18", "{0}=0 OR {0} IS NULL".format(zdmc))

arcpy.SetProgressorLabel("������ʱ����...")
# arcpy.Delete_management(midFile18)
# arcpy.Delete_management(midFile2)
# arcpy.Delete_management(midFile19)
