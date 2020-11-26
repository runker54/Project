# This Python file uses the following encoding: utf-8
import os, sys
import arcpy
import arcpy.da
import logging
import math
logging.basicConfig(level=logging.INFO)

inWorkSpacePath = sys.argv[1]
inLayer = sys.argv[2]
ispolygon = sys.argv[3]
arcpy.env.workspace = inWorkSpacePath
#arcpy.env.overwriteOutput = true
try:
	arcpy.DeleteField_management(inLayer,["COORS", "ANGLES"])
except Exception as err:
	print(err)

arcpy.AddField_management(inLayer,"COORS","TEXT","","",99999999)
arcpy.AddField_management(inLayer,"ANGLES","TEXT","","",99999999)

codeblock="""
def GetFeatureVerticesStr(feat):
 if feat.type=="point":
     pnt=feat.getPart()
     px='%f' %pnt.X
     py='%f' %pnt.Y
     #TranCoorform degree minute second
     #px,py=TranCoorform(px,py)
     return "["+px+","+py+"]"
 if feat.type=="multipoint":
     multstr=''
     part=feat.getPart()
     pnt=part.next()
     while pnt:
         px='%f' %pnt.X
         py='%f' %pnt.Y
         #TranCoorform degree minute second
         #px,py=TranCoorform(px,py)
         multstr=multstr+"["+px+","+py+"],"
         pnt=part.next()
     return multstr[:-1]
 elif feat.type in["polygon","polyline"]:
     partnum = 0
     partcount = feat.partCount
     pntcount = 0
     ringcount=0
     str=''
     while partnum < partcount:
         part = feat.getPart(partnum)
         partstr=getpartstr(part)
         partnum += 1
         if partnum!=1:
             partstr=","+partstr
         str=str+partstr
     return str
def getpartstr(part):
    strpart=''
    flag=False
    pnt = part.next()
    strpart=strpart+"["
    while pnt:
        px='%f' %pnt.x
        py='%f' %pnt.y
        #TranCoorform degree minute second
        #px,py=TranCoorform(px,py)
        strpart=strpart+px+","+py +";"
        pnt = part.next()
        # interior ring
        if not pnt:
            pnt = part.next()
            if pnt:
                if flag:
                    strpart=strpart[:-1]
                    strpart=strpart+"};"
                    flag=False
                strpart=strpart+"{"
                flag=True
            else:
                if flag:
                    strpart=strpart+"}"
                    flag=False
                if strpart[-1]!="}":
                    strpart=strpart[:-1]
                else:
                    strlen=len(strpart)-2
                    strpart = strpart[:strlen] + strpart[strlen+1:]
	        strpart=strpart+"]"
    return strpart
def TranCoorform(x,y):
    dfmx=str(x).split('.')
    dx=dfmx[0]
    ftempx=float("0."+dfmx[1])*60
    fx=str(int(ftempx))
    mx=str(float("0."+str(ftempx).split('.')[1])*60)
    px=dx+"°"+fx+"′"+mx+"″"
    dfmy=str(y).split('.')
    dy=dfmy[0]
    ftempy=float("0."+dfmy[1])*60
    fy=str(int(ftempy))
    my=str(float("0."+str(ftempy).split('.')[1])*60)
    py=dy+"°"+fy+"′"+my+"″"
    return px,py
	"""

arcpy.CalculateField_management(inLayer, "COORS", "GetFeatureVerticesStr(!Shape!)", "PYTHON_9.3", codeblock)

codeblock = """
def getAngles(coorStr, ispolygon):
	angls = ""
	try:
		qkCoorStrs = coorStr.split(']')
		for qkCoorStr in qkCoorStrs:
			qkCoor = qkCoorStr.strip(',').strip('[')
			coors = qkCoor.split('{')
			for coor in coors:
				coss = coor.strip().lstrip().strip('[').strip(']').strip('}').strip(';')
				cos = coss.split(';')
				count = len(cos)
				if (count < 3):
					continue

				for i in range(0, count):
					if i < count - 1:
						first = cos[i]
						second = ""
						third = ""
						if(i < count - 2):
							second = cos[i + 1]
							third = cos[i + 2]
						else:
							if(ispolygon != 1):
								continue

							second = cos[i + 1]
							third = cos[1]
						angle = mathAngles(first, second, third)
						if angle < 5:
							angls = angls + first + ";" + second + ";" + third + "("+ str(angle)+ ")"+ "|"
							#return angle
	except:
		return "ERROR"
	return angls

def mathAngles(s, o, e):
    cosfi = 0
    fi = 0
    norm = 0

    scs = s.split(',')
    ocs = o.split(',')
    ecs = e.split(',')

    dsx = float(scs[0]) - float(ocs[0])
    dsy = float(scs[1]) - float(ocs[1])
    dex = float(ecs[0]) - float(ocs[0])
    dey = float(ecs[1]) - float(ocs[1])

    cosfi = dsx * dex + dsy * dey
    norm = (dsx * dsx + dsy * dsy) * (dex * dex + dey * dey)
    cosfi = cosfi / math.sqrt(norm)

    if (cosfi >= 1.0):
        return 0
    if (cosfi <= -1.0):
        return math.pi
    fi = math.acos(cosfi)
    if (180 * fi / math.pi < 180):
        return 180 * fi / math.pi
    else:
        return 360 - 180 * fi / math.pi
    return 0
"""

arcpy.CalculateField_management(inLayer, "ANGLES", "getAngles(!COORS!,"+ ispolygon + ")", "PYTHON_9.3", codeblock)
