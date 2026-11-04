# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_selectionFilter.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

def vertexCount(MIN=8,MAX=16):
	RET=[]
	MESH=cmds.ls(type='mesh')
	for each in MESH:
		if MIN<=cmds.polyEvaluate(each,v=True)<=MAX:
			RET.append(each)
	if RET:
		cmds.select(RET,r=True)


def edgeLength(MIN=0,MAX=40):
	cmds.polySelectConstraint(dis=True)
	RET=[]
	SEL=cmds.ls(dag=True,type='mesh')
	cmds.select(SEL,r=True)
	cmds.polySelectConstraint(m=3,t=0x8000,l=1,lb=[MIN,MAX])
	#RET=cmds.listRelatives(cmds.listRelatives(p=True,s=True,f=True),p=True,type='transform',f=True)
	COMP=cmds.filterExpand(sm=32)
	RET=cmds.listRelatives(cmds.listRelatives(COMP,p=True,s=True,f=True),p=True,type='transform',f=True)

	cmds.polySelectConstraint(dis=True)
	if RET:
		cmds.select(RET,r=True)


def LayoutA():
	cmds.columnLayout('MS_selectionFilter_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_selectionFilter',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	#
	cmds.text(l='vertexCount')
	cmds.gridLayout(nc=4,cw=50)
	cmds.button(l='8',c=lambda *args:vertexCount(8,8))
	cmds.button(l='16',c=lambda *args:vertexCount(16,16))
	cmds.button(l='8-16',c=lambda *args:vertexCount(8,16))
	cmds.button(l='16-',c=lambda *args:vertexCount(16,65535))
	cmds.setParent('..')
	#
	cmds.separator()
	#
	cmds.text(l='edgeLength')
	cmds.gridLayout(nc=4,cw=50)
	cmds.button(l='40',c=lambda *args:edgeLength(0,40))
	cmds.button(l='40-100',c=lambda *args:edgeLength(40,100))
	cmds.button(l='100-1000',c=lambda *args:edgeLength(100,1000))
	cmds.button(l='1000-',c=lambda *args:edgeLength(1000,65535))
	cmds.setParent('..')
	#
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_selectionFilter',q=True,ex=True):
		cmds.deleteUI('MS_selectionFilter')
	cmds.window('MS_selectionFilter',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_selectionFilter')
	