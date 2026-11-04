# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_railTools.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import MSG2_atgiTools.MSG2_railCreator as MSG2_railCreator
reload(MSG2_railCreator)

import MSG2_atgiTools.MSG2_railPartsCreator as MSG2_railPartsCreator
reload(MSG2_railPartsCreator)

LO=MSG2_railCreator.LayoutA

def main(MODE):
	global LO
	if MODE=='RailCreator':
		LO=MSG2_railCreator.LayoutA

	if MODE=='PartsCreator':
		LO=MSG2_railPartsCreator.LayoutA
	UI()

def LayoutA():
	cmds.columnLayout('MSG2_railTools.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_railTools.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.gridLayout(nc=2,cwh=[80,16])
	cmds.button(l='RailCreator',c=lambda *args:main('RailCreator'),bgc=[0.7,0.8,0.7])
	cmds.button(l='PartsCreator',c=lambda *args:main('PartsCreator'),bgc=[0.7,0.7,0.8])
	cmds.setParent('..')
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MSG2_railTools_window',q=True,ex=True):
		cmds.deleteUI('MSG2_railTools_window')
	cmds.window('MSG2_railTools_window',rtf=True,s=True)
	
	LayoutA()
	LO()
	
	cmds.showWindow('MSG2_railTools_window')
	