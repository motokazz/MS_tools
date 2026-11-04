# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_pivotSetter
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds

import MS_primitives
reload(MS_primitives)

import MS_getBestBB
reload(MS_getBestBB)

import MS_resetPivot
reload(MS_resetPivot)

def pivotToComponent():
	COMP=cmds.ls(sl=True)
	OBJ=cmds.ls(o=True,hl=True)
	for EACH in OBJ:
		cmds.xform(EACH,ws=True,piv=MS_getBestBB.bbCenter(COMP,MODE='pivot'))
		MS_resetPivot.reset_exe(EACH)
		cmds.makeIdentity(EACH,a=True,s=True)


def pivotSetter(MODE='center',CENTER_RESETTER=True):

	CENTER_RESETTER=cmds.checkBox('MS_primitives_pivotSetter_CENTER_RESETTER',q=True,v=True)
	COMP=cmds.ls(sl=True)
	OBJ=cmds.ls(o=True,hl=True)
	
	if not OBJ:
		OBJ=cmds.ls(sl=True)

	for EACH in OBJ:
		
		if MODE=='pivot':
			cmds.xform(EACH,ws=True,piv=MS_getBestBB.bbCenter(COMP,MODE))
		else:
			cmds.xform(EACH,ws=True,piv=MS_getBestBB.bbCenter(EACH,MODE))
		
		if CENTER_RESETTER:
			CR=MS_getBestBB.centerResetter(EACH)
		
		MS_resetPivot.reset_exe(EACH)
		cmds.makeIdentity(EACH,a=True,s=True)
		
	cmds.select(OBJ,r=True)


def rotToCompornentNormal():#ローテーションを選択コンポーネントの法線方向に合わせる
	
	SEL=cmds.ls(hl=True,l=True)
	COMP=cmds.filterExpand(sm=[31,32,34])
	for each in SEL:
		PARENT=cmds.listRelatives(each,p=True,f=True)
		
		#TRN=cmds.xform(COMP[0],q=True,t=True,ws=True)
		BB=cmds.polyEvaluate(COMP[0],bc=True)

		TX=(BB[0][1]+BB[0][0])*0.5
		TY=(BB[1][1]+BB[1][0])*0.5
		TZ=(BB[2][1]+BB[2][0])*0.5

		LOC=cmds.spaceLocator()
		cmds.xform(LOC[0],t=[TX,TY,TZ],ws=True)
		CONST = cmds.normalConstraint(COMP,LOC[0],weight=1,aimVector=(0,1,0),upVector=(0,1,0),worldUpType='vector',worldUpVector=(0,1,0))

		cmds.delete(CONST)
		

		PARENTED=cmds.parent(each,LOC)
		cmds.makeIdentity(PARENTED,r=True,a=True)
		if PARENT:
			cmds.parent(PARENTED,PARENT)
		else:
			cmds.parent(PARENTED,w=True)
			
		cmds.delete(LOC)


def rotToBestBB():
	SEL=cmds.ls(sl=True,l=True)
	for each in SEL:
		
		PARENT=cmds.listRelatives(each,p=True,f=True)
		cmds.select(each,r=True)
		LOC=MS_primitives.MS_locator()

		PARENTED=cmds.parent(each,LOC)
		cmds.makeIdentity(PARENTED,r=True,a=True)
		if PARENT:
			cmds.parent(PARENTED,PARENT)
		else:
			cmds.parent(PARENTED,w=True)
			
		cmds.delete(LOC)

def componentRotToBestBB():
	HIL=cmds.ls(hl=True,l=True)
	SEL=cmds.ls(sl=True,l=True)
	LOC=MS_primitives.MS_locator()
	RX=cmds.getAttr(LOC[0]+'.rx')
	RY=cmds.getAttr(LOC[0]+'.ry')
	RZ=cmds.getAttr(LOC[0]+'.rz')
	cmds.delete(LOC)

	cmds.select(SEL,r=True)
	cmds.hilite(HIL)
	cmds.manipPivot(o=[ RX , RY , RZ ])

def main():
	pass


def LayoutA(
	LABEL='pivotSetter'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.iconTextButton( style='iconAndTextHorizontal', image1='menuIconModify.png', label='pivotToComponent',c=lambda *args:pivotToComponent() )
	cmds.rowLayout(nc=2)#row1
	
	cmds.columnLayout()#column1
	cmds.button(label='componentCenter',c=lambda *args:pivotSetter('pivot') )
	
	cmds.gridLayout(nc=3)#grid1
	cmds.text(l='')
	cmds.button(label='Y+',c=lambda *args:pivotSetter('YPositive') )
	cmds.button(label='Z-',c=lambda *args:pivotSetter('ZNegative') )
	cmds.button(label='X-',c=lambda *args:pivotSetter('XNegative') )
	cmds.button(label='CP',c=lambda *args:pivotSetter('center') )
	cmds.button(label='X+',c=lambda *args:pivotSetter('XPositive') )
	cmds.button(label='Z+',c=lambda *args:pivotSetter('ZPositive') )
	cmds.button(label='Y-',c=lambda *args:pivotSetter('YNegative') )
	cmds.button(label='0',c=lambda *args:MS_resetPivot.pivot0() )
	cmds.setParent('..')#grid1
	
	cmds.checkBox('MS_primitives_pivotSetter_CENTER_RESETTER',l='centerResetter',v=True)
	cmds.setParent('..')#column1

	cmds.columnLayout()#column2
	cmds.text(l=u'オブジェクト回転を\n選択コンポーネント法線に\n合わせる')
	cmds.button(label=u'Object Rotation\nFit To\nCompornent Normal',c=lambda *args:rotToCompornentNormal() )
	cmds.text(l=u'オブジェクト回転を\n最適バウンディングボックスに\n合わせる')
	cmds.button(label=u'Object Rotation\nFit To\nbest BB',c=lambda *args:rotToBestBB() )
	cmds.text(l=u'ピボット回転を\n最適バウンディングボックスに\n合わせる\n(コンポーネント選択時)')
	cmds.button(label=u'Pivot Rotation\nFit To\nbest BB',c=lambda *args:componentRotToBestBB() )

	cmds.setParent('..')#column2

	cmds.setParent('..')#row1

	cmds.setParent('..')


def UI():
	if cmds.window('MS_pivotSetter_window',q=True,ex=True):
		cmds.deleteUI('MS_pivotSetter_window')
	cmds.window('MS_pivotSetter_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_pivotSetter_window')
	