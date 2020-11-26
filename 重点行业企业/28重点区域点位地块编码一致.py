# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)	 # 地块面层
lPoint = arcpy.GetParameterAsText(1)	 # 地块点层
outputgeodatabase = arcpy.GetParameterAsText(2)  # 输出路径

outputfile = "检查结果28"
midFile = "mid28"
midFile2 = "mid28_2"
zdmc = "编码一致"

arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

arcpy.SetProgressorLabel("导出重点区域点位...")
arcpy.Select_analysis(lPoint, midFile,"LXDM = '11' OR LXDM = '12' OR LXDM = '13' OR LXDM = '14' OR LXDM = '10'")

arcpy.SetProgressorLabel("空间连接...")
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

arcpy.SetProgressorLabel("清理临时数据...")
arcpy.Delete_management(midFile)
arcpy.Delete_management(midFile2)

