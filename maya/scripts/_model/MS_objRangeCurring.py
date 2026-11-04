# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_objRangeCurring
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import s2000_tools.MS_lib.MS_distance as MS_distance
reload(MS_distance)


def grouping():
	
	SEL=cmds.ls(sl=True)
	if not SEL:
		return
	TARGET_A=cmds.textField('originTarget',q=True,tx=True)
	if not TARGET_A:
		return
	TRN=cmds.xform(TARGET_A,q=True,ws=True,t=True)
	ROT=cmds.xform(TARGET_A,q=True,ws=True,ro=True)
	SCL=cmds.xform(TARGET_A,q=True,s=True)
	LOC=cmds.spaceLocator()
	cmds.xform(LOC,ws=True,t=[TRN[0],TRN[1],TRN[2]],ro=[ROT[0],ROT[1],ROT[2]],s=[SCL[0],SCL[1],SCL[2]])
	cmds.parent(SEL,LOC)
	cmds.select(LOC,r=True)
	
def resetPosition():
	SEL=cmds.ls(sl=True)
	cmds.xform(SEL,ws=True,t=[0,0,0],ro=[0,0,0],s=[1,1,1])
	
def do(TARGET_A='',THRESHOULD=0):
	#ditect center target
	if not TARGET_A:
		TARGET_A=cmds.textField('originTarget',q=True,tx=True)
		if not TARGET_A:
			return
	#range threshould
	if not THRESHOULD:
		THRESHOULD=cmds.floatSliderGrp('threshould',q=True,v=True)
		if not THRESHOULD:
			return
		
	OBJ=cmds.ls(type='transform',l=True)
	DELETELIST=[]
	
	# searchable nodes
	CERTAIN_TYPES=[
		'GraviteAtgiLocatorNode'
		,'mesh'
		,'light'
		]
	for EACH in OBJ:
		if EACH==TARGET_A:
			continue
		SHAPE=cmds.listRelatives(EACH,s=True,type=CERTAIN_TYPES)
		if not SHAPE:
			continue
		
		#DISTANCE=MS_distance.distance(TARGET_A,EACH,MODE='pivot')
		DISTANCE=MS_distance.BBdistance(TARGET_A,EACH)
		if DISTANCE<THRESHOULD and not EACH==TARGET_A:
			DELETELIST.append(EACH)
	
	cmds.select(DELETELIST,r=True)
	

def getOriginTarget():
	OBJ=cmds.ls(sl=True,type='transform',l=True)
	if OBJ:
		cmds.textField('originTarget',e=True,tx=OBJ[0])
	
	
	
def layoutA(
	LABEL='MS_objRangeCurring'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.rowLayout(nc=2)
	cmds.textField('originTarget',w=WIDTH-60,tx='')
	cmds.button(l='getOriginTarget',w=80,c=lambda *args:getOriginTarget())
	cmds.setParent('..')
	cmds.floatSliderGrp('threshould',f=True,v=1000,min=100,max=5000,fmn=0.0,fmx=20000,cc=lambda *args:do())
	cmds.button(l='grouping',w=WIDTH,c=lambda *args:grouping())
	cmds.button(l='resetPosition',w=WIDTH,c=lambda *args:resetPosition())
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_objRangeCurring_main_window',q=True,ex=True):
		cmds.deleteUI('MS_objRangeCurring_main_window')
	cmds.window('MS_objRangeCurring_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_objRangeCurring_main_window')
	


