# _*_coding:utf-8_*_
########################################
# ファイル名
#			MP_MS_toolBoard
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel
import os
import csv

from . import MS_explororUtil
#reload(MS_explororUtil)

from . import MS_readFileText
#reload(MS_readFileText)

from . import MS_toolsPath
#reload(MS_toolsPath)

path=MS_toolsPath.MS_toolsPath()
pythonRootPath=path.parentPath

#####実行部

def toShelfIcon(TOOL_NAME,COMMAND,ICON,ANNO):
	def pre(dummy,TOOL_NAME=TOOL_NAME,COMMAND=COMMAND,ICON=ICON,ANNO=ANNO):
		TAB=mel.eval("global string $gShelfTopLevel; $temp=$gShelfTopLevel;")
		SELECTED_TAB=cmds.shelfTabLayout(TAB,q=True,st=True)
		cmds.shelfButton(p=SELECTED_TAB,i1=ICON,imageOverlayLabel=TOOL_NAME,ann=ANNO,c=COMMAND)
	return pre

def layoutToolBoard(cls):
	prefix='MS_toolBoard_'

	cmds.columnLayout(cat=('both',1),adj=True)
	cmds.scrollLayout(w=650,h=400)
	#カテゴリごとのフレームレイアウト
	for cathegory in cls.indexList:
		cmds.frameLayout(prefix+cathegory,l=cathegory,w=650,cl=False,cll=True)

		cmds.text(l=cathegory,w=220,bgc=[0.2,0.2,0.2],p=prefix+cathegory)
		cmds.separator(w=220,p=prefix+cathegory)
		cmds.setParent('..')

	#各ツールチップ行作成
	for each in cls.dataList:
		cmds.rowLayout(nc=7,p=prefix+each.cathegory)
		iconPath='D:/Mproject/gtools/icons/'
		cmds.iconTextButton( style='iconAndTextHorizontal', w=200,image1=each.iconImage, label=each.toolName,ann=each.annotation,c=each.exCommand)
		cmds.text(l=each.annotation,w=300,al='left')

		#シェルフ登録するボタン
		cmds.button(l='=> TAB',w=40,h=16,bgc=[0.8,0.8,0.8],c=toShelfIcon(each.toolLabel,each.exCommand,each.iconImage,each.annotation))

		#openFile ファイルを開く
		MS_explororUtil.oButton(pythonRootPath+each.rDirectry,w=24,h=16,bgc=[0.8,0.8,0.75],label='o',ann=u'スクリプトファイルを開く')
		 
		#openDirectory 設置ディレクトリを開く
		MS_explororUtil.eButton(pythonRootPath+each.rDirectry,w=24,h=16,bgc=[0.75,0.8,0.8],label='e',ann=u'設置ディレクトリを開く')
		
		#readFilehead 先頭行から何文字かを表示
		MS_readFileText.rButton(pythonRootPath+each.rDirectry,readLine=10)

		#link ドキュメントなどを開く
		if each.link:
			MS_explororUtil.oButton(path=each.link,w=24,h=16,bgc=[0.75,0.8,0.75],label='doc',ann='Document Link')
		else:
			cmds.text(l='')

		cmds.setParent('..')
	cmds.setParent('..')
	cmds.setParent('..')

#####UI
def UI(cls):
	if cmds.window('MS_toolShelf',q=True,ex=True):
		cmds.deleteUI('MS_toolShelf')
	cmds.window('MS_toolShelf',rtf=True,s=True)
	cmds.scrollLayout()

	layoutToolBoard(cls)
	
	cmds.setParent('..')
	cmds.showWindow('MS_toolShelf')

	


