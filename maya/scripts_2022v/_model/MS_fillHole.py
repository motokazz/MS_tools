# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_fillHole
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import os

import _uv.MS_bestUVSize as MS_bestUVSize
reload(MS_bestUVSize)

#execCheckList
#import MS_module.MS_execCheck
#reload(MS_module.MS_execCheck)
#MS_module.MS_execCheck.execCheckSafe('MS_fillHole.py')

DICT_MAT={
	'TEMP':['MAT_MS_TEMP','D:/Projects/Gravite2/graphic/bg/textures/rock/az2rock_kk_04_c.tif']
	,'STONE':['MAT_MS_TEMP_STONE','D:/Projects/Gravite2/graphic/bg/textures/rock/az2rock_kk_04_c.tif']
	,'METAL':['MAT_MS_TEMP_METAL','D:/Projects/Gravite2/graphic/bg/textures/metal/metal_nt_01_c.tif']
	,'WOOD':['MAT_MS_TEMP_WOOD','D:/Projects/Gravite2/graphic/bg/textures/object/wood_sk_02_c.tif']
	,'RUBBLE':['MAT_MS_TEMP_RUBBLE','D:/Projects/Gravite2/graphic/bg/textures/ground/gareki_ms_01_c.tif']
	,'HEAP':['MAT_MS_TEMP_HEAP','D:/Projects/Gravite2/graphic/bg/textures/wall/pi_wall_kk_05_c.tif']
}

def selectMaterialFromMesh(SEL):
	cmds.select(SEL,r=True)
	if not SEL:
		return
	cmds.hyperShade(smn=True)
	MATS=cmds.ls(sl=True,type=['G2_BG_Main'])
	return MATS[0]

def createTempMaterial(FACE=[],MAT_NAME='MAT_MS_TEMP'):
	if not FACE:
		FACE=cmds.ls(sl=True)
	if not cmds.objExists(MAT_NAME):
		MAT_NAME=cmds.shadingNode('G2_BG_Main',asShader=True,n=MAT_NAME)
	if not FACE:#メッシュ選択がなければマテリアル作るだけ
		return
	cmds.select(FACE,r=True)
	cmds.hyperShade(a=MAT_NAME)

	return MAT_NAME

def createFTN(TXN=''):
	RET=[False,False]

	#
	FILE=cmds.ls(type='file')
	for each in FILE:
		EACH_FTN=cmds.getAttr(each+'.fileTextureName')
		if TXN==EACH_FTN:
			RET[0]=each

		if TXN.replace('_c.','_n.')==EACH_FTN:
			RET[1]=each
		elif TXN.replace('_c.','_na.')==EACH_FTN:
			RET[1]=each

		if RET[0] and RET[1]:
			break

	if not RET[0]:
		if os.path.exists(TXN):
			COL=cmds.shadingNode('file',asTexture=True)
			cmds.setAttr(COL+'.fileTextureName',TXN,type='string')
			RET[0]=COL


	if not RET[1]:
		if  os.path.exists(TXN.replace('_c.','_n.')):
			NRM=cmds.shadingNode('file',asTexture=True)
			cmds.setAttr(NRM+'.fileTextureName',TXN.replace('_c.','_n.'),type='string')
			RET[1]=NRM
		elif os.path.exists(TXN.replace('_c.','_na.')):
			NRM=cmds.shadingNode('file',asTexture=True)
			cmds.setAttr(NRM+'.fileTextureName',TXN.replace('_c.','_na.'),type='string')
			RET[1]=NRM

	return RET

def connectTextureToMat(MAT_NAME,FTN=[]):
	
	if FTN[0]:
		if not cmds.isConnected(FTN[0]+'.outColor',MAT_NAME+'.color'):
			cmds.connectAttr(FTN[0]+'.outColor',MAT_NAME+'.color')
	
	if FTN[1]:
		if not cmds.isConnected(FTN[1]+'.outColor',MAT_NAME+'.normal'):
			cmds.connectAttr(FTN[1]+'.outColor',MAT_NAME+'.normal')

def MS_quad():
	cmds.polyTriangulate(ch=False)
	cmds.polyQuad(a=50,kgb=True,ktb=True,khe=True,ws=True,ch=False)

def createMaterialTemplate(KEY='TEMP'):
	SEL=cmds.ls(sl=True,l=True)
	#マテリアルアサイン
	if KEY=='TEMP':
		MAT_NAME=selectMaterialFromMesh(SEL)
		createTempMaterial(NEW_FACE,MAT_NAME)
	else:
		MAT_NAME=DICT_MAT[KEY][0]
		createTempMaterial([],MAT_NAME)

		TXN=DICT_MAT[KEY][1]
		FTN=createFTN(TXN)

		connectTextureToMat(MAT_NAME,FTN)

	#
	cmds.select(SEL,r=True)
	bestUV()

def bestUV():
	POST_FACE=cmds.polyListComponentConversion(tf=True)
	FACE=cmds.filterExpand(POST_FACE,ex=True,sm=34)
	
	cmds.polyAutoProjection(FACE,ch=False)
	
	#MS_bestUVSize
	if cmds.control('MS_fillHole_main_window',q=True,ex=True):
		TEX_SIZE=cmds.intFieldGrp('textureSize',q=True,v1=True)
		SIZE_PER_PIX=cmds.floatFieldGrp('polySizePerPixels',q=True,v1=True)
	else:
		TEX_SIZE=1024
		SIZE_PER_PIX=0.5
	MS_bestUVSize.docore(OBJ=[],POLYS=FACE,TEX_SIZE_U=TEX_SIZE,TEX_SIZE_V=TEX_SIZE,SIZE_PER_PIX=SIZE_PER_PIX)


#################
# CORE
#################
def do(KEY='TEMP'):
	SEL=cmds.ls(sl=True)
	if cmds.nodeType(SEL[0])=='transform':
		for each in SEL:
			cmds.select(each,r=True)
			core(KEY)
	else:
		core(KEY)

def core(KEY='TEMP'):
	SEL=cmds.ls(sl=True)
	
	#事前リスト
	cmds.select(SEL,r=True)
	PRE_FACE=cmds.polyListComponentConversion(tf=True)
	PRE_COMP=cmds.filterExpand(PRE_FACE,ex=True,sm=34)
	
	#
	cmds.polyCloseBorder(SEL,ch=False,n='test')
	
	#事後リスト
	cmds.select(SEL,r=True)
	POST_FACE=cmds.polyListComponentConversion(tf=True)
	
	POST_COMP=cmds.filterExpand(POST_FACE,ex=True,sm=34)
	
	#
	SET_AB=set(POST_COMP)-set(PRE_COMP)
	NEW_FACE=list(SET_AB)
	
	if not NEW_FACE:
		return
	
	cmds.polyAutoProjection(NEW_FACE,ch=False)
	
	#MS_bestUVSize
	TEX_SIZE=cmds.intFieldGrp('textureSize',q=True,v1=True)
	SIZE_PER_PIX=cmds.floatFieldGrp('polySizePerPixels',q=True,v1=True)
	for EACH in NEW_FACE:
		MS_bestUVSize.docore(OBJ=[],POLYS=[EACH],TEX_SIZE_U=TEX_SIZE,TEX_SIZE_V=TEX_SIZE,SIZE_PER_PIX=SIZE_PER_PIX)

	#マテリアルアサイン
	if KEY=='TEMP':
		MAT_NAME=selectMaterialFromMesh(SEL)
		createTempMaterial(NEW_FACE,MAT_NAME)
	else:
		MAT_NAME=DICT_MAT[KEY][0]
		createTempMaterial(NEW_FACE,MAT_NAME)

		TXN=DICT_MAT[KEY][1]
		FTN=createFTN(TXN)

		connectTextureToMat(MAT_NAME,FTN)

	
	cmds.select(NEW_FACE,r=True)
	
	if cmds.checkBox('MS_quad',q=True,v=True):
		MS_quad()


#################
# UI
#################
def layoutB(
	LABEL='MaterialTemplate'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)

	cmds.gridLayout(cw=50,nc=5)
	
	for each in DICT_MAT.keys():
		cmds.button(l=each,c=lambda *args:createMaterialTemplate(KEY=each))
	#cmds.button(l=u'TEMP',c=lambda *args:createMaterialTemplate())
	#cmds.button(l=u'STONE',c=lambda *args:createMaterialTemplate(KEY='STONE'))
	#cmds.button(l=u'METAL',c=lambda *args:createMaterialTemplate(KEY='METAL'))
	#cmds.button(l=u'WOOD',c=lambda *args:createMaterialTemplate(KEY='WOOD'))
	#cmds.button(l=u'RUBBLE',c=lambda *args:createMaterialTemplate(KEY='RUBBLE'))
	cmds.setParent('..')
	
	cmds.setParent('..')
	cmds.setParent('..')

def layoutA(
	LABEL='MS_fillHole'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.checkBox('MS_bestUVSize',v=True)
	cmds.checkBox('MS_quad',v=True)
	cmds.intFieldGrp('textureSize',l='textureSize',v1=512)
	cmds.floatFieldGrp('polySizePerPixels',l='polySizePerPixels',v1=0.5)
	#
	cmds.gridLayout(cw=50,nc=5)
	for each in DICT_MAT.keys():
		cmds.button(l=each,c=lambda *args:do(KEY=each))
	#cmds.button(l=u'TEMP',c=lambda *args:do())
	#cmds.button(l=u'STONE',c=lambda *args:do(KEY='STONE'))
	#cmds.button(l=u'METAL',c=lambda *args:do(KEY='METAL'))
	#cmds.button(l=u'WOOD',c=lambda *args:do(KEY='WOOD'))
	#cmds.button(l=u'RUBBLE',c=lambda *args:do(KEY='RUBBLE'))
	cmds.setParent('..')
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_fillHole_main_window',q=True,ex=True):
		cmds.deleteUI('MS_fillHole_main_window')
	cmds.window('MS_fillHole_main_window',rtf=True,s=True)
	
	layoutA()

	layoutB()
	
	cmds.showWindow('MS_fillHole_main_window')
	


