# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_autoUV
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel

#LOAD PLUGIN
try:
	if not cmds.pluginInfo("LMUVFitter.mll",loaded=1,q=1):
		cmds.loadPlugin("LMUVFitter.mll")
except:
	cmds.confirmDialog(m=u'LMUVFitter.mllをインストールしてください')

def autoUV(NODES,RESX=512,RESY=512,PAD=1):
	cmds.delete(NODES,ch=True)
	#LMUV
	mel.eval('eval("gdhLMUV -d 0 -rd -max %s %s -name "+"map1"+" -msa 45 -pad %s")'%(RESX,RESY,PAD))

def LayoutA():
	cmds.frameLayout('MS_autoUV_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_autoUV',cll=True,cl=False)
	cmds.columnLayout('MS_autoUV_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_autoUV',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	
	cmds.button(l='autoUV',c=lambda *args:autoUV(cmds.ls(sl=True)))
	
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_autoUV_window',q=True,ex=True):
		cmds.deleteUI('MS_autoUV_window')
	cmds.window('MS_autoUV_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_autoUV_window')
	