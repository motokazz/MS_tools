# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_calcPoly.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.OpenMaya as om

########
# calc
########

class MS_calcPolyScale():
	# ポリゴンオブジェクトの面積を求めるclass。実行MethodはdoIt＿～。引数はポリゴンオブジェクト。
	# 面積の合計を返す
	def transFaceIt(self,  targetObject):
		#オブジェクトをいれるとＦａｃｅＩｔｅｒａｔｏｒを返す
		sel = om.MSelectionList()
		sel.add(targetObject)
		dagPath = om.MDagPath()
		obj = om.MObject()
		sel.getDagPath(0,  dagPath, obj)
		return om.MItMeshPolygon(dagPath, obj)
	def areaTriangle(self, aP, bP, cP):
		#三つの点で三角形の面積を計算
		v1 = om.MVector(bP - aP)
		v2 = om.MVector(cP - aP)		
		return (v1 ^ v2).length() * 0.5
	def doIt_PolyScale(self,  targetObject):
		#ポリゴンオブジェクトのＦａｃｅ面積を求める
		currentFace = self.transFaceIt(targetObject)			
		scaleTotal = 0		
		while not currentFace.isDone():				
			pointArr = om.MPointArray()
			intArr = om.MIntArray()				
			currentFace.getTriangles(pointArr, intArr, om.MSpace.kWorld)				
			for x in range(pointArr.length() / 3):					
				scaleTotal += self.areaTriangle(pointArr[0 + (x*3)], pointArr[1 + (x*3)], pointArr[2 + (x*3)])					
			currentFace.next()					
		return scaleTotal
	def doIt_BBoxScale(self,  targetObject):
		#オブジェクトのBoundingBoxの面積を求める
		BBcoord = mc.xform(targetObject,  q=1,  bb=1)
		scaleTotal = (BBcoord[3] - BBcoord[0]) * (BBcoord[4] - BBcoord[1]) * (BBcoord[5] - BBcoord[2])
		return scaleTotal
	def isItPolygonMesh(self, targetList):
		#オブジェクトがポリゴンオブジェクトかどうかを検査する。
		try:
			polyMeshObj = mc.filterExpand(targetList,  sm=12)
		except:
			return 0
		else:
			if polyMeshObj and len(targetList) == len(polyMeshObj):
				if len(polyMeshObj) > 1:								  
					return 1
				elif len(polyMeshObj) < 2:				
					return 0
			else:				
				return 0

def exec_MS_calcPolyScale():
	CPS=MS_calcPolyScale()
	scaleResult=[]
	TOTAL=0
	targetList = cmds.ls(sl=True,l=True)
	
	for x in targetList:
		TOTAL_AREA=0
		SEL=cmds.listRelatives(x,ad=True,type='mesh',f=True)

		#BBox
		XF = cmds.xform(x,q=True,bb=True,ws=True)
		BBSize=((XF[3]-XF[0])*(XF[4]-XF[1])*(XF[5]-XF[2]))


		#calcPolyArea
		for EACH in SEL:
			EACH_MESH_TRN=cmds.listRelatives(EACH,p=True,type='transform',f=True)[0]
			POLYAREA=CPS.doIt_PolyScale(EACH_MESH_TRN)
			TOTAL_AREA+=POLYAREA

		#mat
		cmds.select(SEL,r=True)
		cmds.hyperShade(smn=True)
		MATS=cmds.ls(sl=True,mat=True)

		print x.split('|')[-1]+'\t'+str(TOTAL_AREA)+'\t'+str(long(BBSize))+'\t'+str(len(MATS))

		scaleResult.append(EACH_MESH_TRN+'\t'+str(TOTAL_AREA))
	
	return scaleResult

