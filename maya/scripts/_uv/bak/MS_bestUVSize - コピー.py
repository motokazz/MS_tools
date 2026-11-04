# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_bestUVSize
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel
import math

import maya.OpenMaya as om

import MS_texCheckResolution
reload(MS_texCheckResolution)
	

THIS_SCRIPT='MS_bestUVSize'

########
# calc
########

class MS_calcPolyScale():
# ポリゴンオブジェクトの面積を求めるclass。実行MethodはdoIt＿～。引数はポリゴンオブジェクト。
# 面積の合計を返す
	def transFaceIt(self,  targetObject):
#オブジェクトをいれるとＦａｃｅＩｔｅｒａｔｏｒを返す
		sel = om.MSelectionList()
		sel.add(targetObject)
		dagPath = om.MDagPath()
		obj = om.MObject()
		sel.getDagPath(0,  dagPath, obj)
		return om.MItMeshPolygon(dagPath, obj)
	def areaTriangle(self, aP, bP, cP):
#三つの点で三角形の面積を計算
		v1 = om.MVector(bP - aP)
		v2 = om.MVector(cP - aP)		
		return (v1 ^ v2).length() * 0.5
	def doIt_PolyScale(self,  targetObject):
#ポリゴンオブジェクトのＦａｃｅ面積を求める
		currentFace = self.transFaceIt(targetObject)			
		scaleTotal = 0		
		while not currentFace.isDone():				
			pointArr = om.MPointArray()
			intArr = om.MIntArray()				
			currentFace.getTriangles(pointArr, intArr, om.MSpace.kWorld)				
			for x in range(pointArr.length() / 3):					
				scaleTotal += self.areaTriangle(pointArr[0 + (x*3)], pointArr[1 + (x*3)], pointArr[2 + (x*3)])					
			currentFace.next()					
		return scaleTotal
	def doIt_BBoxScale(self,  targetObject):
#オブジェクトのBoundingBoxの面積を求める
		BBcoord = mc.xform(targetObject,  q=1,  bb=1)
		scaleTotal = (BBcoord[3] - BBcoord[0]) * (BBcoord[4] - BBcoord[1]) * (BBcoord[5] - BBcoord[2])
		return scaleTotal
	def isItPolygonMesh(self, targetList):
#オブジェクトがポリゴンオブジェクトかどうかを検査する。
		try:
			polyMeshObj = mc.filterExpand(targetList,  sm=12)
		except:
			return 0
		else:
			if polyMeshObj and len(targetList) == len(polyMeshObj):
				if len(polyMeshObj) > 1:								  
					return 1
				elif len(polyMeshObj) < 2:				
					return 0
			else:				
				return 0

def exec_MS_calcPolyScale():
	CPS=MS_calcPolyScale()
	scaleResult=[]
	TOTAL=0
	targetList = cmds.ls(sl=True,l=True)
	
	for x in targetList:
		TEMP=0
		SEL=cmds.listRelatives(x,ad=True,type='mesh',f=True)

		#BBox
		XF = cmds.xform(x,q=True,bb=True,ws=True)
		BBSize=((XF[3]-XF[0])*(XF[4]-XF[1])*(XF[5]-XF[2]))


		#calcPolyArea
		for EACH in SEL:
			EACH_MESH_TRN=cmds.listRelatives(EACH,p=True,type='transform',f=True)[0]
			POLYAREA=CPS.doIt_PolyScale(EACH_MESH_TRN)
			TEMP+=POLYAREA

		#mat
		cmds.select(SEL,r=True)
		cmds.hyperShade(smn=True)
		MATS=cmds.ls(sl=True,mat=True)

		print x.split('|')[-1]+'\t'+str(TEMP)+'\t'+str(long(BBSize))+'\t'+str(len(MATS))

		scaleResult.append(EACH_MESH_TRN+'\t'+str(TEMP))
	
	return scaleResult

def calcPolyArea():
	sl=om.MSelectionList()
	om.MGlobal.getActiveSelectionList(sl)
	it=om.MItSelectionList(sl,om.MFn.kMeshPolygonComponent)
	dp=om.MDagPath()
	comp=om.MObject()
	result=0.0
	while it.isDone() is False:
		it.getDagPath(dp,comp)
		itMeshPoly=om.MItMeshPolygon(dp,comp)
		while itMeshPoly.isDone() is False:
			aP=om.MPointArray()
			aVtxList=om.MIntArray()
			itMeshPoly.getTriangles(aP,aVtxList,om.MSpace.kWorld)
			nTri=int(aVtxList.length()/3)
			i=0
			for i in range(nTri):
			#while i<nTri:
				try:
					idx=i*3

					a=aP[idx].distanceTo(aP[idx+1])
					b=aP[idx+1].distanceTo(aP[idx+2])
					c=aP[idx+2].distanceTo(aP[idx])
					s=(a+b+c)/2.0
					_result=math.sqrt(s*(s-a)*(s-b)*(s-c))
					result=_result+result
				except:
					pass
				#i+=1

			itMeshPoly.next()
		it.next()
	return result

def calcUVArea(uvset=''):
	sl=om.MSelectionList()
	om.MGlobal.getActiveSelectionList(sl)
	it=om.MItSelectionList(sl,om.MFn.kMeshPolygonComponent)
	dp=om.MDagPath()
	comp=om.MObject()
	result=0.0
	iPoly=0
	while it.isDone() is False:
		it.getDagPath(dp,comp)
		itMeshPoly=om.MItMeshPolygon(dp,comp)
		mesh=om.MFnMesh(dp)
		aMeshU=om.MFloatArray()
		aMeshV=om.MFloatArray()
		if uvset=='': mesh.getUVs(aMeshU,aMeshV)
		else: mesh.getUVs(aMeshU,aMeshV,uvset)
		
		while itMeshPoly.isDone() is False:
			aP=om.MPointArray()
			aVtxList=om.MIntArray()
			itMeshPoly.getTriangles(aP,aVtxList)
			aU=[0.0,0.0,0.0]
			aV=[0.0,0.0,0.0]

			nTri=int(aVtxList.length()/3)
			
			i=0
			for i in range(nTri):
				try:
					index0 = om.MScriptUtil().asIntPtr()
					index1 = om.MScriptUtil().asIntPtr()
					index2 = om.MScriptUtil().asIntPtr()


					idx=i*3

					itMeshPoly.getUVIndex(aVtxList[idx],index0)
					i0 = om.MScriptUtil.getInt(index0)
					#print 'idx0 '+str(i0)
					
					itMeshPoly.getUVIndex(aVtxList[idx+1],index1)
					i1 = om.MScriptUtil.getInt(index1)
					#print 'idx1 '+str(i1)

					itMeshPoly.getUVIndex(aVtxList[idx+2],index2)
					i2 = om.MScriptUtil.getInt(index2)
					#print 'idx2 '+str(i2)

					aU[0]=aMeshU[i0]
					aU[1]=aMeshU[i1]
					aU[2]=aMeshU[i2]
					aV[0]=aMeshV[i0]
					aV[1]=aMeshV[i1]
					aV[2]=aMeshV[i2]

					a=(aU[0]-aU[2])*(aV[1]-aV[0])
					b=(aU[0]-aU[1])*(aV[2]-aV[0])

					_result=(abs(a-b))/2
					result=_result+result
					print result

				except:
					print 'error'
					pass

			itMeshPoly.next()
		it.next()
	return result


##################
#####ユーティリティ
##################

##### UVShell move to 0,1
def UVShellNormalize():
	SEL=cmds.ls(sl=True)
	UVIL = separateUVIslands(SEL)
	for each in UVIL:
		PU=cmds.polyEditUVShell(each[0],q=True)
		cmds.select(each,r=True)
		cmds.polyEditUVShell(u=-math.floor(PU[0]),v=-math.floor(PU[1]))

##### easy uv
def easyUV(SIZE_PER_PIX=0.002):
	UV=cmds.polyListComponentConversion(tuv=True)
	#cmds.unfold(UV,i=0,ss=0.001,gb=0,gmb=0,pub=0,ps=0,oa=1,us=False)
	cmds.unfold(UV,i=10000,ss=0.001,gb=0,gmb=0,pub=0,ps=0,oa=1,us=False)#なぜか2回やらないとまともにならない
	cmds.unfold(UV,i=10000,ss=0.001,gb=0,gmb=0,pub=0,ps=0,oa=2,us=False)#なぜか2回やらないとまともにならない
	cmds.unfold(UV,i=0,ss=0.001,gb=0,gmb=0.5,pub=0,ps=0,oa=0,us=True,s=SIZE_PER_PIX)
	cmds.polyMultiLayoutUV(UV, lm=0,sc=0,rbf=1,fr=1,ps=0.2,l=2,psc=0,su=1,sv=1,ou=0,ov=0)

def easyResize(SIZE_PER_PIX=0.002):
	UV=cmds.polyListComponentConversion(tuv=True)
	cmds.unfold(UV,i=0,ss=0.001,gb=0,gmb=0.5,pub=0,ps=0,oa=0,us=True,s=SIZE_PER_PIX)

##### createUVmap
	
def bestPlanePerPoly(SEL=[],TEX_SIZE=1024,SIZE_PER_PIX=0.002,considerUVIsland=True):
	
	if not SEL:
		preFACES=cmds.polyListComponentConversion(tf=True)
	else:
		preFACES=cmds.polyListComponentConversion(SEL,tf=True)
	
	FACES=cmds.filterExpand(preFACES,sm=34,ex=True)
	for EACH in FACES:
		cmds.select(EACH,r=True)
		cmds.polyProjection(EACH,ch=False,type='Planar',ibd=False,kir=True,md='b')
		cmds.select(EACH,r=True)
		cmds.unfold(i=0,ss=0.001,gb=0,gmb=0.5,pub=0,ps=0,oa=0,us=True,s=SIZE_PER_PIX)
	cmds.select(FACES,r=True)
	
def layoutUV():
	UV=cmds.polyListComponentConversion(tuv=True)
	cmds.polyMultiLayoutUV(UV, lm=0,sc=0,rbf=1,fr=1,ps=0.2,l=2,psc=0,su=1,sv=1,ou=0,ov=0)
	#cmds.polyLayoutUV(lm=0,sc=0,se=0,rbf=0,fr=1,ps=0.2,l=2,ch=False);

def bestPlaneProjection(TEX_SIZE=1024,PERCENTAGESPACE=0.002):
	SEL=cmds.ls(sl=True)
	cmds.polyAutoProjection(
		ch=False
		,layoutMethod=0
		,projectBothDirections=0
		,insertBeforeDeformers=1
		,planes=6
		,optimize=1
		,skipIntersect=False
		,scaleMode=1
		,layout=2
		,percentageSpace=PERCENTAGESPACE
		,createNewMap=False
		,ws=False
		)
	cmds.select(SEL,r=True)

###################
#####フィットUVコア
###################
	
def preservedList(ORG,RESERVE=[]):
	if not RESERVE:
		preRESERVE=cmds.textFieldButtonGrp('MS_hahen_preserveList',q=True,tx=True)
		RESERVE=preRESERVE.split(';')
	for EACH in RESERVE:
		while EACH in ORG:ORG.remove(EACH)
	return ORG
		
def separateUVIslands(UVS):
	#UVアイランドごとのUVリストを返す。
	#戻り値:[[アイランドのUVリスト１],[アイランドのUVリスト2],...]
	RET=[]
	cmds.select(UVS,r=True)
	cmds.select(cmds.polyListComponentConversion(tuv=True),r=True)
	UVS_EX=cmds.filterExpand(sm=35)
	while UVS_EX:
		cmds.select(UVS_EX[0])
		cmds.polySelectConstraint(t=0x0010,m=2,sh=True,bo=False,pp=0)
		TEMP=cmds.filterExpand(sm=35)
		UVS_EX=preservedList(UVS_EX,TEMP)
		RET.append(TEMP)
	cmds.polySelectConstraint(dis=True)
	return RET

#####
def listCompornentPerPoly(COMP):
	#オブジェクト複数選択時、オブジェクトごとのコンポーネントを辞書化
	#戻り値:{'オブジェクト名',[コンポーネントID]}
	DICT={}
	for EACH in COMP:
		TEMP=EACH.split('.')
		if not TEMP[0] in DICT.keys():
			DICT[TEMP[0]]=[TEMP[1]]
		else:
			DICT[TEMP[0]].append(TEMP[1])
	return DICT

##### フィットUV面積
def docore(OBJ,POLYS=[],Q=False,TEX_SIZE_U=1024,TEX_SIZE_V=1024,SIZE_PER_PIX=0.5,considerUVIsland=True):
	RET=[]
	DICT=listCompornentPerPoly(OBJ)
	for EACH in DICT.keys():
		preCOMP=[]
		COMPLIST=[]
		for EACHB in DICT[EACH]:
			preCOMP.append(EACH+'.'+EACHB)
		#UVShellで分ける
		if considerUVIsland:
			COMPLISTS=separateUVIslands(preCOMP)
		else:
			COMPLISTS=[preCOMP]
		#Shellごとに値リストを返す
		for COMPLIST in COMPLISTS:
			CurrentUVSet=cmds.polyUVSet(COMPLIST,q=True,cuv=True)[0]
			POLY=cmds.polyListComponentConversion(COMPLIST,tf=True)
			cmds.select(POLY,r=True)
			#エリア計測
			POLY_AREA=calcPolyArea()
			UV_AREA=calcUVArea(uvset=CurrentUVSet)

			#ギャップ計測
			try:
				SVALUE=math.sqrt((POLY_AREA*(SIZE_PER_PIX**2))/(UV_AREA*(TEX_SIZE_U*TEX_SIZE_V)))
				#SVALUE=math.sqrt(((POLY_AREA*SIZE_PER_PIX)**2)/((UV_AREA*TEX_SIZE*TEX_SIZE)**2))
				#SVALUE=math.sqrt((POLY_AREA*SIZE_PER_PIX**2)/(UV_AREA*TEX_SIZE**2))
			except:
				SVALUE=1

			if Q:
				cmds.floatField('MS_bestUVSize_checkGap',e=True,v=SVALUE)
				print '-------------------------------------------------'
				print 'polyArea = '+str(POLY_AREA)
				print 'sizePerPixels = '+str(POLY_AREA*(SIZE_PER_PIX**2))
				print 'uvArea = '+str(UV_AREA)+'*'+str(TEX_SIZE_U*TEX_SIZE_V)+'='+str(UV_AREA*TEX_SIZE_U*TEX_SIZE_V)
				print 'size gap = '+str(SVALUE)
				print '-------------------------------------------------'
			else:
				cmds.select(COMPLIST,r=True)
				#print COMPLIST
				#print  SVALUE
				#cmds.polyNormalizeUV(COMPLIST,uvs=CurrentUVSet,normalizeType=1,preserveAspectRatio=True)
				cmds.polyEditUV(COMPLIST , uvs=CurrentUVSet , scaleU=SVALUE , scaleV=SVALUE , pivotU=0.5 , pivotV=0.5 )

def fitUVbyArea(POLYS=[],Q=False,TEX_SIZE_U=1024,TEX_SIZE_V=1024,SIZE_PER_PIX=0.5,considerUVIsland=True):#フェースを利用してUVサイズをフィッティング
	if not POLYS:
		POLYS=cmds.ls(sl=True)
		if not POLYS:
			return
						
	if cmds.nodeType(POLYS[0])=='transform':
		for EACH in POLYS:
			CurrentUVSet=cmds.polyUVSet(EACH,q=True,cuv=True)[0]
			EACHPOLYS=cmds.polyListComponentConversion(EACH,tf=True)
			docore(EACHPOLYS,POLYS=POLYS,Q=Q,TEX_SIZE=TEX_SIZE,SIZE_PER_PIX=SIZE_PER_PIX,considerUVIsland=considerUVIsland)
	else:
		docore(POLYS,POLYS=POLYS,Q=Q,TEX_SIZE_U=TEX_SIZE_U,TEX_SIZE_V=TEX_SIZE_V,SIZE_PER_PIX=SIZE_PER_PIX,considerUVIsland=considerUVIsland)
	
	cmds.select(POLYS,r=True)
	
def pre_fitUVbyArea(Q=False):
	TEX_SIZE_U=cmds.intField('MS_bestUVSize_texsizeU',q=True,v=True)
	TEX_SIZE_V=cmds.intField('MS_bestUVSize_texsizeV',q=True,v=True)
	SIZE_PER_PIX=cmds.floatField('MS_bestUVSize_sizeperpix',q=True,v=True)
	considerUVIsland=cmds.checkBox('MS_bestUVSize_considerUVIsland',q=True,v=True)
	fitUVbyArea(POLYS=[],Q=Q,TEX_SIZE_U=TEX_SIZE_U,TEX_SIZE_V=TEX_SIZE_V,SIZE_PER_PIX=SIZE_PER_PIX,considerUVIsland=considerUVIsland)

def printCalcPoly():
	print calcPolyArea()
	print calcUVArea()

##### UI
	

def getTextureSize():
	#選択ファイルテクスチャノードからサイズを取得
	SEL=cmds.ls(sl=True)
	TEX=cmds.ls(sl=True,typ='file')
	if not TEX:
		cmds.hyperShade(smn=True)
		try:
			FTN=cmds.listConnections('.color')[0]
			if FTN:
				TEX_SIZE=cmds.getAttr(FTN+'.outSize')[0]
		except:
			TEX_SIZE=(0,0)
	else:
		TEX_SIZE=cmds.getAttr(TEX[0]+'.outSize')[0]

	cmds.intField('MS_bestUVSize_texsizeU',e=True,v=int(TEX_SIZE[0]))
	cmds.intField('MS_bestUVSize_texsizeV',e=True,v=int(TEX_SIZE[1]))
	
	cmds.select(SEL,r=True)

def layoutOldMethod():#main
	cmds.frameLayout('MS_bestUVSize_frameLayout',w=135,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'oldMethod',cll=True,cl=True)
	cmds.columnLayout()
	
	cmds.text(l='textureSize')
	cmds.rowLayout(nc=2,cw2=[50,50])
	cmds.intField('MS_bestUVSize_texsizeU',v=1024)
	cmds.intField('MS_bestUVSize_texsizeV',v=1024)
	cmds.setParent('..')
	cmds.button(l='getSize',c=lambda *args:getTextureSize(),ann='選択ファイルテクスチャノードからサイズを取得')
	
	cmds.text(l='1mayaUnits = ?Pixel')
	cmds.floatField('MS_bestUVSize_sizeperpix',w=100,v=2.0)
	cmds.checkBox('MS_bestUVSize_considerUVIsland',l='considerUVIsland',v=True)

	cmds.separator(w=100)
	cmds.floatField('MS_bestUVSize_checkGap',w=100,v=0.0)
	cmds.button(w=100,l=u'checkGap',c=lambda *args:pre_fitUVbyArea(Q=True))
	cmds.separator(w=100)
	cmds.button(w=100,l=u'fitUVbyArea',c=lambda *args:pre_fitUVbyArea())
	
	cmds.button(w=100,l=u'calcPoly',c=lambda *args:exec_MS_calcPolyScale())

	cmds.setParent('..')
	cmds.setParent('..')
	
def layoutUVTools():#uvTools
	cmds.frameLayout('MS_bestUVSize_UVTools_frameLayout',w=135,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'UVTools',cll=True,cl=False)
	cmds.columnLayout()
	#cmds.button(w=100,l=u'bestPlanePerPoly',c=lambda *args:bestPlanePerPoly())
	cmds.button(w=100,l=u'bestPlaneProjection',c=lambda *args:bestPlaneProjection())
	cmds.button(w=100,l=u'layoutUV',c=lambda *args:layoutUV())
	cmds.button(w=100,l=u'UVShellNormalize',c=lambda *args:UVShellNormalize())
	cmds.setParent('..')
	cmds.setParent('..')

def layoutEasyUV():#EasyUV
	cmds.frameLayout('MS_bestUVSize_layoutEasyUV_frameLayout',w=135,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'EasyUV',cll=True,cl=False)
	
	cmds.text(w=100,l=u'easyResize',bgc=(0.9,0.9,0.9))
	cmds.gridLayout(nc=4)
	cmds.button(w=100,l=u'256',c=lambda *args:easyResize(SIZE_PER_PIX=0.008))
	cmds.button(w=100,l=u'512',c=lambda *args:easyResize(SIZE_PER_PIX=0.004))
	cmds.button(w=100,l=u'1024',c=lambda *args:easyResize(SIZE_PER_PIX=0.002))
	cmds.button(w=100,l=u'2048',c=lambda *args:easyResize(SIZE_PER_PIX=0.001))
	cmds.setParent('..')

	cmds.text(w=100,l=u'unfold and layout',bgc=(0.9,0.9,0.9))
	cmds.gridLayout(nc=4)
	cmds.button(w=100,l=u'256',c=lambda *args:easyUV(SIZE_PER_PIX=0.008))
	cmds.button(w=100,l=u'512',c=lambda *args:easyUV(SIZE_PER_PIX=0.004))
	cmds.button(w=100,l=u'1024',c=lambda *args:easyUV(SIZE_PER_PIX=0.002))
	cmds.button(w=100,l=u'2048',c=lambda *args:easyUV(SIZE_PER_PIX=0.001))
	cmds.setParent('..')
	MS_texCheckResolution.LayoutA()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_bestUVSize_main_window',q=True,ex=True):
		cmds.deleteUI('MS_bestUVSize_main_window')
	cmds.window('MS_bestUVSize_main_window',rtf=True,s=True)
	cmds.columnLayout()

	#layoutPipeUV()
	layoutEasyUV()

	layoutUVTools()
	layoutOldMethod()
	cmds.setParent('..')
	cmds.showWindow('MS_bestUVSize_main_window')
	
def MS_bestUVSize():
	UI()


