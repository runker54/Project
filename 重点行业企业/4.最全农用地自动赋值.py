# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

NYD = arcpy.GetParameterAsText(0)	 # 农用地（最全）
PJDY = arcpy.GetParameterAsText(1)  # 各类元素详查范围内农用地
element = arcpy.GetParameterAsText(2)	 # Cd
outputgeodatabase = arcpy.GetParameterAsText(3)  # 输出路径

d = defaultdict(dict)
pjdyObjectId = "CID_PJDY"
nydObjectId = "CID_NYD"

outputfile = "{}_temp".format(element)
midFile = "{}_zqnyd".format(element)
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

nydDesc = arcpy.Describe(NYD)
pjdydesc = arcpy.Describe(PJDY)

pjdyoid = pjdydesc.OIDFieldName
className = "{}_CLASS".format(element)
nClassName = "{}_N".format(element)
lineLength = "{}_Len".format(element)

arcpy.Select_analysis(NYD, midFile)

try:
	arcpy.DeleteField_management(PJDY, [pjdyObjectId, nClassName])
	arcpy.DeleteField_management(midFile, [nydObjectId])
except Exception as err:
	print(err)

try:
	arcpy.AddField_management(midFile, className, "LONG")
except Exception as err:
	print(err)


arcpy.AddField_management(PJDY, pjdyObjectId, "LONG")
arcpy.AddField_management(PJDY, nClassName, "LONG")
arcpy.AddField_management(midFile, nydObjectId, "LONG")
arcpy.SetProgressorLabel("更新ID...")
arcpy.CalculateField_management(PJDY, pjdyObjectId,  "!{}!".format(pjdyoid), "PYTHON_9.3")
arcpy.CalculateField_management(PJDY, nClassName,  "!{}_CLASS!".format(element), "PYTHON_9.3")
arcpy.CalculateField_management(midFile, nydObjectId,  "!{}!".format(nydDesc.OIDFieldName), "PYTHON_9.3")

# 查询相邻面
objectid_list = set()
len_list = defaultdict(dict)
class_list = defaultdict(dict)
arcpy.SetProgressorLabel("查询相邻面...")
arcpy.Intersect_analysis([midFile, PJDY], outputfile, "ALL", None, "LINE")

arcpy.SetProgressorLabel("计算接边线长度...")
arcpy.AddField_management(outputfile, lineLength, "DOUBLE")
arcpy.CalculateField_management(outputfile, lineLength, "!Shape.Length!", "PYTHON_9.3")

arcpy.SetProgressorLabel("取出接边线最长的地块级别...")
fields = (nydObjectId, pjdyObjectId, nClassName, lineLength)
for row in arcpy.da.SearchCursor(outputfile, fields):
	nydid, pjdyid, claName, llength = row
	dybh = int(nydid)
	pjdybh = int(pjdyid)
	dy_class = int(claName)
	objectid_list.add(dybh)
	len_list[dybh][pjdybh] = len_list[dybh].get(pjdybh, 0.0000) + float(llength)
	class_list[dybh][pjdybh] = dy_class

filter_reason = defaultdict()
for k, v in len_list.items():
	max_bh = 0
	max_value = 0
	# arcpy.AddMessage(str(len_list[k]))
	for vv in v.keys():
		if float(len_list[k].get(vv, 0)) > max_value:
			max_value = float(len_list[k].get(vv, 0))
			max_bh = vv

	if max_bh > 0:
		filter_reason[k] = class_list[k][max_bh]
		# arcpy.AddMessage(max_bh)

#
arcpy.SetProgressorLabel("更新结果数据...")
fields = (nydObjectId, className)
with arcpy.da.UpdateCursor(midFile, fields) as cursor:
	for row in cursor:
		if row[0] in objectid_list:
			try:
				row[1] = filter_reason[row[0]]
			except Exception as err:
				print(err)
		cursor.updateRow(row)

# arcpy.Select_analysis(midFile, outputfile)

arcpy.SetProgressorLabel("清理临时数据...")
arcpy.DeleteField_management(PJDY, [pjdyObjectId, nClassName])
# arcpy.DeleteField_management(NYD, [nydObjectId])
arcpy.Delete_management(outputfile)

