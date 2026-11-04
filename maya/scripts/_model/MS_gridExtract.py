# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_gridExtract.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds



import math
#################
# 分割数指定
#################
def main():
	SEL=cmds.ls(sl=True,l=True)
	BB=cmds.xform(SEL[0],q=True,bb=True,ws=True)
	BBC=[(BB[0]+BB[3])*0.5,(BB[1]+BB[4])*0.5,(BB[2]+BB[5])*0.5]

	SUB=cmds.intSliderGrp('MS_gridExtract_Subdivision',q=True,v=True)	
	if cmds.checkBox('MS_gridExtract_X',q=True,v=True):
		subX(SUB,BBCenter=BBC)
	if cmds.checkBox('MS_gridExtract_Y',q=True,v=True):
		subY(SUB,BBCenter=BBC)
	if cmds.checkBox('MS_gridExtract_Z',q=True,v=True):
		subZ(SUB,BBCenter=BBC)
	if cmds.checkBox('MS_gridExtract_separate',q=True,v=True):
		cmds.polySeparate()
	
def subX(SUB,BBCenter=[0,0,0]):
	BB=cmds.xform(q=True,bb=True,ws=True)
	VX=(BB[3]-BB[0])/SUB
	for txi in range(SUB):
		tx=(txi-(SUB*0.5))*VX
		cmds.polyCut(ch=False
			,cutPlaneCenter=[BBCenter[0]+tx,BBCenter[1],BBCenter[2]]
			,cutPlaneRotate=[0,90,0]
			,extractFaces=True
			)

def subY(SUB,BBCenter=[0,0,0]):
	BB=cmds.xform(q=True,bb=True,ws=True)
	VY=(BB[4]-BB[1])/SUB
	for tyi in range(SUB):
		ty=(tyi-(SUB*0.5))*VY
		cmds.polyCut(ch=False
			,cutPlaneCenter=[BBCenter[0],BBCenter[1]+ty,BBCenter[2]]
			,cutPlaneRotate=[90,0,0]
			,extractFaces=True
			)
def subZ(SUB,BBCenter=[0,0,0]):
	BB=cmds.xform(q=True,bb=True,ws=True)
	VZ=(BB[5]-BB[2])/SUB
	for tzi in range(SUB):
		tz=(tzi-(SUB*0.5))*VZ
		cmds.polyCut(ch=False
			,cutPlaneCenter=[BBCenter[0],BBCenter[1],BBCenter[2]+tz]
			,cutPlaneRotate=[0,0,0]
			,extractFaces=True
			)

#################
# サイズ指定
#################

def volumeDivide():
	SEL=cmds.ls(sl=True,l=True)
	BB=cmds.xform(SEL[0],q=True,bb=True,ws=True)

	BBC=[(BB[0]+BB[3])*0.5,(BB[1]+BB[4])*0.5,(BB[2]+BB[5])*0.5]
	BBV=[(BB[3]-BB[0]),(BB[4]-BB[1]),(BB[5]-BB[2])]


	VOLUME=cmds.floatSliderGrp('MS_gridExtract_volumeDivide',q=True,v=True)	

	SUBX=int(math.floor(BBV[0]/VOLUME)-1)
	SUBY=int(math.floor(BBV[1]/VOLUME)-1)
	SUBZ=int(math.floor(BBV[2]/VOLUME)-1)

	PLANE_ROTATE=[[0,90,0,1,0,0],[90,0,0,0,1,0],[0,0,0,0,0,1]]#0~2=cutPlaneRotate 3~5=DivideShiftValue

	for EPR in PLANE_ROTATE:
		CHECK=True

	#X
	if not SUBX<0:
		for EACH in range(SUBX+1):
			VAR=VOLUME*(EACH-SUBX*0.5)
			cmds.polyCut(ch=False,cutPlaneCenter=[BBC[0]+VAR,BBC[1],BBC[2]],cutPlaneRotate=[0,90,0],extractFaces=True,extractOffset=[0,0,0])
	#Y
	if not SUBY<0:
		for EACH in range(SUBY+1):
			VAR=VOLUME*(EACH-SUBY*0.5)
			cmds.polyCut(ch=False,cutPlaneCenter=[BBC[0],BBC[1]+VAR,BBC[2]],cutPlaneRotate=[90,0,0],extractFaces=True,extractOffset=[0,0,0])
	#Z
	if not SUBZ<0:
		for EACH in range(SUBZ+1):
			VAR=VOLUME*(EACH-SUBZ*0.5)
			cmds.polyCut(ch=False,cutPlaneCenter=[BBC[0],BBC[1],BBC[2]+VAR],cutPlaneRotate=[0,0,0],extractFaces=True,extractOffset=[0,0,0])

	if cmds.checkBox('MS_gridExtract_separate',q=True,v=True):
		cmds.polySeparate()



def LayoutA():
	cmds.columnLayout('MS_gridExtract.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_gridExtract.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	#
	cmds.rowLayout(nc=3)
	cmds.checkBox('MS_gridExtract_X',l='X',v=True)
	cmds.checkBox('MS_gridExtract_Y',l='Y',v=True)
	cmds.checkBox('MS_gridExtract_Z',l='Z',v=True)
	cmds.setParent('..')
	cmds.checkBox('MS_gridExtract_separate',l='separate',v=True)
	#
	cmds.intSliderGrp('MS_gridExtract_Subdivision',l='Subdivision',f=True,v=1)	
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.floatSliderGrp('MS_gridExtract_volumeDivide',l='volume',f=True,min=1,max=1000000,v=1000.0)
	cmds.button(l='do',c=lambda *args:volumeDivide())
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	
