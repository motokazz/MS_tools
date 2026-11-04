# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_oppositeKill
# 説明
#			シーン内すべてのオブジェクトのoppositeフラグをチェックして、入っているものは外して法線を反転します。
# 作成日
#			
########################################

import maya.cmds as cmds

#execCheckList
#import MS_module.MS_execCheck
#reload(MS_module.MS_execCheck)
#MS_module.MS_execCheck.execCheckSafe('MS_oppositeKill.py')

def do():
	OBJ=cmds.ls(typ='mesh')
	for EACH in OBJ:
		if cmds.getAttr(EACH+'.opposite'):
			cmds.setAttr(EACH+'.opposite',0)
			cmds.polyNormal(EACH,normalMode=0,userNormalMode=0,ch=0)

def layoutA(
	LABEL='MS_oppositeKill'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.text(l=u'シーン内すべてのオブジェクトの\noppositeフラグをチェックして、\n入っているものは外して法線を反転します。')
	cmds.button(w=WIDTH-4,l=u'do',c=lambda *args:do())
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_oppositeKill_main_window',q=True,ex=True):
		cmds.deleteUI('MS_oppositeKill_main_window')
	cmds.window('MS_oppositeKill_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_oppositeKill_main_window')
	


