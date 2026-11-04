# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_selectByScaleAttr
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds


def main():
	RET=[]

	LIMIT=cmds.intField('MSG2_selectByScaleAttr_threshould',q=True,v=True)

	SEL=cmds.ls(sl=True,type='transform',l=True)
	for each in SEL:
		SHAPE=cmds.listRelatives(each,s=True,f=True)
		print SHAPE
		if not SHAPE:
			continue
		elif not cmds.nodeType(SHAPE[0])=='mesh':
			continue
			
		if cmds.getAttr(each+'.sx')>LIMIT or cmds.getAttr(each+'.sy')>LIMIT or cmds.getAttr(each+'.sz')>LIMIT:continue
		
		RET.append(each)
		
	if RET:
		cmds.select(RET,r=True)

def LayoutA():
	cmds.columnLayout('MSG2_selectByScaleAttr_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_selectByScaleAttr',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.intField('MSG2_selectByScaleAttr_threshould',v=50)
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	