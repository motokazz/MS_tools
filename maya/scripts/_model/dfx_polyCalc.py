#coding: utf-8

"""
Terms of Use
The following script is provided for your conveniece and is used at your
own discretion and risk. Digital Frontier is not responsible for any
damage to your computer system or loss of data that results from the
access, download and use of the content on this site.
"""

import maya.cmds as mc
import maya.cmds as mc
import maya.OpenMaya as om
import maya.mel as mm
import math
class calcPolyScale():
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

class aboutUVClass():
#ＵＶに関するclass
	def calcUVscale(self,  targetObject):
#各ＵＶの最小最大値を求め四角の面積を求める
		listUV = mc.polyEditUV('%s.map[:]' % targetObject,  q=1) 
		return (max(listUV[0::2]) - min(listUV[0::2])) * (max(listUV[1::2]) - min(listUV[1::2])),  min(listUV[0::2]), min(listUV[1::2])
	def reScaleUV(self, objName, uMin, vMin, scaleRate):		
#比率に合わせＵＶのサイズを変える
		mc.polyEditUV('%s.map[:]'%objName,  pu=uMin,  pv=vMin, su=math.sqrt(scaleRate),  sv=math.sqrt(scaleRate))
	def UVScaleRate(self,  scaleResult,  UVResultList):
#ポリゴン面積とＵＶ面積を比較し比率を求める
		scaleRate = []
		for i, x in enumerate(UVResultList):  
			scaleRate.append((scaleResult[i] * UVResultList[0][0]) / (scaleResult[0] * x[0]))
		return scaleRate

class UvRateScaling():   
#実行class				 
	def doIt(self,  calcKind):
		scaleResult = []
		targetList = mc.ls(sl=1)
		calcClass = calcPolyScale()
		if calcClass.isItPolygonMesh(targetList) == 1:			
			if calcKind == 1:				
				for x in targetList:					
					scaleResult.append(calcClass.doIt_PolyScale(x))
			else:
				for x in targetList:					
					scaleResult.append(calcClass.doIt_BBoxScale(x))						
			UVClass = aboutUVClass()
			UVResultList = []
			for x in targetList:
				UVResultList.append(UVClass.calcUVscale(x))
			scaleRate = UVClass.UVScaleRate(scaleResult,  UVResultList)			
			for i, x in enumerate(targetList):
				if i != 0:
					UVClass.reScaleUV(x, UVResultList[i][1], UVResultList[i][2], scaleRate[i])		   
			return 1
		else:
			mm.eval('warning \"Need to select One Standard Polygon Object and Target Polygon Object(s)\"')
			return 0		

class UVScalinToolUI():
#UIのClass。ＵＩが存在する場合消して新たに作成する。
	def __init__(self):
		self.executeClass = UvRateScaling()
	def makeIt(self):
		try: 
			mc.deleteUI('ScaleRateUVAuto')		
		except:
			return		
		finally:				
			winName = mc.window('ScaleRateUVAuto')		
			mc.frameLayout( l='Calculate Sytle', bs='etchedIn',  mh=7,  mw=7 )
			mc.columnLayout()
			self.radioName = mc.radioButtonGrp(nrb=2,  la2=['FaceSizeTotal',  'BoundingBox'],  sl=1, h=30)
			mc.button(l='ReScaleUV',  c='uvRateTool.executeClass.doIt(mc.radioButtonGrp(uvRateTool.radioName, q=1, sl=1))',  h=50,  w=190)
			mc.button(l='calcArea',c=lambda *args:do())
			mc.window(winName, e=1, w=230, h=140, s=0)
			mc.showWindow()

def do():
	CPS=calcPolyScale()
	scaleResult=[]
	targetList = mc.ls(sl=1)
	for x in targetList:					
		scaleResult.append(CPS.doIt_PolyScale(x))
	print scaleResult

#UVS=UVScalinToolUI()
#UVS.makeIt()
