# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_fileExport.py
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import os
import importlib

import _lib.MS_STORE_RECALL_UI as MS_STORE_RECALL_UI
importlib.reload(MS_STORE_RECALL_UI)

##### エクスプローラーで開く系 #####
def OPEN_EXPLOROR(DIR,MODE=''):
	DIR=DIR.replace('/','\\')
	
	if DIR[-1]=='\\':#行末がバックスラッシュの場合
		WINDOWS_PATH=DIR
	elif MODE=='file':#
		WINDOWS_PATH
	else :#ファイルパスの場合
		WINDOWS_PATH='\\'.join(DIR.split('\\')[:-1])
	
	os.popen('explorer "%s"' % WINDOWS_PATH)
	
	
def PRE_OPEN_Exploror(*args):
	CONTROLL_NAME=cmds.columnLayout('MS_fileExport_COLUMNLAYOUT',q=True,ann=True)
	OPEN_EXPLOROR(cmds.textField(CONTROLL_NAME+'_FILE_PATH',q=True,tx=True))
	
def PRE_OPEN_Exploror2(CONTROLL_NAME):
	OPEN_EXPLOROR(cmds.textField(CONTROLL_NAME+'_FILE_PATH',q=True,tx=True))
	
def FILE_BROUSER(*args):#TOROパスファイルダイアログ
	CONTROLL_NAME=cmds.columnLayout('MS_fileExport_COLUMNLAYOUT',q=True,ann=True)
	TORO_FILE_PATH=cmds.fileDialog2(ds=2,okc='SelectDir',fm=3,dir=cmds.textField(CONTROLL_NAME+'_FILE_PATH',q=True,fileName=True))
	if TORO_FILE_PATH:
		cmds.textField(CONTROLL_NAME+'_FILE_PATH',e=True,fileName=TORO_FILE_PATH[0]+'\\')
		STORE_RECALL(CONTROLL_NAME,'store')
		
#####

def FILE_BROUSER_A(*args):#TOROパスファイルダイアログ
	CONTROLL_NAME=cmds.columnLayout('MS_fileExport_COLUMNLAYOUT',q=True,ann=True)
	TORO_FILE_PATH=cmds.fileDialog2(ds=2,okc='SelectDir',fm=3,dir=cmds.textField(CONTROLL_NAME+'A_PATH',q=True,fileName=True))
	if TORO_FILE_PATH:
		cmds.textField(CONTROLL_NAME+'A_PATH',e=True,fileName=TORO_FILE_PATH[0]+'\\')
		STORE_RECALL(CONTROLL_NAME,'store')
			
def FILE_BROUSER_B(*args):#TOROパスファイルダイアログ
	CONTROLL_NAME=cmds.columnLayout('MS_fileExport_COLUMNLAYOUT',q=True,ann=True)
	TORO_FILE_PATH=cmds.fileDialog2(ds=2,okc='SelectDir',fm=3,dir=cmds.textField(CONTROLL_NAME+'B_PATH',q=True,fileName=True))
	if TORO_FILE_PATH:
		cmds.textField(CONTROLL_NAME+'B_PATH',e=True,fileName=TORO_FILE_PATH[0]+'\\')
		STORE_RECALL(CONTROLL_NAME,'store')
	
def USE_OBJECT_NAME_CHECK(*args):
	CONTROLL_NAME=cmds.columnLayout('MS_fileExport_COLUMNLAYOUT',q=True,ann=True)
	if cmds.checkBox(CONTROLL_NAME+'USE_OBJECT_NAME_CHECK',q=True,v=True):
		cmds.textField(CONTROLL_NAME+'FILE_NAME',e=True,en=0)
	else:
		cmds.textField(CONTROLL_NAME+'FILE_NAME',e=True,en=1)
	STORE_RECALL(CONTROLL_NAME,'store')
	
def STORE_RECALL(CONTROLL_NAME,MODE):
	PREFIX=''
	CONTROLL_DICT={}
	CONTROLL_DICT.setdefault('floatFieldList', [''])
	CONTROLL_DICT.setdefault('intFieldList', [''])
	CONTROLL_DICT.setdefault('floatSliderGrpList', [''])
	CONTROLL_DICT.setdefault('intSliderGrpList', [''])
	CONTROLL_DICT.setdefault('checkBoxList', [CONTROLL_NAME+'USE_OBJECT_NAME_CHECK'])
	CONTROLL_DICT.setdefault('radioButtonGrpList', [''])
	CONTROLL_DICT.setdefault('frameLayoutList', [''])
	CONTROLL_DICT.setdefault('textFieldList', [CONTROLL_NAME+'FILE_NAME'])
	CONTROLL_DICT.setdefault('textFieldList_file', [CONTROLL_NAME+'_FILE_PATH',CONTROLL_NAME+'A_PATH',CONTROLL_NAME+'B_PATH',])
	
	if MODE=='store':
		MS_STORE_RECALL_UI.store(PREFIX,CONTROLL_DICT)
	if MODE=='recall':
		MS_STORE_RECALL_UI.recall(PREFIX,CONTROLL_DICT)
	if MODE=='reset':
		MS_STORE_RECALL_UI.reset(PREFIX,CONTROLL_DICT)

def NORMAL_UI(CONTROLL_NAME,FILE_FILTER='*.*',LABEL=u'ファイルパス',MODE='file',Q=False):#ノーマルエキスポートのファイルのブラウザ
	if Q:
		return cmds.textField(CONTROLL_NAME+'_FILE_PATH',q=True,tx=True)
	
	cmds.columnLayout('MS_fileExport_COLUMNLAYOUT',ann=CONTROLL_NAME)
	cmds.rowLayout(nc=3 ,cw3=[100,80,20])
	cmds.text(w=100,label=u'ファイルパス',ann=u'ファイルを出力するパスを設定します')
	cmds.button(CONTROLL_NAME+'Brouse',w=80,label='Brouse',c=FILE_BROUSER)
	cmds.button(w=20,bgc=[0.6,0.8,0.9],label='e',c=PRE_OPEN_Exploror)
	cmds.setParent('..')
	cmds.textField(CONTROLL_NAME+'_FILE_PATH',w=200,en=0,fileName='D:/export/')
	
	cmds.rowLayout(nc=2,cw2=[50,160],ann=u'オブジェクト名をファイル名に使用するオプションがOFFのときに有効です')
	cmds.text(label=u'ファイル名')
	
	ECC=True
	if MS_STORE_RECALL_UI.check('fileExport__'+CONTROLL_NAME+'USE_OBJECT_NAME_CHECK'):
		ECC=False
	cmds.textField(CONTROLL_NAME+'FILE_NAME',en=ECC,w=160,tx='default',cc='MS_fileExport.STORE_RECALL(\''+CONTROLL_NAME+'\',\'store\')')
	cmds.setParent('..')
	
	cmds.checkBox(
		CONTROLL_NAME+'USE_OBJECT_NAME_CHECK',
		l=u'オブジェクト名をファイル名に使用する',
		ann=u'※expoerAllするとシーン名が出力されます。\n※複数のオブジェクト選択時、それぞれ出力されます',
		v=0,
		onc=USE_OBJECT_NAME_CHECK,
		ofc=USE_OBJECT_NAME_CHECK
		)
	cmds.setParent('..')
	STORE_RECALL(CONTROLL_NAME,'recall')
	
def DUAL_UI(CONTROLL_NAME):
	cmds.columnLayout('MS_fileExport_COLUMNLAYOUT',ann=CONTROLL_NAME)
	cmds.rowLayout(nc=4)
	cmds.text(w=100,label=u'ファイルパス',ann=u'ファイルを出力するパスを設定します')
	cmds.textField(CONTROLL_NAME+'A_PATH',w=200,en=0,fileName='D:/export/')
	cmds.button(CONTROLL_NAME+'Brouse',w=80,label='Brouse',c=FILE_BROUSER_A)
	cmds.button(w=20,bgc=[0.6,0.8,0.9],label='e',c=PRE_OPEN_Exploror)
	cmds.setParent('..')
	
	cmds.columnLayout('MS_fileExport_COLUMNLAYOUT',ann=CONTROLL_NAME)
	cmds.rowLayout(nc=4)
	cmds.text(w=100,label=u'ファイルパス',ann=u'ファイルを出力するパスを設定します')
	cmds.textField(CONTROLL_NAME+'B_PATH',w=200,en=0,fileName='D:/export/')
	cmds.button(CONTROLL_NAME+'Brouse',w=80,label='Brouse',c=FILE_BROUSER_B)
	cmds.button(w=20,bgc=[0.6,0.8,0.9],label='e',c=PRE_OPEN_Exploror)
	cmds.setParent('..')

	ECC=True
	if MS_STORE_RECALL_UI.check('fileExport__'+CONTROLL_NAME+'USE_OBJECT_NAME_CHECK'):
		ECC=False
	cmds.textField(CONTROLL_NAME+'FILE_NAME',en=ECC,w=160,tx='default',cc='MS_fileExport.STORE_RECALL(\''+CONTROLL_NAME+'\',\'store\')')
	cmds.setParent('..')
	
	cmds.checkBox(
		CONTROLL_NAME+'USE_OBJECT_NAME_CHECK',
		l=u'オブジェクト名をファイル名に使用する',
		ann=u'※expoerAllするとシーン名が出力されます。\n※複数のオブジェクト選択時、それぞれ出力されます',
		v=0,
		onc=USE_OBJECT_NAME_CHECK,
		ofc=USE_OBJECT_NAME_CHECK
		)
	cmds.setParent('..')
	STORE_RECALL(CONTROLL_NAME,'recall')




#####　NYA
def NYA_FILE_BROUSER(CONTROLL_NAME='NYA',FILE_FILTER="*.nya"):#NYAパスファイルダイアログ
	TORO_FILE_PATH=cmds.fileDialog2(fileFilter=FILE_FILTER,ds=2,okc='SelectDir',fm=1,dir=cmds.textField(CONTROLL_NAME+'_FILE_PATH',q=True,fileName=True))
	if TORO_FILE_PATH:
		cmds.textField(CONTROLL_NAME+'_FILE_PATH',e=True,tx=TORO_FILE_PATH[0].replace('\\','/'))
		STORE_RECALL(CONTROLL_NAME,'store')
			
def NYA(CONTROLL_NAME,FILE_FILTER='*.nya',LABEL=u'ファイルパス',Q=False):#NYAファイルのブラウザ
	if Q:
		return cmds.textField(CONTROLL_NAME+'_FILE_PATH',q=True,tx=True)
		
	cmds.columnLayout(ann=CONTROLL_NAME)
	cmds.rowLayout(nc=3 ,cw3=[100,80,20])
	cmds.text(w=100,label=LABEL,ann=u'ファイルを出力するパスを設定します')
	cmds.button(CONTROLL_NAME+'Brouse',w=80,label='Brouse',c=lambda *args:NYA_FILE_BROUSER(CONTROLL_NAME=CONTROLL_NAME,FILE_FILTER=FILE_FILTER))
	cmds.button(w=20,bgc=[0.6,0.8,0.9],label='e',c=lambda *args:PRE_OPEN_Exploror2(CONTROLL_NAME))
	cmds.setParent('..')
	cmds.textField(CONTROLL_NAME+'_FILE_PATH',w=200,en=0,fileName='D:/export/')
	
	cmds.setParent('..')
	STORE_RECALL(CONTROLL_NAME,'recall')


#####　標準
def singleFileBrouser(CONTROLL_NAME='single',FILE_FILTER="*.*",MODE='file',STORE=True):#ファイルブラウザ
	if MODE=='file' :MODE=1
	if MODE=='filedir' :MODE=2
	if MODE=='dir' :MODE=3
	
	TORO_FILE_PATH=cmds.fileDialog2(fileFilter=FILE_FILTER,ds=2,okc='SelectDir',fm=MODE,dir=cmds.textField(CONTROLL_NAME+'_FILE_PATH',q=True,fileName=True))
	
	if TORO_FILE_PATH:
		PATH=TORO_FILE_PATH[0].replace('\\','/')
		if MODE==2 or MODE==3:
			PATH+='/'
		cmds.textField(CONTROLL_NAME+'_FILE_PATH',e=True,fileName=PATH)
		STORE_RECALL(CONTROLL_NAME,'store')
			
def single(CONTROLL_NAME
	,Q=False			#クエリモード,戻り値：FILENAMEの文字列
	,E=False			#エディットモード
	,LABEL=u'filePath'
	,FILE_FILTER='*.*'	#ダイアログ表示する時のファイルフィルター
	,MODE='file'		#ダイアログの表示モード：'file' or 'filedir' or 'dir'
	,ANN=''			#注釈
	,FILENAME='D:'	#デフォルトのファイルパス
	,RECALL=True	#STORE_RECALL有効
	):#ファイルダイアログ
	
	if Q:
		return cmds.textField(CONTROLL_NAME+'_FILE_PATH',q=True,tx=True)
	if E:
		cmds.textField(CONTROLL_NAME+'_FILE_PATH',e=True,tx=FILENAME)
		return
	
	cmds.columnLayout(ann=ANN,adj=True)
	cmds.rowLayout(nc=3 ,cw3=[100,80,20],adj=True)
	cmds.text(w=100,label=LABEL,ann=u'ファイルを出力するパスを設定します')
	cmds.button(CONTROLL_NAME+'Brouse',w=80,label='Brouse',c=lambda *args:singleFileBrouser(CONTROLL_NAME=CONTROLL_NAME,FILE_FILTER=FILE_FILTER,MODE=MODE,STORE=RECALL))
	cmds.button(w=20,bgc=[0.6,0.8,0.9],label='e',c=lambda *args:PRE_OPEN_Exploror2(CONTROLL_NAME))
	cmds.setParent('..')
	cmds.textField(CONTROLL_NAME+'_FILE_PATH',w=200,en=0,fileName=FILENAME)
	
	cmds.setParent('..')
	if RECALL:
		STORE_RECALL(CONTROLL_NAME,'recall')


