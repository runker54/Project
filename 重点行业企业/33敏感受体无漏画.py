# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)	 # 地块面层
lPoint = arcpy.GetParameterAsText(1)	 # 地块点层
outputgeodatabase = arcpy.GetParameterAsText(2)  # 输出路径

outputfile = "检查结果33"
midFile = "mid33_buffer"
midFile2 = "mid33_join"
midFile3 = "mid33"
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

arcpy.SetProgressorLabel("创建缓冲区...")
arcpy.Buffer_analysis(lPolygon, midFile, "1000 METERS")

arcpy.SetProgressorLabel("导出敏感受体点...")
arcpy.Select_analysis(lPoint, midFile3, "LXDM = '21' OR LXDM = '22' OR LXDM = '23' OR LXDM = '24' OR LXDM = '20'  OR LXDM = '25' OR LXDM = '26' OR LXDM = '27' OR LXDM = '28' OR LXDM = '29' OR LXDM = '41' OR LXDM = '42'")

arcpy.SetProgressorLabel("空间连接...")
arcpy.SpatialJoin_analysis(midFile3 ,midFile, midFile2,join_operation="JOIN_ONE_TO_MANY", match_option="INTERSECTS")

#zdmc = "编码一致"
#try:
#	arcpy.DeleteField_management(midFile2, [zdmc])
#except Exception as err:
#	print(err)

#try:
#	arcpy.AddField_management(midFile2, zdmc, "Short")
#except Exception as err:
#	print(err)

#arcpy.SetProgressorLabel("字段计算...")
#arcpy.CalculateField_management(midFile2, zdmc, "[DKBM] = [DKBM_1]")

#arcpy.Select_analysis(midFile2, outputfile,"{0}=0 OR {0} IS NULL".format(zdmc))
arcpy.Select_analysis(midFile2, outputfile, "DKBM_1 IS NOT NULL")
arcpy.SetProgressorLabel("清理临时数据...")
#arcpy.Delete_management(midFile)
#arcpy.Delete_management(midFile2)
#arcpy.Delete_management(midFile3)

