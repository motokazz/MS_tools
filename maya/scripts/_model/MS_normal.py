#coding=utf-8
#MP_MS_normal
import maya.cmds as cmds
import maya.mel as mel
import math

#import MP_MS_normal
#reload(MP_MS_normal)

import _lib.MP_MS_undoUtil as MP_MS_undoUtil
reload(MP_MS_undoUtil)

#execCheckList
#import MS_module.MS_execCheck
#reload(MS_module.MS_execCheck)
#MS_module.MS_execCheck.execCheckSafe('MP_MS_normal.py')



THIS_SCRIPT='MP_MS_normal.'

#####　2ベクトル角度計測
def dotproduct(v1, v2):
	return sum((a*b) for a, b in zip(v1, v2))

def length(v):
	return math.sqrt(dotproduct(v, v))
	
def angle(v1, v2):
	DP=dotproduct(v1, v2)
	if DP>1:DP=1
	return math.acos(DP / (length(v1) * length(v2)))
	
	
#####　math系
def normalize(vec):
	#ノーマライズ
    l=math.sqrt((vec[0]*vec[0])+(vec[1]*vec[1])+(vec[2]*vec[2]))
    result = [0.0,0.0,0.0]
    if l<0.00001:
        return [0,1,0]
    result[0]=vec[0]/l
    result[1]=vec[1]/l
    result[2]=vec[2]/l
    return result

##### 面積
def areaFace(FACE):
	#ポリゴンバウンディングボックス面積
	BB=cmds.xform(FACE,q=True,bb=True)
	RET=((BB[3]-BB[0])*(BB[4]-BB[1])*(BB[5]-BB[2]))
	return RET
	
def edgeLength(EDGE):#エッジの長さ計算
	POINTS=getVerts(EDGE)
	POINT_A = cmds.xform(POINTS[0],q=True,ws=True,t=True)
	POINT_B = cmds.xform(POINTS[1],q=True,ws=True,t=True)
	LEN = math.sqrt((POINT_A[0]-POINT_B[0])*(POINT_A[0]-POINT_B[0])+(POINT_A[1]-POINT_B[1])*(POINT_A[1]-POINT_B[1])+(POINT_A[2]-POINT_B[2])*(POINT_A[2]-POINT_B[2]))
	
	return LEN
	
#####角度計測

def polyAngleByEdge(EDGE):
	#print EDGE
	OBJ=EDGE.split('.')[0]
	FACESINFO=cmds.polyInfo(EDGE,ef=True)
	FACES=FACESINFO[0].split()
	FACES.pop(0)
	FACES.pop(0)
	if len(FACES)>1:
		vec1=getFaceNormal(OBJ+'.f['+FACES[0]+']')
		vec2=getFaceNormal(OBJ+'.f['+FACES[1]+']')
		RET_ANGLE=math.degrees(angle(vec1,vec2))
	else:
		RET_ANGLE=0.0
	return RET_ANGLE
	
##### オブジェクト選択
def ditectObj():#コンポーネントからオブジェクト選択
	RET=''
	OBJ=cmds.ls(sl=True)
	if OBJ:
		RET=OBJ[0].split('.')[0]
	return RET
	
#####コンポーネント選択

def getFaces(CONP):#フェース選択
	FACE=cmds.polyListComponentConversion(CONP,tf=True)
	result=cmds.filterExpand(FACE,ex=True,sm=34)
	return result
	
def getVerts(CONP):#頂点選択
	VTX=cmds.polyListComponentConversion(CONP,tv=True)
	result=cmds.filterExpand(VTX,ex=True,sm=31)
	return result
	
def getEdges(CONP):#エッジ選択
	EDGE=cmds.polyListComponentConversion(CONP,te=True)
	result=cmds.filterExpand(EDGE,ex=True,sm=32)
	return result

def getVertsFaces(CONP):#フェース頂点選択
	FACE=cmds.polyListComponentConversion(CONP,tvf=True)
	result=cmds.filterExpand(FACE,ex=True,sm=70)
	return result
	
def selectFaceEdge():
	#選択オブジェクトの境界線
	BORDER_EDGES=[]
	FACE=cmds.filterExpand(sm=34)
	BORDER_EDGES=cmds.polyListComponentConversion(FACE,fv=True,ff=True,fuv=True,fvf=True,te=True,bo=True)
	return BORDER_EDGES
	
#####　MAYA標準機能
def hardEdge(CONP):
	EDGES=getEdges(CONP)
	cmds.polySoftEdge(EDGES,a=0,ch=0)
	
def softEdge(CONP):
	EDGES=getEdges(CONP)
	cmds.polySoftEdge(EDGES,a=180,ch=0)
		
def softEdge2(OBJ):
	EDGES=getEdges(OBJ)
	SOFT_ANGLE=cmds.floatSliderGrp('MP_MS_normal_polySoftEdge_Angle',q=True,v=True)
	cmds.polySoftEdge(EDGES,a=SOFT_ANGLE,ch=0)
	
def getFaceNormal( face ):
	try:
		normal = cmds.polyInfo( face, faceNormals=True )[0]
		temp   = normal.split(" ")
		result = [ float( temp[-3] ), float( temp[-2] ), float( temp[-1] ) ]
		return result
	except:
		return False
	
#####　リスト作成

def byAngle(OBJ):#指定角度内のエッジを選択する
	RESULT_EDGE=[]
	MIN_ANGLE=cmds.floatSliderGrp('MP_MS_vtxNrmAlignFaceNrm_LimitAngleMIN',q=True,v=True)
	if cmds.checkBoxGrp('MP_MS_normal_range',q=True,v1=True):
		MAX_ANGLE=MIN_ANGLE+cmds.floatSliderGrp('MP_MS_normal_rangeSlider',q=True,v=True)
	else:
		MAX_ANGLE=cmds.floatSliderGrp('MP_MS_vtxNrmAlignFaceNrm_LimitAngleMAX',q=True,v=True)
		
	EDGES=getEdges(OBJ)
	for EACH in EDGES:#対象エッジ選択
		FACE_ANGLE=polyAngleByEdge(EACH)
		if MIN_ANGLE<FACE_ANGLE<MAX_ANGLE:#角度の閾値
			RESULT_EDGE.append(EACH)
	
	#エッジが無ければ終了
	if not RESULT_EDGE:
		return
	
	#cmds.select(RESULT_EDGE,r=True)
	return RESULT_EDGE
	
	
def hosonagaCheck(FACE):
	RET=[]
	EDGES=getEdges(FACE)
	for EACH_EDGE in EDGES:
		RET.append([EACH_EDGE,edgeLength(EACH_EDGE)])
	return sorted(RET,key=lambda x:x[1],reverse=True)

def hosonagaList(OBJ):
	RET=[]
	VAR=cmds.floatSliderGrp('MP_MS_normal_hosonagaEdge',q=True,v=True)
	FACES=getFaces(OBJ)
	for EACH_FACE in FACES:
		EDGES=hosonagaCheck(EACH_FACE)
		if EDGES[1][1]/EDGES[2][1]>VAR:
			RET.append(EDGES[0][0])
			RET.append(EDGES[1][0])
	
	return RET
	
def hosonagaFace(OBJ):
	RET=[]
	VAR=cmds.floatSliderGrp('MP_MS_normal_hosonagaFace',q=True,v=True)
	FACES=getFaces(OBJ)
	for EACH_FACE in FACES:
		EDGES=hosonagaCheck(EACH_FACE)
		if EDGES[1][1]/EDGES[2][1]>VAR:
			RET.append(EACH_FACE)
	
	return RET

def areaCompArroundVertex(VTX):#頂点に隣接するフェースを面積比較してソート済みリスト作成
	RET=[]
	OBJ=VTX.split('.')[0]
	VF = cmds.polyInfo(VTX,vf=True )
	VFS=VF[0].split()
	VFS.pop(0)
	VFS.pop(0)
	
	for EACH_VF in VFS:
		POLY=OBJ+'.f['+EACH_VF+']'
		AREA=areaFace(POLY)
		RET.append([POLY,str(AREA)])
	
	return sorted(RET,key=lambda x:x[1],reverse=False)
	
	
def areaCompArroundEdge(EDGE):#エッジに隣接するフェースを面積比較してソート済みリスト作成
	RET=[]
	OBJ=EDGE.split('.')[0]
	FACEINFO = cmds.polyInfo(EDGE,ef=True )
	FACES=FACEINFO[0].split()
	FACES.pop(0)
	FACES.pop(0)
	
	for EACH_VF in FACES:
		POLY=OBJ+'.f['+EACH_VF+']'
		AREA=areaFace(POLY)
		RET.append([POLY,str(AREA)])
	
	return sorted(RET,key=lambda x:x[1],reverse=False)
	
	
def convList():#頂点周囲の一番広いフェース法線を取得
	RET=[]
	try:
		OBJ=cmds.polyListComponentConversion(fe=True,fuv=True,ff=True,fvf=True,tv=True)
		VTX=cmds.filterExpand(OBJ,ex=True,sm=31)
	except:
		VTX=cmds.filterExpand(ex=True,sm=31)
	
	for EACH in VTX:
		FACE=areaCompArroundVertex(EACH)[0][0]#エリア一番広いとこ
		AFN=getFaceNormal(FACE)
		RET.append([EACH,normalize(AFN)])
	return RET
	
def flatList(FACES):#選択フェースの法線にあわせた値リスト
	#単純フラット化
	RET=[]
	for EACH in FACES:
		AFN=getFaceNormal(EACH)
		VTX=getVerts(EACH)
		RET.append([VTX,normalize(AFN)])
	return RET
	
#####　コマンド
	
def areaCompArroundEdgeFitNormal(EDGES):
	hardEdge(EDGES)
	#エッジアングル両脇のポリゴン面積比較して大きいほうに法線を合わせる
	for EACH_EDGE in EDGES:
		PREFIX=EACH_EDGE.split('.')[0]
		SORTED_FACE=areaCompArroundEdge(EACH_EDGE)
		VTX=getVerts(EACH_EDGE)
		VTX0 = VTX[0].encode().split('[')[-1].split(']')[0]
		VTX1 = VTX[1].encode().split('[')[-1].split(']')[0]
		FACE0=SORTED_FACE[0][0].split('[')[-1].split(']')[0]
		FACE1=SORTED_FACE[0][1].split('[')[-1].split(']')[0]
		NRM0=cmds.polyNormalPerVertex(PREFIX+'.vtxFace['+VTX0+']['+FACE0+']',q=True,xyz=True)
		NRM1=cmds.polyNormalPerVertex(PREFIX+'.vtxFace['+VTX1+']['+FACE0+']',q=True,xyz=True)
		cmds.polyNormalPerVertex(PREFIX+'.vtxFace['+VTX0+']['+FACE1+']',xyz=NRM0)
		cmds.polyNormalPerVertex(PREFIX+'.vtxFace['+VTX1+']['+FACE1+']',xyz=NRM1)
		
	
def unfreeze(OBJ=[]):
	#VTXS=getVerts(OBJ)
	if not OBJ:
		OBJ=cmds.ls(sl=True)
	VTXS=cmds.polyListComponentConversion(OBJ,tvf=True)
	cmds.polyNormalPerVertex(VTXS,ufn=True)
	
def margeNormals(*args):#ハードエッジ化後に選択エッジをソフトエッジ
	RET=[]
	SEL=cmds.ls(sl=True)
	OBJ=ditectObj()
	cmds.select(OBJ,r=True)
	unfreeze
	softEdge(OBJ)
	
	VTX=getVerts(SEL)
	for EACH_VTX in VTX:
		AREA_CONP_LIST=areaCompArroundVertex(EACH_VTX)
		VEC=cmds.polyNormalPerVertex(AREA_CONP_LIST[0][0],q=True,xyz=True)
		RET.append([EACH_VTX,VEC])
		
	exe_polySoftEdge
	
	PNPV(RET)
	
def PNPV(ARRAY_DOUBLE):#リストを渡してPolyNormalPerVertex実行
	for EACH in ARRAY_DOUBLE:
		cmds.polyNormalPerVertex(EACH[0],xyz=[EACH[1][0],EACH[1][1],EACH[1][2]])

##### 強引ベベル
def forceBevel(MESH):#トランスファーアトリビュートを利用した強引なやつ
	
	unfreeze(MESH)
	BEVEL_ANGLE=cmds.floatSliderGrp('MP_MS_normal_bevel_Angle',q=True,v=True)
	OBJ2=cmds.duplicate(MESH)
	cmds.polyBevel(OBJ2[0],offset=BEVEL_ANGLE,offsetAsFraction=True,autoFit=1,segments=1,worldSpace=1,uvAssignment=0,fillNgons=1,mergeVertices=1,mergeVertexTolerance=0.0001,smoothingAngle=30,miteringAngle=180,angleTolerance=180,ch=False)
	cmds.transferAttributes(OBJ2[0],MESH,spa=1,nml=True)
	cmds.delete(MESH,ch=True)
	cmds.delete(OBJ2)
	
def forceBevelConp(MESH):#ガイド残してやる
	unfreeze(MESH)
	BEVEL_ANGLE=cmds.floatSliderGrp('MP_MS_normal_bevel_Angle',q=True,v=True)
	OBJ2=cmds.duplicate(MESH)
	#cmds.polyBevel(OBJ2[0],offset=BEVEL_ANGLE,offsetAsFraction=True,autoFit=1,segments=1,worldSpace=1,uvAssignment=0,fillNgons=1,mergeVertices=1,mergeVertexTolerance=0.0001,smoothingAngle=30,miteringAngle=180,angleTolerance=180,ch=False)
	cmds.transferAttributes(OBJ2[0],MESH,spa=1,nml=True)
	
	BB=cmds.xform(MESH,q=True,bb=True)
	
	cmds.move((BB[0]-BB[3]),0,0,OBJ2[0],r=True,ws=True)
	
def freezeConstructionHistory(MESH):
	cmds.delete(MESH,ch=True)
	
##### プリコマンド
def angleWalk(METHOD):#インタラクティブ・アングルウォーク
	

	HL=cmds.ls(hl=True,l=True)
	if not HL:
		HL=cmds.ls(sl=True,l=True)

	if cmds.undoInfo(q=True,stateWithoutFlush=True):
		cmds.undoInfo(stateWithoutFlush=False)
		UNDO_CHECK=1
	else:
		UNDO_CHECK=0
		
	#
	
	RESULT=[]
	MESHES=getAllMesh()
	for OBJ in MESHES:
		COMP=[]
		if METHOD=='byAngle':
			COMP=byAngle(OBJ)
		elif METHOD=='hosonagaList':
			COMP=hosonagaList(OBJ)
		elif METHOD=='hosonagaFace':
			COMP=hosonagaFace(OBJ)
		if COMP:
			RESULT.extend(COMP)
		
	#cmds.select(MESHES,r=True)

	if RESULT:
		cmds.select(RESULT,r=True)
	cmds.hilite(HL)


	#
	'''
	if UNDO_CHECK:
		cmds.undoInfo(stateWithoutFlush=True)
		MP_MS_undoUtil.undoState()
	'''

	
def exe_disableUndo(COMMAND):
	if cmds.undoInfo(q=True,stateWithoutFlush=True):
		cmds.undoInfo(stateWithoutFlush=False)
		UNDO_CHECK=1
	else:
		UNDO_CHECK=0
	
	MESHES=getAllMesh()
	if COMMAND=='flatList':
		OBJ=cmds.ls(sl=True)
		FACES=getFaces(OBJ)
		RET=flatList(FACES)
		print RET
		PNPV(RET)
	
	for MESH in MESHES:
		
		if COMMAND=='unfreeze':
			unfreeze(MESH)
			
		if COMMAND=='softEdge2':
			unfreeze(MESH)
			softEdge2(MESH)
			
		if COMMAND=='areaCompArroundEdgeFitNormal':
			OBJ=cmds.ls(sl=True)
			EDGES=getEdges(OBJ)
			areaCompArroundEdgeFitNormal(EDGES)
			

		if COMMAND=='convList':
			CONV_LIST=convList()
			PNPV(CONV_LIST)
			
		if COMMAND=='margeNormals':
			margeNormals
			
		if COMMAND=='forceBevel':
			forceBevel(MESH)
		
		if COMMAND=='forceBevelConp':
			forceBevelConp(MESH)
		
		if COMMAND=='freezeConstructionHistory':
			freezeConstructionHistory(MESH)
	'''
	if UNDO_CHECK:
		cmds.undoInfo(stateWithoutFlush=True)
		MP_MS_undoUtil.undoState()
	
	'''

def getAllMesh():#全選択オブジェクトの子供込みメッシュリスト
	RET=[]
	OBJS=cmds.ls(sl=True)
	if not OBJS:
		OBJS=cmds.ls(o=True,hl=True)
	for OBJ in OBJS:
		if cmds.listRelatives(OBJ,s=True,type='mesh'):
			RET.append(OBJ)
		TRNS=cmds.listRelatives(OBJ,c=True,type='transform')
		if TRNS:
			for TRN in TRNS:
				if cmds.listRelatives(TRN,s=True,type='mesh'):
					RET.append(TRN)
	return RET
		
		
		
##### UI

def uiActControll1(*args):
	if cmds.checkBoxGrp('MP_MS_normal_range',q=True,v1=True):
		cmds.floatSliderGrp('MP_MS_normal_rangeSlider',e=True,en=True)
		cmds.floatSliderGrp('MP_MS_vtxNrmAlignFaceNrm_LimitAngleMAX',e=True,en=False)
	else:
		cmds.floatSliderGrp('MP_MS_normal_rangeSlider',e=True,en=False)
		cmds.floatSliderGrp('MP_MS_vtxNrmAlignFaceNrm_LimitAngleMAX',e=True,en=True)

def layout_selectionWalk():
	cmds.frameLayout(l=u'選択リスト作成',bgc=[0.5,0.5,0.4],cll=True,cl=False)
	cmds.columnLayout()
	cmds.button(u'角度でエッジを選択',w=250,c=lambda *args:angleWalk('byAngle')
		,ann=u'細長いフェース内の長いエッジを2本選択します。')
	cmds.floatSliderGrp('MP_MS_vtxNrmAlignFaceNrm_LimitAngleMIN',cw3=[60,30,100],l='MIN',field=True,min=0,max=180,v=60,cc=lambda *args:angleWalk('byAngle')
		,ann=u'対象エッジの最小角度。')
	cmds.floatSliderGrp('MP_MS_vtxNrmAlignFaceNrm_LimitAngleMAX',cw3=[60,30,100],l='MAX',field=True,min=0,max=180,v=120,cc=lambda *args:angleWalk('byAngle')
		,ann=u'対象エッジの最大角度')
	cmds.floatSliderGrp('MP_MS_normal_rangeSlider',l=u'Range値',cw3=[60,30,100],field=True,v=60.0,cc=lambda *args:angleWalk('byAngle')
		,ann=u'MIN値を動かすとき、MIN値から加算したRange値の間のエッジを選択します。')
	cmds.checkBoxGrp('MP_MS_normal_range',l=u'レンジを使う',cw2=[60,10],v1=True,cc=uiActControll1
		,ann=u'ON時、MIN値とRange値を使用した選択方法になります。\nOFF時はMIN値とMAX値を利用した選択方法になります。')
	cmds.separator(w=250)
	cmds.button(u'細長い部分のエッジを選択',w=250,c=lambda *args:angleWalk('hosonagaList')
		,ann=u'細長いフェース内の長いエッジを2本選択します。')
	cmds.floatSliderGrp('MP_MS_normal_hosonagaEdge',l=u'細長エッジ',cw3=[60,30,100],field=True,max=100,v=2.0,cc=lambda *args:angleWalk('hosonagaList')
		,ann=u'細長いフェース内の長いエッジを2本選択します。')
	cmds.separator(w=250)
	cmds.button(u'細長いフェースを選択',w=250,c=lambda *args:angleWalk('hosonagaFace')
		,ann=u'細長いフェースを選択します。')
	cmds.floatSliderGrp('MP_MS_normal_hosonagaFace',l=u'細長フェース',cw3=[60,30,100],field=True,max=100,v=2.0,cc=lambda *args:angleWalk('hosonagaFace')
		,ann=u'')
	cmds.setParent('..')
	cmds.setParent('..')
	#

def layout_commands():
	cmds.frameLayout(l=u'コマンドボタン',bgc=[0.5,0.5,0.4],mh=0,cll=True,cl=False)
	cmds.columnLayout()
	cmds.button(u'選択フェースの法線にあわせる',w=250,c=lambda *args:exe_disableUndo('flatList')
		,ann=u'選択フェースの法線にあわせる')
	cmds.button(u'ハードエッジ中選択コンポーネントをソフトエッジ',w=250,c=lambda *args:exe_disableUndo('margeNormals')
		,ann=u'')
	cmds.button(u'※激重：選択頂点周囲の一番広いフェースにフィット',w=250,c=lambda *args:exe_disableUndo('convList')
		,ann=u'')
	cmds.button(u'選択エッジ両端の広いほうのフェースにフィット',w=250,c=lambda *args:exe_disableUndo('areaCompArroundEdgeFitNormal')
		,ann=u'')
	cmds.setParent('..')
	cmds.setParent('..')
		
def layout_transferAttributes():
	#強引ベベル
	cmds.frameLayout(l=u'アトリビュート転送系',bgc=[0.5,0.5,0.4],cll=True,cl=False)
	cmds.columnLayout()
	cmds.floatSliderGrp('MP_MS_normal_bevel_Angle',l=u'強引ベベル角度',pre=3,min=0.001,max=2.0,fmx=100000,v=1.0,cw3=[60,30,100],field=True
		,ann=u'実際にベベルした法線を転写するコマンド'
		,cc=lambda *args:changeMinMax('MP_MS_normal_bevel_Angle')
		)
	cmds.button(u'強引ベベル',w=250,c=lambda *args:exe_disableUndo('forceBevel')
		,ann=u'実際にベベルした法線を転写するコマンド')
	cmds.button(u'強引ベベル・ヒストリー残し',w=250,c=lambda *args:exe_disableUndo('forceBevelConp')
		,ann=u'実際にベベルした法線を転写するコマンド')
	cmds.button(u'強引ベベル・フリーズ',w=250,c=lambda *args:exe_disableUndo('freezeConstructionHistory')
		,ann=u'ヒストリーをフリーズ')
	
	cmds.setParent('..')
	cmds.setParent('..')
	
def changeMinMax(CONTROLL):#コントロールのMIN/MAX値を変更する
	VALUE=cmds.floatSliderGrp(CONTROLL,q=True,v=True)
	if VALUE<cmds.floatSliderGrp(CONTROLL,q=True,min=True):
		cmds.floatSliderGrp(CONTROLL,e=True,min=VALUE)
	if VALUE>cmds.floatSliderGrp(CONTROLL,q=True,max=True):
		cmds.floatSliderGrp(CONTROLL,e=True,max=VALUE)
	
def layout_maya_common():
	cmds.frameLayout(l=u'標準機能系',bgc=[0.5,0.5,0.4],mh=0,cll=True,cl=False)
	cmds.columnLayout()
	cmds.button('UNFREEZE',w=250,c=lambda *args:unfreeze()
		,ann=u'')
	cmds.floatSliderGrp('MP_MS_normal_polySoftEdge_Angle',l=u'ソフト角度',max=180,cw3=[60,30,100],field=True,v=60
		,ann=u''
		)
	cmds.button('POLY_SOFT_EDGE',w=250,c=lambda *args:exe_disableUndo('softEdge2')
		,ann=u'')
	cmds.setParent('..')
	cmds.setParent('..')
	
def clearENV():
	#過去に使っていた環境変数を消したい。
	if cmds.optionVar(ex='MP_MS_normal_last_selected'):
		cmds.optionVar( remove='MP_MS_normal_last_selected' )
	
def UI():
	
	clearENV()
	
	if cmds.window('MP_MS_vtxNrmAlignFaceNrm',q=True,ex=True):
		cmds.deleteUI('MP_MS_vtxNrmAlignFaceNrm')
	cmds.window('MP_MS_vtxNrmAlignFaceNrm')
	cmds.columnLayout()
	layout_maya_common()
	
	cmds.separator(w=250)
	
	layout_selectionWalk()
	
	cmds.separator(w=250)
	
	layout_commands()
	
	cmds.separator(w=250)
	
	layout_transferAttributes()
	#
	cmds.separator(w=250)

	MP_MS_undoUtil.controll()

	cmds.setParent('..')
	#
	cmds.window('MP_MS_vtxNrmAlignFaceNrm',e=True,w=160,h=150)
	
	cmds.showWindow('MP_MS_vtxNrmAlignFaceNrm')
	
	uiActControll1()
	
def MP_MS_normal():
	UI()



