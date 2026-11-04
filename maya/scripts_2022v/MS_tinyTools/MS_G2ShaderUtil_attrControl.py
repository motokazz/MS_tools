# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_G2ShaderUtil_attrControl.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds


def setDecalMaskingAll(VAR=False):
	sel = cmds.ls(type='G2_BG_Main')
	for each in sel:
		cmds.setAttr(each+'.decalMasking',VAR)



def LayoutA():
	cmds.frameLayout(l='attrControl',cl=True,cll=True,bgc=[0.4,0.4,0.4])
	cmds.separator()
	#
	cmds.gridLayout(nc=3,cw=70)
	cmds.text(l='decalMasking')
	cmds.button(l='on',c=lambda *args:setDecalMaskingAll(True))
	cmds.button(l='off',c=lambda *args:setDecalMaskingAll(False))
	cmds.setParent('..')
	#
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	