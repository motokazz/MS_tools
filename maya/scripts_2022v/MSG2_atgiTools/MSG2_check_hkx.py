# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_check_hkx.py
# 説明
#			
#			
# 作成日
#			
########################################


import maya.cmds as cmds
import glob

import _lib.MS_explororUtil as MS_explororUtil
reload(MS_explororUtil)

PATH='D:/Projects/Gravite2/assets/bg/collision'

DATASHEETS_EVS='D:/Projects/Gravite2/target/common/script/datasheets.evs'
AREADEFINITION_EVD='D:/Projects/Gravite2/target/common/script/area/areaDefinition.evd'

### 出力パス ###
EXPORT_PATH='D:/Projects/Gravite2/tools/maya/maya2014/scripts/python/s2000_tools/MSG2_atgiTools/'

ANILIZED_LIST=EXPORT_PATH+'MSG2_check_hkx_anlize.csv'
PLACED_LIST=EXPORT_PATH+'MSG2_check_hkx.csv'
NOT_PLACED_LIST=EXPORT_PATH+'MSG2_check_atgi_not_located.csv'


#################
# IO
#################

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
	TEMP=ATGIPATH.split('/')[-1].split('\\')[-1].split('.')[0]
	return TEMP

#################
# メインリスト（アナライズリスト）作成
#################
#子供にAtgi配置しているものを全てリスト
def anlize_hkx(DATA):
	TEMP=[]
	TYPECHECK=True
	for each in DATA:
		#TYPECHECK
		if TYPECHECK:
			if '"hknpCompressedMeshShape"' in each:
				TEMP.append('MESH')
				TYPECHECK=False
			if '"hknpConvexPolytopeShape"' in each:
				TEMP.append('HULL')
				TYPECHECK=False

		#EXTRARADIUS
		if '<field name="convexRadius">' in each:
			DEC=each.split('"')[3]
		elif '<real name="convexRadius">' in each:
			DEC=each.split(' -->')[0].split('<!-- ')[1]
		else:
			continue

		

		#ERRORCHECK
		if float(DEC)>0.01:
			TEMP.append('TRUE')
		else:
			TEMP.append('FALSE')

		TEMP.append(DEC)

		break

	try:
		if TEMP[0]=='MESH':
			if TEMP[1]=='TRUE':
				TEMP.append('ERROR')
			elif not TEMP[2]=='0.01':
				TEMP.append('WARRNING')
			else:
				TEMP.append('OK')

		elif TEMP[0]=='HULL':
			if TEMP[1]=='FALSE':
				TEMP.append('ERROR')
			elif TEMP[2]=='0':
				TEMP.append('ERROR:exrad=0')
			elif not TEMP[2]=='0.05':
				TEMP.append('WARRNING')
			else:
				TEMP.append('OK')
		else:
			TEMP.append('ERROR:cant ditect type')
		
	except:
		TEMP.append('DATA ERROR')

	return TEMP

def listAtgiInAtgi():				#　全ATGI設置情報をリスト化
	
	FILES=glob.glob(PATH+'/*.hkx')
	
	#プログレスバー
	MS_Progress()
	cmds.progressBar('MS_progress',edit=True,beginProgress=True,isInterruptable=True,maxValue=len(FILES))

	DATA=[]
	for each in FILES:
		#壊れ物スキップ
		if '_bk.' in each:continue
		if '_db.' in each:continue
		

		ROW=checkFileName(each)
		LOADED=LOAD(each)
		USE=anlize_hkx(LOADED)
		if USE:
			ROW+=','+','.join(USE)
			DATA.append(ROW)
		cmds.progressBar('MS_progress',edit=True,s=1)#プログレス

	SAVE(DATA,ANILIZED_LIST)

	cmds.deleteUI('MS_ProgressWindow')#プログレス

#################
# 　検索リスト作成　
#################

### 　検索コア　###

def searchPlaced(DATA,ATGINAME=''):	#Atgiファイル内の記述（メインリスト）から配置情報を取得
	RET=[]
	for each in DATA:
		TEMP=each.split(',')
		PARENT_ATGINAME=TEMP.pop(0)
		if ATGINAME in TEMP:
			RET.append(PARENT_ATGINAME)
	return RET

def searchCollisionAttr(DATA,ATGINAME=''):
	for each in DATA:
		if ATGINAME in each:
			return each.strip()
	return False

### 　検索リスト作成コア　###
#配置されているものリストと配置されていない物リストを作成

def searchHkxFromName():			#名前を指定してAtgi配置状況を調べる
	LOG=[]
	DATA=LOAD(ANILIZED_LIST)
	NAME=cmds.scrollField('MSG2_check_hkx_seachWord',q=True,tx=True).split()
	for each in NAME:
		GET=searchCollisionAttr(DATA,ATGINAME=each.strip())
		if GET:
			LOG.append(GET)

	
	cmds.scrollField('MSG2_check_hkx_logField',e=True,tx='\n'.join(LOG))




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

def LayoutA():
	cmds.columnLayout('MSG2_check_hkx_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_check_hkx',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	#
	cmds.rowLayout(nc=3,cw3=[200,16,16])
	cmds.button(l=u'リスト更新（１５分くらいかかります）',w=200,c=lambda *args:listAtgiInAtgi())
	MS_explororUtil.oButton(path=ANILIZED_LIST)
	MS_explororUtil.eButton(path=ANILIZED_LIST)
	cmds.setParent('..')	
	#
	cmds.separator()
	#
	cmds.separator()
	#
	cmds.scrollField('MSG2_check_hkx_seachWord')
	cmds.button(l=u'hkx名からコリジョンアトリビュートを表示',c=lambda *args:searchHkxFromName())
	cmds.separator()

	#LOG
	cmds.text(l=u'LOG',w=150)
	cmds.scrollField('MSG2_check_hkx_logField')

	cmds.setParent('..')


def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	