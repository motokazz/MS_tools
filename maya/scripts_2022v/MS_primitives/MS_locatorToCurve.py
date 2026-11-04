# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_locatorToCurve
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

def selectCurve(OBJ=[]):
	#選択カーブを返す
	#ポリゴンコンポーネントはカーブ化する
	
	#
	if not OBJ:
		return False
	#
	SHAPE=cmds.listRelatives(OBJ,s=True,f=True)
	if cmds.nodeType(SHAPE) == 'nurbsCurve':
		CURVE=OBJ
	else:
		#コンポーネントをカーブ化
		EDG=cmds.filterExpand(OBJ,sm=32)
		if not EDG:
			EDG=cmds.polyListComponentConversion(OBJ,te=True)
		cmds.select(EDG,r=True)
		CURVE=cmds.polyToCurve(form=2,degree=1)
	return CURVE

def locatorToCurve(QUANTITY=10,FLOW=False,DETAIL=100):
	#パスアニメーションを利用した配置
	#回転値取得可能
	#flow変形可能
	#

	QUANTITY=cmds.intField('MS_locatorToCurve_locatorQuantity',q=True,v=True)

	SEL=cmds.ls(sl=True)
	LOC=cmds.spaceLocator()
	
	CUV = selectCurve(SEL)
	
	RCV=cmds.duplicate(CUV)
	cmds.delete(CUV)
	
	cmds.rebuildCurve(RCV,keepRange=0,rt=0,s=DETAIL)

	MP=cmds.pathAnimation(RCV,LOC[0]
		,fractionMode=True
		,followAxis='x'
		,upAxis='y'
		,worldUpType='scene'
		,inverseUp=False
		,inverseFront=True
		)

	if FLOW:
		cmds.flow(LOC[0])
	#パスアニメーション削除
	cmds.cutKey(MP,cl=True,at="u")
	varstep=1.0/(QUANTITY-1)

	for i in range(0,QUANTITY):
		var=varstep*i
		cmds.setAttr(MP+'.uValue',var)
		XT=cmds.xform(LOC[0],q=True,t=True,ws=True)
		XR=cmds.xform(LOC[0],q=True,ro=True,ws=True)
		XS=cmds.xform(LOC[0],q=True,s=True,ws=True)

		DUPED=cmds.duplicate(LOC[0])
		cmds.xform(DUPED[0],t=[XT[0],XT[1],XT[2]],ro=[XR[0],XR[1],XR[2]],s=[XS[0],XS[1],XS[2]])

	cmds.delete(MP)
	cmds.delete(RCV)
	cmds.delete(LOC)



def main(NODE=[],QUANTITY=10,DETAIL=100):
	#pointPositionを利用した配置：
	NODE=cmds.ls(sl=True)
	
	OBJ=cmds.duplicate(NODE)
	cmds.rebuildCurve( OBJ,keepRange=0,rt=0,s=DETAIL)
	
	spans=1.0
	stepValue=(spans/(QUANTITY-1))
	
	i=0
	while(i<QUANTITY):
		LOC=cmds.pointPosition(OBJ[0]+'.u['+str(stepValue*i)+']',w=True)
		LOCNAME=cmds.spaceLocator()
		cmds.xform(LOCNAME[0],t=[LOC[0],LOC[1],LOC[2]],ws=True)
		RENAMED=cmds.rename(LOCNAME[0],'MS_locatorToCurve')
		i+=1
	
	cmds.delete(OBJ)



def LayoutA():
	cmds.columnLayout('MS_locatorToCurve_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_locatorToCurve',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.gridLayout(nc=2,cw=100)
	cmds.text(l='Quantity')
	cmds.intField('MS_locatorToCurve_locatorQuantity',v=10)
	cmds.button(l='locatorToCurve',c=lambda *args:locatorToCurve())
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')

#UI()


