# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_superScreenShot.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

#追加モジュール
import MS_swatchMaker
reload(MS_swatchMaker)

def searchNodes(SEARCHWORD=''):
	SEL = cmds.ls(l=True,tr=True)
	SEARCHED=[]
	for each in SEL:
		if SEARCHWORD in each:
			SEARCHED.append(each)
	return SEARCHED
			

def main():
	MS_swatchMaker.objSwatchMaker( [each] , self.filePath , self.fileName , RENDER_NAME = 'vp2Renderer' , RENDER_OVERRIDE = 'G2Renderer' , REFFERENCE_MODEL = 'D:/Projects/Gravite2/assets/bg/model/kitten_notex.atgi')

def LayoutA():
	cmds.columnLayout('MS_superScreenShot.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_superScreenShot.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	