# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_G2ShaderUtil.py
# 説明
#			シェーダーの差し替えツール
#
# 作成日
#
########################################

import maya.cmds as cmds

#ButtonCommands

def_bevel = [
	[0.1, 1, 2, 3]
	, [0.25, 1, 2, 3]
	,[0.5,1,3,5]
	,[1,1,5,10]
]

def_offset = [
	[0,0.1]
	,[0, 0.25]
	, [0, 0.5]
	, [0, 1]
	, [0, 2]
]

def_extrude = [
	[0.1,0]
	,[0.25,0]
	,[0.5,0]
	,[1,0]
	,[-0.1,0]
	,[-0.25,0]
	,[-0.5,0]
	,[-1,0]
	,[-2,0]
]

def_gully = [
	[-0.1,0.1]
	, [-0.2, 0.2]
	,[-0.25, 0.25]
	, [-0.5, 0.5]
	, [-1, 1]
]
def to_edge():
	edges = cmds.polyListComponentConversion(te=True, internal=True)
	cmds.select(edges, r=True)

def to_face():
	faces = cmds.polyListComponentConversion(tf=True, internal=True)
	cmds.select(faces, r=True)

def exec_extrude(THICKNESS,OFFSET):
	def ret(dummy=''):
		edge_selection = False
		if cmds.filterExpand(sm=34):
			cmds.polyExtrudeFacet(
				constructionHistory=1
				,keepFacesTogether=1
				,divisions=1
				,twist=0
				,taper=1
				,off=OFFSET
				,thickness=THICKNESS
				,smoothingAngle=30
			)
		elif cmds.filterExpand(sm=32):
			cmds.polyExtrudeEdge(
				constructionHistory = 1
				,keepFacesTogether = 1
				,divisions=1
				,twist=0
				,taper=1
				,offset=OFFSET
				,thickness=THICKNESS
				,smoothingAngle=30
			)
			edge_selection =True

		mergeVertexTolerance = cmds.floatField('mergeVertexTolerance',q=True,v=True)
		merge_target = cmds.polyListComponentConversion(tv=True)
		cmds.polyMergeVertex(merge_target,d=mergeVertexTolerance,ws=True)

		if edge_selection:
			to_edge()
		else:
			to_face()

	return ret

def exec_bevel(OFFSET,SEGMENTS):
	def ret(dummy=''):
		MergeVertexTolerance = cmds.floatField('mergeVertexTolerance', q=True, v=True)
		convertToEdgePerimeter()
		cmds.polyBevel3(
			offset=OFFSET
			,offsetAsFraction=0
			,autoFit=1
			,depth=1
			,mitering=0
			,miterAlong=0
			,chamfer=1
			,segments=SEGMENTS
			,worldSpace=1
			,smoothingAngle=30
			,subdivideNgons=1
			,mergeVertices=1
			,mergeVertexTolerance=MergeVertexTolerance
			,miteringAngle=180
			,angleTolerance=180
			,ch=1
		)
	return ret

def customBevel():
	OFFSET = cmds.floatField('var_offset', q=True, v=True)
	SEGMENTS = cmds.intField('var_segment', q=True , v=True)
	MergeVertexTolerance = cmds.floatField('mergeVertexTolerance', q=True, v=True)

	#
	convertToEdgePerimeter()
	#

	cmds.polyBevel3(
		offset=OFFSET
		,offsetAsFraction=0
		,autoFit=1
		,depth=1
		,mitering=0
		,miterAlong=0
		,chamfer=1
		,segments=SEGMENTS
		,worldSpace=1
		,smoothingAngle=30
		,subdivideNgons=1
		,mergeVertices=1
		,mergeVertexTolerance=MergeVertexTolerance
		,miteringAngle=180
		,angleTolerance=180
		,ch=1
	)

def customExtrude():
	THICKNESS = cmds.floatField('var_thickness', q=True, v=True)
	OFFSET = cmds.floatField('var_offset', q=True, v=True)

	if cmds.filterExpand(sm=34):
		cmds.polyExtrudeFacet(
			constructionHistory=1
			,keepFacesTogether=1
			,divisions=1
			,twist=0
			,taper=1
			,off=OFFSET
			,thickness=THICKNESS
			,smoothingAngle=30
		)
	elif cmds.filterExpand(sm=32):
		cmds.polyExtrudeEdge(
			constructionHistory = 1
			,keepFacesTogether = 1
			,divisions=1
			,twist=0
			,taper=1
			,offset=OFFSET
			,thickness=THICKNESS
			,smoothingAngle=30
	)

def convertToEdgePerimeter():
	if cmds.checkBox('preConvertToEdgePerimeter',q=True,v=True):
		edge_perimeter = cmds.polyListComponentConversion(te=True, bo=True)
		cmds.select(edge_perimeter,r=True)


#######
#UI
#######

def createCustomCommand():
	if cmds.gridLayout('MS_custom_command_gridLayout',q=True,ex=True):
		cmds.deleteUI('MS_custom_command_gridLayout')
	cmds.gridLayout('MS_custom_command_gridLayout',nc=5,nr=6,cw=70,ch=30)

	cmds.text(l='thickness')
	cmds.text(l='offset')
	cmds.text(l='segment')
	cmds.text(l='bevel')
	cmds.text(l='extrude')

	cmds.floatField('var_thickness',v=1)
	cmds.floatField('var_offset', v=1)
	cmds.intField('var_segment', v=1)
	cmds.button(l='bevel',c=lambda *args:customBevel())
	cmds.button(l='extrude', c=lambda *args: customExtrude())


	cmds.setParent('..')

def createGullyPalette():
	if cmds.gridLayout('MS_gullyPalette_gridLayout',q=True,ex=True):
		cmds.deleteUI('MS_gullyPalette_gridLayout')
	cmds.gridLayout('MS_gullyPalette_gridLayout',nc=4,nr=6,cw=80,ch=30,p='MS_gullyPalette_scrollLayout')

	for each in def_gully:
		cmds.columnLayout(p='MS_gullyPalette_gridLayout',adj=True)
		cmds.button(l=str(each[0])+','+str(each[1]),c=exec_extrude(each[0],each[1]))
		cmds.setParent('..')

	cmds.setParent('..')

def createExtrudePalette():
	if cmds.gridLayout('MS_extrudePalette_gridLayout',q=True,ex=True):
		cmds.deleteUI('MS_extrudePalette_gridLayout')
	cmds.gridLayout('MS_extrudePalette_gridLayout',nc=4,nr=6,cw=80,ch=30,p='MS_extrudePalette_scrollLayout')

	for each in def_extrude:
		cmds.columnLayout(p='MS_extrudePalette_gridLayout',adj=True)
		cmds.button(l=str(each[0])+','+str(each[1]),c=exec_extrude(each[0],each[1]))
		cmds.setParent('..')

	cmds.setParent('..')

def createOffsetPalette():
	if cmds.gridLayout('MS_offsetPalette_gridLayout',q=True,ex=True):
		cmds.deleteUI('MS_offsetPalette_gridLayout')
	cmds.gridLayout('MS_offsetPalette_gridLayout',nc=4,nr=6,cw=80,ch=30,p='MS_offsetPalette_scrollLayout')

	for each in def_offset:
		cmds.columnLayout(p='MS_offsetPalette_gridLayout',adj=True)
		cmds.button(l=str(each[0])+','+str(each[1]),c=exec_extrude(each[0],each[1]))
		cmds.setParent('..')

	cmds.setParent('..')

def createBevelPalette():
	if cmds.gridLayout('MS_bevelPalette_gridLayout',q=True,ex=True):
		cmds.deleteUI('MS_bevelPalette_gridLayout')
	cmds.gridLayout('MS_bevelPalette_gridLayout',nc=4,nr=6,cw=80,ch=90,p='MS_bevelPalette_scrollLayout')

	for each in def_bevel:
		cmds.columnLayout(p='MS_bevelPalette_gridLayout',adj=True)

		cmds.button(l=str(each[0])+','+str(each[1]),c=exec_bevel(each[0],each[1]))
		cmds.button(l=str(each[0])+','+str(each[2]),c=exec_bevel(each[0],each[2]))
		cmds.button(l=str(each[0])+','+str(each[3]),c=exec_bevel(each[0],each[3]))

		cmds.setParent('..')

	cmds.setParent('..')

def LayoutOption():

	cmds.frameLayout(l='options',cl=True,cll=False,bgc=[0.4,0.4,0.4])
	cmds.separator()
	cmds.columnLayout()
	cmds.checkBox('preConvertToEdgePerimeter',l='pre Convert To EdgePerimeter (for Bevel)',v=True)
	cmds.text(l='mergeVertexTolerance')
	cmds.floatField('mergeVertexTolerance',v=0.03)
	cmds.setParent('..')
	cmds.setParent('..')

def LayoutA():
	cmds.frameLayout(l='materialList',cl=True,cll=False,bgc=[0.4,0.4,0.4])
	cmds.separator()
	#

	cmds.columnLayout(adj=True)
	createCustomCommand()
	cmds.button(l='refleshList',c=lambda *args:createBevelPalette())


	cmds.text(l='Bevel',fn='boldLabelFont')
	cmds.scrollLayout('MS_bevelPalette_scrollLayout',h=100)
	cmds.setParent('..')

	cmds.text(l='Extrude', fn='boldLabelFont')
	cmds.scrollLayout('MS_extrudePalette_scrollLayout', h=100)
	cmds.setParent('..')

	cmds.text(l='Offset', fn='boldLabelFont')
	cmds.scrollLayout('MS_offsetPalette_scrollLayout', h=100)
	cmds.setParent('..')

	cmds.text(l='Gully', fn='boldLabelFont')
	cmds.scrollLayout('MS_gullyPalette_scrollLayout', h=100)
	cmds.setParent('..')

	cmds.setParent('..')

	#
	cmds.separator()
	cmds.setParent('..')


def UI():
	if cmds.window('MS_tools_window', q=True, ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window', rtf=True, s=True)
	
	LayoutA()

	LayoutOption()

	cmds.showWindow('MS_tools_window')
	
	createBevelPalette()
	createExtrudePalette()
	createOffsetPalette()
	createGullyPalette()

