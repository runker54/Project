# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

lPolygon = arcpy.GetParameterAsText(0)  # 地块面层
lPoint = arcpy.GetParameterAsText(1)  # 地块点层
outputgeodatabase = arcpy.GetParameterAsText(2)  # 输出路径

outputfile = "检查结果18"
midFile_buffer = "mid18_buffer"
midFile_join = "mid18_join"
midFile18 = "mid18"
midFile18_2 = "mid18_2"
midFile18_3 = "mid18_3"
midFile19 = "mid19"
zdmc = "生产状态"
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

try:
    arcpy.Delete_management(midFile18)
except Exception as err:
    print(err)

arcpy.Select_analysis(lPolygon, midFile18)

arcpy.SetProgressorLabel("字段计算...")
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

arcpy.SetProgressorLabel("创建缓冲区...")
arcpy.Buffer_analysis(midFile18_2, midFile_buffer, "30 METERS")
arcpy.Delete_management(midFile18_2)

arcpy.SetProgressorLabel("空间连接...")
arcpy.SpatialJoin_analysis(midFile_buffer, lPoint, midFile_join, join_operation="JOIN_ONE_TO_MANY",
                           match_option="INTERSECTS")
arcpy.SpatialJoin_analysis(lPoint, midFile_buffer, midFile18_3, match_option="INTERSECTS")
arcpy.Select_analysis(midFile18_3, "检查18地块范围外点", "DKBM IS NULL")
arcpy.Delete_management(midFile18_3)

zdmc = "编码一致"
try:
    arcpy.DeleteField_management(midFile_join, [zdmc])
except Exception as err:
    print(err)

try:
    arcpy.AddField_management(midFile_join, zdmc, "Short")
except Exception as err:
    print(err)

arcpy.SetProgressorLabel("字段计算...")
arcpy.CalculateField_management(midFile_join, zdmc, "[DKBM] = [地块编码]")

# arcpy.Select_analysis(midFile2, outputfile,"地块编码 IS NULL")
# arcpy.Select_analysis(midFile2, midFile19,"地块编码 IS NOT NULL")
# arcpy.SetProgressorLabel("处理19...")

arcpy.SetProgressorLabel("输出结果...")
arcpy.Select_analysis(midFile_join, "检查结果18", "{0}=0 OR {0} IS NULL".format(zdmc))

arcpy.SetProgressorLabel("清理临时数据...")
# arcpy.Delete_management(midFile18)
# arcpy.Delete_management(midFile2)
# arcpy.Delete_management(midFile19)
