# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)	 # 地块面层
lPoint = arcpy.GetParameterAsText(1)	 # 地块点层
outputgeodatabase = arcpy.GetParameterAsText(2)  # 输出路径

outputfile = "检查结果27"
midFile = "mid27"
midFile2 = "mid27_2"
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

arcpy.SetProgressorLabel("导出重点区域点位...")
arcpy.Select_analysis(lPoint, midFile,"LXDM = '11' OR LXDM = '12' OR LXDM = '13' OR LXDM = '14' OR LXDM = '10'")

arcpy.SetProgressorLabel("空间连接...")
arcpy.SpatialJoin_analysis(midFile,lPolygon, midFile2, match_option="INTERSECTS")

arcpy.Select_analysis(midFile2, outputfile,"DKBM_1 IS NULL")

arcpy.SetProgressorLabel("清理临时数据...")
arcpy.Delete_management(midFile)
arcpy.Delete_management(midFile2)

