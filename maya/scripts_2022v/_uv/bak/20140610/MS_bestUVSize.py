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

import MS_calcUVArea
reload(MS_calcUVArea)

import MS_calcPolyArea
reload(MS_calcPolyArea)

#execCheckList
#import MS_module.MS_execCheck
#reload(MS_module.MS_execCheck)
#MS_module.MS_execCheck.execCheckSafe('MS_bestUVSize.py')

THIS_SCRIPT='MS_bestUVSize'

##################
#####ユーティリティ
##################

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
	cmds.polyAutoProjection(SEL
		,ch=False
		,planes=6
		,optimize=1
		,skipIntersect=False
		,scaleMode=0
		,layout=2
		,percentageSpace=0
		,createNewMap=False
		)
	fitUVbyArea(SEL,TEX_SIZE=TEX_SIZE,SIZE_PER_PIX=SIZE_PER_PIX,considerUVIsland=True)
	
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
def fitUVbyArea(POLYS=[],Q=False,TEX_SIZE=1024,SIZE_PER_PIX=0.5,considerUVIsland=True):#フェースを利用してUVサイズをフィッティング
	if not POLYS:
		POLYS=cmds.ls(sl=True)
		if not POLYS:
			return
	print '1'
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
			print'2'
			for COMPLIST in COMPLISTS:
				CurrentUVSet=cmds.polyUVSet(COMPLIST,q=True,cuv=True)[0]
				POLY=cmds.polyListComponentConversion(COMPLIST,tf=True)
				cmds.select(POLY,r=True)

				#エリア計測
				cmds.polyTriangulate(POLY)#以下コマンドはTriangle化必須。

				POLY_AREA=MS_calcPolyArea.calcPolyArea()
				
				UV_AREA=MS_calcUVArea.calcUVArea(uvset=CurrentUVSet)
				
				#cmds.undo()
				#
				print '3'
				try:
					SVALUE=math.sqrt((POLY_AREA*(100/SIZE_PER_PIX**2))/(UV_AREA*TEX_SIZE**2))
				except:
					SVALUE=1
				print '4'
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
					print COMPLIST
					print CurrentUVSet
					print SVALUE
					cmds.polyEditUV(COMPLIST , uvs=CurrentUVSet , scaleU=SVALUE , scaleV=SVALUE , pivotU=0.5 , pivotV=0.5 )
						
	if cmds.nodeType(POLYS[0])=='transform':
		for EACH in POLYS:
			CurrentUVSet=cmds.polyUVSet(EACH,q=True,cuv=True)[0]
			#cmds.polyNormalizeUV(EACH,uvs=CurrentUVSet,normalizeType=1,ch=False,preserveAspectRatio=True)
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

##### UI
	

def getTextureSize():
	#選択ファイルテクスチャノードからサイズを取得
	TEX=cmds.ls(sl=True,typ='file')
	TEX_SIZE=cmds.getAttr(TEX[0]+'.outSize')
	cmds.intField('MS_bestUVSize_texsize',e=True,v=int(TEX_SIZE[0][0]))
	
def layoutA():#main
	cmds.frameLayout('MS_bestUVSize_frameLayout',w=107,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'MS_bestUVSize',cll=True,cl=False)
	cmds.columnLayout()
	
	cmds.text(l='textureSize')
	cmds.rowLayout(nc=2,cw2=[50,50])
	cmds.intField('MS_bestUVSize_texsize',v=1024)
	cmds.button(l='getSize',c=lambda *args:getTextureSize(),ann='選択ファイルテクスチャノードからサイズを取得')
	cmds.setParent('..')
	
	cmds.text(l='polySize perPixels')
	cmds.floatField('MS_bestUVSize_sizeperpix',w=100,v=0.5)
	cmds.checkBox('MS_bestUVSize_considerUVIsland',l='considerUVIsland',v=True)

	cmds.separator(w=100)
	
	cmds.button(w=100,l=u'fitUVbyArea',c=lambda *args:pre_fitUVbyArea())
	cmds.button(w=100,l=u'checkGap',c=lambda *args:pre_fitUVbyArea(Q=True))
	
	cmds.setParent('..')
	cmds.setParent('..')
	
def layoutUVTools():#uvTools
	cmds.frameLayout('MS_bestUVSize_UVTools_frameLayout',w=107,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'UVTools',cll=True,cl=False)
	cmds.columnLayout()
	cmds.button(w=100,l=u'bestPlanePerPoly',c=lambda *args:bestPlanePerPoly())
	cmds.button(w=100,l=u'bestPlaneProjection',c=lambda *args:bestPlaneProjection())
	cmds.setParent('..')
	cmds.setParent('..')
	
def UI():
	if cmds.window('MS_bestUVSize_main_window',q=True,ex=True):
		cmds.deleteUI('MS_bestUVSize_main_window')
	cmds.window('MS_bestUVSize_main_window',rtf=True,s=True)
	cmds.columnLayout()
	layoutA()
	layoutUVTools()
	#layoutPipeUV()

	cmds.setParent('..')
	cmds.showWindow('MS_bestUVSize_main_window')
	
def MS_bestUVSize():
	UI()


