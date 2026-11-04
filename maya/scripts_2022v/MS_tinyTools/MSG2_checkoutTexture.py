# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_P4Lib.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import subprocess

import s2000_tools.MS_lib.MSG2_P4Lib as MSG2_P4Lib
reload(MSG2_P4Lib)

def checkoutTexture():
	if cmds.checkBox('EnableConfirmDialog',q=True,v=True):
		MSG2_P4Lib.ENABLE_DIALOG=True
	else:
		MSG2_P4Lib.ENABLE_DIALOG=False

	PATHES=[]
	FTN=cmds.ls(sl=True,type='file')
	for EACH in FTN:
		FTPATH=cmds.getAttr(EACH+'.fileTextureName')
		PATHES.append(FTPATH)
	MSG2_P4Lib.P4CheckOut(PATHES)

#################
# UI
#################

def LayoutA():
	cmds.columnLayout('MSG2_P4Lib.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_P4Lib.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.checkBox('EnableConfirmDialog',l='Enable ConfirmDialog',v=True)
	cmds.button('checkoutTexture',c=lambda *args:checkoutTexture())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	