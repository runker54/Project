# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)	 # 地块面层
lPoint = arcpy.GetParameterAsText(1)	 # 地块点层
outputgeodatabase = arcpy.GetParameterAsText(2)  # 输出路径

outputfile = "检查结果33"
midFile_buffer = "mid33_buffer"
midFile_join = "mid33_join"
midFile3 = "mid33"
zdmc1 = "生产状态1"
zdmc2 = "生产状态2"
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

arcpy.SetProgressorLabel("创建缓冲区...")
arcpy.Buffer_analysis(lPolygon, midFile_buffer, "1000 METERS")

arcpy.SetProgressorLabel("导出敏感受体点...")
arcpy.Select_analysis(lPoint, midFile3, "LXDM = '21' OR LXDM = '22' OR LXDM = '23' OR LXDM = '24' OR LXDM = '20'  OR LXDM = '25' OR LXDM = '26' OR LXDM = '27' OR LXDM = '28' OR LXDM = '29' OR LXDM = '41' OR LXDM = '42'")

arcpy.SetProgressorLabel("空间连接...")
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

arcpy.SetProgressorLabel("字段计算...")
arcpy.CalculateField_management(midFile_join, zdmc1, "Mid([DKBM],7,1)")
arcpy.CalculateField_management(midFile_join, zdmc2, "Mid([DKBM_1],7,1)")

arcpy.Select_analysis(midFile_join, outputfile, "DKBM_1 IS NOT NULL")
arcpy.SetProgressorLabel("清理临时数据...")
#arcpy.Delete_management(midFile)
#arcpy.Delete_management(midFile2)
#arcpy.Delete_management(midFile3)

