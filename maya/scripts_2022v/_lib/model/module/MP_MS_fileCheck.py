# _*_coding:utf-8_*_
########################################
# ファイル名
#			MP_MS_fileCheck
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds

import MS_module.MP_MS_createEntityIDList as MP_MS_createEntityIDList
reload(MP_MS_createEntityIDList)

import MS_module.MP_MS_gimmickListChecker as MP_MS_gimmickListChecker
reload(MP_MS_gimmickListChecker)
	
import MS_module.MP_MS_gimmickFileChecker as MP_MS_gimmickFileChecker
reload(MP_MS_gimmickFileChecker)


def UI():
	if cmds.window('MP_MS_fileCheck_main_window',q=True,ex=True):
		cmds.deleteUI('MP_MS_fileCheck_main_window')
	cmds.window('MP_MS_fileCheck_main_window',rtf=True,s=True)
	cmds.columnLayout()
	MP_MS_createEntityIDList.layoutA()
	MP_MS_gimmickListChecker.layoutA()
	MP_MS_gimmickFileChecker.layoutA()
	cmds.setParent('..')
	cmds.showWindow('MP_MS_fileCheck_main_window')
	

