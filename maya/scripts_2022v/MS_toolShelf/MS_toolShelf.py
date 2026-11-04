# -*- coding:utf-8 -*-
#ヘルプ表示
import maya.cmds as cmds
import maya.mel as mel
import os
import csv

import importlib
from . import MS_toolDataReader
importlib.reload(MS_toolDataReader)

from . import MS_explororUtil
importlib.reload(MS_explororUtil)

from . import MS_toolBoard
importlib.reload(MS_toolBoard)

from . import MS_tools_init
importlib.reload(MS_tools_init)

from . import MS_tools_ranking
importlib.reload(MS_tools_ranking)

#ツール設定読み込み
#ToolListCls=MS_toolDataReader.initFileToClass()
#高速化に成功したので、常にリビルドかけるようにした。20150625
ToolListCls=MS_toolDataReader.BuildInitFileClass()


###############
# storeRecall
###############

def nothing():
	pass

def MS_shelf_storeTab(tab):
	if not MS_tools_init.store_recall_enabled:
		return lambda *args:nothing

	def ret(dummy=''):
		PREFIX='MS_toolsShelf___'
		tls=cmds.tabLayout(tab,q=True,selectTab=True)
		cmds.optionVar(sv=((PREFIX+tab),tls))
	return ret

def MS_shelf_Recall():
	if not MS_tools_init.store_recall_enabled:
		return lambda *args:nothing


	PREFIX='MS_toolsShelf___'

	#tablayouts
	tabLayoutList = []

	for each in ToolListCls:
		tabLayoutList.append(each.tabLabel)

	for each in tabLayoutList:
		try:
			cmds.tabLayout(each,e=True,selectTab=cmds.optionVar(q=(PREFIX+each)))
		except:
			continue

###############
# ユーティリティ
###############

def RebuildInitFileClass():#設定ファイルのリビルド
	global ToolListCls
	ToolListCls=MS_toolDataReader.BuildInitFileClass()
	UI()


###############
# MS_toolBoard
###############

def SendTo_MS_toolBoard(eachShelfTab,clsID=0):
	
	def RetDef(clsID):
		layoutUtil='MS_GToolsShelf_inUtilLayout'

		if cmds.layout(layoutUtil,q=True,ex=True):
			cmds.deleteUI(layoutUtil)
		cmds.columnLayout(layoutUtil,adj=True,p='MS_GToolsShelf_utilLayout')

		#ツールタブの見出し
		cmds.rowLayout(h=16,nc=4,adj=2,cl4=['left','left','right','right'],bgc=[0.4,0.4,0.4])
		cmds.button(l='TS',w=32,h=14,bgc=[0.6,0.8,0.7],c=lambda *args:UI(),annotation='Open MS_ToolBoard')
		cmds.text(l=eachShelfTab.tabLabel,bgc=[0.4,0.4,0.4],al='left',font='boldLabelFont')
		MS_explororUtil.oButton(eachShelfTab.initFilePath,w=30,h=14,ann=u'設定ファイルを開きます')
		MS_explororUtil.eButton(eachShelfTab.initFilePath,w=30,h=14,ann=u'設定ファイルのあるフォルダを開きます')
		cmds.setParent('..')
		
		MS_toolBoard.layoutToolBoard(ToolListCls[int(clsID)])
		
		cmds.setParent('..')

	return RetDef(clsID)

###############
# UI
###############
def midasi(eachShelfTab,clsID):
	#ツールタブの見出し
	cmds.rowLayout(h=16,nc=4,adj=2,cl4=['left','left','right','right'],bgc=[0.4,0.4,0.4])
	cmds.button(l='TB',w=32,h=14,bgc=[0.8,0.7,0.5],c=lambda *args:SendTo_MS_toolBoard(eachShelfTab,clsID),annotation='Open MS_ToolBoard')
	cmds.text(l=eachShelfTab.tabLabel,bgc=[0.4,0.4,0.4],al='left',font='boldLabelFont')
	MS_explororUtil.oButton(eachShelfTab.initFilePath,w=30,h=14,ann=u'設定ファイルを開きます')
	MS_explororUtil.eButton(eachShelfTab.initFilePath,w=30,h=14,ann=u'設定ファイルのあるフォルダを開きます')
	cmds.setParent('..')

def loCreation():

	layoutMenuBar='MS_GToolsShelf_menuBarLayout'
	layoutUtil='MS_GToolsShelf_inUtilLayout'

	if cmds.layout(layoutUtil,q=True,ex=True):
		cmds.deleteUI(layoutUtil)
	cmds.columnLayout(layoutUtil,adj=True,p='MS_GToolsShelf_utilLayout')

	clsID=0	#クラス受け渡し用ツールID
	for eachShelfTab in ToolListCls:
		#ツールメニュー
		cmds.menu(eachShelfTab.tabLabel,l=eachShelfTab.tabLabel,tearOff=True,p=layoutMenuBar)

		#ツールタブの見出し
		midasi(eachShelfTab,clsID)


		#ツールタブレイアウト作成
		cmds.shelfTabLayout( eachShelfTab.tabLabel
			, imageVisible=True
			,cc=MS_shelf_storeTab(eachShelfTab.tabLabel)
			)
		
		#カテゴリ作成
		for cathegory in eachShelfTab.indexList:
			#メニューカテゴリ作成
			cmds.menuItem(eachShelfTab.tabLabel+cathegory,l=cathegory,subMenu=True,tearOff=True,p=eachShelfTab.tabLabel)

			#カテゴリータブ作成
			cmds.shelfLayout(cathegory,p=( eachShelfTab.tabLabel))
			cmds.setParent('..')
		

		#各アイテム作成
		for each in eachShelfTab.dataList:
			#メニューアイテム作成
			cmds.menuItem(
				p=eachShelfTab.tabLabel+each.cathegory
				,label=each.toolName
				,annotation=each.annotation
				,i=each.iconImage
				,c=each.exCommand
			)
			#shelfButton作成
			cmds.shelfButton(
				p=( eachShelfTab.tabLabel+'|'+each.cathegory)
				,iol=each.toolLabel
				,l=each.toolLabel
				,fn='boldLabelFont'
				,i=each.iconImage
				,annotation=each.annotation
				,c=each.exCommand
			)
			
		cmds.setParent( '..' )
		clsID+=1
	cmds.setParent( '..' )


def loOption():
	cmds.frameLayout(l='toolShelfOption',cl=True,cll=True)
	cmds.gridLayout(nc=4,cwh=[150,20])
	cmds.button(l='RebuildInitFileClass',c=lambda *args:RebuildInitFileClass())
	cmds.button(l='MS_tools_ranking',c=lambda *args:MS_tools_ranking.UI())
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_toolShelf',ex=True):
		cmds.deleteUI('MS_toolShelf')
	cmds.window('MS_toolShelf',menuBar=False)
	#mainLayout
	cmds.columnLayout('MS_GToolsShelf_mainLayout',adj=True)
	#menu
	cmds.menuBarLayout('MS_GToolsShelf_menuBarLayout')
	cmds.setParent( '..' )

	#layoutCreation
	cmds.columnLayout('MS_GToolsShelf_utilLayout',adj=True)
	cmds.columnLayout('MS_GToolsShelf_inUtilLayout',adj=True)
	loCreation()
	cmds.setParent( '..' )
	cmds.setParent( '..' )

	#Layout Option
	loOption()

	#/mainLayout
	cmds.setParent( '..' )

	#
	cmds.window('MS_toolShelf',e=True,sizeable=True)
	cmds.showWindow('MS_toolShelf')

	#cmds.window('MS_toolShelf',e=True,te=20,le=20,w=400,h=200)
	MS_shelf_Recall()
	

