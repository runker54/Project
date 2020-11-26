# -*- coding: cp936 -*-
from collections import defaultdict
import arcpy

XCDW = arcpy.GetParameterAsText(0)	 # ����λ
PJDY = arcpy.GetParameterAsText(1)  # ���۵�Ԫ
element = arcpy.GetParameterAsText(2)	 # Cd
outputgeodatabase = arcpy.GetParameterAsText(3)  # ���·��

d = defaultdict(dict)
tempFile = "temp_pjdy"
pjdyjoinfile = "Join_pjdy"
pjdyObjectId = "CID_PJDY"
pjdyObjectId2 = "CCID_PJDY"
outputfile = "dddy_filter"
arcpy.env.workspace = outputgeodatabase
arcpy.env.overwriteOutput = True

xcdwDesc = arcpy.Describe(XCDW)
pjdydesc = arcpy.Describe(PJDY)

tjjg = "ͳ�ƽ��"
pjdyoid = pjdydesc.OIDFieldName
className = "{}_CLASS_1".format(element)

try:
	arcpy.DeleteField_management(PJDY, [pjdyObjectId])
except Exception as err:
	print(err)

arcpy.AddField_management(PJDY, pjdyObjectId, "LONG")

arcpy.SetProgressorLabel("�������۵�ԪID...")
arcpy.CalculateField_management(PJDY, pjdyObjectId,  "!{}!".format(pjdyoid), "PYTHON_9.3")

# �����и����ռ���۵�Ԫ���������
arcpy.SetProgressorLabel("��Ԫ���λ���пռ�λ�÷���...")
arcpy.SpatialJoin_analysis(XCDW, PJDY, pjdyjoinfile, "JOIN_ONE_TO_MANY", "KEEP_COMMON")

# ȡ��ֻ��һ����λ�����۵�Ԫ
arcpy.SetProgressorLabel("ȡ��ֻ��һ����λ�����۵�Ԫ...")
d2 = defaultdict(int)
d3 = defaultdict(int)
objectid_list = set()
fields = (pjdyObjectId, "{}_LEVEL".format(element))
for row in arcpy.da.SearchCursor(pjdyjoinfile, fields):
	cid, lev = row
	d2[cid] = int(d2[cid]) + 1
	d3[cid] = int(lev)

for k, v in d2.items():
	if int(v) < 2:
		objectid_list.add(int(k))

if len(objectid_list) == 0:
	whereclause = pjdyoid + ' in (-1)'
elif len(objectid_list) == 1:
	whereclause = pjdyoid + ' in ({})'.format((objectid_list.pop()))
else:
	whereclause = pjdyoid + ' in {}'.format(tuple(objectid_list))

arcpy.Select_analysis(PJDY, outputfile, whereclause)

arcpy.SetProgressorLabel("�������۵�Ԫ...")
arcpy.AddField_management(outputfile, tjjg, "TEXT")
arcpy.AddField_management(outputfile, pjdyObjectId2, "LONG")
arcpy.CalculateField_management(outputfile, pjdyObjectId2,  "!{}!".format(arcpy.Describe(outputfile).OIDFieldName), "PYTHON_9.3")

# ��ѯ������
objectid_list = set()
zdh_list = defaultdict(list)
arcpy.SetProgressorLabel("��ѯ������...")
arcpy.Intersect_analysis([outputfile, PJDY], tempFile, "ALL", None, "LINE")
fields = (pjdyObjectId2, className, pjdyObjectId, "{}_1".format(pjdyObjectId))
for row in arcpy.da.SearchCursor(tempFile, fields):
	cid, clas, id1, id2 = row
	if(int(id1) != int(id2)):
		dybh = int(cid)
		dy_class = int(clas)
		objectid_list.add(dybh)
		try:
			zdh_list[dybh].index(id2)
		except Exception as err:
			zdh_list[dybh].append(id2)
			d[dybh][dy_class] = d[dybh].get(dy_class, 0) + 1

#
arcpy.SetProgressorLabel("���½������...")
fields = (pjdyObjectId, "{}_CLASS".format(element), pjdyObjectId2, tjjg)
with arcpy.da.UpdateCursor(outputfile, fields) as cursor:
	for row in cursor:
		if row[2] in objectid_list:
			count = 0
			for v in d[row[2]].values():
				count += int(v)
			row[3] = "m:{},d:{},{},{}".format(row[1], str(d3[row[0]]), count, str(d[row[2]]))
		cursor.updateRow(row)

arcpy.SetProgressorLabel("������ʱ����...")
# arcpy.DeleteField_management(PJDY, [pjdyObjectId])
# arcpy.Delete_management(pjdyjoinfile)
# arcpy.Delete_management(tempFile)

