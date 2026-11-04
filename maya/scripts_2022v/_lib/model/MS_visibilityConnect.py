# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_visibilityConnect
# 説明
#			シェイプノードのvisibilityをTransformノードのvisibilityとリンクする
#			Transformノードのvisibilityを変更すると、ShapeノードのVisibilityも同様に変更されるようになる。
# 作成日\n#			
########################################

import maya.cmds as cmds
	
	
def disconnectAll():
	SHAPE=cmds.ls(typ='mesh',l=True)
	for each in SHAPE:
		NODE=cmds.listRelatives(each,p=True,type='transform',f=True)
		cmds.disconnectAttr(NODE[0]+'.visibility',each+'.visibility')
		cmds.setAttr(each+'.visibility',True)
	
def connectAll():
	SHAPE=cmds.ls(typ='mesh',l=True)
	for each in SHAPE:
		NODE=cmds.listRelatives(each,p=True,type='transform',f=True)
		cmds.connectAttr(NODE[0]+'.visibility',each+'.visibility',f=True)
	
def connectSelection():
	NODE=cmds.ls(sl=True,typ='transform',l=True)
	for each in NODE:
		SHAPE=cmds.listRelatives(each,s=True,f=True)
		cmds.connectAttr(each+'.visibility',SHAPE[0]+'.visibility',f=True)
	
def layoutA(
	LABEL='MS_visibilityConnect'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout(ann=u'シェイプノードのvisibilityをTransformノードのvisibilityとリンクする\nTransformノードのvisibilityを変更すると、ShapeノードのVisibilityも同様に変更されるようになる。')
	
	cmds.text(l=LABEL)

	cmds.button(w=WIDTH-4,l=u'connect Selection',c=lambda *args:connectSelection())
	cmds.button(w=WIDTH-4,l=u'disconnect Selection',c=lambda *args:disconnectSelection())
	cmds.separator(w=120)
	cmds.button(w=WIDTH-4,l=u'connect All',c=lambda *args:connectAll())
	cmds.button(w=WIDTH-4,l=u'disconnect All',c=lambda *args:disconnectAll())
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_visibilityConnect_main_window',q=True,ex=True):
		cmds.deleteUI('MS_visibilityConnect_main_window')
	cmds.window('MS_visibilityConnect_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_visibilityConnect_main_window')
	

