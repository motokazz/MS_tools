# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_hull
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel

import _lib.MS_polyUnite as MS_polyUnite
reload(MS_polyUnite)


#LOAD PLUGIN
#if not cmds.pluginInfo("hctMayaSceneExport.mll",loaded=1,q=1):
#	cmds.loadPlugin("hctMayaSceneExport.mll")


def raducer(TARGET=[],REDUCE_TARGET_POLY=15):

	#REDUCE_TARGET_POLY=cmds.intField('MSG2_hull_reduceTargetPoly',q=True,v=True)

	for i in range(50):
		
		if cmds.polyEvaluate(TARGET,v=True)<=REDUCE_TARGET_POLY:
			break
	
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


	cmds.delete(TARGET,ch=True)
	#




def main(TARGETS=[],MAX_VTX=10,DELFLAG=False,REDUCE_TARGET_POLY=0):
	mods = cmds.getModifiers()
	if (mods & 4) > 0:#+ctrl
		DELFLAG=True
	#
	
	FIRST_SEL=cmds.ls(type='transform',l=True)

	#
	ORGTARGETS=TARGETS
	COMPORNENT=False
	if cmds.nodeType(TARGETS[0])=='mesh':
		CO=MS_polyUnite.MS_polyChipOff()
		if len(CO)>1:
			TARGETS=cmds.polyUnite(CO,ch=False)
		else:
			TARGETS=CO
		COMPORNENT=True

	MAX_VTX=cmds.intField('MSG2_hull_HULL_MAX_VTX',q=True,v=True)
	for each in TARGETS:
		cmds.select(each,r=True)
		mel.eval('hkCmdCreateConvexHull -mv %s'%MAX_VTX)

	if COMPORNENT:
		cmds.delete(TARGETS)

	if DELFLAG:
		cmds.delete(ORGTARGETS)

	# 出来たHULLを選択

	NEW=list(set(cmds.ls(type='transform',l=True))-set(FIRST_SEL))
	if REDUCE_TARGET_POLY:
		for each in NEW:
			raducer(each,REDUCE_TARGET_POLY=REDUCE_TARGET_POLY)
	cmds.select(NEW,r=True)


def LayoutA():
	cmds.columnLayout('MSG2_hull_mainLayout',adj=True)
	cmds.separator()
	#cmds.text(l='MSG2_hull',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.rowLayout(nc=3,cw3=[50,50,50])
	cmds.text(l='base count')
	cmds.intField('MSG2_hull_HULL_MAX_VTX',v=64)
	cmds.button(l='HULL',c=lambda *args:main(cmds.ls(sl=True,l=True)))

	#cmds.button(l='SWAP',c=lambda *args:main(cmds.ls(sl=True,l=True),DELFLAG=True))
	cmds.setParent('..')

	cmds.text(l='SWAP mode = ctrl+button')

	#
	cmds.separator()
	cmds.text(l='reduce target',bgc=[0.9,0.9,0.9])
	#cmds.intField('MSG2_hull_reduceTargetPoly',v=12)

	cmds.gridLayout(nc=4)
	cmds.button(l='8',c=lambda *args:main(cmds.ls(sl=True,l=True),REDUCE_TARGET_POLY=8))
	cmds.button(l='12',c=lambda *args:main(cmds.ls(sl=True,l=True),REDUCE_TARGET_POLY=12))
	cmds.button(l='16',c=lambda *args:main(cmds.ls(sl=True,l=True),REDUCE_TARGET_POLY=16))
	cmds.button(l='20',c=lambda *args:main(cmds.ls(sl=True,l=True),REDUCE_TARGET_POLY=20))
	cmds.button(l='24',c=lambda *args:main(cmds.ls(sl=True,l=True),REDUCE_TARGET_POLY=24))
	cmds.button(l='28',c=lambda *args:main(cmds.ls(sl=True,l=True),REDUCE_TARGET_POLY=28))
	cmds.button(l='32',c=lambda *args:main(cmds.ls(sl=True,l=True),REDUCE_TARGET_POLY=32))
	cmds.button(l='36',c=lambda *args:main(cmds.ls(sl=True,l=True),REDUCE_TARGET_POLY=36))
	cmds.setParent('..')

	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MSG2_hull_window',q=True,ex=True):
		cmds.deleteUI('MSG2_hull_window')
	cmds.window('MSG2_hull_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MSG2_hull_window')
	