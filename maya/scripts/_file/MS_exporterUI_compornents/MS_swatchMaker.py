# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_swatchMaker.py
# 説明
#			
# 作成日
#			
########################################
import maya.cmds as cmds
import maya.mel as mel
import shutil

import time

import MS_filePathUI as MS_filePathUI
reload(MS_filePathUI)

fpf=MS_filePathUI.filePathField()
fpf.controlName='MS_swatchMaker_pathField'
fpf.startingDirectry='D:/work/'

def swatchMaker(EX_PATH,IMAGE_NAME,SWATCH_MODE='SUMBNAIL',RENDER='playblast',X=64,Y=64):
	
	#選択状況取得＆選択をクリア
	SEL = cmds.ls(sl=True)
	cmds.select(cl=True)

	#パス作成
	EX_PATH=EX_PATH.replace('\\','/')
	playblastPath = EX_PATH+IMAGE_NAME+'.jpg'

	cmds.setAttr("defaultRenderGlobals.imageFormat",8)
	
	if RENDER=='playblast':
	#PlayBlastで作る
		RENDER_NAME=cmds.playblast(cf=playblastPath,fr=1,fo=True,fp=4,w=X,h=Y,clearCache=True,offScreen=True,format='image',percent=100,viewer=False,showOrnaments=False)
	else:
	#MayaRendererで作る
		RENDER_NAME=cmds.render(x=X,y=Y)

		RENDER_NAME=RENDER_NAME.replace('#','0')
		if SWATCH_MODE=='SWATCH':
			shutil.copyfile(RENDER_NAME,(EX_PATH+'.mayaSwatches/'+IMAGE_NAME+'.swatch'))
			
		if SWATCH_MODE=='SUMBNAIL':
			shutil.move(RENDER_NAME,(EX_PATH+'/'+IMAGE_NAME+'.jpg'))

	#選択状況復活
	cmds.select(SEL,r=True)

def setCamera(CAM):
	PANEL=cmds.getPanel(wf=True)
	if cmds.getPanel(to=PANEL)=='modelPanel':
		cmds.modelPanel(PANEL,e=True,cam=CAM)
	return
	
def checkViewport():
	targetPanel = cmds.getPanel(withFocus=True)
	if not 'modelPanel' in targetPanel:
		#cmds.confirmDialog( m=u'warning ビューポートを選択してください\nサムネイルは出力されません')
		return
	else:
		return targetPanel
	
def hideOthers(NODES=[]):
	#cmds.showHidden(a=True)
	#mel.eval('hideKeepSelection `listUnselected`;')
	cmds.hide(all=True)
	cmds.showHidden(NODES,a=True)


def showNodes(NODES=[]):
	cmds.hide(all=True)
	for each in NODES:
		cmds.showHidden(each)

def getVisibleAll():
	temp=[]
	Meshes=cmds.ls(l=True)
	for each in Meshes:
		if cmds.attributeQuery('visibility',ex=True,node=each):
			if cmds.getAttr(each+'.visibility'):
				temp.append(each)
	Ret=cmds.listRelatives(temp,p=True,f=True)
	return temp

def objSwatchMaker(
	NODE_NAME
	,EX_PATH
	,EX_FILENAME
	,RENDER_NAME='hwRender_OpenGL_Renderer'
	,RENDER_OVERRIDE=''
	,REFFERENCE_MODEL=''
	,CAMSETS=[[0,0,0,-20,30,0],[0,0,0,-20,120,0],[0,0,0,-20,210,0],[0,0,0,-20,300,0],[0,0,0,-70,30,0],[0,0,0,70,30,0]]):
	
	REFFERENCE_MODEL='' #リファレンスモデルを使わないように暫定処理

	targetPanel = checkViewport()
	if not targetPanel:targetPanel='modelPanel4'

	#ターゲットパネルのレンダー設定取得
	CURRENT_RENDER_NAME = cmds.modelEditor(targetPanel,q=True,rnm=True)
	CURRENT_RENDER_OVERRIDE = cmds.modelEditor(targetPanel,q=True,rom=True)

	targetCamera=cmds.modelPanel(targetPanel,q=True,cam=True)
	hadEnable = cmds.modelEditor(targetPanel, q=True, hud=True)

	Visible=getVisibleAll()

	if NODE_NAME:
		hideOthers(NODE_NAME)

	cmds.select(NODE_NAME,r=True)
	cmds.select(clear=True)



	#新規カメラ作成設定
	CAMERA=cmds.camera(n="MS_OBJ_RENDER")
	cmds.modelEditor (targetPanel,edit=True,displayAppearance="smoothShaded",rnm=RENDER_NAME,rom=RENDER_OVERRIDE,displayTextures=True,cam=CAMERA[0])

	#RenderSettings
	cmds.setAttr('defaultResolution.nodeState',0)
	cmds.setAttr('defaultResolution.aspectLock',0)
	cmds.setAttr('defaultResolution.width',64)
	cmds.setAttr('defaultResolution.height',64)
	cmds.setAttr('defaultResolution.pixelAspect',1.0)
	cmds.setAttr('defaultResolution.deviceAspectRatio',1.0)	

	#CameraSettings
	cmds.viewSet(CAMERA[1],p=False)
	CAMSHAPE = cmds.listRelatives(CAMERA[0],s=True)
	cmds.setAttr((CAMSHAPE[0]+".nearClipPlane"), 1)
	cmds.setAttr((CAMSHAPE[0]+".farClipPlane"), 1000000)


	#参照モデルを立たせる（スケール見本など）
	REFFERENCE_NODE_TRN=''
	if REFFERENCE_MODEL:
		REFFERENCE_NODE = cmds.createNode('GraviteAtgiLocatorNode')
		cmds.setAttr(REFFERENCE_NODE + '.atgiFilename',REFFERENCE_MODEL,type='string')
		BB=cmds.xform(NODE_NAME,q=True,bb=True,ws=True)
		REFFERENCE_NODE_TRN=cmds.listRelatives(REFFERENCE_NODE,ap=True)
		cmds.xform(REFFERENCE_NODE_TRN,t=[BB[3]+100,0,0],ws=True)

	#撮影
	i=0


	for each in CAMSETS:
		#VewFit
		cmds.setAttr((CAMERA[0]+".tx"), each[0])
		cmds.setAttr((CAMERA[0]+".ty"), each[1])
		cmds.setAttr((CAMERA[0]+".tz"), each[2])
		cmds.setAttr((CAMERA[0]+".rx"), each[3])
		cmds.setAttr((CAMERA[0]+".ry"), each[4])
		cmds.setAttr((CAMERA[0]+".rz"), each[5])
		cmds.select(NODE_NAME,r=True)
		if REFFERENCE_MODEL:
			cmds.select(REFFERENCE_NODE_TRN,add=True)
		cmds.viewFit(CAMSHAPE,f=1,an=False,all=False)

		#SwatchMaker
		if len(CAMSETS)==1:
			FINFILENAME=EX_FILENAME
		else:
			FINFILENAME=EX_FILENAME+str(i)
		swatchMaker(EX_PATH,FINFILENAME,X=400,Y=400)
		i+=1
		

	#シェーディングを元に戻す
	cmds.modelEditor(targetPanel, e=True , rnm=CURRENT_RENDER_NAME , rom=CURRENT_RENDER_OVERRIDE , da='smoothShaded', dtx=True, hud=hadEnable)
	
	cmds.delete(CAMERA)

	if NODE_NAME:
		showNodes(Visible)
		
	#参照モデルを消す（スケール見本など）
	if REFFERENCE_MODEL:
		cmds.delete(REFFERENCE_NODE_TRN)

def matSwatchMaker(MAT_NAME,EX_PATH):
	targetPanel = checkViewport()
	if not targetPanel:return

	targetCamera=cmds.modelPanel(targetPanel,q=True,cam=True)
	hadEnable = cmds.modelEditor(targetPanel, q=True, hud=True)
	
	#
	OBJ=cmds.polySphere(r=25,sx=20,sy=20,ax=[0,1,0],cuv=2,ch=1)
	
	cmds.select(OBJ,r=True)
	cmds.hyperShade(assign=MAT_NAME)
	
	CAMERA=cmds.camera(n="MS_MAT_RENDER")
	#
	cmds.modelEditor (targetPanel,edit=True,displayAppearance="smoothShaded",rnm="hwRender_OpenGL_Renderer",displayTextures=True,cam=CAMERA[0])
	#
	cmds.viewSet(CAMERA[1],p=False)
	cmds.setAttr((CAMERA[0]+".tx"), 0)
	cmds.setAttr((CAMERA[0]+".ty"), 0)
	cmds.setAttr((CAMERA[0]+".tz"), 55)
	cmds.setAttr((CAMERA[0]+".rx"), 0)
	cmds.setAttr((CAMERA[0]+".ry"), 0)
	cmds.setAttr('defaultResolution.nodeState',0)
	cmds.setAttr('defaultResolution.aspectLock',0)
	cmds.setAttr('defaultResolution.width',64)
	cmds.setAttr('defaultResolution.height',64)
	cmds.setAttr('defaultResolution.pixelAspect',1.0)
	cmds.setAttr('defaultResolution.deviceAspectRatio',1.0)
	
	swatchMaker(EX_PATH,MAT_NAME)
	
	cmds.modelEditor(targetPanel, e=True, rnm='base_OpenGL_Renderer', da='smoothShaded', dtx=True, hud=hadEnable)
	cmds.modelPanel(targetPanel,e=True,cam=targetCamera)
	
	cmds.delete(CAMERA)
	cmds.delete(OBJ)
	

def do():
	#NODE_NAME
	NODENAMES=cmds.ls(sl=True,l=True)
	#EX_PATH
	#EX_PATH='D:/work/'
	EX_PATH=fpf.startingDirectry
	#EX_FILENAME = NODENAME

	#RENDER_NAME/RENDER_OVERRIDE
	RENDER=cmds.radioCollection('RENDER_NAME',q=True,sl=True)

	if RENDER=='hwRender_OpenGL_Renderer':
		RENDER_NAME='hwRender_OpenGL_Renderer'
		RENDER_OVERRIDE=''

	if RENDER=='G2Renderer':
		RENDER_NAME = 'vp2Renderer'
		RENDER_OVERRIDE = 'G2Renderer'

	#REFFERENCE_MODEL
	REFMODEL=cmds.radioCollection('REFFERENCE_MODEL',q=True,sl=True)
	if REFMODEL=='none':
		REFFERENCE_MODEL = ''
	if REFMODEL=='kitten_notex':
		REFFERENCE_MODEL = 'D:/Projects/Gravite2/assets/bg/model/kitten_notex.atgi'

	#CAMSETS
	METHOD=cmds.radioCollection('SSMETHODS',q=True,sl=True)
	if METHOD=='single':
		CAMSETS=[[0,0,0,-20,30,0]]
	if METHOD=='6shots':
		CAMSETS=[[0,0,0,-20,30,0],[0,0,0,-20,120,0],[0,0,0,-20,210,0],[0,0,0,-20,300,0],[0,0,0,-70,30,0],[0,0,0,70,30,0]]


	for NODE_NAME in NODENAMES:
		EX_FILENAME=NODE_NAME.split('|')[-1]
		objSwatchMaker(NODE_NAME,EX_PATH,EX_FILENAME,RENDER_NAME,RENDER_OVERRIDE,REFFERENCE_MODEL,CAMSETS)


def layoutOptions():
	cmds.columnLayout()

	cmds.text(l='SSMETHODS',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.radioCollection('SSMETHODS')
	cmds.radioButton('single',sl=True)
	cmds.radioButton('6shots')

	cmds.text(l='RENDER_NAME',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.radioCollection('RENDER_NAME')
	cmds.radioButton('hwRender_OpenGL_Renderer')
	cmds.radioButton('G2Renderer',sl=True)

	cmds.text(l='REFFERENCE_MODEL',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.radioCollection('REFFERENCE_MODEL')
	cmds.radioButton('none')
	cmds.radioButton('kitten_notex',sl=True)

	cmds.button(l='do',c=lambda *args:do())
	cmds.setParent('..')


def LayoutA():
	cmds.columnLayout('MS_swatchMaker.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_swatchMaker.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	fpf.fileMode=2
	fpf.single()
	layoutOptions()
	
	cmds.showWindow('MS_tools_window')
	