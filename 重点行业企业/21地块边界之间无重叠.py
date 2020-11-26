# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

lPolygon = arcpy.GetParameterAsText(0)	 # �ؿ���ͼ��
outputgeodatabase = arcpy.GetParameterAsText(1)  # ���·��

midFile = "mid21"
outputfile = "�����21"
topname = "���˼��21"
topo_name = "�����ص�21"
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

arcpy.SetProgressorLabel("��������...")
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

arcpy.SetProgressorLabel("������ʱ����...")
#arcpy.DeleteField_management(midFile, [zdmc])
#arcpy.Delete_management(midFile)

