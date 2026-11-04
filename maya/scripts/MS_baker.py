# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_baker.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds


def main():
	SEL=cmds.ls(sl=True,l=True)
	DUPED=cmds.duplicate(SEL)
	UNITED=cmds.polyUnite(DUPED)
	cmds.polyMultiLayoutUV(UNITED,lm=1,sc=0,rbf=2,fr=1,ps=0.1,l=2,psc=0,su=1,sv=1,ou=0,ov=0)
	cmds.surfaceSampler(#target=UNITED[0],uvSet='map1',searchOffset=5.936448562,maxSearchDistance=0,searchCage="",source=SEL[0])
		target=UNITED[0]
		,uvSet='map1'
		,searchOffset=5.936448562
		,maxSearchDistance=0
		,searchCage=""
		,source=SEL[0]
		,mapOutput='diffuseRGB'
		,mapWidth=1024
		,mapHeight=1024
		,max=1
		,mapSpace='tangent'
		,mapMaterials=1
		,shadows=1
		,filename="D:/work/baked_c"
		,fileFormat="tif"
		,superSampling=2
		,filterType=0
		,filterSize=3
		,overscan=100
		,searchMethod=0
		,useGeometryNormals=1
		,ignoreMirroredFaces=0
		,flipU=0
		,flipV=0
		)
	
def LayoutA():
	cmds.columnLayout('MS_baker.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_baker.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
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


