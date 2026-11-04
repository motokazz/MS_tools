# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_workToAsset.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

def nodeTypeSafe(NODE):
	SHAPE = cmds.listRelatives(NODE,s=True,f=True)
	try:
		NODETYPE = cmds.nodeType(SHAPE[0])
		return NODETYPE
	except:
		return False
	
def notParentIsMesh(NODE):
	PARENT = cmds.listRelatives(NODE,p=True,f=True)
	if nodeTypeSafe(PARENT[0])=='mesh':
		return False
	else:
		return True
	
def createRoot():
	if not cmds.objExists('|root'):cmds.group(n='|root',em=True)
	if not cmds.objExists('|root|mesh'):cmds.group(n='mesh',em=True,p='|root')
	if not cmds.objExists('|root|pre_atgi'):cmds.group(n='pre_atgi',em=True,p='|root')
	if not cmds.objExists('|root|atgi'):cmds.group(n='atgi',em=True,p='|root')


def main():
	createRoot()
	SEL = cmds.listRelatives(ad=True,typ='transform',f=True)
	for each in SEL:	

		NODETYPE = nodeTypeSafe(each)
		if NODETYPE=='mesh':
			DUPED = cmds.duplicate(each)
			DUPED = cmds.ls(DUPED,l=True)
			cmds.parent(DUPED[0],'root|mesh')
			
		if NODETYPE=='GraviteAtgiLocatorNode':
			DUPED = cmds.duplicate(each)
			DUPED = cmds.ls(DUPED,l=True)
			cmds.parent(DUPED[0],'root|atgi')

	cmds.select(['|root'],r=True)
	if cmds.objExists('|col'):
		cmds.select(['|col'],add=True)
	if cmds.objExists('|sdw'):
		cmds.select(['|sdw'],add=True)
	if cmds.objExists('|low'):
		cmds.select(['|low'],add=True)
	if cmds.objExists('|occ'):
		cmds.select(['|occ'],add=True)



def LayoutA():
	cmds.columnLayout('MSG2_workToAsset.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_workToAsset.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	
UI()