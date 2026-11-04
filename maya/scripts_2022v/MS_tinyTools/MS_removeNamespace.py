# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_removeNamespace.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds


def main(NAMESPACECHAR='__'):
	NAMESPACECHAR=cmds.textField('MS_removeNamespace_NamespaceChar',q=True,tx=True)
	OBJS=cmds.ls(l=True)
	for each in reversed(OBJS):
		if NAMESPACECHAR in each:
			TEMP=each.split(NAMESPACECHAR)[-1]
			cmds.rename(each,TEMP)

def LayoutA():
	cmds.columnLayout('MS_removeNamespace_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_removeNamespace.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.text(l='NamespaceChar')
	cmds.textField('MS_removeNamespace_NamespaceChar',tx='__')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')

