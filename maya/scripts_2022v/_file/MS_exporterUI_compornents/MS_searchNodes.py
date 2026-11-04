# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_searchNodes.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

def searchNodes(SEARCHWORD=''):
	SEL = cmds.ls(l=True,tr=True)
	SEARCHED=[]
	for each in SEL:
		if SEARCHWORD in each:
			SEARCHED.append(each)
	return SEARCHED
			
def main():
	SEARCHWORD=cmds.textField('MS_searchNodes_searchWrod',q=True,tx=True)
	SEARCHED = searchNodes(SEARCHWORD)
	cmds.select(SEARCHED,r=True)

def LayoutA():
	cmds.columnLayout('MS_searchNodes.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_searchNodes.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.textField('MS_searchNodes_searchWrod',tx='')
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