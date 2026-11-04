# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_superImport.py
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds
import maya.mel as mel


import MS_filePathUI as MS_filePathUI
reload (MS_filePathUI)


fpf=MS_filePathUI.filePathField()

def superImport():
	fname = fpf.startingDirectry

	if '.mb' in fname:
		cmds.file(fname,i=True,options="mo=1",pr=True,loadReferenceDepth="all")

	if '.obj' in fname:
		if not cmds.pluginInfo('objExport.mll',q=True,loaded=True):
			cmds.loadPlugin('objExport.mll')
		cmds.file(fname,i=True,type="OBJ",pr=True,loadReferenceDepth="all")

	if '.fbx' in fname:
		if not cmds.pluginInfo('fbxmaya.mll',q=True,loaded=True):
			cmds.loadPlugin('fbxmaya.mll')
		cmds.file(fname,i=True,type='FBX',pr=True,loadReferenceDepth="all")

	if '.3DS' in fname:
		if not cmds.pluginInfo('studioImport.mll',q=True,loaded=True):
			cmds.loadPlugin('studioImport.mll')
		cmds.file(fname,i=True,type='3DS',pr=True,loadReferenceDepth="all")

def layoutA():
	fpf.domainLayout='MS_superImport_domainLayout'
	fpf.fileMode=1
	fpf.fileFilter="All Files (*.*)"
	cmds.columnLayout(fpf.domainLayout)
	fpf.pathBrouser()
	cmds.button(l='import',c=lambda *args:superImport())
	cmds.button(l='import options',c=lambda *args:mel.eval('ImportOptions'))
	cmds.setParent('..')

def UI():
	if cmds.window('MS_superImport_window',q=True,ex=True):
		cmds.deleteUI('MS_superImport_window')
	cmds.window('MS_superImport_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_superImport_window')
	
