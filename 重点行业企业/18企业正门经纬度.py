# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)	 # 地块面层
lPoint = arcpy.GetParameterAsText(1)	 # 地块点层
outputgeodatabase = arcpy.GetParameterAsText(2)  # 输出路径

outputfile = "检查结果18"
midFile = "mid18_buffer"
midFile2 = "mid18_join"
midFile18 = "mid18"
midFile18_2 = "mid18_2"
midFile19 = "mid19"
zdmc = "生产状态"
arcpy.env.workspace = outputgeodatabase  # 设置工作控家
arcpy.env.overwriteOutput = True   # 设置可覆盖输出

arcpy.Select_analysis(lPolygon, midFile18)  # 选择要素

arcpy.SetProgressorLabel("字段计算...")   # 打印消息
try:
	arcpy.DeleteField_management(midFile18, [zdmc])  # 删除字段
except Exception as err:
	print(err)

try:
	arcpy.AddField_management(midFile18, zdmc, "String")  # 增加字段
except Exception as err:
	print(err)
arcpy.CalculateField_management(midFile18, zdmc, "Mid([DKBM],7,1)")  # 计算字段  得出各企业类型
arcpy.Select_analysis(midFile18, midFile18_2, "{0}='1' OR {0}='2' OR {0}='3'".format(zdmc))   # 从midfile18中选出在产，关闭，填埋产企业。
arcpy.Delete_management(midFile18)  # 删除要素

arcpy.SetProgressorLabel("创建缓冲区...")
arcpy.Buffer_analysis(midFile18_2, midFile, "30 METERS")   # 创建30米缓冲区
arcpy.Delete_management(midFile18_2)  # 删除中间要素

arcpy.SetProgressorLabel("空间连接...")
arcpy.SpatialJoin_analysis(midFile, lPoint, midFile2, match_option="INTERSECTS")
#arcpy.SpatialJoin_analysis(lPoint, midFile, "检查结果18-2", match_option="INTERSECTS")
arcpy.Select_analysis(midFile2, outputfile, "地块编码 IS NULL")

arcpy.Select_analysis(midFile2, midFile19, "地块编码 IS NOT NULL")

arcpy.SetProgressorLabel("处理19...")
zdmc = "编码一致"
try:
	arcpy.DeleteField_management(midFile19, [zdmc])
except Exception as err:
	print(err)

try:
	arcpy.AddField_management(midFile19, zdmc, "Short")
except Exception as err:
	print(err)

arcpy.SetProgressorLabel("字段计算...")
arcpy.CalculateField_management(midFile19, zdmc, "[DKBM] = [地块编码]")

arcpy.Select_analysis(midFile19, "检查结果19","{0}=0".format(zdmc))

arcpy.SetProgressorLabel("清理临时数据...")
#arcpy.Delete_management(midFile)
#arcpy.Delete_management(midFile2)
#arcpy.Delete_management(midFile19)

