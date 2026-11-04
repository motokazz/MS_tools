# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_polyCut.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds


def main(AXIS='x'):
	TARGETS=[]
	SEEDS=[]

	TARGETS=cmds.ls(sl=True)
	PRESEEDS=cmds.textField('MS_polyCut_seedObjects',q=True,tx=True)
	KEEP_FACES_TOGETHER=cmds.checkBox('MS_polyCut_KeepFacesTogether',q=True,v=True)
	if PRESEEDS:
		SEEDS=PRESEEDS.split(',')

	#ditectAxis
	AXISRO=[0.0,0.0,0.0]
	if AXIS=='x':
		AXISRO=[0,90,0]
	if AXIS=='y':
		AXISRO=[90,0,0]
	if AXIS=='z':
		AXISRO=[0,0,0]

	#EXEC
	if PRESEEDS=='' and KEEP_FACES_TOGETHER :
		cmds.polyCut(TARGETS,df=False,cd=AXIS)
		return

	for EACHTARGET in TARGETS:

		for EACHSEEDS in SEEDS:
			XF=cmds.xform(EACHSEEDS,q=True,t=True,ws=True)
			cmds.polyCut(EACHTARGET,df=False,ro=AXISRO,pc=[XF[0],XF[1],XF[2]])


def storeSeedObjects():
	SEL=cmds.ls(sl=True)
	CONPORNENTS=cmds.filterExpand(sm=[31,32,34,35],ex=True)
	#
	SEEDS=''
	if SEL:
		if len(SEL)>1:
			SEEDS+=','.join(SEL)
		else:
			SEEDS=SEL[0]

	if CONPORNENTS:
		if len(CONPORNENTS)>1:
			SEEDS+=','.join(CONPORNENTS)
		else:
			SEEDS=CONPORNENTS[0]


	cmds.textField('MS_polyCut_seedObjects',e=True,tx=SEEDS)

def clearSeedObjects():
	cmds.textField('MS_polyCut_seedObjects',e=True,tx='')

def LayoutA():
	cmds.columnLayout('MS_polyCut_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_polyCut',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.textField('MS_polyCut_seedObjects')
	cmds.button(l='store seedObjects',c=lambda *args:storeSeedObjects())
	cmds.button(l='clear',c=lambda *args:clearSeedObjects())
	cmds.checkBox('MS_polyCut_KeepFacesTogether',v=True)
	cmds.button(l='x',c=lambda *args:main('x'))
	cmds.button(l='y',c=lambda *args:main('y'))
	cmds.button(l='z',c=lambda *args:main('z'))
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	

UI()
