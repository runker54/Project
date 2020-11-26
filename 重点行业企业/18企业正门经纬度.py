# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)	 # �ؿ����
lPoint = arcpy.GetParameterAsText(1)	 # �ؿ���
outputgeodatabase = arcpy.GetParameterAsText(2)  # ���·��

outputfile = "�����18"
midFile = "mid18_buffer"
midFile2 = "mid18_join"
midFile18 = "mid18"
midFile18_2 = "mid18_2"
midFile19 = "mid19"
zdmc = "����״̬"
arcpy.env.workspace = outputgeodatabase  # ���ù����ؼ�
arcpy.env.overwriteOutput = True   # ���ÿɸ������

arcpy.Select_analysis(lPolygon, midFile18)  # ѡ��Ҫ��

arcpy.SetProgressorLabel("�ֶμ���...")   # ��ӡ��Ϣ
try:
	arcpy.DeleteField_management(midFile18, [zdmc])  # ɾ���ֶ�
except Exception as err:
	print(err)

try:
	arcpy.AddField_management(midFile18, zdmc, "String")  # �����ֶ�
except Exception as err:
	print(err)
arcpy.CalculateField_management(midFile18, zdmc, "Mid([DKBM],7,1)")  # �����ֶ�  �ó�����ҵ����
arcpy.Select_analysis(midFile18, midFile18_2, "{0}='1' OR {0}='2' OR {0}='3'".format(zdmc))   # ��midfile18��ѡ���ڲ����رգ��������ҵ��
arcpy.Delete_management(midFile18)  # ɾ��Ҫ��

arcpy.SetProgressorLabel("����������...")
arcpy.Buffer_analysis(midFile18_2, midFile, "30 METERS")   # ����30�׻�����
arcpy.Delete_management(midFile18_2)  # ɾ���м�Ҫ��

arcpy.SetProgressorLabel("�ռ�����...")
arcpy.SpatialJoin_analysis(midFile, lPoint, midFile2, match_option="INTERSECTS")
#arcpy.SpatialJoin_analysis(lPoint, midFile, "�����18-2", match_option="INTERSECTS")
arcpy.Select_analysis(midFile2, outputfile, "�ؿ���� IS NULL")

arcpy.Select_analysis(midFile2, midFile19, "�ؿ���� IS NOT NULL")

arcpy.SetProgressorLabel("����19...")
zdmc = "����һ��"
try:
	arcpy.DeleteField_management(midFile19, [zdmc])
except Exception as err:
	print(err)

try:
	arcpy.AddField_management(midFile19, zdmc, "Short")
except Exception as err:
	print(err)

arcpy.SetProgressorLabel("�ֶμ���...")
arcpy.CalculateField_management(midFile19, zdmc, "[DKBM] = [�ؿ����]")

arcpy.Select_analysis(midFile19, "�����19","{0}=0".format(zdmc))

arcpy.SetProgressorLabel("������ʱ����...")
#arcpy.Delete_management(midFile)
#arcpy.Delete_management(midFile2)
#arcpy.Delete_management(midFile19)

