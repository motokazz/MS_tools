# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_importDragDrop.py
# 説明
#			ウィンドウにインポートしたいファイルをドラッグアンドドロップしてインポートする
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.OpenMaya as OpenMaya


#id = OpenMaya.MSceneMessage_addCheckFileCallback(OpenMaya.MSceneMessage.kBeforeImportCheck, MS_pyDragDrop)
global jobNum
global fid

def aimpo(retCode, fileObject ,c):
	path = fileObject.rawPath ()
	comPath=path[:-1]
	name = fileObject.rawName()
	#comName=name.replace(".py","")
	comName = name.split('.')[0]

	if '.obj' in name:
		if not cmds.pluginInfo('objExport.mll',q=True,loaded=True):
			cmds.loadPlugin('objExport.mll')
		print path+name
		cmds.file(path+name,i=True,type="OBJ",rpr="l",options="mo=1",pr=True,loadReferenceDepth="all")
		print 'OBJ file importing..'

	else:
		util = OpenMaya.MScriptUtil()
		util.setBool ( retCode, True)



def job():
	jobNum = cmds.scriptJob(uid=['MS_importDragDrop',"import file.MS_importDragDrop as MS_importDragDrop\nMS_importDragDrop.killJob()"],protected = True)
	print 'modeStarted : '+str(fid)
	print 'jobStarted : '+str(jobNum)
	print cmds.scriptJob( listJobs=True )

def killJob():
	global fid
	global jobNum
	OpenMaya.MMessage.removeCallback( fid )
	cmds.scriptJob(kill=jobNum,force=True)
	print 'modekilled : '+str(fid)
	print 'killed : '+str(jobNum)
	print cmds.scriptJob( listJobs=True )

def LayoutA():
	
	cmds.columnLayout('MS_tools_mainLayout',adj=True)
	cmds.text('MS_importDragDrop',l='ok')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')

	global jobNum
	
	job()
UI()
