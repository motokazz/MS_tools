# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_lmuv
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds

#LOAD PLUGIN
if not cmds.pluginInfo("LMUVFitter.mll",loaded=1,q=1):
	cmds.loadPlugin("D:/MS_tools/maya/plug-ins/LMUVFitter.mll")

def main():
	pass

def LayoutA():
	cmds.frameLayout('MS_lmuv_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_lmuv',cll=True,cl=False)
	cmds.columnLayout('MS_lmuv_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_lmuv',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_lmuv_window',q=True,ex=True):
		cmds.deleteUI('MS_lmuv_window')
	cmds.window('MS_lmuv_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_lmuv_window')
	