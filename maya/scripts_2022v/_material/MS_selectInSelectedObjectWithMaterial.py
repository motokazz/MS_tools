# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_selectInSelectedObjectWithMaterial
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds


def getFaces(CONP):  # フェース選択
	FACE = cmds.polyListComponentConversion(CONP, tf=True)
	result = cmds.filterExpand(FACE, ex=True, sm=34)
	return result


def getShapeSelectionList():
	currentSelectionList = []
	childrenBuffer = []
	resultList = []

	currentSelectionList = cmds.ls(sl=True, o=True)
	for this in currentSelectionList:

		nodeType = cmds.nodeType(this)

		if nodeType == "transform":
			childrenBuffer = cmds.listRelatives(this, c=True)

			if len(childrenBuffer) > 0:
				resultList.append(childrenBuffer[0])
	return resultList


def getHyperGraphShapeSelectionList():
	currentSelectionList = []
	parentBuffer = []
	childrenBuffer = []
	resultList = []

	currentSelectionList = cmds.ls(sl=True, typ='transform')

	for this in currentSelectionList:
		parentBuffer = cmds.listRelatives(this, p=True)

		if cmds.nodeType(this) == 'shape':
			resultList.append(this)
		elif cmds.listRelatives(this, ad=True, s=True):
			resultList.append(cmds.listRelatives(this, ad=True, s=True)[0])
		elif len(parentBuffer) > 0:
			nodeType = cmds.nodeType(parentBuffer[0])

			if nodeType == "transform":

				childrenBuffer[0] = this

				if childrenBuffer:
					resultList.append(childrenBuffer[0])
					resultList.extend(resultList, childrenBuffer)
	return resultList


def selectInSelectedObjectWithMaterial(node=''):
	crrentShapesList = []
	crrentComponentsList = []
	hyperShadeShapesList = []
	hyperShadeComponentsList = []

	currentShapesList = getShapeSelectionList()
	currentComponentsList = getFaces(cmds.ls(sl=True))

	cmds.hyperShade(objects=node)

	hyperShadeShapesList = getHyperGraphShapeSelectionList()
	hyperShadeComponentsList = getFaces(cmds.ls(sl=True))

	cmds.select(clear=True)

	exact_match_list = set(hyperShadeComponentsList) & set(currentComponentsList)

	# exact match -- component

	exact_match_list = set(hyperShadeComponentsList) & set(currentComponentsList)
	cmds.select(exact_match_list, r=True)


def do():
	SEL = cmds.ls(sl=True, mat=True)
	selectInSelectedObjectWithMaterial(SEL)


def layoutA():
	cmds.frameLayout('MS_selectInSelectedObjectWithMaterial_frameLayout', w=217, bgc=[0.2, 0.2, 0.2],
					 fn='boldLabelFont', l=u'MS_selectInSelectedObjectWithMaterial', cll=True, cl=False)
	cmds.columnLayout()

	cmds.text(l='MS_selectInSelectedObjectWithMaterial')
	cmds.button(w=150, l=u'do', c=lambda *args: do())

	cmds.setParent('..')
	cmds.setParent('..')


def UI():
	if cmds.window('MS_selectInSelectedObjectWithMaterial_main_window', q=True, ex=True):
		cmds.deleteUI('MS_selectInSelectedObjectWithMaterial_main_window')
	cmds.window('MS_selectInSelectedObjectWithMaterial_main_window', rtf=True, s=True)

	layoutA()
	cmds.showWindow('MS_selectInSelectedObjectWithMaterial_main_window')


