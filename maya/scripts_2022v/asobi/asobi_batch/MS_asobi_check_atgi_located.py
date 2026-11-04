# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_asobi_check_atgi_located.py
# 説明
#			
#			
# 作成日
#			
########################################


import maya.cmds as cmds
import sys
import glob
import csv
import collections

from _lib.MS_xlsx2csv import Xlsx2csv

import _lib.MS_explororUtil as MS_explororUtil
reload(MS_explororUtil)

#AtgiPath
PATH = 'D:/asobi/asset/graphic/multi_platformer/bg/models'

#LevelPath
LEVEL_PATH = 'D:/asobi/asset/graphic/multi_platformer/levels'

#その他のドキュメント
MUP_LEVELS_XML = 'D:/asobi/target/data/multi_platformer/mup_levels.xml'
PLACEMENT_XLSX ='D:/Projects/Gravite2/planning/datasheets/Placements.xlsx'
PLACEMENT_CSV ='D:/MS_tools/maya/scripts/asobi/asobi_batch/Placements.csv'

EVDS=[
	'D:/Projects/Gravite2/target/common/script/bg/debrisDefinition.evd'
	,'D:/Projects/Gravite2/target/common/script/bg/FurnitureList.evd'
	,'D:/Projects/Gravite2/target/common/script/bg/GuidanceHandResourceInfo.evd'
	,'D:/Projects/Gravite2/target/common/script/bg/treeDefinition.evd'
	,'D:/Projects/Gravite2/target/common/script/bg/tvDamageAndSound.evd'
	,'D:/Projects/Gravite2/target/common/script/bg/tvDefinition.evd'
	,'D:/Projects/Gravite2/target/common/script/bg/tvSchedule.evd'
	]


### 出力パス ###
EXPORT_PATH = 'D:/MS_tools/maya/scripts/asobi/asobi_batch/'

ANILIZED_LIST = EXPORT_PATH+'MS_asobi_check_atgi_anlize_location.csv'
PLACED_LIST = EXPORT_PATH+'MS_asobi_check_atgi_located.csv'
NOT_PLACED_LIST = EXPORT_PATH+'MS_asobi_check_atgi_not_located.csv'

LOGFILE = EXPORT_PATH + 'MS_asobi_check_atgi_log.csv'


#################
# IO
#################

# ファイルが書き込み可能かどうかを調べる
def checkFileWritable(FILE_PATH=''):
	def TRY_OPEN():
		try:
			f=open(FILE_PATH,'w')#'r'読み込み：'w'書き込み：'a'追記：'+'読み書き両方' 't'テキストモード：'b'バイナリーモード
			f.close()
			return True
		except:
			
			return False
	CON=True
	while(CON):
		if TRY_OPEN():
			CON=False
			return
		else:
			DS=cmds.confirmDialog(m=u'ログファイルがロックされています。\rログを開いている場合は、閉じてください',button=['Continue','Cancel'],defaultButton='Continue',dismissString='Cancel')
			if DS=='Cancel':
				CON=False
				sys.exit()

def SAVE(ROW=[],FILE_PATH=''):
	f=open(FILE_PATH,'w')#'r'読み込み：'w'書き込み：'a'追記：'+'読み書き両方' 't'テキストモード：'b'バイナリーモード
	for each in ROW:
		f.write(each+'\n')
	f.close()

def LOAD(FILE_PATH):
	f=open(FILE_PATH)
	DATA=[]
	for ROW in f:
		DATA.append(ROW)
	f.close()
	return DATA

#################
# ファイルネーム最適化
#################

def checkFileName(ATGIPATH):		#フルパス文字列からATGI名だけ抜き出す。
	TEMP=ATGIPATH.strip().split('/')[-1].split('\\')[-1].split('.')[0]
	return TEMP

#################
# XLSX2CSV
#################

def xlsx2csv(XLSX='',CSV=''):
	X=Xlsx2csv(XLSX)
	X.convert(CSV)

def csvImport(PATH=''):
	RET=[]
	f = open(PATH, 'rb')

	dataReader = csv.reader(f)

	for ROW in dataReader:
		RET.append(ROW)
	return RET

def anlizePlacements_core(DATA):
	DICT={}
	MIDASHI=DATA.pop(0)
	i=0
	for key in MIDASHI:
		TEMP=[]
		for each in DATA:
			AAA=each[i].split()
			for eachAAA in AAA:
				TEMP.append(eachAAA.strip())	
		DICT.setdefault(key,TEMP)
		i+=1
	return DICT
	'''
	datasheet_placements
	grab
	levitation
	fall
	move
	shake
	broken_model
	debris_model
	mid_models
	dynamic_model
	'''

def anlizePlacements():
	RET=[]
	xlsx2csv(PLACEMENT_XLSX,PLACEMENT_CSV)
	DATA=csvImport(PLACEMENT_CSV)
	NEW = anlizePlacements_core(DATA)
	RET.append('datasheet_placements'+','.join(NEW['datasheet_placements']))
	RET.append('broken_model'+','.join(NEW['broken_model']))
	RET.append('debris_model'+','.join(NEW['debris_model']))
	RET.append('mid_models'+','.join(NEW['mid_models']))
	RET.append('dynamic_model'+','.join(NEW['dynamic_model']))
	return RET

#################
# メインリスト（アナライズリスト）作成
#################
#子供にAtgi配置しているものを全てリスト

def anilize_AtgiInAtgi(DATA): 		#Atgiファイルから、設置されているAtgiを抜き出す。
	TEMP=[]
	for EACHDATA in DATA:

		if '.atgi' in EACHDATA:
			PRE = EACHDATA.split('/')[-1].split('\\')[-1].strip().replace('"','').replace(';','')
			PRE=checkFileName(PRE)
			TEMP.append(PRE)

	return TEMP
	
def listAtgiInAtgi():				#全ATGI設置情報をリスト化
	checkFileWritable(ANILIZED_LIST)#ログ書き込み可能確認

	DATA=[]

	#listAreaDefinition
	#DATA.append(listAreaDefinition())

	#anlizePlacements
	#DATA.extend(anlizePlacements())

	#anlizeEVD
	#for each in EVDS:
	#	DATA.append(anlizeEVD(each))
		

	##################
	#assets/modelsフォルダ
	##################

	#FILES=glob.glob(PATH+'/*.ma')
	FILES = listAreaDefinition()
	#プログレスバー
	MS_Progress()
	cmds.progressBar('MS_progress',edit=True,beginProgress=True,isInterruptable=True,maxValue=len(FILES))

	
	for each in FILES:
		try:
			each = LEVEL_PATH+'/mup_level_'+each+'.ma'
			ROW=checkFileName(each)
			LOADED=LOAD(each)
			USE=anilize_AtgiInAtgi(LOADED)

			if USE:
				ROW+=','+','.join(USE)
				DATA.append(ROW)
		except:
			print 'error　: '+each
		cmds.progressBar('MS_progress',edit=True,s=1)#プログレス


	SAVE(DATA,ANILIZED_LIST)

	cmds.deleteUI('MS_ProgressWindow')#プログレス

def listAreaDefinition():
	LOADED=LOAD(MUP_LEVELS_XML)
	TEMP=[]
	for each in LOADED:
		if '<File>' in each:
			LS = each.replace('<File>','').replace('</File>','').strip()
			TEMP.append(LS)
	TEMP=list(set(TEMP))
	TEMP=sorted(TEMP)
	
	#cmds.scrollField('MS_asobi_check_atgi_located_logField',e=True,tx='\n'.join(TEMP))
	return TEMP

def anlizeEVD(PATH=''):
	NAME=PATH.split('/')[-1].replace('.','_')
	LOADED=LOAD(PATH)
	TEMP=[]
	for each in LOADED:
		LS=each.replace('"',':').split(':')
		for eachLS in LS:
			eachLS=eachLS.strip()

			#SKIP
			if '#' in eachLS:continue
			if not eachLS:continue
			
			#
			TEMP.append(eachLS)

	TEMP=list(set(TEMP))
	TEMP=sorted(TEMP)
	
	#cmds.scrollField('MS_asobi_check_atgi_located_logField',e=True,tx='\n'.join(TEMP))
	return NAME+','+','.join(TEMP)

def test():
	for each in EVDS:
		print anlizeEVD(each)


#################
# 　検索リスト作成　
#################

def listSortAndCount(LIST=[]):
	RET=[]
	DICT=collections.Counter(LIST)
	for each in DICT.keys():
		RET.append(each+','+str(DICT[each]))
	return RET

### 　検索コア　###

def searchPlaced(DATA,ATGINAME=''):	#Atgiファイル内の記述（メインリスト）から配置情報を取得
	RET=[]
	for each in DATA:
		TEMP=each.strip().split(',')
		PARENT_ATGINAME=TEMP.pop(0)
		if ATGINAME in TEMP:
			RET.append(PARENT_ATGINAME)
	return RET

def searchChilds(DATA,ATGINAME=''):
	RET=[]
	for each in DATA:
		TEMP=each.strip().split(',')
		PARENT_ATGINAME=TEMP.pop(0).strip()
		if ATGINAME == PARENT_ATGINAME:
			if len(TEMP):
				RET.extend(TEMP)
	return RET

def searchDocument(DATA,ATGINAME=''):	#テキストファイルから記述を検索
	RET=[]
	for each in DATA:
		if '#' in each:
			continue
		if ATGINAME in each:
			return True
	return False

def searchList2(DATA,ATGINAME=''):	#2重リストファイルから記述を検索
	for each in DATA:
		for each2 in each:
			if ATGINAME == each2.strip():
				return True
	return False

### 　検索リスト作成コア　###
#配置されているものリストと配置されていない物リストを作成

#　全配置情報
def searchNotPlaced(NMIN=0,NMAX=0):			#未使用Atgiをリスト化

	checkFileWritable(NOT_PLACED_LIST)#　ログ書き込み可能確認

	NMIN=int(cmds.intField('MS_asobi_check_atgi_located_NMIN',q=True,v=True))
	NMAX=int(cmds.intField('MS_asobi_check_atgi_located_NMAX',q=True,v=True))
	LOG=[]

	FILES=glob.glob(PATH+'/*.ma')

	### 壊れ物削除 ###
	#i=0
	#for each in FILES:
	#	if '_brk_' in each:
	#		FILES.pop(i)
	#	i+=1

	#プログレスバー
	MS_Progress()


	### 未配置Atgiを探す ###
	cmds.progressBar('MS_progress',edit=True,beginProgress=True,isInterruptable=True,maxValue=len(FILES))

	DATA=LOAD(ANILIZED_LIST)

	ATGIPLACED=[]
	for each in FILES:
		NAME=checkFileName(each)
		RESULT=searchPlaced(DATA,ATGINAME=NAME)
		if len(RESULT)>=NMIN and len(RESULT)<=NMAX:
			ATGIPLACED.append(NAME)
		cmds.progressBar('MS_progress',edit=True,s=1)#プログレス
	cmds.deleteUI('MS_ProgressWindow')#プログレス

	SAVE(ATGIPLACED,NOT_PLACED_LIST)

	#### areaDefinition を探す ###
	#DATA=LOAD(MUP_LEVELS_XML)
	#AREAPLACED=[]
	#for each in ATGIPLACED:
	#	RESULT=searchDocument(DATA,ATGINAME=each)
	#	if not RESULT:
	#		AREAPLACED.append(each)

	### 壊れ物削除 ###
	#for each in AREAPLACED:
	#	if not '_brk_' in each:
	#		LOG.append(each)

	#SAVE(LOG,NOT_PLACED_LIST)

def searchPlacedALL():			#使用中のAtgiをリスト化

	def searchPlaced2(DATA,ATGINAME=''):	#Atgiファイル内の記述（メインリスト）から配置情報を取得
		RET=[]
		for each in DATA:
			TEMP=each.strip().split(',')
			PARENT_ATGINAME=TEMP.pop(0)
			if ATGINAME in TEMP:
				COUNT = TEMP.count(ATGINAME)
				RET.append([PARENT_ATGINAME,COUNT])
		return RET

	checkFileWritable(PLACED_LIST)#　ログ書き込み可能確認

	LOG=[]

	#ATGI配置情報をリスト化
	FILES=glob.glob(PATH+'/*.ma')


	#プログレスバー
	MS_Progress()

	### 未配置Atgiを探す ###
	cmds.progressBar('MS_progress',edit=True,beginProgress=True,isInterruptable=True,maxValue=len(FILES))

	DATA=LOAD(ANILIZED_LIST)

	ATGIPLACED=['NAME,level_count,total_placed,placed_lvl_1,count1,placed_lvl_2,count2']
	for each in FILES:
		NAME=checkFileName(each)
		GET=searchPlaced2(DATA,ATGINAME=NAME)
		if GET:
			TEMP = ''
			TOTAL_COUNT = 0
			for GETS in GET:
				TOTAL_COUNT+=GETS[1]
				TEMP += ','+GETS[0]+','+str(GETS[1])

			ATGIPLACED.append(NAME+','+str(len(GET))+','+str(TOTAL_COUNT)+TEMP)
		cmds.progressBar('MS_progress',edit=True,s=1)#プログレス
	cmds.deleteUI('MS_ProgressWindow')#プログレス


	#### areaDefinition を探す ###
	DATA=LOAD(MUP_LEVELS_XML)
	AREAPLACED=[]
	for each in FILES:
		if searchDocument(DATA,ATGINAME=each):
			AREAPLACED.append(each)


	LOG=ATGIPLACED

	SAVE(LOG,PLACED_LIST)

#　指定検索
def searchAtgiFromName(NAME=[]):			#名前を指定してAtgi配置状況を調べる

	checkFileWritable(LOGFILE)#　ログ書き込み可能確認

	LOG=['name,count,parents']
	DATA=LOAD(ANILIZED_LIST)

	if not NAME:
		SNAME=cmds.scrollField('MS_asobi_check_atgi_located_seachWord',q=True,tx=True).split()
	else:
		SNAME=NAME

	for each in SNAME:
		GET=searchPlaced(DATA,ATGINAME=each.strip())
		if GET:
			LOG.append(each+','+str(len(GET))+','+','.join(GET))
		else:

			LOG.append(each+',0')

	if not NAME:
		cmds.scrollField('MS_asobi_check_atgi_located_logField',e=True,tx='\n'.join(LOG))
		SAVE(LOG,LOGFILE)
	else:
		return LOG

def searchAtgiFromRoot():	#子供に使われている全Atgiを調べる
	
	checkFileWritable(LOGFILE)#　ログ書き込み可能確認

	LOG=['name,count']
	#LOG.append('atginame,count,placed')
	DATA=LOAD(ANILIZED_LIST)
	NAME=cmds.scrollField('MS_asobi_check_atgi_located_seachWord',q=True,tx=True).split()
	ALLGETS=[]
	ALLGETS.extend(NAME)

	GET_ALL_USE=[]

	i=0
	while(i<len(ALLGETS)):
		GET=searchChilds(DATA,ATGINAME=ALLGETS[i].strip())
		GET_ALL_USE.extend(GET)
		for each in GET:
			if not each in ALLGETS:
				ALLGETS.append(each.strip())

		#無限ループ防止
		i+=1
		if i>1000000: 
			break
	
	LOG.extend(listSortAndCount(GET_ALL_USE))

	cmds.scrollField('MS_asobi_check_atgi_located_logField',e=True,tx='\n'.join(LOG))
	SAVE(LOG,LOGFILE)

def searchAtgiChildlen(): #子供のみ出力
	
	checkFileWritable(LOGFILE)#　ログ書き込み可能確認

	LOG=['name,count']
	#LOG.append('atginame,count,placed')
	DATA=LOAD(ANILIZED_LIST)
	NAME=cmds.scrollField('MS_asobi_check_atgi_located_seachWord',q=True,tx=True).split()
	ALLGETS=[]
	ALLGETS.extend(NAME)

	GET_ALL_USE=[]


	for each in ALLGETS:
		GET=searchChilds(DATA,ATGINAME=each.strip())
		GET_ALL_USE.extend(GET)

	LOG.extend(listSortAndCount(GET_ALL_USE))

	cmds.scrollField('MS_asobi_check_atgi_located_logField',e=True,tx='\n'.join(LOG))
	SAVE(LOG,LOGFILE)


#################
# UI
#################

def MS_Progress():
	#プログレスウィンドウ
	if cmds.window('MS_ProgressWindow',ex=True):
		cmds.deleteUI('MS_ProgressWindow')
	if cmds.windowPref('MS_ProgressWindow',ex=True):
		cmds.windowPref('MS_ProgressWindow',r=True)
	cmds.window('MS_ProgressWindow',wh=[248,70],tlc=[414,516],tlb=True,s=True,t='Calculating')
	cmds.columnLayout()
	cmds.progressBar('MS_progress',pr=0,minValue=0,maxValue=10,width=246)
	cmds.setParent ('..')
	cmds.showWindow ('MS_ProgressWindow')

def MS_Progress_():
	cmds.progressBar('MS_progress',edit=True,s=1)#プログレス
	cmds.getModifiers()

def Layout_allPlacedList():
	cmds.frameLayout(l=u'全配置情報リスト',cl=True,cll=True)
	#
	cmds.rowLayout(nc=3,cw3=[150,50,50])
	cmds.text(l=u'配置数検索：最小値・最大値',w=150)
	cmds.intField('MS_asobi_check_atgi_located_NMIN',v=0,w=50)
	cmds.intField('MS_asobi_check_atgi_located_NMAX',v=0,w=50)
	cmds.setParent('..')
	#
	cmds.rowLayout(nc=3,cw3=[200,16,16])
	cmds.button(l=u'未配置Atgiリスト',w=200,c=lambda *args:searchNotPlaced())
	MS_explororUtil.oButton(path=NOT_PLACED_LIST)
	MS_explororUtil.eButton(path=NOT_PLACED_LIST)
	cmds.setParent('..')
	#
	cmds.rowLayout(nc=3,cw3=[200,16,16])
	cmds.button(l=u'配置済みAtgiリスト',w=200,c=lambda *args:searchPlacedALL())
	MS_explororUtil.oButton(path=PLACED_LIST)
	MS_explororUtil.eButton(path=PLACED_LIST)
	cmds.setParent('..')
	#
	cmds.setParent('..')

def LayoutA():
	cmds.columnLayout('MS_asobi_check_atgi_located_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_asobi_check_atgi_located',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	#
	cmds.rowLayout(nc=3,cw3=[200,16,16])
	cmds.button(l=u'リスト更新（１５分くらいかかります）',w=200,bgc=[0.6,0.8,0.6],c=lambda *args:listAtgiInAtgi())
	MS_explororUtil.oButton(path=ANILIZED_LIST)
	MS_explororUtil.eButton(path=ANILIZED_LIST)
	cmds.setParent('..')

	cmds.separator(h=20)
	#
	cmds.frameLayout(l=u'指定検索',cl=False,cll=False)
	cmds.columnLayout(adj=True)
	cmds.text(l=u'ターゲットアセット名（複数記入可）')
	
	cmds.scrollField('MS_asobi_check_atgi_located_seachWord')
	#execbutton
	cmds.rowLayout(nc=3,cw3=[82,82,82],cat=[(1,'both',0),(2,'both',0),(3,'both',0)])
	cmds.button(l=u'親検索',bgc=[0.8,0.8,0.6],c=lambda *args:searchAtgiFromName())
	cmds.button(l=u'子検索',bgc=[0.6,0.8,0.8],c=lambda *args:searchAtgiChildlen())
	cmds.button(l=u'子孫検索',bgc=[0.6,0.6,0.8],c=lambda *args:searchAtgiFromRoot())
	cmds.setParent('..')
	#
	cmds.separator()

	#LOG
	cmds.rowLayout(nc=3,cw3=[200,16,16])
	cmds.text(l=u'LOG',w=150)
	MS_explororUtil.oButton(path=LOGFILE)
	MS_explororUtil.eButton(path=LOGFILE)
	cmds.setParent('..')

	cmds.scrollField('MS_asobi_check_atgi_located_logField')
	cmds.setParent('..')
	cmds.setParent('..')
	#
	cmds.separator(h=20)
	Layout_allPlacedList()

	cmds.button(l=u'test',bgc=[0.6,0.6,0.8],c=lambda *args:test())

	cmds.setParent('..')

def UI():
	if cmds.window('MS_asobi_check_atgi_located_window',q=True,ex=True):
		cmds.deleteUI('MS_asobi_check_atgi_located_window')
	cmds.window('MS_asobi_check_atgi_located_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_asobi_check_atgi_located_window')
	

