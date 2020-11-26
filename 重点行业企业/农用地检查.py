# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

XCDW = arcpy.GetParameterAsText(0)	 # Join output file
XCDYXH = arcpy.GetParameterAsText(1)
element = arcpy.GetParameterAsText(2)  # Cd
outputgeodatabase = arcpy.GetParameterAsText(3)

d = defaultdict(dict)
joinfile = "Join_{}.shp".format(element)
objectid = "ID_custom"
outputfile = "{}_filter".format(element)
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

oid = "OBJECTID"
tjjg="统计结果"

try:
	arcpy.DeleteField_management(XCDYXH, [tjjg])
	arcpy.DeleteField_management(XCDYXH, ["ID_custom"])
except Exception as err:
	print(err)

arcpy.AddField_management(XCDYXH, "ID_custom", "LONG")

with arcpy.da.UpdateCursor(XCDYXH, (oid, "ID_custom")) as cursor:
	# 新建一个字段保存OBJECTID，作为每一个评价单元的唯一标识
	for row in cursor:
		row[1] = int(row[0])
		cursor.updateRow(row)

arcpy.SpatialJoin_analysis(XCDW, XCDYXH, joinfile)

fields = (objectid, "{}_LEVEL".format(element))	 # object_2, cd_level, cd_class

# for each dybh, count the number of points in each level
# also record the class of the dybh as "dy_class"
for row in arcpy.da.SearchCursor(joinfile, fields):
	# 统计每个单元内各类点位的个数
	dybh_s, point_s = row
	dybh = int(dybh_s)
	point = int(point_s)
	d[dybh][point] = d[dybh].get(point, 0) + 1
	# d[dybh]["dy_class"] = max(d[dybh].get("dy_class", 0), dy_class)

objectid_list = set()
for k, v in d.items():
	# 检查是否超过一类
	if len(set([1, 2, 3])&set(v.keys())) > 1:
		objectid_list.add(k)
try:
	arcpy.DeleteField_management(XCDYXH, [tjjg])
except Exception as err:
	print(err)

arcpy.AddField_management(XCDYXH, tjjg, "TEXT")

fields = (oid, tjjg)
with arcpy.da.UpdateCursor(XCDYXH, fields) as cursor:
	for row in cursor:
		if row[0] in objectid_list:
			row[1] = str(d[row[0]])
		cursor.updateRow(row)

if len(objectid_list) == 0:
	whereclause = oid + ' in (-1)'
elif len(objectid_list) == 1:
	whereclause = oid + ' in ({})'.format((objectid_list.pop()))
else:
	whereclause = oid + ' in {}'.format(tuple(objectid_list))
arcpy.Select_analysis(XCDYXH, outputfile, whereclause)

#arcpy.AddField_management(outputfile, "专家审核意见", "TEXT")
#mxd = arcpy.mapping.MapDocument("CURRENT")
#df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
#addLayer = arcpy.mapping.Layer(outputfile)
#arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")
#del mxd, addLayer











































