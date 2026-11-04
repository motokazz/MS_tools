# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_BatchRefference.py
# 説明
#			モーションMBをエフェクト用にリファレンスします
# 作成日
#			2012/07/30	坂井元一
########################################

import maya.cmds as cmds
import maya.mel as mel

import MS_STORE_RECALL_UI
reload(MS_STORE_RECALL_UI)

'''-----------------------------------------------------------------------------
指定入力フォルダ内のファイルのを、ひとつづつリファレンス化して 指定出力フォルダ内に新しいシーンとして作成。
リファレンス元のスクリプトパスから、トータルフレーム数をぬきだして、出力シーンに設定する。
'''
def MS_BatchRefferenceScene( EXPORT_DIR, BASE_NAME ):
	charsetName = BASE_NAME [4:]
	stringLengthN = BASE_NAME
	stringLength = BASE_NAME [:-4]
	animName =BASE_NAME
	
	filename = EXPORT_DIR + animName + "_eff.mb"
	
	print ("baseName = [" + BASE_NAME + "] " + stringLengthN + ":\n")
	print ("charName = [" + charsetName + "] : animName [" + animName + "]\n" )
	print("fileName = [" + filename + "]\n" )
	
	#ここからシーン読み込み後のセーブコマンド
	
	SAVE_SCENE_COMMAND = ("file -rename \""+ filename + "\";file -f -options \"v=0\" -type \"mayaBinary\" -save;")
	
	print SAVE_SCENE_COMMAND
	mel.eval( SAVE_SCENE_COMMAND )


def MS_BatchRefferenceAll():
	#リファレンス作成
	SOURCE_DIR=cmds.textField( 'refferencePath',q=True,fileName=True)+'/'
	EXPORT_DIR=cmds.textField('exportPath',q=True,fileName=True)+'/'
	cmds.workspace( dir=SOURCE_DIR)
	print ( "------------------------------\nexport directory : " + EXPORT_DIR + "\n\n" )
	
	#***************** MB 
	
	SCENE_FILES = cmds.getFileList(folder=SOURCE_DIR ,filespec="*.mb")
	for EACH_SCENE in SCENE_FILES:
		
		REAL_NAME = SOURCE_DIR + EACH_SCENE
		print REAL_NAME + "\n"
		BASE_NAME = REAL_NAME.split('/')[-1].split('.')[0]
		
		print( "export : [" + BASE_NAME + "]\n" )
		
		#ファイル読み込み
		cmds.file(f=True,new=True)
		cmds.file(REAL_NAME,r=True,type='mayaBinary',gl=True,namespace=BASE_NAME,options="v=0")
		
		#scriptNodeの実行
		SCRIPT_NODE_NAME=cmds.ls(typ='script')#読み込み時のスクリプトをリスト
		for EACH in SCRIPT_NODE_NAME:
			if EACH in '*sceneConfigurationScriptNode*':
				SET_TIME_COMMAND=cmds.scriptNode(q=True,bs=each)
				mel.eval(SET_TIME_COMMAND)
		MS_BatchRefferenceScene( EXPORT_DIR, BASE_NAME )
		
	cmds.file(f=True,new=True)
	
	#***************** MA 
	'''
		SCENE_FILES[] = getFileList -folder workspace -filespec "*.ma"
		for( i=0 i<size SCENE_FILES i++ )
		
			REAL_NAME = workspace + EACH_SCENE
			print( REAL_NAME + "\n" )
			
			#file -f -options "v=0"  -typ "mayaAscii" -o REAL_NAME
			
			FILE_BASE = basename REAL_NAME ".ma"
			#FileNameMender FILE_BASE
			BASE_NAME = basenameEx FILE_BASE
			stringLengthNX = size BASE_NAME
			
			print( "export : [" + BASE_NAME + "]\n" )
			
			#MS_BatchRefferenceScene( EXPORT_DIR, BASE_NAME )
			
			file -f -new
		
		file -f -new
	'''
	print("file convert end...\n")
	
def storeRecallUI( MODE ):
	PREFIX='MP_MS_BatchRefference__'
	CONTROLL_DICT={}
	CONTROLL_DICT.setdefault('textFieldList_file', ['refferencePath','exportPath'])
	if MODE=='store':
		MS_STORE_RECALL_UI.store(PREFIX,CONTROLL_DICT)
	if MODE=='recall':
		MS_STORE_RECALL_UI.recall(PREFIX,CONTROLL_DICT)
	if MODE=='reset':
		MS_STORE_RECALL_UI.reset(PREFIX,CONTROLL_DICT)
	
def MS_BatchRefference_fileBrowser(CONTROLL_NAME):
	FILE_PATH=cmds.fileDialog2(ds=2,okc='SelectDir',fm=3,dir=cmds.textField(CONTROLL_NAME,q=True,fileName=True))
	if FILE_PATH:
		cmds.textField(CONTROLL_NAME,e=True,fileName=FILE_PATH[0].replace('\\','/'))
		storeRecallUI('store')
		
def UI():
	
	if cmds.window ('MS_BatchRefference',q=True,ex=True):
		cmds.deleteUI('MS_BatchRefference')
	cmds.window('MS_BatchRefference')
	cmds.columnLayout()
	
	#--DataPart--#
	cmds.text(bgc=[0.7,0.7,1.0],width=200,font='boldLabelFont', label='refferencePath') #Data#
	cmds.rowLayout(nc=2,cw2=[150,50])
	cmds.textField ('refferencePath',fileName='',width=150) #Data#
	cmds.button(width=50,label='Brouse',c=lambda *args:MS_BatchRefference_fileBrowser('refferencePath'))
	cmds.setParent('..')
		
	cmds.text(bgc=[0.7,0.7,1.0],width=200,font='boldLabelFont', label='exportPath') #Data#
	cmds.rowLayout(nc=2,cw2=[150,50])
	cmds.textField ('exportPath',fileName='',width=150) #Data#
	cmds.button(width=50,label='Brouse',c=lambda *args:MS_BatchRefference_fileBrowser('exportPath'))
	cmds.setParent('..')
	
	cmds.separator(width=200,height=10)
	cmds.button(width=200,bgc=[0.7,1.0,0.7],label='batchRefference' ,c=lambda *args:MS_BatchRefferenceAll())
	#--DataPart--#
	cmds.window('MS_BatchRefference',edit=True,width=208,height=136)
	cmds.showWindow('MS_BatchRefference')
	storeRecallUI('recall')


