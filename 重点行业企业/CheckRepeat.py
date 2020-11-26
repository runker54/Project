import os, sys
import arcpy
import arcpy.da

inWorkSpacePath = "D:\JC17_530102.gdb"
#sys.argv[1]
inLayer = "UV_LCRA"
#sys.argv[2]

arcpy.env.workspace = inWorkSpacePath
arcpy.env.overwriteOutput = True

fields = arcpy.ListFields(inLayer)
fieldsNames = []
for field in fields:
    # Check the field name, perform a calculation when finding the field 'Flag'
    if field.name.upper() == 'SHAPE' or field.name.upper() == 'SHAPE_LENGTH' or field.name.upper() == 'SHAPE_AREA' or field.name.upper() == 'OBJECTID':
        continue
    fieldsNames.append(field.name)

arcpy.FindIdentical_management(inLayer, fieldsNames + "REP", fieldsNames)
print(ids)
