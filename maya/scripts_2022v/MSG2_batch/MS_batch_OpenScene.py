# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_batch_OpenScene.py
# 説明
#			
#			
# 作成日
#			
########################################


import maya.cmds as cmds

import os
import re
import subprocess
import shutil
import glob
#
import s2000_tools.MS_lib.MSG2_P4Lib as MSG2_P4Lib
reload(MSG2_P4Lib)
#
import s2000_tools.MS_exporterUI_compornents.MS_swatchMaker as MS_swatchMaker
reload(MS_swatchMaker)

#
import MSG2_auto_export
reload(MSG2_auto_export)




#モジュールのロード
import s2000_tools.MSG2_batch.modules as modules
reload(modules)


#プラグインのロード
import s2000_tools.MSG2_sceneCleanup_compornents.MSG2_loadPlugin as MSG2_loadPlugin
reload(MSG2_loadPlugin)
MSG2_loadPlugin.main()

#DEF
EXPORT_LOG_PATH='D:/Projects/Gravite2/tools/maya/maya2014/scripts/python/s2000_tools/MSG2_batch/MS_batch.csv'

###############
##### IO #####
###############
def OpenMB(MBNAME):
	LOG=[]
	#BGMBRoot
	FPATH=searchPath('D:/Projects/Gravite2/graphic/bg/scenes',MBNAME)
	LOG.append(MSG2_P4Lib.P4CheckOut([FPATH],False))
	cmds.file(FPATH,o=True,options='v=0',f=True)
	return LOG

##### ファイルセーブ #####
def SAVE(ROW,FILE_PATH):
	f=open(FILE_PATH,'w')#'r'読み込み：'w'書き込み：'a'追記：'+'読み書き両方' 't'テキストモード：'b'バイナリーモード
	for each in ROW:
		f.write(each+'\n')
	f.close()
	
#################
# Module Readers
#################

def module_list():
	MODULES=[]
	MODDIR='D:/Projects/Gravite2/tools/maya/maya2014/scripts/python/s2000_tools/MSG2_batch/modules/'
	ML=glob.glob(MODDIR+'*.py')
	for each in ML:
		if '__' in each:
			continue
		MODULES.append(each.replace('\\','/').replace('.py','').replace(MODDIR,''))
	return MODULES

def commandCreation(MODULES_PATH,MODULE_NAME,TARGET_NAME='',dummy=''):
	IMPC='import ' + MODULES_PATH+MODULE_NAME+'\n'
	IMPC+='reload('+MODULES_PATH+MODULE_NAME+')\n'
	COMMAND=MODULES_PATH+MODULE_NAME+'.main("'+TARGET_NAME+'")\n'
	RET=execs(IMPC,COMMAND)
	if RET:
		return RET
	else:
		return 'ok'

def moduleExecuter(MODULE_NAME='',TARGET_NAME=''):
	TARGET_NAME=cmds.file(q=True,sn=True).split('/')[-1].strip('.mb')
	MODULES_PATH = 's2000_tools.MSG2_batch.modules.'
	def ret(dummy=''):
		commandCreation(MODULES_PATH,MODULE_NAME,TARGET_NAME)
	return ret

def execs(IMPC,COMMAND):
	print COMMAND
	exec(IMPC)
	RET=eval(COMMAND)
	return RET

#################
# CORE
#################
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


def doScript(TARGET_NAME):
	RET=[]
	#FP=searchPath('D:/Projects/Gravite2/graphic/bg/scenes',TARGET_NAME)
	if not cmds.checkBox('MS_batch_mainLayout_open_scene',q=True,v=True):
		RET.append(doScript2(TARGET_NAME))
		return RET

	try:
		OpenMB(TARGET_NAME)
	except:
		return
	#
	LOG=doScript2(TARGET_NAME)

	#SAVE
	if cmds.checkBox('MS_batch_mainLayout_save_scene',q=True,v=True):
		try:
			cmds.file(save=True,options='v=0')
			LOG+=',SAVE succes !'
		except:
			LOG+=',ERROR! : SAVE Failure!'

	#MSG2_auto_export
	if cmds.checkBox('MS_batch_mainLayout_export_scene',q=True,v=True):
		try:
			LOG+=MSG2_auto_export.main(TARGET_NAME)
			LOG+=',Export succes !'
		except:
			LOG+=',ERROR! : Export Failure!'

	RET.append(TARGET_NAME+','+LOG)
	return RET

def doScript2(TARGET_NAME):
	LOG=[]
	LOG.append(TARGET_NAME)
	MODULES_PATH = 's2000_tools.MSG2_batch.modules.'

	MODULES=module_list()

	for each in MODULES:
		print each
		if not cmds.checkBox(each,q=True,ex=True):
			LOG.append('notfound')
			continue
		if cmds.checkBox(each,q=True,v=True):
			LOG.append(commandCreation(MODULES_PATH,each,TARGET_NAME))

	return ','.join(LOG)

#################
# EXEC
#################

def main():
	#事前確認
	DS=cmds.confirmDialog(m=u'しっかりチェックした？\n続ける？',button=['yes','No'],defaultButton='yes',cancelButton='No',dismissString='No')
	if DS=='No':
		return
	DS=cmds.confirmDialog(m=u'本当に続けますか？',button=['yes','No'],defaultButton='yes',cancelButton='No',dismissString='No')
	if DS=='No':
		return
	
	#####
	ALLLOG = []
	
	#UIから情報を取得
	TARGET_NAMES = cmds.scrollField('MS_batch_List',q=True,tx=True)
	TARGET_NAME_LIST = TARGET_NAMES.replace(' ','').replace('\t','').replace('\\','/').split()
	
	#メインループ
	for each in TARGET_NAME_LIST:
		if not each:
			continue
		ALLLOG.extend(doScript(each))

	#ログをプリント
	for eachlog in ALLLOG:
		print eachlog

	#ログを保存
	SAVE(ALLLOG,EXPORT_LOG_PATH)


#################
# UI
#################


def Layout_modules():
	MODULES=module_list()
	cmds.columnLayout()
	for each in MODULES:
		cmds.rowLayout(nc=2,cw2=(200,50))
		cmds.checkBox(each,l=each,v=False)
		cmds.button(l='do',w=50,c=moduleExecuter(each))
		cmds.setParent('..')
	cmds.setParent('..')


def LayoutA():
	cmds.columnLayout('MS_batch_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_batch.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.scrollField('MS_batch_List',h=300)
	cmds.rowLayout(nc=2,cw2=[150,100],adj=2,ad2=True)
	#
	cmds.columnLayout(adj=True)
	cmds.checkBox('MS_batch_mainLayout_open_scene',l='OpenMB',v=True)
	cmds.checkBox('MS_batch_mainLayout_save_scene',l='Save MB',v=False)
	cmds.checkBox('MS_batch_mainLayout_export_scene',l='G2 auto export',v=False)

	cmds.setParent('..')
	cmds.button(l='autoExport',h=30,bgc=[0.6,0.8,0.6],c=lambda *args:MSG2_auto_export.auto())
	cmds.setParent('..')
	cmds.button(l='doThat',c=lambda *args:main())
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	Layout_modules()
	cmds.showWindow('MS_tools_window')
	
