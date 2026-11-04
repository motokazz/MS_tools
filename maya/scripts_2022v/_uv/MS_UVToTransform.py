# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_UVToTransform.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

def UVAverage(Value):
	u,v=0,0
	NUM=len(Value)/2
	i=0
	for i in range(NUM):
		u+=Value[i*2]
		v+=Value[i*2+1]
	return u/NUM,v/NUM
	


def main():
	SEL=cmds.ls(sl=True)
	for each in SEL:
		cmds.select(each,r=True)
		UL=cmds.polyListComponentConversion(each,tuv=True)
		UValue = cmds.polyEditUV(UL,q=True,r=False)
		UVV = UVAverage(UValue)
		cmds.xform(each,t=[(UVV[0]-0.5)*500,0,-(UVV[1]-0.5)*500],ws=True)


def LayoutA():
	cmds.columnLayout('MS_UVToTransform_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_UVToTransform',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	