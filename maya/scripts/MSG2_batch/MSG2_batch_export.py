# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_batch_export.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm

import os
import re
import subprocess
import shutil

import gravite_ui


import s2000_tools.MS_lib.MSG2_P4Lib as MSG2_P4Lib
reload(MSG2_P4Lib)

import s2000_tools.MS_tinyTools.MS_G2ShaderUtil as MS_G2ShaderUtil
reload(MS_G2ShaderUtil)

import s2000_tools.MS_tinyTools.MS_G2RenderUtil as MS_G2RenderUtil
reload(MS_G2RenderUtil)

import s2000_tools.MS_tinyTools.MS_G2lightUtil as MS_G2lightUtil
reload(MS_G2lightUtil)

#プラグインのロード
import s2000_tools.MSG2_sceneCleanup_compornents.MSG2_loadPlugin as MSG2_loadPlugin
reload(MSG2_loadPlugin)
MSG2_loadPlugin.main()


ATGI_NAME_LIST=['']

MB_ROOT_PATH = 'D:/Projects/Gravite2/graphic/bg/scenes'

#PATH DEFINE
ATGI_ASSET_PATH = 'D:/Projects/Gravite2/assets/bg/model'
HKX_ASSET_PATH = 'D:/Projects/Gravite2/assets/bg/collision'
TIF_ASSET_PATH = 'D:/Projects/Gravite2/assets/common/texture'

ASSET_LOCAL_PATH = 'D:/Projects/Gravite2/assets_local'
ATGI_ASSET_LOCAL_PATH = '/bg/model'
HKX_ASSET_LOCAL_PATH = '/bg/collision'
TIF_ASSET_LOCAL_PATH = '/common/texture'

#EXPORT_LOG_PATH
EXPORT_LOG_PATH = 'D:/Projects/Gravite2/tools/maya/maya2014/scripts/python/s2000_tools/MSG2_atgiTools/MS_batch_export_log.txt'


def OpenMB(MBNAME):
	try:
		LOG=[]
		#BGMBRoot
		FPATH=searchPath(MB_ROOT_PATH,MBNAME)
		LOG.append(MSG2_P4Lib.P4CheckOut([FPATH],ENABLE_DIALOG=False))
		cmds.file(FPATH,o=True,options='v=0',f=True,prompt=False)
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
	SEARCHFILENAME=cmds.textField('MS_batch_export_SEARCH_OPEN_MB',q=True,tx=True)
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

#正規データとしてAssetフォルダにコピーする
def copyLocalToAsset(SRC,DST):
	LOG=[]
	LOG.append(DST)
	MSG2_P4Lib.ENABLE_DIALOG=False
	MSG2_P4Lib.P4CheckOut([DST],ENABLE_DIALOG=False)
	LOG.append(SRC+' COPY---> '+DST)

	try:
		shutil.copy(SRC,DST)
		LOG.append('COPY SUCCESS! : '+DST)
	except:
		LOG.append('ERROR! : COPY Failure! : '+DST)
	#
	if not MSG2_P4Lib.P4headRev([DST]):
		if MSG2_P4Lib.P4AddMarking([DST]):
			LOG.append('ADD SUCCESS!'+DST+'\n')
		else:
			LOG.append('ADD FAILURE!'+DST+'\n')

	return LOG

#開いてから実行するスクリプト
def doScript():
	LOG=[]
	
	#CameraFit
	cmds.select('|root',r=True)
	cmds.viewFit(f=1)
	
	#forScreenshot
	MS_G2RenderUtil.G2RenderSetup()
	
	MS_G2lightUtil.previewDirectionalLights()
	
	#PRESET
	LOG.append(MS_G2ShaderUtil.autoPreset())
	
	#UTIL
	LOG.append(time30fps())
	return LOG


def CORE(ATGI_NAME,MB_SAVE=False):

	LOG=['=*=*=*=*=*=*=*=*=* '+ATGI_NAME+' =*=*=*=*=*=*=*=*=*']
	
	IGNORE_WORDS=['_bk$','_db$','_low$','_sdw$','_occ$']
	for EACH_IGNORE in IGNORE_WORDS:
		if re.search(EACH_IGNORE,ATGI_NAME):
			LOG.append('IGNORE_WORDS_HIT : '+EACH_IGNORE) 
			return LOG

	#OPENMB
	RESULT_OPEN_MB = OpenMB(ATGI_NAME)
	LOG.append(str(RESULT_OPEN_MB))
	if not RESULT_OPEN_MB:
		return LOG

	#開いてから実行するスクリプト
	LOG.extend(doScript())

	#SAVE
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
	
	#atgi
	ATGI_LOCAL_PATH = ASSET_LOCAL_PATH+'/'+ATGI_NAME+ATGI_ASSET_LOCAL_PATH+'/'+ATGI_NAME+'.atgi'
	ATGI_PATH=ATGI_ASSET_PATH+'/'+ATGI_NAME+'.atgi'
	LOG.extend(copyLocalToAsset(ATGI_LOCAL_PATH,ATGI_PATH))

	#collision
	HKX_LOCAL_PATH=ASSET_LOCAL_PATH+'/'+ATGI_NAME+HKX_ASSET_LOCAL_PATH+'/'+ATGI_NAME+'.hkx'
	HKX_PATH=HKX_ASSET_PATH+'/'+ATGI_NAME+'.hkx'
	LOG.extend(copyLocalToAsset(HKX_LOCAL_PATH,HKX_PATH))
	
	#texture
	'''
	TIF_ASSET_LOCAL_PATH=ASSET_LOCAL_PATH+'/'+ATGI_NAME+HKX_ASSET_LOCAL_PATH+'/'+ATGI_NAME+'.tif'
	HKX_PATH=HKX_ASSET_PATH+'/'+ATGI_NAME+'.tif'
	LOG.extend(copyLocalToAsset(HKX_ASSET_LOCAL_PATH,HKX_PATH))
	'''

	#################
	#COPY
	#LOG.extend(copyLocalToAsset(ASSET_LOCAL_PATH,ATGI_PATH))
	
	'''
	if cmds.objExists('|low'):
		LOW_ATGI_PATH=ATGI_ASSET_PATH+'/'+ATGI_NAME+'_low.atgi'
		LOW_ASSET_LOCAL_PATH = ASSET_LOCAL_PATH+'/'+ATGI_NAME+ATGI_ASSET_LOCAL_PATH+'/'+ATGI_NAME+'_low.atgi'
		LOG.append('Low Model Catched !')
		LOG.extend(copyLocalToAsset(LOW_ASSET_LOCAL_PATH,LOW_ATGI_PATH))
	'''
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
	#TOPWINDOW_HANDLE_NAME = 'GraviteExportUIWindow'
	gravite_ui.open_ui()
	DS=cmds.confirmDialog(m=u'エキスポート設定しっかりチェックした？\n続ける？',button=['yes','No'],defaultButton='yes',cancelButton='No',dismissString='No')
	if DS=='No':
		return
	DS=cmds.confirmDialog(m=u'本当に続けますか？',button=['yes','No'],defaultButton='yes',cancelButton='No',dismissString='No')
	if DS=='No':
		return

	SAVE_MB=cmds.checkBox('MS_batch_export_MB_SAVE',q=True,v=True)
	ATGI_NAMES = cmds.scrollField('MS_batch_export_atgi_list',q=True,tx=True)

	ATGI_NAME_LIST = ATGI_NAMES.split()

	ALLLOG = []

	for each in ATGI_NAME_LIST:
		gMainProgressBar = mel.eval('$tmp = $gMainProgressBar')
		if cmds.progressBar( gMainProgressBar, q=True , isCancelled = True):
			DS=cmds.confirmDialog(m='Continue?',button=['yes','No'],defaultButton='yes',cancelButton='No',dismissString='No')
			if DS=='No':
				continue
			else:
				break

		if not each:
			continue
		ALLLOG.extend(CORE(each,MB_SAVE=SAVE_MB))

	for eachlog in ALLLOG:
		print eachlog

	SAVE(ALLLOG,EXPORT_LOG_PATH)



def LayoutA():
	cmds.columnLayout('MS_batch_export_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_batch_export',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.checkBox('MS_batch_export_MB_SAVE',l='SaveMB',v=False)
	cmds.scrollField('MS_batch_export_atgi_list',h=300)

	cmds.button(l='doThat',c=lambda *args:main())
	cmds.separator(w=200)
	cmds.textField('MS_batch_export_SEARCH_OPEN_MB')
	cmds.button(l='SEARCH_OPEN',c=lambda *args:searchOpenMB())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	
