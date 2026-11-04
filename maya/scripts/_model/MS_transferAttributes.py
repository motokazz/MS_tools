# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_transferAttributes.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel

def getTarget():
	SEL=cmds.ls(sl=True,l=True)
	cmds.textField('MS_transferAttributes_target_mesh',e=True,tx=';'.join(SEL))

def core(SRC=[],DST=[],TRANSFER_SHADINGSETS=False):

	#
	POSITIONS		= cmds.optionVar(q='transferAttributesPositionsOption')
	NORMALS		= cmds.optionVar(q='transferAttributesNormalsOption')
	UVSETS		= cmds.optionVar(q='transferAttributesUVSetsOption')
	COLORSETS		= cmds.optionVar(q='transferAttributesColorSetsOption')
	SEARCHMETHOD	= cmds.optionVar(q='transferAttributesSearchMethodOption')
	MIRROR		= cmds.optionVar(q='transferAttributesMirrorOption')
	FLIPUVS		= cmds.optionVar(q='transferAttributesFlipUVsOption')
	COLORBORDERS	= cmds.optionVar(q='transferAttributesColorBordersOption')
	SPACE		= cmds.optionVar(q='transferAttributesSpaceOption')

	cmds.transferAttributes(
		SRC[0]
		,DST[0]
		,transferPositions	=POSITIONS
		,transferNormals	=NORMALS
		,transferUVs		=UVSETS
		,transferColors	=COLORSETS
		,sampleSpace		=SPACE
		,searchMethod	=SEARCHMETHOD
		,flipUVs		=FLIPUVS
		,colorBorders		=COLORBORDERS
	)

	#
	cmds.select(SRC[0],r=True)
	cmds.select(DST[0],tgl=True)
	
	if cmds.checkBox('MS_transferAttributes_transferShadingSets',q=True,ex=True):
			TRANSFER_SHADINGSETS=cmds.checkBox('MS_transferAttributes_transferShadingSets',q=True,v=True)

	if TRANSFER_SHADINGSETS:
		cmds.transferShadingSets( sampleSpace=1 )

def core2(SRC=[],DST=[],TRANSFER_SHADINGSETS=False):
	cmds.select(SRC,r=True)
	cmds.select(DST,tgl=True)
	mel.eval('performTransferAttributes 0;')

def openOption():
	mel.eval('performTransferAttributes 1;')


def main(SM=0):
	SEL=cmds.ls(sl=True,l=True)
	TXF=cmds.textField('MS_transferAttributes_target_mesh',q=True,tx=True).strip()

	if TXF:
		TARGET=TXF.split(';')
	else:
		if len(SEL)>1:
			TARGET=SEL.pop(0)
		else:
			return

	
	if cmds.ls(sl=True,type='transform'):
		#SEL=cmds.ls(sl=True,l=True)
		#cmds.polySoftEdge(SEL,a=180)
		core(TARGET,SEL)

	else:
		VTX=cmds.polyListComponentConversion(tv=True)
		core(TARGET,VTX)
		SEL=[VTX[0].split('.')[0]]




def LayoutA():
	cmds.columnLayout('MS_transferAttributes.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_transferAttributes.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.rowLayout(nc=2)
	cmds.textField('MS_transferAttributes_target_mesh',en=False,w=200)
	cmds.button(l='getTarget',w=100,c=lambda *args:getTarget())
	cmds.setParent('..')

	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def layout_options():
	cmds.frameLayout('MS_transferAttributes_options_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_transferAttributes_option',cll=True,cl=False)
	cmds.columnLayout('MS_transferAttributes_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_transferAttributes',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.checkBox('MS_transferAttributes_transferShadingSets',l=u'マテリアル転写')
	cmds.iconTextButton( style='iconAndTextHorizontal', image1='polyTransferAttributes.png', label='open_transferAttributes_option',c=lambda *args:openOption() )
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	layout_options()

	cmds.showWindow('MS_tools_window')
	