# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_locator
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds


def pivotToComponent():
	OBJ=cmds.ls(o=True,hl=True)
	CONP=cmds.filterExpand(ex=True,sm=(31,32,34,35,47))
	if not CONP:
		return
	print CONP
	BBOX=cmds.polyEvaluate(CONP,bc=True)
	TRN=[]
	TRN.append((BBOX[0][0]+BBOX[0][1])*0.5)
	TRN.append((BBOX[1][0]+BBOX[1][1])*0.5)
	TRN.append((BBOX[2][0]+BBOX[2][0])*0.5)
	
	for EACH in OBJ:
		cmds.xform(EACH,ws=True,piv=TRN)


def create():
	CONP=cmds.filterExpand(ex=True,sm=(31,32,34,35,47))
	if not CONP:
		CONP=cmds.ls(sl=True)
	for EACH in CONP:
		TRN=cmds.xform(EACH,q=True,ws=True,t=True)
		LOC=cmds.spaceLocator()
		cmds.xform(LOC[0],t=TRN)
		cmds.rename(LOC[0],'ms_locator')



def layoutA(
	LABEL='MS_locator'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.button(w=150,l=u'create',c=lambda *args:create())
	cmds.button(w=150,l=u'pivotToComponent',c=lambda *args:pivotToComponent())
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_locator_main_window',q=True,ex=True):
		cmds.deleteUI('MS_locator_main_window')
	cmds.window('MS_locator_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_locator_main_window')
	

