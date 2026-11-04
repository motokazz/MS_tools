# -*- coding:utf-8 -*-
#ツールデータフォーマットをクラスリストに読み込む

import os
import csv
import pickle

#パス設定ファイル読み込み
import MS_toolsPath
reload(MS_toolsPath)

#ツール定義用CSV
import MS_tools_init
reload(MS_tools_init)

##### 初期設定
path=MS_toolsPath.MS_toolsPath() #本スクリプト設置フォルダ取得クラス作成
currentPath=path.currentPath#本スクリプト設置フォルダ取得

main_tools_path=MS_tools_init.maintools_path

#scriptPath ※今のところスクリプトパスはpython、mel、同じフォルダとする
pythonRootPath=MS_tools_init.python_path
melRootPath=MS_tools_init.mel_path

#initPath　csv設定ファイルの場所
initPath=MS_tools_init.init_path

#picklePath
picklePath=MS_tools_init.pickle_path

#iconsPath
iconPath=MS_tools_init.icon_path

#deficonsPath
deficonPath=MS_tools_init.deficon_path

#Datacard用の名前定義
cathegory='cathegory'
iconImage='image' #カラムが無い場合labelと同名を使用
toolLabel='label'
exeMethod='exec'
exCommand='command'
annotation='annotation'
link='link'

###############
#クラス
###############

class IndexedList:#設定ファイル内のインデックス一覧と対応する辞書データ
	def __init__(self,tabLabel='',initFilePath='',indexList=[],dataList=[]):
		self.tabLabel = tabLabel	# タブ名
		self.initFilePath = initFilePath	# 設定ファイルのパス
		self.indexList= indexList	# かぶりの無いインデックス一覧
		self.dataList = dataList	# dataCardクラスのリスト

class dataCard:#各ツールの詳細データクラス
	def __init__(self,cathegory,rDirectry,toolName,iconImage,toolLabel,exeMethod,exCommand,annotation,link):
		self.cathegory=cathegory	#カテゴリ（タブ名）
		self.rDirectry=rDirectry	#ツール設置パス（pythonRootPathからの相対パス）
		self.toolName =toolName		#ツール名
		self.iconImage=iconImage	#アイコンパス
		self.toolLabel=toolLabel	#ツールラベル、アイコンに使用
		self.exeMethod=exeMethod	#実行形式
		self.exCommand=exCommand	#実行コマンド
		self.annotation=annotation	#注釈
		self.link=link


###############
#設定ファイルの指定
###############

#指定フォルダ内の設定ファイルを検索

######################

def initFileToClass():
	initFileClass=[]#InitFileクラスで構成されているリスト
	try:
		initFileClass=loadClass(picklePath) #pickle設定ファイルがあるならそれを使う。
	except:
		initFileClass=BuildInitFileClass() #pickleが無ければ再ビルドして、結果をpickleファイルに保存。
	return initFileClass

def initFileToClass_forceRebuild():
	#強制リビルド
	initFileClass=BuildInitFileClass() #pickleが無ければ再ビルドして、結果をpickleファイルに保存。
	return initFileClass

def BuildInitFileClass():
	#パスリスト作成
	walked(main_tools_path)

	initFileClass=[]
	initFiles = os.listdir(initPath)
	for each in initFiles:
		if not '.csv' in each:
			continue
		else:
			initFileClass.append(dataCardsToClass(each))

	#saveClass(picklePath,initFileClass) #pickleをセーブ

	return initFileClass


###############
# データ作成
###############

def dataCardsToClass(fileName,index=cathegory):
	
	#tabName
	temp=fileName.split('/')
	temp=temp[-1].split('.')
	tabname=temp[0].replace('_ini','')
	
	initFilePath=initPath+fileName
	
	if '.csv' in initFilePath:
		csvFile = open(initFilePath)
	else:
		return
		
	indexList=[]
	dataList=[]

	for row in csv.DictReader(csvFile):

		if not row[index] in indexList:
			indexList.append(row[index])
		
		if not row[exeMethod]:
			continue
			
		#
		if 'py' in row[exeMethod]:
			if 'py' == row[exeMethod]:
				rDpath=''
			else:
				rDpath=searchPath(pythonRootPath,row[exCommand],'py')
				print rDpath
		else:
				rDpath=searchPath(melRootPath,row[exCommand],'mel')

		#CheckIcon　imageカラムが存在するときはそれを使用、なければtoollabelを使用
		try:
			icon=CheckIcon(row[iconImage],row[toolLabel], row[exeMethod],row[cathegory])
		except:
			icon=CheckIcon(row[toolLabel],row[toolLabel], row[exeMethod],row[cathegory])
		
		command=CommandChooser(row[exeMethod],rDpath,row[exCommand],row[toolLabel])

		dataList.append(
			dataCard(
				cathegory=row[cathegory]
				,rDirectry=rDpath
				,toolName=row[toolLabel]
				,iconImage=icon['path']
				,toolLabel=icon['label']
				,exeMethod=row[exeMethod]
				,exCommand=command
				,annotation=row[annotation]
				,link=row[link]
				)
			)
	csvFile.close()
	return IndexedList(tabname,initFilePath,indexList,dataList)

def loadClass(path):
	with open(path,'rb') as f:
		ret = pickle.load(f)
	return ret

def saveClass(path,data):
	with open(path,'wb') as f:
		pickle.dump(data,f)

###############
# メインユーティリティ
###############

WALKED_DATA=[]

def walked(SEARCH_PATH):
	global WALKED_DATA
	WALKED_DATA=[]
	for (root,dir,files) in os.walk(SEARCH_PATH):
		WALKED_DATA.append([root,files])
	print WALKED_DATA

def searchPath(SEARCH_PATH,SEARCH_FILE='',TARGET_EXT='py'):
	global WALKED_DATA
	for EACH in WALKED_DATA:
		if TARGET_EXT=='py':
			if SEARCH_FILE+'.py' in EACH[1]:
				root=EACH[0].replace('\\','/').replace('//','/')
				if root+'/' == pythonRootPath:
					return SEARCH_FILE+'.py'
				else:
					return root.replace(pythonRootPath,'')+'/'+SEARCH_FILE+'.py'
		elif TARGET_EXT=='mel':
			if SEARCH_FILE+'.mel' in EACH[1]:
				root=EACH[0].replace('\\','/').replace('//','/')
				if root+'/' == melRootPath:
					return SEARCH_FILE+'.mel'
				else:
					return root.replace(melRootPath,'')+'/'+SEARCH_FILE+'.mel'
	return ''

def searchIcon(SEARCH_PATH,SEARCH_FILE=''):
	global WALKED_DATA
	FORMAT=['','.bmp','.png','.xpm']

	if '/' in SEARCH_FILE or '\\' in SEARCH_FILE:

		SPLITTED_PATH = SEARCH_FILE.replace('\\','/').split('/')
		RPATH = '/'.join(SPLITTED_PATH[:-1])
		for EACH in WALKED_DATA:
			if RPATH in EACH[0]:
				root=EACH[0].replace('\\','/').replace('//','/')
				if os.path.exists(root+'/'+SPLITTED_PATH[-1]):
					return root+'/'+SPLITTED_PATH[-1]

	for EACH in WALKED_DATA:
		for EACHFORMAT in FORMAT:
			if SEARCH_FILE+EACHFORMAT in EACH[1]:
				root=EACH[0].replace('\\','/').replace('//','/')
				if os.path.exists(root+'/'+SEARCH_FILE+EACHFORMAT):
					return root+'/'+SEARCH_FILE+EACHFORMAT
	return ''

def pathToImportString(path=''):#指定パスからのパス指定をピリオドつなぎで返す　例）module.MS_primitives
	ret=path.replace(pythonRootPath,'').replace('.py','').replace('\\','.').replace('/','.')
	if ret[0] == '.':
		ret=ret[1:]
	return ret

def CommandChooser(exeMethod,rDirectry,execCommand,toolName):#設定ファイルの内容を見て実行コマンドを振り分け
	print rDirectry
	pre_Command=''
	#userSetup.py を使わない場合。各ツール起動ごとに、sys.path.appendを試みる。
	if not MS_tools_init.use_userSetup_py:
		pre_Command+='import sys\r\nif not "'+pythonRootPath+'" in sys.path:sys.path.append("'+pythonRootPath+'")\r\n\r\n'

	#execCheckList
	if MS_tools_init.exec_check_enabled:
		
		pre_Command+='import MS_toolShelf.MS_toolShelf_execCheck as MS_toolShelf_execCheck\r\n'
		pre_Command+='reload(MS_toolShelf_execCheck)\r\n'
		pre_Command+='MS_toolShelf_execCheck.execCheckSafe("'+toolName+'")#execCheckList\r\n\r\n'



	
	#print rDirectry
	if not execCommand:
		return 'none'
	command=''
	#コマンド作成：カラム２を見てコマンド振り分け
	########
	# mel
	########
	if exeMethod=='mel':#Mayaのスクリプトパスに設置してあり、かつ、ファイル名とメインproc名が一致する場合。設定ファイルcommand内をそのまま実行。
		command=('import maya.mel as mel\nmel.eval(\''+execCommand+';\')')
		
	elif exeMethod=='melx':#メインprocなしでの呼び出し。melをsourceするだけ。
		command=('import maya.mel as mel\nmel.eval(\'source\"'+melRootPath+rDirectry+'";\')')
	
	elif exeMethod=='melc':#Mayaのスクリプトパス外に設置してあ、りファイル名とメインproc名が一致する場合。フルパスをsourceしてcommand内を実行。
		command=('import maya.mel as mel\nmel.eval(\'source\"'+melRootPath+rDirectry+'\";'+execCommand+';\')')

	elif exeMethod=='melmel':#ファイル名とメインproc名が一致しない場合
		SPLIT_command=execCommand.split(';')
		command=('import maya.mel as mel\nmel.eval(\'source\"'+melRootPath+SPLIT_command[0]+'\";'+SPLIT_command[1]+';\')')
	
	elif exeMethod=='melexf':#execfileのみ、pythonからmelを実行
		command=('execfile(\''+pythonRootPath+rDirectry+'\')\n')

	########
	# python
	########
	elif exeMethod=='pyex':#ファイル名とメインdef名が一致する場合
		command=('execfile(\''+pythonRootPath+rDirectry+'\')\n'+execCommand+'()\n')

	elif exeMethod=='py':#設定ファイル内に直接起動コマンドを書く場合。
		for TEMP in execCommand.split('\\n') : command+=(TEMP+"\n")#コマンド中の改行を置換
			
	elif exeMethod=='pyui':#メインdef名が[UI()]
		command=('execfile(\''+pythonRootPath+rDirectry+'\')\n'+'UI()\n')

	elif exeMethod=='ipyui':#メインdef名が[UI()]execFileを使わないでちゃんと呼び出す
		if rDirectry : path=pathToImportString(rDirectry)
		else : path=''
		if path : command = ('import '+path+' as '+execCommand+'\n')
		else : command = ('import '+execCommand+'\n')
		command += ('reload('+execCommand+')\n'+execCommand+'.UI()\n')
		
	elif exeMethod=='pyexf':#execfileのみ
		command=('execfile(\''+pythonRootPath+rDirectry+'\')\n')

	else:
		return

	return pre_Command+command
	
def CheckIcon(iconName,labelName,scriptExt,hashString):#アイコンファイルをチェック＆指定
	#空アイコンチェック
	RET=''
	LABEL=''

	if os.path.exists(iconPath+iconName+'.bmp'):#bmpアイコン見つかったら
		RET=(iconPath+iconName+'.bmp')
		LABEL=''
	elif os.path.exists(iconPath+iconName+'.png'):#pngアイコン見つかったら
		RET=(iconPath+iconName+'.png')
		LABEL=''
	elif os.path.exists(iconPath+iconName+'.xpm'):#xpmアイコン見つかったら
		RET=(iconPath+iconName+'.xpm')
		LABEL=''
	elif searchIcon(main_tools_path,iconName):
		RET=searchIcon(main_tools_path,iconName)
	elif 'py' in scriptExt:#アイコン無しでパイソン
		LABEL=''
		ff=deficonPath+'MS_pydef'+str(MS_haser(hashString[0:3]))+'.bmp'
		if os.path.exists(ff):
			RET=ff
		else:
			RET='pythonFamily.xpm'
		LABEL=labelName
	elif 'mel' in scriptExt:#アイコン無しでMel
		ff=deficonPath+'MS_meldef'+str(MS_haser(hashString[0:3]))+'.bmp'
		if os.path.exists(ff):
			RET=ff
		else:
			RET='commandButton.xpm'
		LABEL=labelName
	return {'path':RET,'label':LABEL}

def MS_haser(baseStr):#文字列しだいで0～9までの整数がかえる
	a=0
	for x in baseStr:
		a+=ord(x)
	return a%8



