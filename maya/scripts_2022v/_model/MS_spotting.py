# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_spotting.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import _material.MS_lambert1_control as MS_lambert1_control
reload(MS_lambert1_control)

import _model.MS_switchVisible as MS_switchVisible
reload(MS_switchVisible)

import _model.MS_componentStepSelections as MS_componentStepSelections
reload(MS_componentStepSelections)



'''
def job():
	UINAME=jobButton('fullAuto','FullAuto')
	jobNum = cmds.scriptJob(e=["SelectionChanged",THIS_SCRIPT+".ccFullAuto()"],parent=UINAME,protected=True)
'''

def create(MODE='plane'):
	if cmds.objExists('MS_spotObj_XXX'):
		cmds.delete('MS_spotObj_XXX')
	if MODE=='plane':
		SPOT_OBJ=cmds.polyPlane(w=200,h=200,sx=1,sy=1,n='MS_spotObj_XXX')
	if MODE=='cube':
		SPOT_OBJ=cmds.polyCube(w=200,h=200,d=200,sx=1,sy=1,sz=1,n='MS_spotObj_XXX')
	#
	if not cmds.objExists('MS_spotObj_BaseMat'):
		MAT=cmds.shadingNode('lambert',asShader=True)
		cmds.setAttr(MAT+'.incandescence',1,0.5,0,type='double3')
		cmds.rename(MAT,'MS_spotObj_BaseMat')

	#
	cmds.select(SPOT_OBJ,r=True)
	cmds.hyperShade(a='MS_spotObj_BaseMat')
	
	SPOT_OBJ=cmds.parent(SPOT_OBJ,'persp')
	cmds.xform(SPOT_OBJ,t=[0,0,-1500],ro=[0,0,0],a=True)
	#SPOT_OBJ=cmds.parent(SPOT_OBJ,w=True)
	cmds.aimConstraint('persp',SPOT_OBJ,aim=[0,1,0])
	#cmds.parentConstraint('persp',SPOT_OBJ)
	cmds.showHidden(SPOT_OBJ,a=True)
	

def slide():
	cmds.setAttr('MS_spotObj_XXX.tz',cmds.floatSlider('MS_spotting_slideSlider',q=True,v=True))

def sizeSlide():
	SIZE=cmds.floatSlider('MS_spotting_sizeSlider',q=True,v=True)
	cmds.setAttr('MS_spotObj_XXX.sx',SIZE)
	cmds.setAttr('MS_spotObj_XXX.sy',SIZE)
	cmds.setAttr('MS_spotObj_XXX.sz',SIZE)

def dup():
	cmds.select(cmds.duplicate('MS_spotObj_XXX')[0],r=True)
	cmds.delete(cmds.listRelatives(c=True,type='aimConstraint',f=True))
	cmds.parent(w=True)
	cmds.rename('MS_spotObj')

def createOcc():
	if cmds.objExists('MS_spotting_OCC'):
		cmds.delete('MS_spotting_OCC')
	CUBE=cmds.polyCube(w=100000,h=100000,d=100000)
	cmds.polyNormal(CUBE,nm=0)
	#
	if not cmds.objExists('MS_spotting_OCCMat'):
		MAT=cmds.shadingNode('lambert',asShader=True)
		cmds.setAttr(MAT+'.incandescence',0,1,0,type='double3')
		cmds.rename(MAT,'MS_spotting_OCCMat')
	#
	cmds.select(CUBE,r=True)
	cmds.hyperShade(a='MS_spotting_OCCMat')
	cmds.rename(CUBE[0],'MS_spotting_OCC')

def setBackgroundColor(R=0,G=1,B=0):
	cmds.displayRGBColor("background",R,G,B)
	cmds.displayRGBColor("backgroundTop",R,G,B)
	cmds.displayRGBColor("backgroundBottom",R,G,B)

def resetBackgroundColor():
	cmds.displayRGBColor("background",0.6309999823570251, 0.6309999823570251, 0.6309999823570251)
	cmds.displayRGBColor("backgroundTop",0.5350000262260437, 0.6169999837875366, 0.7020000219345093)
	cmds.displayRGBColor("backgroundBottom",0.052000001072883606, 0.052000001072883606, 0.052000001072883606)

def coverOcculuder():
	SEL=cmds.duplicate(cmds.listRelatives('|occ',c=True,type='transform',f=True))
	for OBJ in SEL:
		cmds.select(OBJ,r=True)
		cmds.showHidden(OBJ,a=True)
		cmds.polySoftEdge(angle=180,ch=False)
		VTX=cmds.polyListComponentConversion(tv=True)
		cmds.select(VTX,r=True)
		VTX=cmds.filterExpand(sm=31)
		for each in VTX:
			cmds.moveVertexAlongDirection(each,n=[10])
		
		OBJ=cmds.parent(OBJ,'root')
		
		import s2000_tools.MS_fillHole as MS_fillHole
		reload(MS_fillHole)
		
		cmds.select(OBJ,r=True)
		MS_fillHole.createMaterialTemplate(KEY='RUBBLE')
		
def main():
	pass

def LayoutA():
	cmds.columnLayout('MS_spotting.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_spotting.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='plane',c=lambda *args:create('plane'))
	cmds.button(l='cube',c=lambda *args:create('cube'))
	cmds.text(l='range')
	cmds.floatSlider('MS_spotting_slideSlider',v=-1500,min=-5000,max=-500,dc=lambda *args:slide())

	cmds.text(l='size')
	cmds.floatSlider('MS_spotting_sizeSlider',v=1,min=0.1,max=2,dc=lambda *args:sizeSlide())

	cmds.button(l='dup',c=lambda *args:dup())
	cmds.separator(h=10)
	cmds.text(l='backgroundColor')
	cmds.button(l='setWorkColor',c=lambda *args:setBackgroundColor())
	cmds.button(l='reset',c=lambda *args:resetBackgroundColor())
	cmds.separator(h=10)
	cmds.text(l='occluderCoverTool')
	cmds.button(l='coverOcculuder',c=lambda *args:coverOcculuder())
	cmds.separator(h=10)
	
	#
	MS_lambert1_control.LayoutA()
	
	#
	MS_switchVisible.LayoutA()

	#
	MS_componentStepSelections.LayoutA()

	cmds.setParent('..')

def UI():
	if cmds.window('MS_spotting_window',q=True,ex=True):
		cmds.deleteUI('MS_spotting_window')
	cmds.window('MS_spotting_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_spotting_window')
	