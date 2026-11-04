# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_toolLauncher.py
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import os
import subprocess

import MS_fileExport
reload(MS_fileExport)

import MS_STORE_RECALL_UI
reload(MS_STORE_RECALL_UI)





def openFile():#Windows登録アプリで開く
	FILE_PATH=MS_fileExport.single(CONTROLL_NAME='GToolsPath',Q=True).replace('\\','/')+'/'+cmds.textScrollList('MS_toolLauncher_main_scrollList_a',q=True,selectItem=True)[0]
	os.system("start "+FILE_PATH)
	
def openEclipse():#Eclipseで開く
	FILE_PATH=MS_fileExport.single(CONTROLL_NAME='GToolsPath',Q=True).replace('\\','/')+cmds.textScrollList('MS_toolLauncher_main_scrollList_a',q=True,selectItem=True)[0]
	subprocess.Popen(['C:/Program Files/eclipse4.2/eclipse/eclipse.exe',FILE_PATH])
	
def execCommand(MODE='execfile',MODULE_EXEC=False):
	#実行コマンド
	PATH=MS_fileExport.single(CONTROLL_NAME='GToolsPath',Q=True)
	FILENAME=cmds.textScrollList('MS_toolLauncher_main_scrollList_a',q=True,selectItem=True)
	
	if not PATH or not FILENAME:
		return
	
	if MODE=='module':
		exec('import '+FILENAME[0].split('.')[0])
		exec('reload ('+FILENAME[0].split('.')[0]+')')
		print dir(FILENAME[0].split('.')[0])
		exec(FILENAME[0].split('.')[0]+'.UI()')
		print 'import '+FILENAME[0].split('.')[0]
		print 'reload ('+FILENAME[0].split('.')[0]+')'
		print FILENAME[0].split('.')[0]+'.UI()'
	
	if MODE=='execfile':
		FUNC={}
		execfile(PATH.replace('\\','/')+'/'+FILENAME[0],FUNC)
		
		if MODULE_EXEC:#実行モジュール名の指定があったら
			try:
				FUNC[cmds.textScrollList('MS_toolLauncher_moduleList_scrollList_a',q=True,selectItem=True)[0]]()
			except:
				print 'none'
		elif FILENAME[0].split('.')[0] in FUNC.keys():#ファイル名と同じ名前のモジュールがあったら
			try:
				FUNC[FILENAME[0].split('.')[0]]()
			except:
				return
		
		elif 'UI' in FUNC.keys():#UIというモジュールがあったら
			FUNC['UI']()
		
		else:
			moduleList(FUNC.keys())
	
#########################
#####　スクリプトリスト作成
#########################

def pathOptimize(PATH):
	
	if PATH[-1] in ['/','\\']:
		PATH=PATH[0:-1]
	PATH=PATH.replace('\\','/')
	
	return PATH

def mainPathRemove(PATH):
	#メインファイルパスを取り除いたパスを返す
	PPATH=MS_fileExport.single(CONTROLL_NAME='GToolsPath',Q=True)
	
	PPATH=pathOptimize(PPATH)
	PATH=pathOptimize(PATH)
	
	PATH=PATH.replace(PPATH,'')
	
	return PATH


def walk(PATH):
	if PATH=='D:':
		return []
	#サブディレクトリリスト
	files=[]
	for dpath,dnames,fnames in os.walk(PATH):
		for fname in fnames:
			ddpath=mainPathRemove(dpath)
			files.append(ddpath+'/'+fname)
	return files
	
	
def getList(SEARCH_STRING='searchWord',ignoreString='_exec',SEARCH_EXT='py'):
	#リストの取得
	RET=[]
	PATH=MS_fileExport.single(CONTROLL_NAME='GToolsPath',Q=True)
	FILES=walk(PATH)
	for EACH in FILES:
		if (SEARCH_STRING.lower() in EACH.lower()
			and EACH.split('.')[-1].lower() in SEARCH_EXT.lower()
			and not ignoreString.lower() in EACH.lower()
			):
			RET.append(EACH)
	print RET
	return RET
	
	
def createList(SEARCH_STRING='',MODE='list'):
	#リスト作成
	SEARCH_STRING=cmds.textField('MS_toolLauncher_textField_a',q=True,tx=True)
	SEARCH_EXT=cmds.textField('MS_toolLauncher_textField_b',q=True,tx=True)
	LIST=getList(SEARCH_STRING=SEARCH_STRING,SEARCH_EXT=SEARCH_EXT)
	if cmds.textScrollList('MS_toolLauncher_main_scrollList_a',ex=True):
		cmds.deleteUI('MS_toolLauncher_main_scrollList_a')
	if MODE=='list':
		cmds.textScrollList('MS_toolLauncher_main_scrollList_a'
			,numberOfRows=8
			,append=LIST
			,p='MS_toolLauncher_main_columnLayout_b'
			,allowMultiSelection=False
			,doubleClickCommand=lambda *args:execCommand()
			,selectCommand=lambda *args:createModuleList()
			)
	#ここで検索語のSTORE
	storeRecallUI('store')
	
	
def createModuleList():
	#ツールリスト選択から関数リストを作成
	PATH=MS_fileExport.single(CONTROLL_NAME='GToolsPath',Q=True)
	FILENAME=cmds.textScrollList('MS_toolLauncher_main_scrollList_a',q=True,selectItem=True)
	if '.mel' in FILENAME[0]:
		moduleList(['mel script'])
		return
	FUNC={}
	execfile(PATH.replace('\\','/')+'/'+FILENAME[0],FUNC)
	moduleList(FUNC.keys())
	
	
def moduleList(LIST):
	if cmds.textScrollList('MS_toolLauncher_moduleList_scrollList_a',ex=True):
		cmds.deleteUI('MS_toolLauncher_moduleList_scrollList_a')
	cmds.textScrollList('MS_toolLauncher_moduleList_scrollList_a'
		,w=150
		,numberOfRows=8
		,append=LIST
		,p='MS_toolLauncher_main_columnLayout_c'
		,allowMultiSelection=False
		,doubleClickCommand=lambda *args:execCommand(MODULE_EXEC=True)
		)
	
	
#########################
##### UI
#########################
def storeRecallUI( MODE ):
	
	PREFIX='MS_toolLauncher__'
	CONTROLL_DICT={}
	CONTROLL_DICT.setdefault('textFieldList', ['MS_toolLauncher_textField_a','MS_toolLauncher_textField_b'])
	
	if MODE=='store':
		print 'store'
		MS_STORE_RECALL_UI.store(PREFIX,CONTROLL_DICT)
	if MODE=='recall':
		print 'recall'
		MS_STORE_RECALL_UI.recall(PREFIX,CONTROLL_DICT)
	if MODE=='reset':
		MS_STORE_RECALL_UI.reset(PREFIX,CONTROLL_DICT)
	
def layoutA	():
	cmds.frameLayout('MS_toolLauncher_frameLayout',bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'MS_toolLauncher',cll=True,cl=False)
	
	#ファイルダイアログ
	cmds.columnLayout(adj=True)
	MS_fileExport.single(CONTROLL_NAME='GToolsPath',MODE='filedir')
	cmds.setParent('..')
	
	#ツール部
	cmds.rowLayout(nc=2,cw2=[100,50],adj=True)
	
	#検索語
	cmds.columnLayout(adj=True)
	cmds.text(l=u'検索語')
	cmds.textField('MS_toolLauncher_textField_a'
		,tx='searchWord'
		,cc=lambda *args:createList()
		)
	cmds.setParent('..')
	
	#検索拡張子
	cmds.columnLayout(adj=True)
	cmds.text(l=u'検索拡張子')
	cmds.textField('MS_toolLauncher_textField_b'
		,tx='py:mel'
		,cc=lambda *args:createList()
		)
	cmds.setParent('..')
	#
	cmds.setParent('..')#row
	
	#ボタン
	cmds.button(l=u'ファイルを開く'
		,bgc=[0.6,0.6,0.8]
		,h=20
		,c=lambda *args:openFile()
		)
	cmds.button(l=u'eclipseでファイルを開く'
		,bgc=[0.6,0.6,0.8]
		,h=20
		,c=lambda *args:openEclipse()
		)
	cmds.button(l=u'モジュールとしてインポート'
		,bgc=[0.6,0.8,0.6]
		,h=20
		,c=lambda *args:execCommand(MODE='module')
		)
	
	#リスト
	cmds.rowLayout(nc=2,cw2=[100,50],adj=True)
	
	#ツールリスト
	cmds.columnLayout('MS_toolLauncher_main_columnLayout_b',w=100,h=200,adj=True)
	cmds.text(l=u'ツールリスト')
	cmds.textScrollList('MS_toolLauncher_main_scrollList_a',h=200)
	cmds.setParent('..')
	
	#関数リスト
	cmds.columnLayout('MS_toolLauncher_main_columnLayout_c',adj=True)
	cmds.text(l=u'関数リスト')
	cmds.textScrollList('MS_toolLauncher_moduleList_scrollList_a',w=150)
	cmds.setParent('..')
	cmds.setParent('..')#row
	
	
def UI():
	if cmds.window('MS_toolLauncher_main_window',q=True,ex=True):
		cmds.deleteUI('MS_toolLauncher_main_window')
	cmds.window('MS_toolLauncher_main_window',w=217,rtf=True,s=True)
	cmds.columnLayout(adj=True)
	
	layoutA()
	
	cmds.setParent('..')
	
	cmds.showWindow('MS_toolLauncher_main_window')
	storeRecallUI('recall')
	createList()
	


