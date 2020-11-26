# This Python file uses the following encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import arcpy
import xml.dom.minidom as DOM
try: 
	import xml.etree.cElementTree as ET 
except ImportError: 
	import xml.etree.ElementTree as ET 


inMxdFilePath = sys.argv[1]
inServiceName = sys.argv[2]
outSDDraftFilePath = sys.argv[3]
copyToServerStr = sys.argv[4]
outServiceDefinition = sys.argv[5]
con = sys.argv[6]
tilingSchemeFile = sys.argv[7]
copyToServer = copyToServerStr == str(True)

mapDoc = arcpy.mapping.MapDocument(inMxdFilePath)
analysis = arcpy.mapping.CreateMapSDDraft(mapDoc, outSDDraftFilePath, inServiceName, 'ARCGIS_SERVER', con, True, None, None, None)

# WMSServer Service参数
soe = 'WMSServer'
soeProperty = 'title'
soePropertyValue = 'WMSServer Desctiption'

# 打开sddraft文件
doc = DOM.parse(outSDDraftFilePath)

# 修改sddraft文件
f = open(outSDDraftFilePath, 'w')
doc.writexml(f)
f.close()

# 分析sddraft文件的错误
analysis = arcpy.mapping.AnalyzeForSD(outSDDraftFilePath)
#print "The following information was returned during analysis of the MXD:"

# Stage and upload the service if the sddraft analysis did not contain errors
if analysis['errors'] == {}:
    # Execute StageService. This creates the service definition.
	#arcpy.StageService_server(outSDDraftFilePath, outServiceDefinition)

    # Execute UploadServiceDefinition. This uploads the service definition and publishes the service.
	#arcpy.UploadServiceDefinition_server(outServiceDefinition, con)
	print "success published service"
else: 
	print "could not be published service because errors were found during analysis."
	for key in ('messages', 'warnings', 'errors'):
		print '----' + key.upper() + '---'
		vars = analysis[key]
		for ((message, code), layerlist) in vars.iteritems():
			print '    ', message, ' (CODE %i)' % code
			print '       applies to:',
			for layer in layerlist:
				print layer.name,
			print

	print arcpy.GetMessages()                              