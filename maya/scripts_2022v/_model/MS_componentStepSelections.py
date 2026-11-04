# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_componentStepSelections.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

def selectEdgeLoop():
	cmds.polySelectSp(loop=True)

def main(START=0,STEP=2):
	
	SEL=cmds.filterExpand(sm=[31,32,34,35],ex=True)
	cmds.select(list(set(SEL)-set(SEL[START::STEP])),r=True)




def LayoutA():
	cmds.columnLayout('MS_componentStepSelections.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_componentStepSelections.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.gridLayout(nc=4)
	cmds.button(l='ev2',c=lambda *args:main(0,2))
	cmds.button(l='ev3',c=lambda *args:main(0,3))
	cmds.button(l='odd2',c=lambda *args:main(1,2))
	cmds.button(l='odd3',c=lambda *args:main(1,3))
	cmds.setParent('..')
	cmds.separator()

	cmds.button(l='selectEdgeLoop',c=lambda *args:selectEdgeLoop())

	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	