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
import importlib
import maya.mel as mel
import math

from . import MS_texCheckResolution
importlib.reload(MS_texCheckResolution)

from . import MS_UVShellNormalize
importlib.reload(MS_UVShellNormalize)

from . import MS_getTextureSize
importlib.reload(MS_getTextureSize)



##################
#####ユーティリティ
##################

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


##### UI

def layoutOldMethod():#main
	cmds.frameLayout('MS_bestUVSize_frameLayout',w=135,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'oldMethod',cll=True,cl=True)
	cmds.columnLayout()
	
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
	cmds.button(w=120,l=u'bestPlaneProjection',c=lambda *args:bestPlaneProjection())
	cmds.button(w=120,l=u'layoutUV',c=lambda *args:layoutUV())
	cmds.button(w=120,l=u'UVShellNormalize',c=lambda *args:MS_UVShellNormalize.main())
	cmds.setParent('..')
	cmds.setParent('..')

def layoutEasyUV():#EasyUV
	cmds.frameLayout('MS_bestUVSize_layoutEasyUV_frameLayout',w=135,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'EasyUV',cll=True,cl=False)
	
	cmds.text(w=100,l=u'easyResize',bgc=(0.9,0.9,0.9))
	cmds.gridLayout(nc=4)
	cmds.button(w=100,l=u'64',c=lambda *args:easyResize(SIZE_PER_PIX=0.064))
	cmds.button(w=100,l=u'128',c=lambda *args:easyResize(SIZE_PER_PIX=0.032))
	cmds.button(w=100,l=u'256',c=lambda *args:easyResize(SIZE_PER_PIX=0.016))
	cmds.button(w=100,l=u'512',c=lambda *args:easyResize(SIZE_PER_PIX=0.008))
	cmds.button(w=100,l=u'1024',c=lambda *args:easyResize(SIZE_PER_PIX=0.004))
	cmds.button(w=100,l=u'2048',c=lambda *args:easyResize(SIZE_PER_PIX=0.002))
	cmds.button(w=100,l=u'4096',c=lambda *args:easyResize(SIZE_PER_PIX=0.001))
	cmds.button(w=100,l=u'8192',c=lambda *args:easyResize(SIZE_PER_PIX=0.0005))
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
	MS_getTextureSize.LayoutA()

	layoutOldMethod()
	cmds.setParent('..')
	cmds.showWindow('MS_bestUVSize_main_window')
	