# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_lambert1_control.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

def stepScale():
	cmds.scale(r=True)

def assignAndWorld():
	cmds.parent(w=True)
	cmds.hyperShade(a='lambert1')

def assign():
	cmds.hyperShade(a='lambert1')

def colorChange(R=0.5,G=0.5,B=0.5,A=0):
	cmds.setAttr('lambert1.colorR',R)
	cmds.setAttr('lambert1.colorG',G)
	cmds.setAttr('lambert1.colorB',B)
	cmds.setAttr('lambert1.transparencyR',A)
	cmds.setAttr('lambert1.transparencyG',A)
	cmds.setAttr('lambert1.transparencyB',A)


def LayoutA():
	cmds.columnLayout('MS_lambert1_control.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_lambert1_control.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.gridLayout(nc=6)
	cmds.button(l='default',c=lambda *args:colorChange())
	cmds.button(l='red',bgc=[1,0,0],c=lambda *args:colorChange(1,0,0,0))
	cmds.button(l='invisible',c=lambda *args:colorChange(A=0))
	cmds.text(l='')
	cmds.button(l='assign',c=lambda *args:assign())
	cmds.button(l='a&w',bgc=[1,1,1],c=lambda *args:assignAndWorld())

	cmds.setParent('..')
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	