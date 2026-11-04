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

#execCheckList
import MS_module.MS_execCheck
reload(MS_module.MS_execCheck)
MS_module.MS_execCheck.execCheckSafe('MS_bestUVSize.py')

def selectInSelectedObjectWithMaterial():
	import MS_selectInSelectedObjectWithMaterial
	reload(MS_selectInSelectedObjectWithMaterial)
	MS_selectInSelectedObjectWithMaterial.do()
############################

THIS_SCRIPT='MS_bestUVSize'

##### プラグインチェッカー #####
	
if not cmds.pluginInfo('mpCalcUVArea.mll',q=True,loaded=True):
	cmds.loadPlugin('mpCalcUVArea.mll')
	
if not cmds.pluginInfo('mpCalcPolyArea.py',q=True,loaded=True):
	cmds.loadPlugin('mpCalcPolyArea.py')
	
	
##################
#####ユーティリティ
##################
	
def getFaces(CONP):#フェース選択
	FACE=cmds.polyListComponentConversion(CONP,tf=True)
	result=cmds.filterExpand(FACE,ex=True,sm=34)
	return result
	
def getEdges(CONP):#エッジ選択
	EDGE=cmds.polyListComponentConversion(CONP,te=True)
	result=cmds.filterExpand(EDGE,ex=True,sm=32)
	return result
	
def getVerts(CONP):#頂点選択
	VTX=cmds.polyListComponentConversion(CONP,tv=True)
	result=cmds.filterExpand(VTX,ex=True,sm=31)
	return result
	
def getUV(CONP):#頂点選択
	UV=cmds.polyListComponentConversion(CONP,tuv=True)
	result=cmds.filterExpand(UV,ex=True,sm=35)
	return result
	
def edgeLength(EDGE):#エッジの長さ計算
	POINTS=getVerts(EDGE)
	POINT_A = cmds.xform(POINTS[0],q=True,ws=True,t=True)
	POINT_B = cmds.xform(POINTS[1],q=True,ws=True,t=True)
	LEN = math.sqrt((POINT_B[0]-POINT_A[0])**2+(POINT_B[1]-POINT_A[1])**2+(POINT_B[2]-POINT_A[2])**2)
	return LEN
	
def edgeUVLength(EDGE):#エッジのUV長さ計算
	POINTS=getUV(EDGE)
	POINT_A = cmds.polyEditUV(POINTS[0],q=True,u=True,v=True)
	POINT_B = cmds.polyEditUV(POINTS[1],q=True,u=True,v=True)
	LEN = math.sqrt((POINT_A[0]-POINT_B[0])**2+(POINT_A[1]-POINT_B[1])**2)
	
	return LEN
	
def getUVLength(POINTS):#エッジのUV長さ計算
	POINT_A = cmds.polyEditUV(POINTS[0],q=True,u=True,v=True)
	POINT_B = cmds.polyEditUV(POINTS[1],q=True,u=True,v=True)
	LEN = math.sqrt((POINT_A[0]-POINT_B[0])**2+(POINT_A[1]-POINT_B[1])**2)
	
	return LEN
	
def lengthCompEdge(EDG):#頂点に隣接するフェースを面積比較してソート済みリスト作成
	RET=[]
	for EACH_EDG in EDG:
		LENGTH=edgeLength(EACH_EDG)
		RET.append([EACH_EDG,LENGTH])
	return sorted(RET,key=lambda x:x[1],reverse=True)
	
def distance(TARGET_A,TARGET_B):
	
	POINT_A = cmds.xform(TARGET_A,q=True,ws=True,t=True)
	POINT_B = cmds.xform(TARGET_B,q=True,ws=True,t=True)
	#2点間の移動距離を計算
	LEN = math.sqrt((POINT_A[0]-POINT_B[0])*(POINT_A[0]-POINT_B[0])+(POINT_A[1]-POINT_B[1])*(POINT_A[1]-POINT_B[1])+(POINT_A[2]-POINT_B[2])*(POINT_A[2]-POINT_B[2]))
	
	return LEN
	
	
##### UVTool
	
def addList():
	COMP=cmds.filterExpand(ex=True,sm=[35])
	if not COMP:
		clearList()
		return
	AI=cmds.textScrollList('MS_PIPEUV_list',q=True,ai=True)
		
	if not AI:
		AI=''
	clearList()
	
	for EACH in AI:
		if EACH in COMP:
			cmds.textScrollList('MS_PIPEUV_list',e=True,append=EACH)
	for EACH in COMP:
		if not EACH in AI:
			cmds.textScrollList('MS_PIPEUV_list',e=True,append=EACH)

def clearList():
	cmds.textScrollList('MS_PIPEUV_list',e=True,ra=True)


def jobPipeUV():
	jobNum = cmds.scriptJob(e=["SelectionChanged",THIS_SCRIPT+".addList()"],parent='MS_bestUVSize_main_window',protected=True)
	
def pipeUV():
	#EDGES=cmds.filterExpand(sm=32)
	UVS=cmds.textScrollList('MS_PIPEUV_list',q=True,ai=True)
	TOTAL_EDGE_LENGTH=0.0
	EDGE_LIST=[]
	
	for EACH in range(len(UVS)-1):
		TOTAL_EDGE_LENGTH+=getUVLength([UVS[EACH],UVS[EACH+1]])
	
	BEFOR_V=0.0
	cmds.polyEditUV(UVS[0],r=False,u=0.0,v=BEFOR_V)
	for EACH in range(len(UVS)-1):
		UVPOS=getUVLength([UVS[EACH],UVS[EACH+1]])/TOTAL_EDGE_LENGTH
		cmds.polyEditUV(UVS[EACH+1],r=False,u=0.0,v=UVPOS)
		print UVS[EACH]
		
		
		
		
##### createUVmap
	
def bestPlanePerPoly(SEL=[],TEX_SIZE=1024,SIZE_PER_PIX=0.5,considerUVIsland=True):
	
	if not SEL:
		preFACES=cmds.polyListComponentConversion(tf=True)
	else:
		preFACES=cmds.polyListComponentConversion(SEL,tf=True)
	
	FACES=cmds.filterExpand(preFACES,sm=34,ex=True)
	for EACH in FACES:
		cmds.select(EACH,r=True)
		cmds.polyProjection(EACH,ch=False,type='Planar',ibd=False,kir=True,md='b')
		#cmds.select(EACH,r=True)
		fitUVbyArea([EACH],TEX_SIZE=TEX_SIZE,SIZE_PER_PIX=SIZE_PER_PIX,considerUVIsland=considerUVIsland)
	cmds.select(FACES,r=True)
	
def bestPlaneProjection(SEL=[],TEX_SIZE=1024,SIZE_PER_PIX=0.5):
	if not SEL:
		SEL=cmds.ls(sl=True)
	cmds.polyProjection(SEL,ch=False,type='Planar',ibd=False,kir=True,md='b')
	fitUVbyArea(SEL,TEX_SIZE=TEX_SIZE,SIZE_PER_PIX=SIZE_PER_PIX,considerUVIsland=True)
	
###################
#####フィットUVコア
###################
	
def fitUV(Q=False):#一番長いエッジを利用してUVサイズをフィッティング
	POLYS=cmds.ls(sl=True)
	if not POLYS:
		return
	TEX_SIZE=cmds.intField('MS_bestUVSize_texsize',q=True,v=True)
	SIZE_PER_PIX=cmds.floatField('MS_bestUVSize_sizeperpix',q=True,v=True)
#	for EACH in POLYS:
	OBJ=cmds.polyListComponentConversion(POLYS,fe=True,fuv=True,ff=True,fvf=True,toEdge=True)
	EDG=cmds.filterExpand(OBJ,ex=True,sm=32)
	
	LONGEST_EDGE=lengthCompEdge(EDG)[0]
	UVLENGTH=edgeUVLength(LONGEST_EDGE[0])
	SVALUE=((LONGEST_EDGE[1]*(10/SIZE_PER_PIX))/(UVLENGTH*TEX_SIZE))
	
	if Q:
		print '-------------------------------------------------'
		print 'longestEdge = '+LONGEST_EDGE[0]
		print 'longestEdgeLength = '+str(LONGEST_EDGE[1])
		print 'sizePerPixels = '+str(LONGEST_EDGE[1]*(10/SIZE_PER_PIX))
		print 'longestEdgeUVLength = '+str(UVLENGTH)+'*'+str(TEX_SIZE)+'='+str(UVLENGTH*TEX_SIZE)
		print 'size gap = '+str(SVALUE)
		print '-------------------------------------------------'
	else:
		cmds.select(getUV(POLYS),r=True)
		cmds.polyEditUV(scaleU=SVALUE,scaleV=SVALUE,pivotU=0.5,pivotV=0.5)
		
	cmds.select(POLYS,r=True)

#####
	
def selectShell(OBJ='',MODE='edge'):
	if not OBJ:
		OBJ=cmds.ls(sl=True)
	cmds.select(OBJ,r=True)
	if MODE=='vtx':
		cmds.select(cmds.polyListComponentConversion(tv=True),r=True)
		cmds.polySelectConstraint(t=0x0001,m=2,sh=False,bo=True,pp=3)
		RET=cmds.filterExpand(sm=31)
	if MODE=='edge':
		cmds.select(cmds.polyListComponentConversion(te=True),r=True)
		cmds.polySelectConstraint(t=0x8000,m=2,sh=False,bo=True,pp=3)
		RET=cmds.filterExpand(sm=32)
	if MODE=='face':
		cmds.select(cmds.polyListComponentConversion(tf=True),r=True)
		cmds.polySelectConstraint(t=0x0008,m=2,sh=False,bo=True,pp=3)
		RET=cmds.filterExpand(sm=34)
	if MODE=='uv':
		cmds.select(cmds.polyListComponentConversion(tuv=True),r=True)
		cmds.polySelectConstraint(t=0x0010,m=2,sh=False,bo=True,pp=3)
		RET=cmds.filterExpand(sm=35)
			
	cmds.polySelectConstraint(dis=True)
	
	return RET
	
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
	
def fitUVbyArea(POLYS=[],Q=False,TEX_SIZE=1024,SIZE_PER_PIX=0.5,considerUVIsland=True):#フェースを利用してUVサイズをフィッティング
	if not POLYS:
		POLYS=cmds.ls(sl=True)
		if not POLYS:
			return
	
	def docore(OBJ):
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
			
			for COMPLIST in COMPLISTS:
				CurrentUVSet=cmds.polyUVSet(COMPLIST,q=True,cuv=True)[0]
				POLY=cmds.polyListComponentConversion(COMPLIST,tf=True)
				cmds.select(POLY,r=True)
				POLY_AREA=mel.eval('mpCalcPolyArea')
				UV_AREA=mel.eval('mpCalcUVArea -set %s' % CurrentUVSet)
				try:
					#SVALUE=math.sqrt((POLY_AREA*(10/SIZE_PER_PIX**2))/(UV_AREA*TEX_SIZE**2))
					SVALUE=math.sqrt((POLY_AREA*(100/SIZE_PER_PIX**2))/(UV_AREA*TEX_SIZE**2))
				except:
					SVALUE=1
				
				if Q:
					print '-------------------------------------------------'
					print 'polyArea = '+str(POLY_AREA)
					print 'sizePerPixels = '+str(POLY_AREA*(10/SIZE_PER_PIX)**2)
					print 'uvArea = '+str(UV_AREA)+'*'+str(TEX_SIZE**2)+'='+str(UV_AREA*TEX_SIZE**2)
					print 'size gap = '+str(SVALUE)
					print '-------------------------------------------------'
				else:
					cmds.select(COMPLIST,r=True)
					#cmds.polyNormalizeUV(COMPLIST,uvs=CurrentUVSet,normalizeType=1,preserveAspectRatio=True)
					cmds.polyEditUV(uvs=CurrentUVSet,scaleU=SVALUE,scaleV=SVALUE,pivotU=0.5,pivotV=0.5)
						
	if cmds.nodeType(POLYS[0])=='transform':
		for EACH in POLYS:
			CurrentUVSet=cmds.polyUVSet(EACH,q=True,cuv=True)[0]
			cmds.polyNormalizeUV(EACH,uvs=CurrentUVSet,normalizeType=1,ch=False,preserveAspectRatio=True)
			EACHPOLYS=cmds.polyListComponentConversion(EACH,tf=True)
			docore(EACHPOLYS)
	else:
		docore(POLYS)
	
	cmds.select(POLYS,r=True)
	
def pre_fitUVbyArea(Q=False):
	TEX_SIZE=cmds.intField('MS_bestUVSize_texsize',q=True,v=True)
	SIZE_PER_PIX=cmds.floatField('MS_bestUVSize_sizeperpix',q=True,v=True)
	considerUVIsland=cmds.checkBox('MS_bestUVSize_considerUVIsland',q=True,v=True)
	fitUVbyArea(POLYS=[],Q=Q,TEX_SIZE=TEX_SIZE,SIZE_PER_PIX=SIZE_PER_PIX,considerUVIsland=considerUVIsland)
	
def putField_a():
	cmds.textField('MS_bestUVSize_textField_a',e=True,tx=cmds.ls(sl=True)[0])
	
def putField_b():
	cmds.textField('MS_bestUVSize_textField_b',e=True,tx=cmds.ls(sl=True)[0])
	
def resizeUV():
	CONP=cmds.ls(sl=True)
	SVALUE=cmds.floatSliderGrp('MS_bestUVSize_size',q=True,v=True)
	
	cmds.polyEditUV(getUV(CONP),scaleU=SVALUE,scaleV=SVALUE,pivotU=0.5,pivotV=0.5)
	
def ditectPivottest():
	print 'v'
	CONP=cmds.ls(sl=True)
	print cmds.polyEditUV(getUV(CONP),q=True,pivotU=True)
	print 'v'


##### UI
	
def layoutPipeUV():
	cmds.frameLayout('PIPEUV',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'PIPEUV',cll=True,cl=True)
	cmds.columnLayout()
	cmds.button(w=150,l=u'PIPEUV',c=lambda *args:pipeUV())
	cmds.separator(w=200)
	cmds.button(w=150,l=u'addlist',c=lambda *args:addList())
	cmds.textScrollList('MS_PIPEUV_list',h=100)
	cmds.button(w=150,l=u'clearlist',c=lambda *args:clearList())
	cmds.setParent('..')
	cmds.setParent('..')
	
def getTextureSize():
	#選択ファイルテクスチャノードからサイズを取得
	TEX=cmds.ls(sl=True,typ='file')
	TEX_SIZE=cmds.getAttr(TEX[0]+'.outSize')
	cmds.intField('MS_bestUVSize_texsize',e=True,v=int(TEX_SIZE[0][0]))
	
def layoutA():#main
	cmds.frameLayout('MS_bestUVSize_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'MS_bestUVSize',cll=True,cl=False)
	cmds.columnLayout()
	
	cmds.text(l='textureSize')
	cmds.rowLayout(nc=2)
	cmds.intField('MS_bestUVSize_texsize',w=150,v=1024)
	cmds.button(l='getSize',w=50,c=lambda *args:getTextureSize(),ann='選択ファイルテクスチャノードからサイズを取得')
	cmds.setParent('..')
	
	cmds.text(l='polySize perPixels')
	cmds.floatField('MS_bestUVSize_sizeperpix',w=150,v=0.5)
	cmds.checkBox('MS_bestUVSize_considerUVIsland',l='considerUVIsland',v=True)
	#cmds.button(w=150,l=u'fitUV',c=lambda *args:fitUV())
	#cmds.button(w=150,l=u'checkGap',c=lambda *args:fitUV(Q=True))
	cmds.separator(w=100)
	cmds.button(w=150,l=u'fitUVbyArea',c=lambda *args:pre_fitUVbyArea())
	cmds.button(w=150,l=u'checkGap',c=lambda *args:pre_fitUVbyArea(Q=True))
	cmds.setParent('..')
	cmds.setParent('..')
	
def layoutB():#uvTools
	cmds.frameLayout('MS_bestUVSize_size_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'MS_UVSize',cll=True,cl=True)
	cmds.columnLayout()
	cmds.floatSliderGrp('MS_bestUVSize_size',w=150,v=1,field=True,min=0,max=10)
	cmds.button(w=150,l=u'resizeUV',c=lambda *args:resizeUV())
	cmds.button(w=150,l=u'ditect',c=lambda *args:ditectPivottest())
	cmds.button(w=150,l=u'bestPlanePerPoly',c=lambda *args:bestPlanePerPoly())
	cmds.setParent('..')
	cmds.setParent('..')
	
def layoutUVTools():#uvTools
	cmds.frameLayout('MS_bestUVSize_UVTools_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'UVTools',cll=True,cl=False)
	cmds.columnLayout()
	cmds.button(w=150,l=u'selectInSelectedObjectWithMaterial',c=lambda *args:selectInSelectedObjectWithMaterial())
	cmds.button(w=150,l=u'bestPlanePerPoly',c=lambda *args:bestPlanePerPoly())
	cmds.setParent('..')
	cmds.setParent('..')
	
	
	
	
def UI():
	if cmds.window('MS_bestUVSize_main_window',q=True,ex=True):
		cmds.deleteUI('MS_bestUVSize_main_window')
	cmds.window('MS_bestUVSize_main_window',rtf=True,s=True)
	cmds.columnLayout()
	layoutA()
	layoutB()
	layoutUVTools()
	layoutPipeUV()

	jobPipeUV()
	cmds.setParent('..')
	cmds.showWindow('MS_bestUVSize_main_window')
	
def MS_bestUVSize():
	UI()


