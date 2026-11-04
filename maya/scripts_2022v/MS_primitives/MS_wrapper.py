# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_wrapper
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import MS_primitives.MS_primitives as MS_primitives
reload(MS_primitives)

import MS_primitives.MS_getBestBB as MS_getBestBB
reload(MS_getBestBB)

import _lib.MS_polyUnite as MS_polyUnite
reload(MS_polyUnite)


def TA():

	TARGET=cmds.ls(sl=True,l=True)[0]
	cmds.makeIdentity(TARGET,a=True,s=True)
	SEL=cmds.textField('MS_wrapper_targetMeshes',q=True,tx=True).split('<>')

	#
	if cmds.filterExpand(SEL,sm=34):
		S = cmds.listRelatives(cmds.listRelatives(SEL,p=True,s=True),p=True,type='transform')
		cmds.select(SEL,r=True)
		cmds.hilite(S)
		CO=MS_polyUnite.MS_polyChipOff()
		if len(CO)>1:
			SOURCE=cmds.polyUnite(CO,ch=False)
		else:
			SOURCE=CO
	else:
		SOURCE=dupUnite(SEL)

	S_XYZ = MS_getBestBB.BBCenterByObj(OBJ=SOURCE)
	T_XYZ = MS_getBestBB.BBCenterByObj(OBJ=TARGET)
	
	#dup target
	TEMPMESH=cmds.duplicate(TARGET)
	cmds.xform(TEMPMESH,t=((S_XYZ[0]*2)-T_XYZ[0],(S_XYZ[1]*2)-T_XYZ[1],(S_XYZ[2]*2)-T_XYZ[2]),ws=True)
	cmds.xform(TEMPMESH,s=(1.1,1.1,1.1),ws=True)

	#mergeSource
	UNITED=cmds.polyUnite(SOURCE,TEMPMESH)


	cmds.transferAttributes(UNITED[0],TARGET,pos=1,spa=0,sm=0)

	cmds.delete(TARGET,ch=True)

	#reduce

	REDUCE_TARGET_POLY=cmds.intField('MS_wrapper_reduceTargetPoly',q=True,v=True)

	for i in range(50):
		cmds.polyReduce(TARGET
			,ver=1
			,trm=0
			,p=20
			,vct=0
			,tct=0
			,shp=0
			,keepBorder=1
			,keepMapBorder=0
			,keepColorBorder=0
			,keepFaceGroupBorder=0
			,keepHardEdge=0
			,keepCreaseEdge=0
			,keepBorderWeight=0.75
			,keepMapBorderWeight=0.2
			,keepColorBorderWeight=0.5
			,keepFaceGroupBorderWeight=0.5
			,keepHardEdgeWeight=1
			,keepCreaseEdgeWeight=1
			,useVirtualSymmetry=1
			,symmetryTolerance=0.01
			,sx=0
			,sy=1
			,sz=0
			,sw=0
			,preserveTopology=1
			,keepQuadsWeight=0
			,vertexMapName=""
			,replaceOriginal=1
			,cachingReduce=1
			,ch=0
		)
		if cmds.polyEvaluate(TARGET,v=True)<REDUCE_TARGET_POLY:
			break
	

	cmds.delete(TARGET,ch=True)
	#
	cmds.delete(UNITED,ch=True)
	try:
		cmds.delete(SOURCE,TEMPMESH)
	except:
		pass
	for each in UNITED:
		try:
			cmds.delete(each)
		except:
			pass

	cmds.select(TARGET,r=True)

def dupUnite(SEL):
	DUPED=cmds.duplicate(SEL)
	if len(DUPED)<2:
		return DUPED[0]
	try:
		UNITED=cmds.polyUnite(DUPED)
	except:
		UNITED=DUPED

	cmds.delete(UNITED,ch=True)

	try:
		cmds.delete(DUPED)
	except:
		pass

	return UNITED[0]


def main():

	SEL=cmds.ls(sl=True,dag=True,type='mesh',l=True)
	if not SEL:
		SEL=cmds.ls(sl=True,l=True)

	cmds.textField('MS_wrapper_targetMeshes',tx='<>'.join(SEL),e=True)

	#


	if cmds.filterExpand(sm=34):
		CO=MS_polyUnite.MS_polyChipOff()
		if len(CO)>1:
			UNITED=cmds.polyUnite(CO,ch=False)
		else:
			UNITED=CO
	else:
		UNITED=dupUnite(SEL)

	cmds.select(UNITED,r=True)
	subX=cmds.intField('MS_wrapper_subX',q=True,v=True)
	subY=cmds.intField('MS_wrapper_subY',q=True,v=True)

	mcp=MS_primitives.createPrimitive()
	mcp.scalemode='BBMesure'
	mcp.GetTransform()
	if mcp.obj:
		mcp.axis=[0,1,0]
		mcp.autoAxis()

	mcp.newObject=cmds.polyPlane(
		axis=mcp.axis,
		width=1,
		height=1,
		subdivisionsX = subX,
		subdivisionsY = subY
		)
	mcp.DoTransform()

	cmds.delete(UNITED)

	return mcp.newObject

def LayoutA():
	cmds.columnLayout('MS_wrapper_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_wrapper',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	#
	cmds.text(l=u'１・選択したオブジェクトからターゲットメッシュリスト作成＆最適プレーン作成')
	cmds.rowLayout(nc=4,cw4=(150,50,50,100))
	cmds.text(l=u'最適プレーンの分割　X・Y',w=150)
	cmds.intField('MS_wrapper_subX',v=100,w=50)
	cmds.intField('MS_wrapper_subY',v=100,w=50)
	cmds.button(l='CREATE PLANE',c=lambda *args:main(),w=100)
	cmds.setParent('..')
	cmds.text(l=u'ターゲットメッシュ群')
	cmds.textField('MS_wrapper_targetMeshes',tx='',en=False)

	#
	cmds.text(l=u'２・最適プレーンをターゲットメッシュに沿わせる')

	cmds.rowLayout(nc=3,cw3=(150,100,100))
	cmds.text(l=u'頂点削減目標',w=150)
	cmds.intField('MS_wrapper_reduceTargetPoly',v=1000)
	cmds.button(l='WRAP!',c=lambda *args:TA(),w=100)
	cmds.setParent('..')


	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_wrapper_window',q=True,ex=True):
		cmds.deleteUI('MS_wrapper_window')
	cmds.window('MS_wrapper_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_wrapper_window')
	