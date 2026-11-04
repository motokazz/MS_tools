# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_checkResolutionPerPoly.py
# 説明
#			
#			
# 作成日
#			
########################################


import maya.cmds as cmds
import maya.mel as mel
import math

import maya.OpenMaya as om

########
# calc
########

def calcPolyArea():
	sl=om.MSelectionList()
	om.MGlobal.getActiveSelectionList(sl)
	it=om.MItSelectionList(sl,om.MFn.kMeshPolygonComponent)
	dp=om.MDagPath()
	comp=om.MObject()
	result=0.0
	while it.isDone() is False:
		it.getDagPath(dp,comp)
		itMeshPoly=om.MItMeshPolygon(dp,comp)
		while itMeshPoly.isDone() is False:
			aP=om.MPointArray()
			aVtxList=om.MIntArray()
			itMeshPoly.getTriangles(aP,aVtxList,om.MSpace.kWorld)
			nTri=int(aVtxList.length()/3)
			i=0
			while i<nTri:
				idx=i*3

				a=aP[idx].distanceTo(aP[idx+1])
				b=aP[idx+1].distanceTo(aP[idx+2])
				c=aP[idx+2].distanceTo(aP[idx])
				s=(a+b+c)/2.0
				_result=math.sqrt(s*(s-a)*(s-b)*(s-c))
				result=_result+result
				i+=1

			itMeshPoly.next()
		it.next()
	return result

def calcUVArea(uvset=''):
	sl=om.MSelectionList()
	om.MGlobal.getActiveSelectionList(sl)
	it=om.MItSelectionList(sl,om.MFn.kMeshPolygonComponent)
	dp=om.MDagPath()
	comp=om.MObject()
	result=0.0
	iPoly=0
	while it.isDone() is False:
		it.getDagPath(dp,comp)
		itMeshPoly=om.MItMeshPolygon(dp,comp)
		mesh=om.MFnMesh(dp)
		aMeshU=om.MFloatArray()
		aMeshV=om.MFloatArray()
		if uvset=='': mesh.getUVs(aMeshU,aMeshV)
		else: mesh.getUVs(aMeshU,aMeshV,uvset)
		
		while itMeshPoly.isDone() is False:
			aP=om.MPointArray()
			aVtxList=om.MIntArray()
			itMeshPoly.getTriangles(aP,aVtxList)
			aU=[0.0,0.0,0.0]
			aV=[0.0,0.0,0.0]

			nTri=int(aVtxList.length()/3)
			
			i=0
			for i in range(nTri):
				try:
					index0 = om.MScriptUtil().asIntPtr()
					index1 = om.MScriptUtil().asIntPtr()
					index2 = om.MScriptUtil().asIntPtr()


					idx=i*3

					itMeshPoly.getUVIndex(aVtxList[idx],index0)
					i0 = om.MScriptUtil.getInt(index0)
					#print 'idx0 '+str(i0)
					
					itMeshPoly.getUVIndex(aVtxList[idx+1],index1)
					i1 = om.MScriptUtil.getInt(index1)
					#print 'idx1 '+str(i1)

					itMeshPoly.getUVIndex(aVtxList[idx+2],index2)
					i2 = om.MScriptUtil.getInt(index2)
					#print 'idx2 '+str(i2)

					aU[0]=aMeshU[i0]
					aU[1]=aMeshU[i1]
					aU[2]=aMeshU[i2]
					aV[0]=aMeshV[i0]
					aV[1]=aMeshV[i1]
					aV[2]=aMeshV[i2]

					a=(aU[0]-aU[2])*(aV[1]-aV[0])
					b=(aU[0]-aU[1])*(aV[2]-aV[0])

					_result=(abs(a-b))/2
					result=_result+result
					print result

				except:
					print 'error'
					pass

			itMeshPoly.next()
		it.next()
	return result


def main():
	RESULT=[]
	SEL=cmds.ls(sl=True)
	PREPOLYS=cmds.polyListComponentConversion(SEL,tf=True)
	POLYS=cmds.filterExpand(sm=34,ex=True)
	SIZE_PER_PIX=2.0
	for EACHPOLY in POLYS:
		
		CurrentUVSet=cmds.polyUVSet(EACHPOLY,q=True,cuv=True)[0]
		cmds.select(EACHPOLY,r=True)
		
		#エリア計測
		POLY_AREA=calcPolyArea()
		UV_AREA=calcUVArea(uvset=CurrentUVSet)
		print POLY_AREA
		print UV_AREA
		cmds.hyperShade(smn=True)
		try:
			FTN=cmds.listConnections('.color')[0]
			if FTN:
				OUTSIZE=cmds.getAttr(FTN+'.outSize')[0]
		except:
			OUTSIZE=(1024,1024)

		try:
			SVALUE=math.sqrt((POLY_AREA*(SIZE_PER_PIX**2))/(UV_AREA*(OUTSIZE[0]*OUTSIZE[1])))
			#SVALUE=math.sqrt(((POLY_AREA*SIZE_PER_PIX)**2)/((UV_AREA*OUTSIZE[0]*OUTSIZE[1])**2))
		except:
			SVALUE=1
		print SVALUE
		#
		if not 0.8<SVALUE<1.5:
			RESULT.append(EACHPOLY)
	print RESULT
	if RESULT:
		cmds.select(RESULT,r=True)

def LayoutA():
	cmds.columnLayout('MS_checkResolutionPerPoly.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_checkResolutionPerPoly.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	
UI()


