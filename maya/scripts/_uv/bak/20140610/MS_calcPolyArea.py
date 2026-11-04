# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import re
import _winreg
import datetime
import codecs
import glob
import math

import maya.cmds as cmds
import maya.OpenMaya as om
import maya.OpenMayaMPx as ompx
import maya.mel as mel

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
