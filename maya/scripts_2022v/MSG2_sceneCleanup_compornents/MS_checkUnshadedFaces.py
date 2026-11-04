# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_checkUnshadedFaces.py
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds

def findUnshadedObjects():
	listOfShapes = cmds.ls(geometry=True)
	RET=[]

	for each in listOfShapes:
		
		shapeType = cmds.ls(each,showType=True)

		# Skip over curves, as they are not rendered anyway.
		if shapeType[1] == 'nurbsCurve':
			continue
		if shapeType[1] == 'nurbsCurve':
			continue
	#
	# Get a list of all shading engines connected 'downstream'
	# from this geometry.
	#

		shaders = cmds.listConnections(each,source=True,type='shadingEngine')
		if shaders:
			numShaders = len(shaders)
		else:
			RET.append(each)

	return RET

def UNSEL():
	RET=[]
	MESH=cmds.ls(type='mesh')
	FACES=cmds.polyListComponentConversion(MESH,tf=True)
	EXFACES=cmds.filterExpand(FACES,sm=34,ex=True)
	for each in EXFACES:
		shaders = cmds.listConnections(each,source=True,type='shadingEngine')
		if not shaders:
			RET.append(each)
	return RET

UNSHADED=findUnshadedObjects()
print UNSHADED
UN=UNSEL()
cmds.select(UN,r=True)

