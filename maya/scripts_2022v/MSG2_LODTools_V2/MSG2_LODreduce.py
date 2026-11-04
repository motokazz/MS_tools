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

def cleanupEdgeGeometry(MESH=[],SIZE=0.01):
	if MESH:
		cmds.select(MESH,r=True)
	#EdgeWith...GeometryWith...
	mel.eval('polyCleanupArgList 3 { "0","1","0","0","0","0","0","0","1","%s","1","%s","0","1e-005","0","1","1" };'%(SIZE,SIZE))

def cleanupZeroMapArea(MESH=[],SIZE=0.0001):
	if MESH:
		cmds.select(MESH,r=True)
	#EdgeWith...GeometryWith...
	mel.eval('polyCleanupArgList 3 { "0","1","0","0","0","0","0","0","1","%s","1","%s","1",%s,"0","1","1" };'%(SIZE,SIZE,SIZE))


#################
# REDUCE
#################

def reduceA(TARGETS=[]):
	for each in TARGETS:
		cmds.select(each,r=True)
		VC=cmds.polyEvaluate(each,vc=True)
		cleanup(each)
		cmds.polyReduce(
			each
			,ver=1
			,trm=1
			,p=80
			,vct=(VC*0.3)
			,tct=10
			,shp=0
			,keepBorder=1
			,keepMapBorder=0
			,keepColorBorder=0
			,keepFaceGroupBorder=0
			,keepHardEdge=1
			,keepCreaseEdge=0
			,keepBorderWeight=0.5
			,keepMapBorderWeight=0.5
			,keepColorBorderWeight=0.5
			,keepFaceGroupBorderWeight=0.5
			,keepHardEdgeWeight=1
			,keepCreaseEdgeWeight=0.5
			,useVirtualSymmetry=0
			,symmetryTolerance=0.01
			,sx=0
			,sy=1
			,sz=0
			,sw=0
			,preserveTopology=1
			,keepQuadsWeight=1
			,vertexMapName=""
			,replaceOriginal=1
			,cachingReduce=0
			,ch=True
			)

def reduce_Balance(TARGETS=[],VCT=1000):
	for each in TARGETS:
		cleanupLaminaFacesAndNonmaifoldGeometry(each)
		cmds.polyReduce(
			each
			,ver=1
			,trm=0
			,p=70
			,vct=VCT
			,tct=10
			,shp=0
			,keepBorder=True
			,keepMapBorder=False
			,keepColorBorder=False
			,keepFaceGroupBorder=False
			,keepHardEdge=False
			,keepCreaseEdge=False
			,keepBorderWeight=0.5
			,keepMapBorderWeight=0.5
			,keepColorBorderWeight=0.5
			,keepFaceGroupBorderWeight=0.5
			,keepHardEdgeWeight=0.5
			,keepCreaseEdgeWeight=0.5
			,useVirtualSymmetry=0
			,symmetryTolerance=0.01
			,sx=0
			,sy=1
			,sz=0
			,sw=0
			,preserveTopology=1
			,keepQuadsWeight=1
			,vertexMapName=""
			,replaceOriginal=1
			,cachingReduce=0
			,ch=False
			)

def reduce_Balance_loop(TARGETS=[],VCT=1000):
	for each in TARGETS:
		cleanupLaminaFacesAndNonmaifoldGeometry(each)
		for i in range(10):
			print i
			cmds.polyReduce(
				each
				,ver=1
				,trm=0
				,p=5
				,vct=VCT
				,tct=10
				,shp=0
				,keepBorder=True
				,keepMapBorder=False
				,keepColorBorder=False
				,keepFaceGroupBorder=False
				,keepHardEdge=False
				,keepCreaseEdge=False
				,keepBorderWeight=0.5
				,keepMapBorderWeight=0.5
				,keepColorBorderWeight=0.5
				,keepFaceGroupBorderWeight=0.5
				,keepHardEdgeWeight=0.5
				,keepCreaseEdgeWeight=0.5
				,useVirtualSymmetry=0
				,symmetryTolerance=0.01
				,sx=0
				,sy=1
				,sz=0
				,sw=0
				,preserveTopology=1
				,keepQuadsWeight=1
				,vertexMapName=""
				,replaceOriginal=1
				,cachingReduce=0
				,ch=False
				)
			if cmds.polyEvaluate(each,v=True)<VCT:
				break

def reduce_Balance2(TARGETS=[],VCT=1000):
	for each in TARGETS:
		cleanupLaminaFacesAndNonmaifoldGeometry(each)
		cmds.polyReduce(
			each
			,ver=1
			,trm=0
			,p=70
			,vct=VCT
			,tct=10
			,shp=0
			,keepBorder=True
			,keepMapBorder=True
			,keepColorBorder=False
			,keepFaceGroupBorder=False
			,keepHardEdge=False
			,keepCreaseEdge=False
			,keepBorderWeight=0.5
			,keepMapBorderWeight=0.5
			,keepColorBorderWeight=0.5
			,keepFaceGroupBorderWeight=1.0
			,keepHardEdgeWeight=1.0
			,keepCreaseEdgeWeight=0.5
			,useVirtualSymmetry=0
			,symmetryTolerance=0.01
			,sx=0
			,sy=1
			,sz=0
			,sw=0
			,preserveTopology=1
			,keepQuadsWeight=1
			,vertexMapName=""
			,replaceOriginal=1
			,cachingReduce=0
			,ch=False
			)


def reduceC(TARGETS=[],VCT=1000):
	for each in TARGETS:
		cmds.polyMergeVertex(each,d=10,am=False,ch=False)
		cleanupLaminaFacesAndNonmaifoldGeometry(each)
		cmds.polyReduce(
			each
			,ver=1
			,trm=1
			,p=70
			,vct=VCT
			,tct=10
			,shp=0
			,keepBorder=0
			,keepMapBorder=1
			,keepColorBorder=0
			,keepFaceGroupBorder=0
			,keepHardEdge=1
			,keepCreaseEdge=0
			,keepBorderWeight=0.5
			,keepMapBorderWeight=1
			,keepColorBorderWeight=0.5
			,keepFaceGroupBorderWeight=1.0
			,keepHardEdgeWeight=1.0
			,keepCreaseEdgeWeight=0.5
			,useVirtualSymmetry=0
			,symmetryTolerance=0.01
			,sx=0
			,sy=1
			,sz=0
			,sw=0
			,preserveTopology=1
			,keepQuadsWeight=1
			,vertexMapName=""
			,replaceOriginal=1
			,cachingReduce=0
			,ch=False
			)

		cmds.polyMergeVertex(each,d=10,am=False,ch=False)
	cmds.select(TARGETS,r=True)

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
	for each in TARGETS:
		cmds.select(each,r=True)
		mel.eval('hkCmdCreateConvexHull -mv %s'%MAX_VTX)

#################
# ANGLEREDUCER
#################

def deleteSoftEdgesPSC(ANGLE=30):
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

def selectLowMesh(LVLMAX=4):
	RET=[]
	SEL = cmds.ls(typ='transform')
	for each in SEL:
		if cmds.attributeQuery('LodLevelMax',n=each,ex=True):
			if cmds.getAttr(each+'.LodLevelMax')==LVLMAX:
				RET.append(each)
	return RET

def duplicateGroups():
	cmds.duplicate()
	DUPED=cmds.ls(sl=True,l=True)
	GP=cmds.group(em=True,n='templow')
	cmds.parent(DUPED,GP)
	return GP

def combine():
	NODES=cmds.ls(sl=True,type='mesh',lf=True,dag=True,l=True)
	try:
		cmds.polyUnite(ch=False)
	except:
		cmds.parent(NODES,w=True)
	return cmds.ls(sl=True,l=True)

def setLODAttr(TARGETS=[]):
	for each in TARGETS:
		if not cmds.attributeQuery("LodLevelMax",node=each,ex=True):
			cmds.addAttr(each,ln="LodLevelMax",at='long')
		if not cmds.attributeQuery("LodLevelMin",node=each,ex=True):
			cmds.addAttr(each,ln="LodLevelMin",at='long')
		cmds.setAttr(each+".LodLevelMax",8)
		cmds.setAttr(each+".LodLevelMin",5)
		cmds.color(each,ud=5)

def groupToLow(SEL):
	if not cmds.objExists('|root|low'):
		GP=cmds.group(em=True)
		NGP=cmds.parent(GP,'|root')
		cmds.rename(NGP,'low')
	return cmds.parent(SEL,'|root|low')

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

def main(REDUCE_TYPE='B'):

	ORGLOW = selectLowMesh()
	if not ORGLOW:
		return False
	#root low　があったら消す。
	if cmds.objExists('|root|low'):
		cmds.delete('|root|low')
	cmds.select(ORGLOW,r=True)

	#ルート内の総頂点数取得 削減目標頂点数を作成
	SEL=cmds.ls('root',lf=True,dag=True,l=True,type='mesh')
	TOTAL_VERTEX = cmds.polyEvaluate(SEL,v=True)
	AIM_VERTEX = TOTAL_VERTEX*0.3

	#テンポラリメッシュグループ作成
	GP=duplicateGroups()

	#ターゲットメッシュ作成
	cmds.select(GP,r=True)
	try:
		COMB=cmds.polyUnite(ch=False)
	except:
		SEL=cmds.ls(sl=True,tr=True,dag=True,l=True,type='mesh')
		COMB=cmds.parent(SEL,w=True)

	#COMB=MS_polyUnite.MS_superPolyUnite(CONSIDER_PARENTS=True)
	TARGETS=cmds.ls(COMB,l=True)

	try:
		TARGETS=cmds.parent(TARGETS,w=True)
	except:
		pass


	#forTRANSFERAttributes
	cmds.select(TARGETS,r=True)
	DUPEDORG = cmds.duplicate(TARGETS)
	DUPED = cmds.ls(sl=True,l=True)
	if cmds.objExists(GP):
		cmds.delete(GP)
	print TARGETS

	#normalEdit
	for each in TARGETS:
		cmds.polyNormalPerVertex(each,ufn=True)
		cmds.polySoftEdge(each,angle=60,ch=False)

	#deleteUselessSets
	deleteUselessUVSet(TARGETS)
	deleteUselessColorSet(TARGETS)

	#ReductionFlow
	#cleanup(TARGETS)
	if REDUCE_TYPE=='A':reduceA(TARGETS)
	elif REDUCE_TYPE=='B':reduce_Balance2(TARGETS,AIM_VERTEX)
	elif REDUCE_TYPE=='C':reduceC(TARGETS,AIM_VERTEX)
	
	TARGETS=deleteChips(TARGETS,MAXV=1000)

	if not TARGETS:
		cmds.delete(DUPED)
		cmds.delete(TARGETS)
		cmds.confirmDialog(m=u'リデュース結果内BB１以上のメにッシュが無いため、LODメッシュを作成しませんでした。')
		return

	#ANGLEREDUCE
	cmds.select(TARGETS,r=True)
	#deleteSoftEdges(30)
	#deleteSoftEdgesPSC(30)

	#cleanup(TARGETS)
	cleanupLaminaFacesAndNonmaifoldGeometry(TARGETS)
	cleanupEdgeGeometry(TARGETS,SIZE=0.01)
	cmds.select(TARGETS,r=True)

	#UV
	autoUV(TARGETS)

	### FINALIZE ###

	#SETAttr
	cmds.select(TARGETS,r=True)
	setLODAttr(TARGETS)

	#transferAttributes
	#MS_transferAttributes(DUPED,TARGETS)

	#normalEdit
	cmds.polyNormalPerVertex(TARGETS,ufn=True)
	cmds.polySoftEdge(TARGETS,angle=30,ch=False)

	#仕上げのクリーンナップ
	#cleanupFinish(TARGETS)
	#cleanupEdgeGeometry(TARGETS,SIZE=0.01)

	#grouping
	RESULTS=groupToLow(TARGETS)
	RESULTS=cmds.rename(RESULTS,'lod_lowmesh')

	#post
	cmds.delete(DUPED)
	#

	return RESULTS

#################
# UI
#################
def LayoutA():
	cmds.columnLayout('MSG2_LODreduce_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_LODreduce',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	
	cmds.text(l=u'オートメーション系ツール')
	cmds.gridLayout(nc=2,cw=80)
	cmds.button(l='Building',c=lambda *args:main('C'))
	cmds.button(l='Smooth',c=lambda *args:main('B'))
	cmds.button(l='BB',c=lambda *args:easy('BB'))
	cmds.setParent('..')

	cmds.text(l=u'ユーティリティ')
	cmds.gridLayout(nc=2,cw=80)
	cmds.button(l='HULL',c=lambda *args:HULL(cmds.ls(sl=True,l=True)))
	cmds.setParent('..')
	cmds.button(l='cleanup',c=lambda *args:cleanupEdgeGeometry())
	cmds.button(l='autoUV',c=lambda *args:autoUV(cmds.ls(sl=True,l=True)))
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	
#UI()