# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_moduleCollections.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import os

import modules as MOD
reload(MOD)

###  ###

MODULE_PATH='D:/MS_tools/maya/scripts/MS_moduleCollections/modules'

def compileSub():
	FILES=os.listdir(MODULE_PATH)
	for EACH in FILES:
		
		if '__init__' in EACH:continue
		if '.pyc' in EACH:continue

		NAME=EACH.replace('.py','')
		try:
			exec('import MS_moduleCollections.modules.'+NAME+' as '+NAME)
			exec('reload('+NAME+')')
		except:
			pass

###


def LayoutA():
	DIR=dir(MOD)
	cmds.columnLayout('MS_moduleCollections.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_moduleCollections.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	for each in DIR:
		if not '__' in  each:
			try:
				exec('MOD.'+each+'.LayoutA()')
			except:
				pass

	cmds.separator()
	cmds.setParent('..')

def UI():
	compileSub()
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')

	