# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_selectAtgi.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

def selectAtgi():
	Nodes=[]
	Shapes=cmds.ls(s=True)
	for each in Shapes:
		if cmds.nodeType(each)=='GraviteAtgiLocatorNode':
			Trn = cmds.listRelatives(ap=True,typ='transform')
			Nodes.append(Trn[0])
	cmds.select(Nodes,r=True)

def LayoutA():
	cmds.columnLayout('MS_tools_mainLayoutselectAtgi',adj=True)
	cmds.separator()
	cmds.text(l='selectAtgi',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='selectAtgi',c=lambda *args:selectAtgi())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	