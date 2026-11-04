# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_checkAtgiFile.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import os
import glob

import _lib.MS_explororUtil as MS_explororUtil
reload(MS_explororUtil)

import asobi.asobi_batch.MS_asobi_checkAtgi_BB as MS_asobi_checkAtgi_BB
reload(MS_asobi_checkAtgi_BB)


#モジュールのロード
import asobi.asobi_batch.modules as modules
reload(modules)

#モジュールリーダー
import asobi.asobi_batch.MS_moduleReaders as MS_moduleReaders
reload(MS_moduleReaders)

MS_moduleReaders.MODDIR='D:/MS_tools/maya/scripts/asobi/asobi_batch/atgi_modules/'
MS_moduleReaders.MODULES_PATH = 'asobi.asobi_batch.ma_modules.'


MAIN_PATH = 'D:/asobi/asset/graphic/multi_platformer/levels/'

#

EXPORT_PATH='D:/MS_tools/maya/scripts/asobi/asobi_batch/MS_checkMAFiles.csv'


#################
# 読み込み後のチェック処理メイン
#################

def CHECK_LIST_INDEX():
	RET=[]
	RET.extend(MS_asobi_checkAtgi_BB.index())
	return RET

def CHECK_COMMANDS(ATGIPATH):
	DATA=LOAD(ATGIPATH)
	RET=[]

	RET.extend(MS_moduleReaders.main(DATA))

	#ここまで

	return RET

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
# SHADER CHECK
#################

def ShaderList():
	SHADERLIST=['G2_BG_Main'
		,'G2_BG_Mask'
		,'G2_CD_Main'
		,'G2_CH_Main'
		,'G2_EF_Main'
		,'G_BG_Cloud'
		,'G_BG_GStone'
		,'G_BG_Glow'
		,'G_BG_Grass'
		,'G_BG_Leaf'
		,'G_BG_Main'
		,'G_BG_Mblend'
		,'G_BG_Multi'
		,'G_BG_Occluder'
		,'G_BG_Shadow'
		,'G_BG_Sky'
		,'G_BG_Vblend'
		,'G_BG_Window'
		,'G_CD_Main'
		,'G_CH_Grasses'
		,'G_CH_Main'
		,'G_CH_Vein'
		,'G_EF_Deform'
		,'G_EF_Distortion'
		,'G_EF_Main'
		,'G_EF_Refraction'
		,'G_EF_Smoke'
		,'G_EF_Core'
		,'G_EN_Main'
		,'G_EN_Vien'
		]
	return SHADERLIST

def checkAtgiShader(DATA):
	SHADERLIST=ShaderList()
	TEMP=[]
	for EACHSHADE in SHADERLIST:
		try:
			CATCH=0
			for EACHDATA in DATA:
				if u'<attribute name="type" type="string">'+EACHSHADE+'</attribute>' in EACHDATA:
					CATCH+=1
			TEMP.append(str(CATCH))
		except:
			TEMP.append('e')

	return TEMP
	

#################
# 担当チェック
#################
def checkAutor(FILENAME):
	AUTHORS=['md','nk','sk','kw','kk','nt','ms','fl','ks','vi','xp']
	for eachAUTHOR in AUTHORS:
		if ('_'+eachAUTHOR+'_') in FILENAME:
			return eachAUTHOR
	return 'none'

#################
# 属性チェック
#################
def RaceList():
	RACELIST=['_bk'
		,'_brk'
		,'_db'
		,'_low'
		,'_sdw'
		,'_occ'
		]
	return RACELIST

def checkRace(FILENAME):
	RET=[]
	for eachRACE in RaceList():
		if eachRACE in FILENAME:
			RET.append('@')
		else:
			RET.append('-')
	return RET

#################
# ファイルネーム最適化
#################
def checkFileName(ATGIPATH):
	TEMP=ATGIPATH.split('/')[-1].split('\\')[-1].split('.')[0]
	return TEMP

#################
# MAIN
#################

def main(PATH=MAIN_PATH):

	#ファイルパス
	QQ=cmds.textField('MS_checkAtgiFile_dir',q=True,tx=True)
	if QQ:
		PATH=QQ

	FILES=glob.glob(PATH+'/*.ma')

	#プログレスバー
	MS_Progress()
	cmds.progressBar('MS_progress',edit=True,beginProgress=True,isInterruptable=True,maxValue=len(FILES))

	#見出し
	DATA=['FILENAME,AUTHOR,'+','.join(RaceList())+','+','.join(CHECK_LIST_INDEX())]

	for each in FILES:
		FN=checkFileName(each)
		#ROW = FN+','+checkAutor(FN)+','+','.join(checkRace(FN))+','+','.join(CHECK_COMMANDS(each))
		ROW=MS_moduleReaders.main(FN)
		DATA.append(ROW)
		cmds.progressBar('MS_progress',edit=True,s=1)#プログレス

	SAVE(DATA,EXPORT_PATH)

	cmds.deleteUI('MS_ProgressWindow')#プログレス

def main_batch_list(PATH=MAIN_PATH):
	#UIから情報を取得
	TARGET_NAMES = cmds.scrollField('MS_batch_List',q=True,tx=True)
	TARGET_NAME_LIST = TARGET_NAMES.replace(' ','').replace('\t','').replace('\\','/').split()
	FILES=[]
	for each in TARGET_NAME_LIST:
		FILES.append(PATH+'/'+each+'.ma')

	#プログレスバー
	MS_Progress()
	cmds.progressBar('MS_progress',edit=True,beginProgress=True,isInterruptable=True,maxValue=len(FILES))

	#見出し
	DATA=['FILENAME,AUTHOR,'+','.join(RaceList())+','+','.join(CHECK_LIST_INDEX())]

	for each in FILES:
		FN=checkFileName(each)
		#ROW = FN+','+checkAutor(FN)+','+','.join(checkRace(FN))+','+','.join(CHECK_COMMANDS(each))
		ROW=MS_moduleReaders.main(FN)
		DATA.append(ROW)
		cmds.progressBar('MS_progress',edit=True,s=1)#プログレス

	SAVE(DATA,EXPORT_PATH)

	cmds.deleteUI('MS_ProgressWindow')#プログレス

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
	cmds.progressBar('MS_progress',maxValue=10,width=246)
	cmds.setParent ('..')
	cmds.showWindow ('MS_ProgressWindow')

def Layout_batch_List():
	cmds.columnLayout(adj=True)
	cmds.separator()
	cmds.text(l='MS_batch_List',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.scrollField('MS_batch_List',h=300)
	cmds.button(l='doThat',c=lambda *args:main_batch_list())
	cmds.setParent('..')

def LayoutA():
	cmds.columnLayout('MS_checkAtgiFile_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_checkAtgiFile',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.textField('MS_checkAtgiFile_dir',tx=MAIN_PATH)
	MS_explororUtil.eButton(path=EXPORT_PATH)
	MS_explororUtil.oButton(path=EXPORT_PATH)
	cmds.button(l='do All',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('asobi_window',q=True,ex=True):
		cmds.deleteUI('asobi_window')
	cmds.window('asobi_window',rtf=True,s=True)
	
	LayoutA()
	Layout_batch_List()
	
	MS_moduleReaders.Layout_modules()

	cmds.showWindow('asobi_window')
	
