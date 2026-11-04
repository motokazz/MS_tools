# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_calcEdgeLength.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import _lib.MS_distance as MS_distance
reload(MS_distance)

##### utility
	
##### mesureTool

def calcEdgeLength():
	EDG=cmds.filterExpand(sm=32)
	LEN=0
	for each in EDG:
		V=cmds.polyListComponentConversion(each,tv=True)
		LEN+=MS_distance.distance(V[0],V[1])
	cmds.scrollField('MS_calcEdgeLength_log',e=True,tx=LEN)

def LayoutA():
	cmds.columnLayout('MS_calcEdgeLength.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_calcEdgeLength.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='calcEdgeLength',c=lambda *args:calcEdgeLength())
	cmds.scrollField('MS_calcEdgeLength_log')
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	