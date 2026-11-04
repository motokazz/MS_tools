# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_branchSetup.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

def main():
	SEL=cmds.ls(sl=True)

	for each in SEL:
		ECS = cmds.polyColorSet(each,q=True,acs=True)
		ECCS= cmds.polyColorSet(each,q=True,ccs=True)
		if not 'branchColor' in ECS:
			cmds.polyColorSet(each,cr=True,cs='branchColor')
			cmds.polyColorSet(each,ccs=True,cs='branchColor')
			cmds.polyColorPerVertex(each,rgb=[0,0,0],a=0)
			cmds.polyColorSet(each,ccs=True,cs=ECCS[0])
		EUVS= cmds.polyUVSet(each,q=True,auv=True)
		ECUVS=cmds.polyUVSet(each,q=True,cuv=True)
		if not 'branchUV' in EUVS:
			cmds.polyUVSet(each,cp=True,cuv=True,nuv='branchUV')


def LayoutA():
	cmds.columnLayout('MSG2_branchSetup.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_branchSetup.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	