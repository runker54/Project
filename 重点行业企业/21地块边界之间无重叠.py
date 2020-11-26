# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

lPolygon = arcpy.GetParameterAsText(0)	 # 地块面图层
outputgeodatabase = arcpy.GetParameterAsText(1)  # 输出路径

midFile = "mid21"
outputfile = "检查结果21"
topname = "拓扑检查21"
topo_name = "不能重叠21"
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True
try:
	arcpy.Delete_management(topo_name)
	arcpy.Delete_management(topname)
except Exception as err:
	print(err)

try:
	sr = arcpy.SpatialReference(4490)
	arcpy.CreateFeatureDataset_management(outputgeodatabase, topname, sr)
except Exception as err:
	print(err)

arcpy.Select_analysis(lPolygon, "{1}\\{0}".format(midFile,topname))

arcpy.SetProgressorLabel("创建拓扑...")
# Input variables
input_dataset = topname
cluster_tol = 0.00001
validate = "true"
rule_type =r"Must Not Overlap (Area)"
# Create the topology
out_topo = arcpy.CreateTopology_management(input_dataset, topo_name, cluster_tol)
arcpy.AddFeatureClassToTopology_management(out_topo, midFile, 1, 1)
arcpy.AddRuleToTopology_management(out_topo, rule_type, midFile)
arcpy.ValidateTopology_management(out_topo)
# Process: Export Topology Errors
arcpy.ExportTopologyErrors_management(out_topo, input_dataset, outputfile)

arcpy.SetProgressorLabel("清理临时数据...")
#arcpy.DeleteField_management(midFile, [zdmc])
#arcpy.Delete_management(midFile)

