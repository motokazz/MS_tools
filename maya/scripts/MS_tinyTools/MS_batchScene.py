#! /usr/bin/python
# -*- coding: utf-8 -*-
# script created by pymel.melparse.mel2py from mel file:
# d:\mproject\gtools\scripts\_mel2py.mel

import maya.cmds as cmds
import maya.mel as mel
import shutil,os
import re

#execCheckList
#import MS_module.MS_execCheck
#reload(MS_module.MS_execCheck)
#MS_module.MS_execCheck.execCheckSafe('MS_batchScene.py')

#前コマンド
def preCommand():
	pass

#後コマンド
def postCommand():
	pass

#テクスチャコピー部
def MS_batchScene_getDir_EX_PATH():
	PATH=cmds.textField("EX_PATH",q=True,fileName=True)
	EXP_DIR=cmds.fileDialog2(fm=3,dir=PATH,okc='selectDirectory')
	cmds.textField("EX_PATH",e=1,fileName=(EXP_DIR[0] + "/"))
	MS_batchScene_storeRecallUI("store")
	
#現在のプロジェクトを取得
def MS_batchScene_getDir_workspace():
	WORKSPACE=cmds.fileDialog2(fm=3,okc='selectDirectory')
	cmds.workspace((WORKSPACE[0] + '/'),o=True)
	UI()

def MS_batchScene_core():
	EX_PATH=str(cmds.textField("EX_PATH",q=1,fileName=1))
	sourceDir=str(cmds.workspace(q=1,rd=1))
	mbfiles=cmds.getFileList(folder=sourceDir,filespec="*.mb")
	mafiles=cmds.getFileList(folder=sourceDir,filespec="*.ma")
	scenefiles=mbfiles + mafiles
	i=0
	for EACH in scenefiles:
		if cmds.checkBox(("fileList_" + str(i)),q=1,v=1):
			formatCheck=cmds.file(EACH,q=1,typ=1,o=1)
			#シーンを開く
			cmds.file(EACH,typ=formatCheck[0],options="v=0;p=17",o=1,f=1)
			
			#事前コマンド実行したいコマンドを書く
			preCommand()
			
			#シーンを保存する
			filename=EACH.split("/\\")
			cmds.file(rename=(EX_PATH + filename[-1]))
			cmds.file(save=1,type=formatCheck[0],options="v=0;p=17",f=1)
		i+=1
		
	cmds.file(new=1,f=1)
	cmds.confirmDialog(bgc=(1.0, 0.8, 0.5),m="====== backup finish ! =====")
	
def MS_batchScene_storeRecallUI(mode):
	prefix="MS_batchScene"
	floatFieldList=[]
	intFieldList=[]
	floatSliderGrpList=[]
	intSliderGrpList=[]
	checkBoxList=[]
	radioButtonGrpList=[]
	frameLayoutList=[]
	textFieldList=[]
	textFieldList_file=["EX_PATH"]
	cnt=0
	if mode == "store":
		for EACH in floatFieldList:
			cmds.optionVar(floatValue=((prefix + str(EACH)), cmds.floatField(EACH,
				q=1,value=1)))
			
		for EACH in intFieldList:
			cmds.optionVar(intValue=((prefix + str(EACH)), cmds.intField(EACH,
				q=1,value=1)))
			
		for EACH in floatSliderGrpList:
			cmds.optionVar(floatValue=((prefix + str(EACH)), cmds.floatSliderGrp(EACH,
				q=1,value=1)))
			
		for EACH in intSliderGrpList:
			cmds.optionVar(intValue=((prefix + str(EACH)), cmds.intSliderGrp(EACH,
				q=1,value=1)))
			
		for EACH in checkBoxList:
			cmds.optionVar(intValue=((prefix + str(EACH)), cmds.checkBox(EACH,
				q=1,value=1)))
			
		for EACH in radioButtonGrpList:
			cmds.optionVar(intValue=((prefix + str(EACH)), cmds.radioButtonGrp(EACH,
				q=1,select=1)))
			
		for EACH in frameLayoutList:
			cmds.optionVar(intValue=((prefix + str(EACH)), cmds.frameLayout(EACH,
				q=1,collapse=1)))
			
		for EACH in textFieldList:
			cmds.optionVar(stringValue=((prefix + str(EACH)), cmds.textField(EACH,
				q=1,tx=1)))
			
		for EACH in textFieldList_file:
			cmds.optionVar(stringValue=((prefix + str(EACH)), cmds.textField(EACH,
				q=1,fileName=1)))
			
		
	if mode == "recall":
		for EACH in floatFieldList:
			if cmds.optionVar(exists=(prefix + str(EACH))):
				cmds.floatField(EACH,
					e=1,value=cmds.optionVar(q=(prefix + str(EACH))))
				
			
		for EACH in intFieldList:
			if cmds.optionVar(exists=(prefix + str(EACH))):
				cmds.intField(EACH,
					e=1,value=cmds.optionVar(q=(prefix + str(EACH))))
				
			
		for EACH in floatSliderGrpList:
			if cmds.optionVar(exists=(prefix + str(EACH))):
				cmds.floatSliderGrp(EACH,
					e=1,value=cmds.optionVar(q=(prefix + str(EACH))))
				
			
		for EACH in intSliderGrpList:
			if cmds.optionVar(exists=(prefix + str(EACH))):
				cmds.intSliderGrp(EACH,
					e=1,value=cmds.optionVar(q=(prefix + str(EACH))))
				
			
		for EACH in checkBoxList:
			if cmds.optionVar(exists=(prefix + str(EACH))):
				cmds.checkBox(EACH,
					e=1,value=cmds.optionVar(q=(prefix + str(EACH))))
				
			
		for EACH in radioButtonGrpList:
			if cmds.optionVar(exists=(prefix + str(EACH))):
				cmds.radioButtonGrp(EACH,
					e=1,select=cmds.optionVar(q=(prefix + str(EACH))))
				
			
		for EACH in frameLayoutList:
			if cmds.optionVar(exists=(prefix + str(EACH))):
				cmds.frameLayout(EACH,
					e=1,collapse=cmds.optionVar(q=(prefix + str(EACH))))
				
			
		for EACH in textFieldList:
			if cmds.optionVar(exists=(prefix + str(EACH))):
				cmds.textField(EACH,
					e=1,tx=cmds.optionVar(q=(prefix + str(EACH))))
				
			
		for EACH in textFieldList_file:
			if cmds.optionVar(exists=(prefix + str(EACH))):
				cmds.textField(EACH,
					e=1,fileName=cmds.optionVar(q=(prefix + str(EACH))))
				
			
		
	if mode == "reset":
		for EACH in floatFieldList:
			cmds.optionVar(remove=(prefix + str(EACH)))
			
		for EACH in intFieldList:
			cmds.optionVar(remove=(prefix + str(EACH)))
			
		for EACH in floatSliderGrpList:
			cmds.optionVar(remove=(prefix + str(EACH)))
			
		for EACH in intSliderGrpList:
			cmds.optionVar(remove=(prefix + str(EACH)))
			
		for EACH in checkBoxList:
			cmds.optionVar(remove=(prefix + str(EACH)))
			
		for EACH in radioButtonGrpList:
			cmds.optionVar(remove=(prefix + str(EACH)))
			
		for EACH in frameLayoutList:
			cmds.optionVar(remove=(prefix + str(EACH)))
			
		for EACH in textFieldList:
			cmds.optionVar(remove=(prefix + str(EACH)))
			
		for EACH in textFieldList_file:
			cmds.optionVar(remove=(prefix + str(EACH)))
			
def LayoutA():
	cmds.columnLayout('MS_batchScene_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_batchScene',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='MS_batchScene',c=lambda *args:UI())
	#cmds.button(l='selectedNodeToStructs',c=lambda *args:selectedNodeToStructs())
	cmds.separator()
	cmds.setParent('..')	
	

def UI():
	sourceDir=str(cmds.workspace(q=1,rd=1))
	#string $sourceDir=`textField -q -fileName "refferencePath"`;
	mbfiles=cmds.getFileList(folder=sourceDir,filespec="*.mb")
	mafiles=cmds.getFileList(folder=sourceDir,filespec="*.ma")
	scenefiles=mbfiles + mafiles
	if cmds.window('MS_batchScene',q=1,ex=1):
		cmds.deleteUI('MS_batchScene')
		
	cmds.window('MS_batchScene')
	#rowLayout(nc=2,cw2=(210,210))
	#frameLayout()
	cmds.columnLayout()
	#ファイルリスト部
	cmds.button(width=200,c=lambda *args:MS_batchScene_getDir_workspace() and UI(),bgc=(0.7, 0.7, 1.0),label="SetProject")
	cmds.setParent('..')
	SCRLAY=cmds.scrollLayout()
	cmds.columnLayout()
	i=0
	name=[]
	for EACH in scenefiles:
		name=EACH.split("/")
		cmds.checkBox(("fileList_" + str(i)),
			l=(name[- 1]))
		i+=1
		
	cmds.setParent('..')
	cmds.setParent('..')
	
	#EX_PATHダイアログ部
	cmds.columnLayout()
	cmds.text(font='boldLabelFont',width=200,bgc=(1.0, 0.7, 0.7),label="EX_PATH")
	cmds.rowLayout(nc=2,cw2=(150, 50))
	cmds.textField("EX_PATH",
		width=150,fileName=cmds.workspace(q=1,rd=1))
	cmds.button(width=50,c=lambda *args:MS_batchScene_getDir_EX_PATH(),label="Browse")
	cmds.setParent('..')

	#実行ボタン
	cmds.button(width=200,c=lambda *args:MS_batchScene_core(),bgc=(0.7, 1.0, 0.7),label="backUP")
	
	#後処理
	MS_batchScene_storeRecallUI("recall")
	cmds.scrollLayout(SCRLAY,
		h=400,e=1,w=200)
	cmds.window('MS_batchScene',edit=1,width=208,h=510)
	cmds.window('MS_batchScene',s=True,e=1)
	cmds.showWindow('MS_batchScene')
	

