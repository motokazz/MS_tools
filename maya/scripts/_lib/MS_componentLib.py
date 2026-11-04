# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_conponentLib
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds
	

def getFaces(CONP):#フェース選択
	FACE=cmds.polyListComponentConversion(CONP,tf=True)
	result=cmds.filterExpand(FACE,ex=True,sm=34)
	return result
	
def getVerts(CONP):#頂点選択
	VTX=cmds.polyListComponentConversion(CONP,tv=True)
	result=cmds.filterExpand(VTX,ex=True,sm=31)
	return result
	
def getEdges(CONP):#エッジ選択
	EDGE=cmds.polyListComponentConversion(CONP,te=True)
	result=cmds.filterExpand(EDGE,ex=True,sm=32)
	return result

def getVertsFaces(CONP):#フェース頂点選択
	FACE=cmds.polyListComponentConversion(CONP,tvf=True)
	result=cmds.filterExpand(FACE,ex=True,sm=70)
	return result
	

