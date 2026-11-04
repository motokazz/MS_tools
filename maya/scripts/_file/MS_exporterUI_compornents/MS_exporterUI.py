# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_exporterUI
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import sys
import os

import MS_exportMb as MS_exportMb
reload(MS_exportMb)
import MS_exportObj as MS_exportObj
reload(MS_exportObj)
import MS_exportFbx as MS_exportFbx
reload(MS_exportFbx)
import MS_mupMa as MS_mupMa
reload(MS_mupMa)

import MS_storeRecallUI as MS_storeRecallUI
reload(MS_storeRecallUI)

OptionVarName = 'MS_exporterUI_formatSelector'

def layoutB(layoutName='mb'):#フォーマット別レイアウト作成
	#store
	cmds.optionVar(stringValue=['MS_exporterUI_formatSelector',layoutName])

	#
	if layoutName=='mb':layoutClass=MS_exportMb
	if layoutName=='obj':layoutClass=MS_exportObj
	if layoutName=='fbx':layoutClass=MS_exportFbx
	if layoutName=='mbgr':layoutClass=MS_mupMa

	if cmds.columnLayout('MS_tools_window_sub',ex=True):
		cmds.deleteUI('MS_tools_window_sub')
	cmds.columnLayout('MS_tools_window_sub',adj=True,p='MS_tools_window_subParent')

	layoutClass.layoutA()
	cmds.setParent('..')


	#selectorChange
	cca=cmds.layout('MS_exporterUI_formatSelector',q=True,ca=True,fpn=True)
	for each in cca:
		cmds.button(each,e=True,bgc=[0.4,0.4,0.4])
	cmds.button ('MS_exporterUI_formatSelector_'+layoutName,e=True,bgc=layoutClass.Exporter.mainLabelColor)


def recallFromatSelector():
	if cmds.optionVar(exists='MS_exporterUI_formatSelector'):
		Ov=cmds.optionVar(q='MS_exporterUI_formatSelector')
		layoutB(layoutName=Ov)


def layoutA():#フォーマットセレクター

	def dark(arr):
		return [ i * j for i, j in zip(arr,[0.4,0.4,0.4])]
	cmds.columnLayout(adj=True)
	cmds.gridLayout('MS_exporterUI_formatSelector',numberOfColumns=4,cellWidthHeight=(50,30))
	cmds.button ('MS_exporterUI_formatSelector_mb',l='mb'	,	bgc=dark(MS_exportMb.Exporter.mainLabelColor)	,c=lambda *args:layoutB('mb'))
	cmds.button ('MS_exporterUI_formatSelector_obj',l='obj'	,	bgc=dark(MS_exportObj.Exporter.mainLabelColor)	,c=lambda *args:layoutB('obj'))
	cmds.button ('MS_exporterUI_formatSelector_fbx',l='fbx'	,	bgc=dark(MS_exportFbx.Exporter.mainLabelColor)	,c=lambda *args:layoutB('fbx'))
	cmds.button ('MS_exporterUI_formatSelector_mbgr',l='mbgr'	,	bgc=dark(MS_mupMa.Exporter.mainLabelColor)	,c=lambda *args:layoutB('mbgr'))
	cmds.setParent('..')
	cmds.setParent('..')



	
def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)

	#フォーマットセレクター
	cmds.columnLayout('MS_tools_window_main',adj=True)

	layoutA()
	
	cmds.setParent('..')
	#フォーマット別レイアウト
	cmds.columnLayout('MS_tools_window_subParent',adj=True)

	cmds.setParent('..')


	cmds.showWindow('MS_tools_window')

	recallFromatSelector()
	#layoutB()



#UI()



