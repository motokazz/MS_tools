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
import shutil


def swatchMaker(EX_PATH,IMAGE_NAME,SWATCH_MODE='SUMBNAIL',RENDER='playblast',X=64,Y=64):
	
	EX_PATH=EX_PATH.replace('\\','/')
	
	cmds.setAttr("defaultRenderGlobals.imageFormat",8)
	
	if RENDER=='playblast':
		RENDER_NAME=cmds.playblast(cf=IMAGE_NAME,fr=1,fo=True,fp=4,w=X,h=Y,clearCache=True,offScreen=True,format='image',percent=100,viewer=False,showOrnaments=False)
	else:
		RENDER_NAME=cmds.render(x=X,y=Y)
	
	RENDER_NAME=RENDER_NAME.replace('#','0')
	if SWATCH_MODE=='SWATCH':
		shutil.copyfile(RENDER_NAME,(EX_PATH+'.mayaSwatches/'+IMAGE_NAME+'.swatch'))
		
	if SWATCH_MODE=='SUMBNAIL':
		shutil.move(RENDER_NAME,(EX_PATH+'/'+IMAGE_NAME+'.jpg'))
	
def setCamera(CAM):
	PANEL=cmds.getPanel(wf=True)
	if cmds.getPanel(to=PANEL)=='modelPanel':
		cmds.modelPanel(PANEL,e=True,cam=CAM)
	return
	
def objSwatchMaker(NODE_NAME,EX_PATH):
	targetPanel = cmds.getPanel(withFocus=True)
	if not 'modelPanel' in targetPanel:
		cmds.confirmDialog( m=u'warning ビューポートを選択してください\nサムネイルは出力されません')
		return
	targetCamera=cmds.modelPanel(targetPanel,q=True,cam=True)
	hadEnable = cmds.modelEditor(targetPanel, q=True, hud=True)
	
	cmds.select(NODE_NAME,r=True)
	cmds.viewFit(f=1)
	cmds.select(clear=True)
	
	swatchMaker(EX_PATH,NODE_NAME,X=256,Y=256)
	
	cmds.modelEditor(targetPanel, e=True, rnm='base_OpenGL_Renderer', da='smoothShaded', dtx=True, hud=hadEnable)
	
	
	
def matSwatchMaker(MAT_NAME,EX_PATH):
	
	targetPanel = cmds.getPanel(withFocus=True)
	if not 'modelPanel' in targetPanel:
		cmds.confirmDialog( m=u'warning ビューポートを選択してください\nサムネイルは出力されません')
		return
	
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
	
	
