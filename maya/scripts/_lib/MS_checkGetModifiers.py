# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_checkGetModifiers.py
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds

def test():
	mods = cmds.getModifiers()
	print 'Modifiers are:'
	if (mods & 1) > 0: print ' Shift'
	if (mods & 4) > 0: print ' Ctrl'
	if (mods & 8) > 0: print ' Alt'
	if (mods & 16): print ' Command/Windows'



def LayoutA():
	cmds.columnLayout('MS_tools_mainLayout',adj=True)
	cmds.button(c=lambda *args:test())
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
UI()