# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_fitVertexToGrid.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds



def fitVertexToGrid(grid=1):
	vtxs = cmds.filterExpand(ex=True,sm=31)
	if not vtxs:
		comp = cmds.polyListComponentConversion(tv=True)
		vtxs = cmds.filterExpand(comp,ex=True,sm=31)

	for each in vtxs:
		trn = cmds.xform(each,q=True,t=True,ws=True)
		trn[0]=round(trn[0]/grid,0)*grid
		trn[1]=round(trn[1]/grid,0)*grid
		trn[2]=round(trn[2]/grid,0)*grid
		cmds.xform(each,t=trn,ws=True)

def doManualSlider():
	V=cmds.floatSliderGrp('MS_fitVertexToGrid_manualSlider',q=True,v=True)
	fitVertexToGrid(V)


def LayoutA():
	cmds.columnLayout('MS_fitVertexToGrid_mainLayout',adj=True,ann=u'選択した頂点を全て指定グリッドにフィットさせる')
	cmds.text(l='fitVertexToGrid',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.gridLayout(nc=4)
	cmds.button(l='1',c=lambda *args:fitVertexToGrid(1))
	cmds.button(l='10',c=lambda *args:fitVertexToGrid(10))
	cmds.button(l='100',c=lambda *args:fitVertexToGrid(100))
	cmds.button(l='1000',c=lambda *args:fitVertexToGrid(1000))
	cmds.setParent('..')
	cmds.floatSliderGrp('MS_fitVertexToGrid_manualSlider',l='input',v=50,f=True)
	cmds.button(l='do',c=lambda *args:doManualSlider())
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	