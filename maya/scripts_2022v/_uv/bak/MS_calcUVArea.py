# -*- coding: utf-8 -*-
import maya.OpenMaya as om

def calcUVArea(uvset=''):
	print '1'
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
			while i<nTri:
				try:
					index0 = om.MScriptUtil().asIntPtr()
					index1 = om.MScriptUtil().asIntPtr()
					index2 = om.MScriptUtil().asIntPtr()

					idx=i*3

					itMeshPoly.getUVIndex(idx,index0)
					i0 = om.MScriptUtil.getInt(index0)
					#print 'idx0 '+str(i0)
					
					itMeshPoly.getUVIndex(idx+1,index1)
					i1 = om.MScriptUtil.getInt(index1)
					#print 'idx1 '+str(i1)

					itMeshPoly.getUVIndex(idx+2,index2)
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
				except:
					pass
				i+=1
			itMeshPoly.next()
		it.next()
	return result




