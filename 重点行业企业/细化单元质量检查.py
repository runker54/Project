# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy
import logging
import logging.handlers

XCDW = arcpy.GetParameterAsText(0)	 # Join output file
XCDYXH = arcpy.GetParameterAsText(1)
element = arcpy.GetParameterAsText(2)	 # Cd
ylzb = arcpy.GetParameter(3)	 # һ��ռ��
elzb = arcpy.GetParameter(4)	 # ����ռ��
slzb = arcpy.GetParameter(5)	 # ����ռ��
outputgeodatabase = arcpy.GetParameterAsText(6)

d = defaultdict(dict)
joinfile = "Join_{}".format(element)
objectid = "ID_custom"
outputfile = "{}_filter".format(element)
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

desc = arcpy.Describe(XCDYXH)

sfhg = "sfhg"
bhgyy = "bhgyy"
oid = desc.OIDFieldName
tjjg = "tjjg"

try:
	arcpy.DeleteField_management(XCDYXH, [sfhg])
	arcpy.DeleteField_management(XCDYXH, [tjjg])
	arcpy.DeleteField_management(XCDYXH, [bhgyy])
	arcpy.DeleteField_management(XCDYXH, ["ID_custom"])
except Exception as err:
	print(err)

arcpy.AddField_management(XCDYXH, "ID_custom", "LONG")

with arcpy.da.UpdateCursor(XCDYXH, (oid, "ID_custom")) as cursor:
	# �½�һ���ֶα���OBJECTID����Ϊÿһ�����۵�Ԫ��Ψһ��ʶ
	for row in cursor:
		row[1] = int(row[0])
		cursor.updateRow(row)

arcpy.SpatialJoin_analysis(XCDW, XCDYXH, joinfile)

fields = (objectid, "{}_LEVEL".format(element), "{}_CLASS".format(element))	#object_2, cd_level, cd_class

# for each dybh, count the number of points in each level
# also record the class of the dybh as "dy_class"
for row in arcpy.da.SearchCursor(joinfile, fields):
	# ͳ��ÿ����Ԫ�ڸ����λ�ĸ���
	dybh_s, point_s, dy_class_s = row
	if not dy_class_s:
		continue
	dybh = int(dybh_s)
	point = int(point_s)
	dy_class = int(dy_class_s)
	d[dybh][point] = d[dybh].get(point, 0) + 1
	d[dybh]["dy_class"] = max(d[dybh].get("dy_class", 0), dy_class)

objectid_list = set()
filter_reason = defaultdict(list)
for k, v in d.items():
	y = int(v.get(1, 0))
	e = int(v.get(2, 0))
	s = int(v.get(3, 0))
	allCount = y + e + s

	arcpy.AddMessage("dy_class:{},1:{},2:{},3:{},��:{}".format(v['dy_class'], y, e, s, allCount))
	# ��鵥Ԫ����3�൫�ǵ�Ԫ����3�������
	if v['dy_class'] != 3 and v.get(3, 0) > 0:
		objectid_list.add(k)
		filter_reason[k].append("{}����Ԫ�к�3����λ".format(v['dy_class']))

	# 3����λ�����������λ������50%
	if v['dy_class'] == 3:
		bl = (y + e) * 100 / allCount
		arcpy.AddMessage("{}, {}".format(bl, slzb))
		if bl > (100 - slzb):
			objectid_list.add(k)
			filter_reason[k].append("��Ԫ��������λռ�Ȳ���{}".format(slzb))  # 3�൥Ԫ�����������λ��������50%

	# 2����λ��������λ��80%����
	if v['dy_class'] == 2:
		bl = (y + s) * 100 / allCount
		arcpy.AddMessage("{}, {}".format(bl, elzb))
		if bl > (100 - elzb):
			objectid_list.add(k)
			filter_reason[k].append("��Ԫ��������λռ�Ȳ���{}".format(elzb))  # 2�൥Ԫ��������λռ��С��80%

	# 1����λ��������λ��80%����
	if v['dy_class'] == 1:
		bl = ((s + e) * 100 / allCount)
		arcpy.AddMessage("{}, {}".format(bl, ylzb))
		if bl > (100 - ylzb):
			objectid_list.add(k)
			filter_reason[k].append("��Ԫ��������λռ�Ȳ���{}".format(ylzb))  # 1�൥Ԫ��������λռ��С��80%

		if e > 2:
			objectid_list.add(k)
			filter_reason[k].append("һ����Ԫ�а�������3��������")  # 1�൥Ԫ��������λռ��С��80%


try:
	arcpy.DeleteField_management(XCDYXH, [sfhg])
	arcpy.DeleteField_management(XCDYXH, [tjjg])
	arcpy.DeleteField_management(XCDYXH, [bhgyy])
except Exception as err:
	print(err)

arcpy.AddField_management(XCDYXH, sfhg, "TEXT")
arcpy.AddField_management(XCDYXH, bhgyy, "TEXT")
arcpy.AddField_management(XCDYXH, tjjg, "TEXT")

fields = (oid, sfhg, bhgyy, tjjg)
with arcpy.da.UpdateCursor(XCDYXH, fields) as cursor:
	for row in cursor:
		row[3] = str(d[row[0]])
		if row[0] in objectid_list:
			row[1] = "��"
			row[2] = "".join(filter_reason[row[0]])
		else:
			row[1] = "��"
		cursor.updateRow(row)

if len(objectid_list) == 0:
	whereclause = oid + ' in (-1)'
elif len(objectid_list) == 1:
	whereclause = oid + ' in ({})'.format((objectid_list.pop()))
else:
	whereclause = oid + ' in {}'.format(tuple(objectid_list))
arcpy.Select_analysis(XCDYXH, outputfile, whereclause)

#arcpy.AddField_management(outputfile, "ר��������", "TEXT")
#mxd = arcpy.mapping.MapDocument("CURRENT")
#df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
#addLayer = arcpy.mapping.Layer(outputfile)
#arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")
#del mxd, addLayer











































