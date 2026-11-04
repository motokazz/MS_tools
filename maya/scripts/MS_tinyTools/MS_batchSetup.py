# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_batchSetup.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import MS_batchScene
reload(MS_batchScene)

import MS_G2BGSceneSetup
reload(MS_G2BGSceneSetup)

def newPreCommand():
	try:
		print 'new'
		if cmds.objExists('root'):
			cmds.delete('root')
			print 'root deleted'

		cmds.select(all=True)
		NODES = cmds.ls(tr=True,sl=True)
		cmds.select(NODES,r=True)
	except:
		pass

	MS_G2BGSceneSetup.G2BGSceneSetup()



def main():
	MS_batchScene.preCommand = newPreCommand
	MS_batchScene.UI()

def LayoutA():
	cmds.columnLayout('MS_batchSetup_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_batchSetup',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	