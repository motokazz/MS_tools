# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_batch_export_hacked.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import pymel.core as pm

import os
import re
import subprocess
import shutil

import gravite_ui

import s2000_tools.MSG2_LODTools.MSG2_LODTool as MSG2_LODTool
reload(MSG2_LODTool)

import s2000_tools.MS_lib.MSG2_P4Lib as MSG2_P4Lib
reload(MSG2_P4Lib)

#プラグインのロード
import s2000_tools.MS_tinyTools.MSG2_loadPlugin as MSG2_loadPlugin
reload(MSG2_loadPlugin)
MSG2_loadPlugin.main()


ATGI_NAME_LIST=['']

ATGI_ROOT_PATH = 'D:/Projects/Gravite2/assets/bg/model'

MB_ROOT_PATH = 'D:/Projects/Gravite2/graphic/bg/scenes'

ASSET_LOCAL_PATH_A = 'D:/Projects/Gravite2/assets_local'

ASSET_LOCAL_PATH_B = '/bg/model'


def OpenMB(MBNAME):
	try:
		LOG=[]
		#BGMBRoot
		FPATH=searchPath(MB_ROOT_PATH,MBNAME)
		LOG.append(MSG2_P4Lib.P4CheckOut([FPATH]))
		cmds.file(FPATH,o=True,options='v=0',f=True)
		return LOG
	except:
		return False

def time30fps():
	CTU=cmds.currentUnit(q=True,time=True)
	cmds.currentUnit(time='ntsc',updateAnimation=True)
	if CTU=='ntsc':
		return 'TimeSetting=OK'
	else:
		return 'TimeSetting=Changed to NTSC'
		
def searchOpenMB():
	SEARCHFILENAME=cmds.textField('MS_batch_export_hacked_SEARCH_OPEN_MB',q=True,tx=True)
	SEARCHFILENAME=SEARCHFILENAME.replace(' ','')

	OpenMB(SEARCHFILENAME)

#指定パスからの相対パスを返す　例）module/MS_primitives.py
def searchPath(SEARCHPATH,searchFile='',searchExt='mb'):
	for (root,dir,files) in os.walk(SEARCHPATH):
		#発見時の処理
		for f in files:
			
			fname=f.split('.')[0]
			if (searchFile+'.'+searchExt) == f:
				root=root.replace('\\','/').replace('//','/')
				print root+'/'+f
				return root+'/'+f
	return ''

def copyLocalToAsset(SRC,DST):
	#COPY
	LOG=[]
	LOG.append(DST)
	MSG2_P4Lib.P4CheckOut([DST])
	LOG.append(SRC+' COPY---> '+DST)

	try:
		shutil.copy(SRC,DST)
		LOG.append('COPY SUCCESS! : '+DST)
	except:
		LOG.append('ERROR! : COPY Failure! : '+DST)
	#

	return LOG

def CORE(ATGI_NAME,MB_SAVE=False,TARGET_SHADER=['G_BG_Main']):

	LOG=['=*=*=*=*=*=*=*=*=* '+ATGI_NAME+' =*=*=*=*=*=*=*=*=*']
	
	IGNORE_WORDS=['_bk$','_brk$','_db$','_low$','_sdw$','_occ$']
	for EACH_IGNORE in IGNORE_WORDS:
		if re.search(EACH_IGNORE,ATGI_NAME):
			LOG.append('IGNORE_WORDS_HIT : '+EACH_IGNORE) 
			return LOG

	#################
	# OPENMB
	#################
	RESULT_OPEN_MB = OpenMB(ATGI_NAME)
	LOG.append(str(RESULT_OPEN_MB))
	if not RESULT_OPEN_MB:
		return LOG

	#################
	# オープン後のコマンド
	#################

	#LOD
	LOG.append(MSG2_LODTool.main())

	#UTIL
	LOG.append(time30fps())
	
	#################
	# SAVE
	#################
	if MB_SAVE:
		try:
			cmds.file(save=True,options='v=0')
			LOG.append('SAVE succes !')
		except:
			LOG.append('ERROR! : SAVE Failure!')


	
	#################
	# 拝借gravite_ui
	#################
	# ウィンドウのハンドル名
	TOPWINDOW_HANDLE_NAME = 'GraviteExportUIWindow'

	if not pm.window(TOPWINDOW_HANDLE_NAME, exists=True):
		gravite_ui.open_ui()
	gravite_ui._button_DoIt_push()
	
	#################
	#正規フォルダにコピー
	#################
	#copy_Assets_Local_To_Assets

	ATGI_PATH=ATGI_ROOT_PATH+'/'+ATGI_NAME+'.atgi'
	ASSET_LOCAL_PATH = ASSET_LOCAL_PATH_A+'/'+ATGI_NAME+ASSET_LOCAL_PATH_B+'/'+ATGI_NAME+'.atgi'

	#################
	#COPY
	LOG.extend(copyLocalToAsset(ASSET_LOCAL_PATH,ATGI_PATH))

	if cmds.objExists('|low'):
		LOW_ATGI_PATH=ATGI_ROOT_PATH+'/'+ATGI_NAME+'_low.atgi'
		LOW_ASSET_LOCAL_PATH = ASSET_LOCAL_PATH_A+'/'+ATGI_NAME+ASSET_LOCAL_PATH_B+'/'+ATGI_NAME+'_low.atgi'
		LOG.append('Low Model Catched !')
		LOG.extend(copyLocalToAsset(LOW_ASSET_LOCAL_PATH,LOW_ATGI_PATH))
	
	return LOG

###############
##### IO #####
###############
##### ファイルセーブ #####
def SAVE(ROW,FILE_PATH):
	f=open(FILE_PATH,'w')#'r'読み込み：'w'書き込み：'a'追記：'+'読み書き両方' 't'テキストモード：'b'バイナリーモード
	for each in ROW:
		f.write(each+'\n')
	f.close()
	

#################
# EXEC
#################
def main():

	ATGI_NAMES = cmds.scrollField('MS_batch_export_hacked_atgi_list',q=True,tx=True)

	TARGET_SHADER_LIST=['G_BG_Main']
	if cmds.checkBox('MS_batch_export_hacked_target_lambert',q=True,v=True):
		TARGET_SHADER_LIST.append('lambert')

	ATGI_NAME_LIST = ATGI_NAMES.split()

	ALLLOG = []

	for each in ATGI_NAME_LIST:
		if not each:
			continue
		ALLLOG.extend(CORE(each,MB_SAVE=True,TARGET_SHADER=TARGET_SHADER_LIST))

	for eachlog in ALLLOG:
		print eachlog

	SAVE(ALLLOG,'D:/Projects/Gravite2/tools/maya/maya2014/scripts/python/s2000_tools/MSG2_LODTools/MS_batch_LODexport_hacked.txt')


def LayoutA():
	cmds.columnLayout('MS_batch_export_hacked.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_batch_export_hacked.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.checkBox('MS_batch_export_hacked_target_lambert',l='lambert',v=False)
	cmds.scrollField('MS_batch_export_hacked_atgi_list',h=300)

	cmds.button(l='do',c=lambda *args:main())
	cmds.separator(w=200)
	cmds.textField('MS_batch_export_hacked_SEARCH_OPEN_MB')
	cmds.button(l='SEARCH_OPEN',c=lambda *args:searchOpenMB())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	

