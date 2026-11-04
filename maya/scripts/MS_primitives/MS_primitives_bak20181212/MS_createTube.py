# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_createTube.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

def ct_extrude (  crv , radius = 0.2 , min = 0.0, max = 1.0 , spans =8 , degree = 3, rot = 0.0 ):

	# get start pos and tan of curve in world space
	pos = cmds.pointOnCurve(pr = .00001, position = crv )
	tan = cmds.pointOnCurve(pr = .00001 , tangent = crv )
	periodic = cmds.getAttr (crv + ".form")

	# make circle at start matching curve tangent
	profile = cmds.circle(c=pos
		,nr=[ 0 ,1 , 0 ]
		,r = radius
		,degree = degree
		,sections = spans
		)

	# put curve under new transform node
	crvGrp = cmds.group( n = profile[0])
	crvGrp = cmds.rename ( crvGrp , "tubeConstruction#" )

	# move circle to curve start point
	cmds.xform( cp = profile[0] )

	# rotate circle into position once before extruding
	tc = cmds.tangentConstraint ( weight = 1 , aimVector = [ 0 , 1 , 0 ] , upVector = [ 0 , 1 , 0 ] , crv = crvGrp )

	# get form (open/periodic)
	form = False
	if periodic == 0 or min != 0 or max != 1 :
		form = True

	# extrude spiral
	#tube = eval ( "extrude -fixedPath true -range true -ucp true -upn " + form + " -et 2 " + profile[0] + " " + crv )
	tube = cmds.extrude( profile[0] , crv
		,fixedPath = True
		,range = True
		,ucp = True
		,upn = form
		,et = 2
		)

	# delete tangentConstraint
	cmds.delete(tc[0])

	# rotate circle into position
	cmds.setAttr( profile[0] + ".ry" , rot)

	# return	(0) profile transform node
	#		(1) make nurbs circle node
	#		(2) tube transform node
	#		(3) extrude node
	#		(4) curve form (open/periodic)
	#		(5) curve group transform node
	return profile[0], profile[1], tube[0], tube[1], (periodic), crvGrp

def attrSetup(CURVE
	,prof_curve_transform
	,prof_curve_shape
	,extruded_surface_transform
	,extruded_surface_shape
	,tube_transform
	,tube_shape
	,radius
	,rot
	,spans
	):
	
	# profile Span

	cmds.addAttr( tube_transform , sn = 'span' , ln = 'profileSpans' , at = "short" , min = 3 , max = 64 )
	cmds.setAttr( tube_transform + ".profileSpans" , spans , keyable = True )
	cmds.connectAttr ( tube_transform + ".profileSpans" , prof_curve_shape + ".sections")


	# profile Radius
	cmds.addAttr( tube_transform , sn ='trd' , ln='tubeRadius' , at = "float" , min = 0 )
	cmds.setAttr(  tube_transform + '.tubeRadius' , radius , keyable=True)
	cmds.connectAttr (tube_transform + '.tubeRadius' , prof_curve_shape + ".radius")

	# profile offset

	cmds.addAttr( tube_transform , sn = 'ofsu', ln = 'profileOffsetU' , at ="float" ) 
	cmds.setAttr( tube_transform + ".profileOffsetU" , 0 , keyable = True )
	cmds.connectAttr( tube_transform + ".profileOffsetU" , prof_curve_transform + ".tx")

	cmds.addAttr( tube_transform , sn = 'ofsv', ln = 'profileOffsetV' , at ="float" ) 
	cmds.setAttr( tube_transform + ".profileOffsetV" , 0 , keyable = True )
	cmds.connectAttr( tube_transform + ".profileOffsetV" , prof_curve_transform + ".ty")


	# profile Scale

	cmds.addAttr( tube_transform , sn = 'sclu', ln = 'profileScaleU' , at ="float" ) 
	cmds.setAttr( tube_transform + ".profileScaleU" , 1 , keyable = True )
	cmds.connectAttr( tube_transform + ".profileScaleU" , prof_curve_transform + ".sx")

	cmds.addAttr( tube_transform , sn = 'sclv', ln = 'profileScaleV' , at ="float" ) 
	cmds.setAttr( tube_transform + ".profileScaleV" , 1 , keyable = True )
	cmds.connectAttr( tube_transform + ".profileScaleV" , prof_curve_transform + ".sy")


	# profile Rotation

	cmds.addAttr( tube_transform , sn = 'rot', ln = 'profileRotation' , at ="float" ) 
	cmds.setAttr( tube_transform + ".profileRotation" , rot , keyable = True )
	cmds.connectAttr( tube_transform + ".profileRotation" , prof_curve_transform + ".rz")


	# curve Range
	subCurve = cmds.connectionInfo( extruded_surface_shape + ".path" , sfd = True )
	buffer= subCurve.split('.')

	cmds.addAttr( tube_transform , sn = 'pmir' , ln = 'pathMinRange' , at = "float" , min = 0 , max = 1) 
	cmds.setAttr ( tube_transform + ".pathMinRange" , 0 ,keyable = True )
	cmds.connectAttr( tube_transform + ".pathMinRange", buffer[0] + ".minValue")

	cmds.addAttr( tube_transform , sn = 'pmar' , ln = 'pathMaxRange' , at = "float" , min = 0 , max = 1)
	cmds.setAttr( tube_transform + ".pathMaxRange" , 1 , keyable = True)
	cmds.connectAttr (tube_transform + ".pathMaxRange" , buffer[0] + ".maxValue")

	# extra attribute for periodic curves and path min/max range
	#if (int ($extrude[4]) != 0)
	#	cmds.expression (s = ("if (" + tube_transform + ".pathMinRange != 0 || " +
	#		tube_transform + ".pathMaxRange != 1)\n" +
	#		extruded_surface_shape + ".useProfileNormal = true\n" +
	#		"else\n" +
	#		extruded_surface_shape + ".useProfileNormal = false\n")
	#	)


def extraAttrCrear():
	cmds.deleteAttr(at='profileSpans')
	cmds.deleteAttr(at='tubeRadius')
	cmds.deleteAttr(at='profileOffsetU')
	cmds.deleteAttr(at='profileOffsetV')
	cmds.deleteAttr(at='profileScaleU')
	cmds.deleteAttr(at='profileScaleV')
	cmds.deleteAttr(at='profileRotation')
	cmds.deleteAttr(at='pathMinRange')
	cmds.deleteAttr(at='pathMaxRange')


def SelectCurve():
	CV = cmds.ls(sl=True)
	cmds.textField('SelectCurve',e=True,tx=CV[0])

def SelectCurve_Clear():
	cmds.textField('SelectCurve',e=True,tx='')


def main(RADIUS=100,ROTATE=45,SPAN=4,DELETE_HISTORY=True):

	RADIUS=cmds.floatField('TubeRadius',q=True,v=True)
	ROTATE=cmds.floatField('TubeRotate',q=True,v=True)
	SPAN=cmds.intField('TubeSubdivision',q=True,v=True)
	DELETE_HISTORY=cmds.checkBox('DELETE_HISTORY',q=True,v=True)
	SELCURVE=cmds.textField('SelectCurve',q=True,tx=True)
	V_SPAN=cmds.intField('v_subdivision',q=True,v=True)
	
	CURVE_QUANTITY=1

	#パスカーブ関連
	SEL=cmds.ls(sl=True,l=True)
	SHAPE=cmds.listRelatives(s=True,f=True)
	if not SEL:
		return
	elif cmds.nodeType(SHAPE) == 'nurbsCurve':
		CURVE=SEL
	else:
		EDG=cmds.filterExpand(sm=32,ex=True)
		if not EDG:
			EDG=cmds.polyListComponentConversion(te=True)
			cmds.select(EDG,r=True)
		
		CURVE=cmds.polyToCurve(form=2,degree=1)
		if V_SPAN>1:
			CURVE_QUANTITY = len(cmds.filterExpand(EDG,sm=32,ex=True))
			cmds.rebuildCurve(CURVE,ch=1,rpo=1,rt=0,end=0,kr=0,kcp=0,kep=0,kt=0,s=0,d=3,tol=0.01)
	cmds.xform(CURVE,cp=True)

	#プロファイルカーブ関連
	if SELCURVE:
		PROFCURVE=['','']
		PROFCURVE[0]=SELCURVE
		PROFCURVE[1]=cmds.listRelatives(SELCURVE,s=True)[0]
		cmds.makeIdentity(PROFCURVE[0],a=True,pn=True,r=True)

	else:
		PROFCURVE=cmds.circle(ch=True,o=True,nr=[0,1,0],r=RADIUS,degree=1,sections=SPAN)
		cmds.xform(PROFCURVE[0],r=True,ro=[-90,0,ROTATE])
		cmds.makeIdentity(PROFCURVE[0],a=True,pn=True,r=True)
		
	#エクストルード実行
	extruded_surface=cmds.extrude(PROFCURVE[0],CURVE[0]
		,ch = True
		,fixedPath = True
		,range = True
		,polygon = 0
		,extrudeType = 2 #押し出しのタイプ(距離 - 0、フラット - 1、チューブ - 2)
		,useComponentPivot = 1 #パスの最近接終点 - 0、コンポーネント ピボット - 1、プロファイルのバウンディング ボックスのセンター - 2 を使用 既定: 0
		,useProfileNormal = True
		,rotation = 0
		,scale = 1
		,reverseSurfaceIfPathReversed = True
		)

	#ポリゴン化
	TUBE=cmds.nurbsToPoly(extruded_surface[0]
		,matchNormalDir=True #フォーマットが CV の場合のみ使用します。true に設定されている場合、法線がオリジナル サーフェスの方向に一致するように CV を並べます
		,ch=True
		,format=3 #フォーマット: 0 - 三角形の数、1 - 標準フィット、2 - 一般、3 - CV
		,polygonType=1 #ポリゴン タイプ: 0 - 三角、1 - 四角
		,polygonCount=200 #作成するポリゴン数。フォーマットが三角形の数の場合のみ使用します。
		,chordHeightRatio=0.9 #弦の高さの比率は、サーフェス スパンの弦の長と弦の高さの比です(長さと高さの比率)。0 は非常に緩いフィットです。1 は非常にきついフィットです(弦の高さについての説明も参照)。フォーマットが標準フィットの場合は必ず使用します。それ以外の場合は、フォーマットが一般で useChordHeightRatio が true の場合のみ使用します。
		,fractionalTolerance=0.01 #端数の許容値。フォーマットが標準フィットの場合のみ使用します。
		,minEdgeLength=0.001 #最小エッジ長。フォーマットが標準フィットの場合のみ使用します
		,delta=0.1 #3D デルタ。フォーマットが標準フィットの場合のみ使用します
		,uType=2
		,uNumber=SPAN+1
		,vType=1
		,vNumber=V_SPAN*CURVE_QUANTITY
		,useChordHeight=0
		,useChordHeightRatio=0
		,chordHeight=0.01
		,edgeSwap=0 #エッジの入れ替えです。このアトリビュートは、四角を三角にテッセレーションするための最適な方法を決めるアルゴリズムを有効にします。フォーマットが一般の場合のみ使用します
		,normalizeTrimmedUVRange=0
		,mrt=0
		,uss=1
		)
	
	cmds.polySoftEdge(TUBE,angle=30)

	#ローテーションをとる
	if DELETE_HISTORY:
		cmds.delete(TUBE,ch=True)

	cmds.parent(TUBE[0],PROFCURVE[0])
	cmds.makeIdentity(TUBE[0],a=True,pn=True,r=True)
	cmds.parent(TUBE[0],w=True)
	cmds.xform(TUBE[0],cp=True)

	#Hideすべき素材をHide
	cmds.hide(extruded_surface)
	

	#作業用素材を消す
	if DELETE_HISTORY:
		cmds.delete(CURVE[0])
		if not SELCURVE:
			cmds.delete(PROFCURVE[0])
		cmds.delete(extruded_surface[0])

	attrSetup(CURVE,PROFCURVE[0],PROFCURVE[1],extruded_surface[0],extruded_surface[1],TUBE[0],TUBE[1],RADIUS,ROTATE,SPAN)
	return CURVE,PROFCURVE[0],PROFCURVE[1],extruded_surface[0],extruded_surface[1],TUBE[0],TUBE[1],RADIUS,ROTATE,SPAN



def MS_polyToCurve():
	CURVE = cmds.polyToCurve(form=2,degree=1)
	#0~1にリビルド
	cmds.rebuildCurve(CURVE,ch=1,rpo=1,rt=4,end=0,kr=0,kcp=0,kep=0,kt=0,s=0,d=3,tol=0.01)

def Layout_Extrude():
	cmds.columnLayout(adj=True)
	cmds.textField('SelectCurve',en=False)
	cmds.rowLayout(nc=2,cw2=[100,100])
	cmds.button('regProfCurve',w=100,c=lambda *args:SelectCurve())
	cmds.button('clear',w=100,c=lambda *args:SelectCurve_Clear())
	cmds.setParent('..')
	cmds.setParent('..')

def Layout_Tube():
	cmds.frameLayout(l='TubeOption',cl=False,cll=True)
	cmds.gridLayout(nc=2,cw=100,ch=20)
	cmds.text(l='TubeRadius')
	cmds.floatField('TubeRadius',v=20)
	cmds.text(l='TubeRotate')
	cmds.floatField('TubeRotate',v=45)
	cmds.text(l='TubeSubdivision')
	cmds.intField('TubeSubdivision',v=4)
	cmds.text(l='v_subdivision')
	cmds.intField('v_subdivision',v=1)
	cmds.setParent('..')
	cmds.setParent('..')


def Layout_Util():
	cmds.frameLayout(l='Util',cl=False,cll=True)
	cmds.columnLayout(adj=True)
	cmds.button('polyToCurve',w=100,c=lambda *args:MS_polyToCurve())
	cmds.button('extraAttrCrear',w=100,c=lambda *args:extraAttrCrear())
	cmds.setParent('..')
	cmds.setParent('..')


def LayoutA():
	cmds.columnLayout('MS_createTube.py_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_createTube.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	Layout_Extrude()
	Layout_Tube()
	

	cmds.checkBox('DELETE_HISTORY',l='delete History',v=False)
	cmds.button(l='do',bgc=[0.8,0.9,0.8],h=30,c=lambda *args:main())
	
	Layout_Util()

	cmds.separator()
	cmds.setParent('..')


def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	



