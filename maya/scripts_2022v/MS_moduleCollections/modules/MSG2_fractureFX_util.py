# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_fractureFX_util.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel

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

#
def fractureSelected():
	SEL=cmds.ls(sl=True,l=True)
	mel.eval('fxFractureSelected')
	GEO=cmds.ls(type='fxBreakGeometry')
	cmds.textField('MSG2_fractureFX_util_targetGEO',e=True,tx=GEO[-1])
	cmds.textField('MSG2_fractureFX_util_targetMesh',e=True,tx=SEL[0])
	return GEO[-1]

def splitPlane(GEO=''):
	GEO=cmds.textField('MSG2_fractureFX_util_targetGEO',q=True,tx=True)
	cmds.setAttr(GEO+".shards",1)#splitPlane
	mel.eval('fxFractureBreakUI_MultiAdd "'+GEO+'.splitPlanePlane" "fxFractureBreakUI_MultiUpdate" "MayaWindow|MainAttributeEditorLayout|formLayout2|AEmenuBarLayout|AErootLayout|AEStackLayout|AErootLayoutPane|AEbaseFormLayout|AEcontrolFormLayout|AttrEdfxBreakGeometryFormLayout|scrollLayout4|columnLayout25|columnLayout26|basic|partition|column|repeat|column|planes|column" "PartitionPlane";')
	mel.eval('fxFractureBreakUI_ConnectPartitionPlane "'+GEO+'.splitPlanePlane[0].splitPlanePlaneTransform" "split#" 1;')
	SP=cmds.ls(type='sketchPlane')
	PSP=cmds.listRelatives(SP,p=True)
	return PSP

def shading(SEL=''):
	SEL=cmds.textField('MSG2_fractureFX_util_targetMesh',q=True,tx=True)
	cmds.select(SEL,r=True)
	SETS = mel.eval('fxCmd shading -autoUV -shader -selectSet')
	cmds.select(SETS,r=True)
	FACE=cmds.filterExpand(sm=34)
	createTempMaterial(FACE,'MS_shardmat')
	cmds.delete(SETS)

def fracture(SEL=''):
	SEL=cmds.textField('MSG2_fractureFX_util_targetMesh',q=True,tx=True)
	cmds.select(SEL,r=True)
	mel.eval('fxFractureSeparateUI;')

def fractureAll():
	GEO=fractureSelected()
	SP=splitPlane()
	shading()
	fracture()

	PGEO=cmds.listRelatives(GEO,p=True)
	cmds.delete(PGEO)
	cmds.delete(SP)


def LayoutA():
	cmds.columnLayout('MSG2_fractureFX_util.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_fractureFX_util.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.textField('MSG2_fractureFX_util_targetMesh',en=False)
	cmds.textField('MSG2_fractureFX_util_targetGEO',en=False)

	cmds.button(l='fractureSelected',c=lambda *args:fractureSelected())
	cmds.button(l='splitPlane',c=lambda *args:splitPlane())
	cmds.button(l='shading',c=lambda *args:shading())
	cmds.button(l='fracture',c=lambda *args:fracture())
	cmds.button(l='all',c=lambda *args:fractureAll())

	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	