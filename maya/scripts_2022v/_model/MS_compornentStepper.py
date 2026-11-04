# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_compornentStepper.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import random


#COM
def add(a,b):
	c=a+b
	return c

def minus(a,b):
	c=a-b
	return c

def multi(a,b):
	c=a*b
	return c

def divide(a,b):
	c=0
	if a or b:
		c=a/b
	return c

def randomf(a,b):
	c=random.uniform(-b,b)
	return a+c
	
	
def ret_a(a,b):
	return a

def interp(a,b,quantity,NUM):
	c=a-(((a-b)/quantity)*(NUM))
	return c

def defcom(MODE):#コマンド定義
	if MODE=='ret_a':
		COM=ret_a
	if MODE=='add':
		COM=add
	if MODE=='minus':
		COM=minus
	if MODE=='multi':
		COM=multi
	if MODE=='divide':
		COM=divide
	if MODE=='randomf':
		COM=randomf
	if MODE=='randoms':
		COM=add
	return COM
	
####

def main(MODE='add',ATTR='',G_MODE='',DIR=[1,0,0]):
	#
	MAG=1
	mods = cmds.getModifiers()
	if (mods & 1) > 0: MAG=10 #shift
	if (mods & 4) > 0: MAG=0.5 #ctrl
	if (mods & 8) > 0: MAG=2 #alt
	
	#
	VAR=cmds.floatField('MS_compornentStepper_STEP',q=True,v=True)
	MAG *= VAR
	
	#FACE
	FACE=cmds.filterExpand(sm=34,fp=True)
	if FACE:
		cmds.polyMoveFacet( lt=[ DIR[0] * MAG , DIR[1] * MAG , DIR[2] * MAG ])
		return

	#EDGE
	EDGE=cmds.filterExpand(sm=32,fp=True)
	if EDGE:
		cmds.polyMoveEdge( lt=[DIR[0]*MAG,DIR[1]*MAG,DIR[2]*MAG])
		return
	#

	PRECOMP=cmds.polyListComponentConversion(tv=True)
	COMPORNENT=cmds.filterExpand(PRECOMP,sm=[31,32,34,35],fp=True)

	VTX=cmds.polyListComponentConversion(tv=True)
	VTX=cmds.filterExpand(VTX,sm=31,fp=True)
	
	if not VTX:
		print ('not')
		return
	
	#RANDOMS用乱数発生
	RANDOMS=[]
	for X in range(len(VTX)):
		RANDOMS.append(random.uniform(-VAR,VAR))

	if ATTR=='normal':
		for EACH_VTX in VTX:
			cmds.moveVertexAlongDirection(EACH_VTX,n=VAR*DIR[0]*MAG)
	else:
		#cmds.polyMoveVertex(t=(DIR),ch=False)
		for EACH_VTX in VTX:
			cmds.moveVertexAlongDirection(EACH_VTX,d=(DIR),m=VAR*MAG)




def LayoutA():
	cmds.columnLayout('MS_compornentStepper.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_compornentStepper.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.floatField('MS_compornentStepper_STEP',v=1)
	cmds.gridLayout(nc=4)
	cmds.button(l='')
	cmds.button(l='Z+',c=lambda *args:main('add','pntz',DIR=[0,0,1]))
	cmds.button(l='')
	cmds.button(l='Y+',c=lambda *args:main('add','pnty',DIR=[0,1,0]))

	cmds.button(l='X-',c=lambda *args:main('minus','pntx',DIR=[-1,0,0]))
	cmds.button(l='')
	cmds.button(l='X+',c=lambda *args:main('add','pntx',DIR=[1,0,0]))
	cmds.button(l='')

	cmds.button(l='')
	cmds.button(l='Z-',c=lambda *args:main('minus','pntz',DIR=[0,0,-1]))
	cmds.button(l='')
	cmds.button(l='Y-',c=lambda *args:main('minus','pnty',DIR=[0,-1,0]))


	cmds.button(l='N-',c=lambda *args:main('minus','normal',DIR=[-1,0,0]))
	cmds.button(l='N+',c=lambda *args:main('add','normal',DIR=[1,0,0]))
	cmds.setParent('..')
	cmds.separator()

	cmds.text(l='shift+   10x')
	cmds.text(l='alt+   2x')
	cmds.text(l='ctrl+   0.5x')

	cmds.setParent('..')

def UI():
	if cmds.window('MS_compornentStepper_window',q=True,ex=True):
		cmds.deleteUI('MS_compornentStepper_window')
	cmds.window('MS_compornentStepper_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_compornentStepper_window')
	