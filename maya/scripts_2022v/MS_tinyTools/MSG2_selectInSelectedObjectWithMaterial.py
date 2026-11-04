# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_selectInSelectedObjectWithMaterial.py
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds

def getFaces(CONP):#フェース選択
	FACE=cmds.polyListComponentConversion(CONP,tf=True)
	result=cmds.filterExpand(FACE,ex=True,sm=34)
	return result
	
def getShapeSelectionList():
	currentSelectionList=[]
	childrenBuffer=[]
	resultList=[]
	
	currentSelectionList = cmds.ls(sl=True,o=True)
	for this in currentSelectionList:
		
		nodeType =cmds.nodeType(this)
		
		if nodeType == "transform":
			childrenBuffer = cmds.listRelatives(this,c=True)
			
			if len(childrenBuffer) > 0:
				resultList.append(childrenBuffer[0])
	return resultList


def getHyperGraphShapeSelectionList():

	currentSelectionList=[]
	parentBuffer=[]
	childrenBuffer=[]
	resultList=[]
	#SEL=cmds.ls(sl=True)
	currentSelectionList = cmds.ls(sl=True,typ='transform')
	#components=cmds.polyListComponentConversion(tf=True)
	#currentSelectionList=cmds.filterExpand(components,sm=34,ex=True)
	for this in currentSelectionList:
		parentBuffer = cmds.listRelatives (this,p=True)
		
		if cmds.nodeType(this)=='shape':
			resultList.append(this)
		elif cmds.listRelatives(this,ad=True,s=True):
			resultList.append(cmds.listRelatives(this,ad=True,s=True)[0])
		elif len(parentBuffer) > 0 :
			nodeType = cmds.nodeType(parentBuffer[0])
			
			if nodeType == "transform":

				childrenBuffer[0] = this
				
				if childrenBuffer:
					resultList.append(childrenBuffer[0])
					resultList.extend(resultList, childrenBuffer)
	return resultList


def selectInSelectedObjectWithMaterial(node=''):
	crrentShapesList=[]
	crrentComponentsList=[]
	hyperShadeShapesList=[]
	hyperShadeComponentsList=[]
	
	currentShapesList = getShapeSelectionList()
	currentComponentsList = getFaces(cmds.ls(sl=True))
	
	cmds.hyperShade(objects=node)
	
	hyperShadeShapesList = getHyperGraphShapeSelectionList()
	hyperShadeComponentsList = getFaces(cmds.ls(sl=True))
	
	cmds.select(clear=True)
	
	for thisHyperShadeShape in hyperShadeShapesList:
		for thisCurrentShape in currentShapesList:
			if thisHyperShadeShape == thisCurrentShape:
				cmds.select(thisHyperShadeShape,add=True)
			
	#exact match -- component
	for thisHyperShadeComponent in hyperShadeComponentsList:
		for thisCurrentComponent in currentComponentsList:
			
			if thisHyperShadeComponent == thisCurrentComponent:

				cmds.select(thisHyperShadeComponent,add=True)
	
	
	parentBuffer=[]
	
	#Include match -- Current Component Oriented
	for thisHyperShadeShape in hyperShadeShapesList:
		for thisCurrentComponent in currentComponentsList:
			
			parentBuffer = cmds.listRelatives(thisCurrentComponent,p=True)
			if parentBuffer:
				if thisHyperShadeShape ==parentBuffer[0]:

					cmds.select(thisCurrentComponent,add=True)
				
			
		
	
	 #Include match --HyperShade Component Oriented
	for thisCurrentShape in currentShapesList:
		for thisHyperShadeComponent in hyperShadeComponentsList:

			parentBuffer = cmds.listRelatives(thisHyperShadeComponent,p=True)
			if parentBuffer:
				if thisCurrentShape ==parentBuffer[0]:

					cmds.select(thisHyperShadeComponent,add=True)
				

	
def main():
	SEL=cmds.ls(sl=True,mat=True)
	selectInSelectedObjectWithMaterial(SEL)


def LayoutA():
	cmds.frameLayout(l='selectInSelectedObjectWithMaterial',cl=True,cll=True,bgc=[0.4,0.4,0.4])
	cmds.columnLayout('MSG2_selectInSelectedObjectWithMaterial.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_selectInSelectedObjectWithMaterial',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	


