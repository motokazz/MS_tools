# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_intersect.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds


def main():
	EDG=cmds.filterExpand(sm=32)
	CI = cmds.curveIntersect(EDG[0],EDG[1],tol=1.0)

	if not CI:
		return False

	CIS = CI.split()
	POC = cmds.pointOnCurve(EDG[0],pr=float(CIS[0]),p=True)
	LOC=cmds.spaceLocator()
	cmds.xform(LOC,t=POC,ws=True)


def LayoutA():
	cmds.columnLayout('MS_intersect.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_intersect.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	