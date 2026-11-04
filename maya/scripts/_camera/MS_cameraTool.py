# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_cameraTool
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds


def checkFilmFit(TARGET='perspShape'):
	FilmFit = cmds.getAttr('%s.filmFit'%TARGET)
	if FilmFit==1:
		cmds.text('MS_cameraTool_FilmFit',e=True,l='Horizontal',w=50,bgc=(0.8,0.5,0.5))
		return 1
	if FilmFit==2:
		cmds.text('MS_cameraTool_FilmFit',e=True,l='Vertical',w=50,bgc=(0.5,0.8,0.5))
		return 2

def cameraFilmFit(TARGET='perspShape'):
	if cmds.getAttr('%s.filmFit'%TARGET)==1:
		cmds.setAttr('%s.filmFit'%TARGET,2)
	else:
		cmds.setAttr('%s.filmFit'%TARGET,1)
	checkFilmFit()

def setAllCamerasNearFar(NEAR=0.1,FAR=10000,CAMERA_DISTANCE=100):
	
	cmds.setAttr("top.translateY",CAMERA_DISTANCE)
	cmds.setAttr( "front.translateZ",CAMERA_DISTANCE)
	cmds.setAttr( "side.translateX",CAMERA_DISTANCE)

	cmds.setAttr( "topShape.nearClipPlane" , NEAR)
	cmds.setAttr( "frontShape.nearClipPlane" , NEAR)
	cmds.setAttr( "sideShape.nearClipPlane" , NEAR)
	cmds.setAttr( "perspShape.nearClipPlane" , NEAR)

	cmds.setAttr( "topShape.farClipPlane" , FAR)
	cmds.setAttr( "frontShape.farClipPlane" , FAR)
	cmds.setAttr( "sideShape.farClipPlane" , FAR)
	cmds.setAttr( "perspShape.farClipPlane" , FAR)


def getActiveCamera():
	#現在アクティブになっているモデルパネルのカメラ名を取得する
	PANEL=cmds.getPanel(wf=True)
	if cmds.getPanel(to=PANEL)=='modelPanel':
		CAMERA=cmds.modelPanel(PANEL,q=True,cam=True)
		return cmds.listRelatives(CAMERA,s=True)[0]
	return
	
	
	
def near():
	ACTIVE_CAMERA=getActiveCamera()
	if not ACTIVE_CAMERA:
		return
	VAR=cmds.floatSliderGrp('MS_cameraTool_Near',q=True,v=True)
	cmds.setAttr('%s.nearClipPlane'%ACTIVE_CAMERA,VAR)
	
def far():
	ACTIVE_CAMERA=getActiveCamera()
	if not ACTIVE_CAMERA:
		return
	VAR=cmds.floatSliderGrp('MS_cameraTool_Far',q=True,v=True)
	cmds.setAttr('%s.farClipPlane'%ACTIVE_CAMERA,VAR)
	
def slide():
	ACTIVE_CAMERA=getActiveCamera()
	if not ACTIVE_CAMERA:
		return
	VAR=cmds.floatSliderGrp('MS_cameraTool_Slide',q=True,v=True)
	NEAR=cmds.floatSliderGrp('MS_cameraTool_Near',q=True,v=True)+VAR
	FAR=cmds.floatSliderGrp('MS_cameraTool_Far',q=True,v=True)+VAR
	if NEAR<0.1:
		NEAR=0.1
	if FAR+VAR<0.1:
		FAR=0.1
	if NEAR>=FAR:
		FAR=NEAR+0.1
	
	cmds.setAttr('%s.farClipPlane'%ACTIVE_CAMERA,NEAR)
	cmds.setAttr('%s.farClipPlane'%ACTIVE_CAMERA,FAR)
	
def layoutA(
	LABEL='MS_cameraTool'
	,WIDTH=257
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	
	#setAllButtons
	cmds.columnLayout('Instant setup for all views')
	cmds.text(l='Preset Buttons',w=257,bgc=(0.7,0.7,0.7),fn='boldLabelFont')
	cmds.gridLayout('MS_cameraTool_Buttons',nc=4,cellWidthHeight=(50,30))
	cmds.button(l='1x',w=50,c=lambda *args:setAllCamerasNearFar(NEAR=0.1,FAR=10000,CAMERA_DISTANCE=100))
	cmds.button(l='10x',w=50,c=lambda *args:setAllCamerasNearFar(NEAR=1,FAR=100000,CAMERA_DISTANCE=1000))
	cmds.button(l='100x',w=50,c=lambda *args:setAllCamerasNearFar(NEAR=10,FAR=1000000,CAMERA_DISTANCE=50000))
	cmds.button(l='1000x',w=50,c=lambda *args:setAllCamerasNearFar(NEAR=10,FAR=100000000,CAMERA_DISTANCE=100000))
	cmds.setParent('..')
	cmds.setParent('..')
	#setFilmFit
	cmds.columnLayout('Instant setup for all views')
	cmds.text(l='FilmFitUtil',w=257,bgc=(0.7,0.7,0.7),fn='boldLabelFont')
	cmds.gridLayout('MS_cameraTool_Buttons',nc=3,cellWidthHeight=(85,30))
	cmds.text(l='FilmFit',w=50)
	cmds.text('MS_cameraTool_FilmFit',l='Horizontal',w=50)
	cmds.button(l='Swap',w=50,c=lambda *args:cameraFilmFit())
	cmds.setParent('..')
	cmds.setParent('..')
	#controllers
	cmds.columnLayout(ann='Quick control for selected view')
	cmds.text(l='QuickController',w=257,bgc=(0.7,0.7,0.7),fn='boldLabelFont')
	cmds.floatSliderGrp('MS_cameraTool_Near',l='Near',cw3=(50,50,150),min=0.1,max=100,fmn=0.1,fmx=10000,field=True,v=0.1,cc=lambda *args:near())
	cmds.floatSliderGrp('MS_cameraTool_Far',l='Far',cw3=(50,50,150),min=10,max=10000,fmn=1,fmx=10000,field=True,v=10000,cc=lambda *args:far())
	cmds.floatSliderGrp('MS_cameraTool_Slide',l='Slide',cw3=(50,50,150),min=-1000,max=1000,fmn=-100000,fmx=100000,field=True,v=0,dc=lambda *args:slide())
	
	cmds.setParent('..')
	cmds.setParent('..')


def UI():
	if cmds.window('MS_cameraTool_main_window',q=True,ex=True):
		cmds.deleteUI('MS_cameraTool_main_window')
	cmds.window('MS_cameraTool_main_window',rtf=True,s=True)

	layoutA()
	
	cmds.showWindow('MS_cameraTool_main_window')
	checkFilmFit()

