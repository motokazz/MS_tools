# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_lockComponent
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds
	
def lockComponent():
	COMP=cmds.filterExpand(sm=[31,32,34])
	for EACH in COMP:
		cmds.setAttr(EACH,lock=True)
	
def unlockComponent():
	COMP=cmds.filterExpand(sm=[31,32,34])
	for EACH in COMP:
		cmds.setAttr(EACH,lock=False)
	
def layoutA(
	LABEL='MS_lockComponent'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.rowLayout(nc=2)
	cmds.button(w=100,bgc=[0.8,0.6,0.6],l=u'lock',c=lambda *args:lockComponent())
	cmds.button(w=100,bgc=[0.6,0.8,0.6],l=u'unlock',c=lambda *args:unlockComponent())
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_lockComponent_main_window',q=True,ex=True):
		cmds.deleteUI('MS_lockComponent_main_window')
	cmds.window('MS_lockComponent_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_lockComponent_main_window')
	

UI()