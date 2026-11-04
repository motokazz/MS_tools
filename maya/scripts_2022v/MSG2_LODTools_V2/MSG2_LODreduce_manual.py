# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_LODreduce.py
# 説明
#			
#			
# 作成日
#			
########################################


import maya.cmds as cmds
import maya.mel as mel

import MS_polyUnite
reload(MS_polyUnite)

import MS_BBfilter
reload (MS_BBfilter)

import MS_getBestBB
reload (MS_getBestBB)


#LOAD PLUGIN
try:
	if not cmds.pluginInfo("LMUVFitter.mll",loaded=1,q=1):
		cmds.loadPlugin("LMUVFitter.mll")
	LMUV_enable=True
except:
	LMUV_enable=False



#################
# CleanUp
#################
def cleanupLaminaFacesAndNonmaifoldGeometry(MESH):
	#LaminaFaces&NonmaifoldGeometry
	cmds.select(MESH,r=True)
	mel.eval('polyCleanupArgList 3 { "0","1","0","0","0","0","0","0","0","10","0","10","0","1e-005","0","1","1" };')

def cleanupFinish(MESH=[]):
	if MESH:
		cmds.select(MESH,r=True)
	mel.eval('polyCleanupArgList 3 { "0","1","0","0","1","1","1","1","0","10","0","1e-005","0","1e-006","0","1","1" };')
	mel.eval('polyCleanupArgList 3 { "0","1","0","0","0","0","0","0","1","1e-005","1","1e-005","1","1e-005","0","1","1" };')

def cleanupPowerful(MESH=[]):
	if MESH:
		cmds.select(MESH,r=True)
	mel.eval('polyCleanupArgList 3 { "0","1","0","0","0","0","0","0","1","1","1","1","1","1e-005","0","1","1" };')

def cleanupEdgeGeometry(MESH=[],SIZE=0.01):
	if MESH:
		cmds.select(MESH,r=True)
	#EdgeWith...GeometryWith...
	mel.eval('polyCleanupArgList 3 { "0","1","0","0","0","0","0","0","1","%s","1","%s","0","1e-005","0","1","1" };'%(SIZE,SIZE))

def deleteUselessUVSet(TARGETS):
	UVS=cmds.polyUVSet(TARGETS,q=True,auv=True)
	if not UVS:
		return
	for each in UVS:
		if not each=='map1':
			cmds.polyUVSet(TARGETS,uvs=each,d=True)

def deleteUselessColorSet(TARGETS):
	CS=cmds.polyColorSet(TARGETS,q=True,acs=True)
	if not CS:
		return
	for each in CS:
		cmds.polyColorSet(TARGETS,cs=each,d=True)


#################
# UTIL
#################

def BBMesure(FACE,MIN=1):
	#ポリゴンバウンディングボックス面積
	BB=cmds.xform(FACE,q=True,bb=True,ws=False)
	X=(BB[3]-BB[0])
	Y=(BB[4]-BB[1])
	Z=(BB[5]-BB[2])

	if X<MIN:X=MIN
	if Y<MIN:Y=MIN
	if Z<MIN:Z=MIN

	RET=(X*Y*Z)
	return RET

#################
# REDUCE
#################

def loopReducer(TARGETS=[]
	,PERCENTAGE=25
	,MS_BBGAP=0.9
	,MS_LOOP_LIMIT=5
	,VCT=1000
	,KEEP_BORDER_WEIGHT=0.5
	,KEEP_MAP_BORDER_WEIGHT=0.5
	,KEEP_COLOR_BORDER_WEIGHT=0
	,KEEP_FACE_GROUP_BORDER_WEIGHT=0
	,KEEP_HARD_EDGE_WEIGHT=0
	,KEEP_CREASE_EDGE_WEIGHT=0
	,USE_VIRTUAL_SYMMETRY=False
	,SYMMETRY_TOLERANCE=0.01
	,SX=0
	,SY=1
	,SZ=0
	,SW=0
	,PRESERVE_TOPOLOGY=1
	,KEEP_QUADS_WEIGHT=1
	,VERTEX_MAP_NAME=""
	,REPLACE_ORIGINAL=1
	,CASHING_REDUCE=1
	,CH=True
	):
	
	def one_reduce(OBJ):
		if cmds.polyEvaluate(each,v=True)<6:
			return False
		cleanupLaminaFacesAndNonmaifoldGeometry(OBJ)
		cmds.polyReduce(
			OBJ
			,ver=1
			,trm=0
			,p							=PERCENTAGE
			,vct=VCT
			,tct=0
			,shp=0
			,keepBorder					=KEEP_BORDER_WEIGHT>0
			,keepMapBorder				=KEEP_MAP_BORDER_WEIGHT>0
			,keepColorBorder			=KEEP_COLOR_BORDER_WEIGHT>0
			,keepFaceGroupBorder		=KEEP_FACE_GROUP_BORDER_WEIGHT>0
			,keepHardEdge				=KEEP_HARD_EDGE_WEIGHT>0
			,keepCreaseEdge				=KEEP_CREASE_EDGE_WEIGHT>0
			,keepBorderWeight			=KEEP_BORDER_WEIGHT
			,keepMapBorderWeight		=KEEP_MAP_BORDER_WEIGHT
			,keepColorBorderWeight		=KEEP_COLOR_BORDER_WEIGHT
			,keepFaceGroupBorderWeight	=KEEP_FACE_GROUP_BORDER_WEIGHT
			,keepHardEdgeWeight			=KEEP_HARD_EDGE_WEIGHT
			,keepCreaseEdgeWeight		=KEEP_CREASE_EDGE_WEIGHT
			,useVirtualSymmetry			=USE_VIRTUAL_SYMMETRY
			,symmetryTolerance			=SYMMETRY_TOLERANCE
			,sx=0
			,sy=1
			,sz=0
			,sw=0
			,preserveTopology=PRESERVE_TOPOLOGY
			,keepQuadsWeight=KEEP_QUADS_WEIGHT
			,vertexMapName=VERTEX_MAP_NAME
			,replaceOriginal=REPLACE_ORIGINAL
			,cachingReduce=CASHING_REDUCE
			,ch=CH
			)
		return True

	for each in TARGETS:
		FIRST_BB = BBMesure(each)
		i=0
		CHECK=True
		while(CHECK):
			#頂点数チェック
			if cmds.polyEvaluate(each,v=True)<10:
				cmds.undo()
				break

			#リデュースコア
			one_reduce(each)

			#BBスケール差チェック
			TEMP_BB=BBMesure(each)
			if (TEMP_BB/FIRST_BB)<MS_BBGAP:
				cmds.undo()
				break

			#リミッターチェック
			i+=1
			if i>=MS_LOOP_LIMIT:#リミッター
				break

def reduce(TARGETS=[]
	,PERCENTAGE=25
	,VCT=1000
	,KEEP_BORDER_WEIGHT=0.5
	,KEEP_MAP_BORDER_WEIGHT=0.5
	,KEEP_COLOR_BORDER_WEIGHT=0
	,KEEP_FACE_GROUP_BORDER_WEIGHT=0
	,KEEP_HARD_EDGE_WEIGHT=0
	,KEEP_CREASE_EDGE_WEIGHT=0
	,USE_VIRTUAL_SYMMETRY=False
	,SYMMETRY_TOLERANCE=0.01
	,SX=0
	,SY=1
	,SZ=0
	,SW=0
	,PRESERVE_TOPOLOGY=1
	,KEEP_QUADS_WEIGHT=1
	,VERTEX_MAP_NAME=""
	,REPLACE_ORIGINAL=1
	,CASHING_REDUCE=1
	,CH=True
	):
	#

	for each in TARGETS:
		if cmds.polyEvaluate(each,v=True)<6:
			continue
		cleanupLaminaFacesAndNonmaifoldGeometry(each)
		cmds.polyReduce(
			each
			,ver=1
			,trm=0
			,p							=PERCENTAGE
			,vct=VCT
			,tct=0
			,shp=0
			,keepBorder					=KEEP_BORDER_WEIGHT>0
			,keepMapBorder				=KEEP_MAP_BORDER_WEIGHT>0
			,keepColorBorder			=KEEP_COLOR_BORDER_WEIGHT>0
			,keepFaceGroupBorder		=KEEP_FACE_GROUP_BORDER_WEIGHT>0
			,keepHardEdge				=KEEP_HARD_EDGE_WEIGHT>0
			,keepCreaseEdge				=KEEP_CREASE_EDGE_WEIGHT>0
			,keepBorderWeight			=KEEP_BORDER_WEIGHT
			,keepMapBorderWeight		=KEEP_MAP_BORDER_WEIGHT
			,keepColorBorderWeight		=KEEP_COLOR_BORDER_WEIGHT
			,keepFaceGroupBorderWeight	=KEEP_FACE_GROUP_BORDER_WEIGHT
			,keepHardEdgeWeight			=KEEP_HARD_EDGE_WEIGHT
			,keepCreaseEdgeWeight		=KEEP_CREASE_EDGE_WEIGHT
			,useVirtualSymmetry			=USE_VIRTUAL_SYMMETRY
			,symmetryTolerance			=SYMMETRY_TOLERANCE
			,sx=0
			,sy=1
			,sz=0
			,sw=0
			,preserveTopology=PRESERVE_TOPOLOGY
			,keepQuadsWeight=KEEP_QUADS_WEIGHT
			,vertexMapName=VERTEX_MAP_NAME
			,replaceOriginal=REPLACE_ORIGINAL
			,cachingReduce=CASHING_REDUCE
			,ch=CH
			)

def BB(TARGETS=[]):
	trn=MS_getBestBB.bbCenter(TARGETS)
	rot=[0,0,0]
	scl=MS_getBestBB.BBMesure_old(TARGETS)

	RET=cmds.polyCube(
		axis=[0,1,0],
		width=1,
		height=1,
		depth=1,
		subdivisionsX = 1,
		subdivisionsY = 1,
		subdivisionsZ = 1,
		)
	cmds.xform(RET,ws=True,t=trn,ro=[0,0,0],s=scl)
	cmds.makeIdentity(RET,a=True,s=True)
	return RET

def HULL(TARGETS=[],MAX_VTX=10):
	DELFLAG=False
	if cmds.nodeType(TARGETS[0])=='mesh':
		CO=MS_polyUnite.MS_polyChipOff()
		if len(CO)>1:
			TARGETS=cmds.polyUnite(CO,ch=False)
		else:
			TARGETS=CO
		DELFLAG=True

	MAX_VTX=cmds.intField('HULL_MAX_VTX',q=True,v=True)
	for each in TARGETS:
		cmds.select(each,r=True)
		mel.eval('hkCmdCreateConvexHull -mv %s'%MAX_VTX)
	if DELFLAG:
		cmds.delete(TARGETS)

#################
# ANGLEREDUCER
#################

def deleteSoftEdgesPSC(ANGLE=30):
	ANGLE=cmds.floatField('ANGLEREDUCER_ANGLE',q=True,v=True)
	cmds.polySoftEdge(angle=ANGLE,ch=False)
	cmds.polySelectConstraint(t=0x8000,m=2,sh=True,bo=False,sm=2)
	EDGS=cmds.filterExpand(sm=32,ex=True)
	#RET.extend(EDGS)
	cmds.polySelectConstraint(dis=True)

	cmds.select(EDGS,r=True)
	mel.eval("DeleteEdge;")

def deleteSoftEdges(ANGLE=30):
	cmds.polySoftEdge(angle=ANGLE,ch=False)
	#selectSoftEdges
	EDGS=cmds.filterExpand(sm=32,ex=True)
	RET=[]
	for each in EDGS:
		CHECK = cmds.polyInfo(each,ev=True)[0].split()[-1]
		if not CHECK=='Hard':
			RET.append(each)
	cmds.select(RET,r=True)
	#
	mel.eval("DeleteEdge;")

#################
# BBFilter
#################

def deleteChips(TARGETS=[],MAXV=1000):
	cmds.select(TARGETS,r=True)
	SEPARATED=MS_polyUnite.MS_polySeparate()
	FILTERD=MS_BBfilter.bbfilter(SEPARATED,MAX=MAXV)
	if FILTERD:
		cmds.delete()
	try:
		cmds.select(TARGETS,r=True)
		UNITED=MS_polyUnite.MS_superPolyUnite()
	except:
		UNITED=[]
	return UNITED


#################
# UTIL
#################

def MS_transferAttributes(SRC,DST):
	cmds.transferAttributes(
		SRC[0]
		,DST[0]
		,transferPositions=0
		,transferNormals=True
		,transferUVs=False
		,sourceUvSet="map1"
		,targetUvSet="map1"
		,transferColors=0
		,sampleSpace=0
		,sourceUvSpace="map1"
		,targetUvSpace="map1"
		,searchMethod=3
		,flipUVs=0
		,colorBorders=1
	)
	cmds.delete(DST,ch=True)

	cmds.select(SRC[0],r=True)
	cmds.select(DST[0],tgl=True)
	cmds.transferShadingSets( sampleSpace=1 )

#################
# UV
#################

def autoUV(NODES,RESX=512,RESY=512,PAD=1):
	#cmds.select(NODES,r=True)
	
	cmds.polyAutoProjection(
		lm=0
		,pb=0
		,ibd=0
		,cm=0
		,l=0
		,sc=0
		,o=1
		,p=6
		,ps=0.1
		,ws=0
		,ch=False
		)
	cmds.delete(NODES,ch=True)
	#LMUV
	if LMUV_enable:
		mel.eval('eval("gdhLMUV -d 0 -rd -max %s %s -name "+"map1"+" -msa 45 -pad %s")'%(RESX,RESY,PAD))

#################
# MAIN
#################

def easy(REDUCE_TYPE='BB'):
	ORGLOW = selectLowMesh()
	if not ORGLOW:
		return False
	#root low　があったら消す。
	if cmds.objExists('|root|low'):
		cmds.delete('|root|low')
	cmds.select(ORGLOW,r=True)

	#テンポラリメッシュグループ作成
	GP=duplicateGroups()

	#ターゲットメッシュ作成
	COMB=MS_polyUnite.MS_superPolyUnite()
	TARGETS=cmds.ls(COMB,l=True)
	
	if REDUCE_TYPE=='BB':
		NEW=BB(TARGETS)[0]
	elif REDUCE_TYPE=='HULL':
		HULL(TARGETS)
		return

	#UV
	autoUV(NEW)

	### FINALIZE ###

	#SETAttr
	cmds.select(NEW,r=True)
	setLODAttr([NEW])

	#grouping
	RESULTS=groupToLow(NEW)
	RESULTS=cmds.rename(NEW,'lod_lowmesh')

	#post
	cmds.delete(TARGETS)
	#

	return RESULTS

def main(MODE='simple'):
	#ルート内の総頂点数取得 削減目標頂点数を作成
	SEL=cmds.ls(sl=True)
	#ReductionFlow
	if MODE=='simple':
		reduce(SEL
			,PERCENTAGE						=cmds.floatField('PERCENTAGE',q=True,v=True)
			,VCT=0							#=cmds.intField('VCT',q=True,v=True)
			,KEEP_BORDER_WEIGHT				=cmds.floatField('KEEP_BORDER_WEIGHT',q=True,v=True)
			,KEEP_MAP_BORDER_WEIGHT			=cmds.floatField('KEEP_MAP_BORDER_WEIGHT',q=True,v=True)
			,KEEP_COLOR_BORDER_WEIGHT		=cmds.floatField('KEEP_COLOR_BORDER_WEIGHT',q=True,v=True)
			,KEEP_FACE_GROUP_BORDER_WEIGHT	=cmds.floatField('KEEP_FACE_GROUP_BORDER_WEIGHT',q=True,v=True)
			,KEEP_HARD_EDGE_WEIGHT			=cmds.floatField('KEEP_HARD_EDGE_WEIGHT',q=True,v=True)
			,KEEP_CREASE_EDGE_WEIGHT		=cmds.floatField('KEEP_CREASE_EDGE_WEIGHT',q=True,v=True)
			,USE_VIRTUAL_SYMMETRY=False
			,SYMMETRY_TOLERANCE=0.01
			,SX=0
			,SY=1
			,SZ=0
			,SW=0
			,PRESERVE_TOPOLOGY=1
			,KEEP_QUADS_WEIGHT=1
			,VERTEX_MAP_NAME=""
			,REPLACE_ORIGINAL=True
			,CASHING_REDUCE=1
			,CH								=cmds.checkBox('CH',q=True,v=True)
			)

	#LoopReduce
	if MODE=='loop':
		loopReducer(SEL
			,PERCENTAGE						=cmds.floatField('PERCENTAGE',q=True,v=True)
			,MS_BBGAP						=cmds.floatField('MS_BBGAP',q=True,v=True)
			,MS_LOOP_LIMIT					=cmds.intField('MS_LOOP_LIMIT',q=True,v=True)
			,VCT=0							#=cmds.intField('VCT',q=True,v=True)
			,KEEP_BORDER_WEIGHT				=cmds.floatField('KEEP_BORDER_WEIGHT',q=True,v=True)
			,KEEP_MAP_BORDER_WEIGHT			=cmds.floatField('KEEP_MAP_BORDER_WEIGHT',q=True,v=True)
			,KEEP_COLOR_BORDER_WEIGHT		=cmds.floatField('KEEP_COLOR_BORDER_WEIGHT',q=True,v=True)
			,KEEP_FACE_GROUP_BORDER_WEIGHT	=cmds.floatField('KEEP_FACE_GROUP_BORDER_WEIGHT',q=True,v=True)
			,KEEP_HARD_EDGE_WEIGHT			=cmds.floatField('KEEP_HARD_EDGE_WEIGHT',q=True,v=True)
			,KEEP_CREASE_EDGE_WEIGHT		=cmds.floatField('KEEP_CREASE_EDGE_WEIGHT',q=True,v=True)
			,USE_VIRTUAL_SYMMETRY=False
			,SYMMETRY_TOLERANCE=0.01
			,SX=0
			,SY=1
			,SZ=0
			,SW=0
			,PRESERVE_TOPOLOGY=1
			,KEEP_QUADS_WEIGHT=1
			,VERTEX_MAP_NAME=""
			,REPLACE_ORIGINAL=True
			,CASHING_REDUCE=1
			,CH								=cmds.checkBox('CH',q=True,v=True)
			)

	cmds.select(SEL,r=True)

#################
# UI
#################
def LayoutB():
	cmds.columnLayout('MSG2_LODreduce_manualLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_LODreduce',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	
	cmds.intField('VCT',v=1000,vis=False)

	cmds.rowLayout(nc=2)
	cmds.text(l='percentage')
	cmds.floatField('PERCENTAGE',v=25)
	cmds.setParent('..')

	cmds.gridLayout(nc=7,cw=60,ch=20)
	cmds.text(l='Border')
	cmds.text(l='mapBorder')
	cmds.text(l='colorBorder')
	cmds.text(l='faceGroup')
	cmds.text(l='hardEdge')
	cmds.text(l='creaseEdge')
	cmds.text(l='CH')
	cmds.floatField('KEEP_BORDER_WEIGHT',v=0.5)
	cmds.floatField('KEEP_MAP_BORDER_WEIGHT',v=0.5)
	cmds.floatField('KEEP_COLOR_BORDER_WEIGHT',v=0.5)
	cmds.floatField('KEEP_FACE_GROUP_BORDER_WEIGHT',v=0.5)
	cmds.floatField('KEEP_HARD_EDGE_WEIGHT',v=0.5)
	cmds.floatField('KEEP_CREASE_EDGE_WEIGHT',v=0.5)
	cmds.checkBox('CH',v=False)
	cmds.setParent('..')
	cmds.button(l='REDUCE',c=lambda *args:main())

	#
	cmds.rowLayout(nc=5)
	cmds.text(l='stopping BB Gap')
	cmds.floatField('MS_BBGAP',v=0.9)

	cmds.text(l='loop Limit')
	cmds.intField('MS_LOOP_LIMIT',v=3)
	
	cmds.button(l='LOOP REDUCE',c=lambda *args:main('loop'))
	cmds.setParent('..')

	cmds.separator()
	cmds.setParent('..')

def LayoutA():
	cmds.columnLayout('MSG2_LODreduce_manual_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_LODreduce',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	
	cmds.text(l=u'オートメーション系ツール')
	
	LayoutB()

	cmds.text(l=u'ユーティリティ')
	cmds.gridLayout(nc=6,cw=80,ch=50)
	#BB
	cmds.button(l='BB',c=lambda *args:easy('BB'))

	#HULL
	cmds.columnLayout(adj=True)
	cmds.intField('HULL_MAX_VTX',v=10)
	cmds.button(l='HULL',c=lambda *args:HULL(cmds.ls(sl=True)))
	cmds.setParent('..')

	#AngleReducer
	cmds.columnLayout(adj=True)
	cmds.floatField('ANGLEREDUCER_ANGLE',v=30)
	cmds.button(l='AngleReduce',c=lambda *args:deleteSoftEdgesPSC())
	cmds.setParent('..')	

	cmds.setParent('..')
	cmds.button(l='cleanup',c=lambda *args:cleanupPowerful())
	cmds.button(l=u'選択オブジェクトをlowmodelとして使う',c=lambda *args:lod_lowmodel())
	cmds.button(l='autoUV',c=lambda *args:autoUV(cmds.ls(sl=True)))
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
