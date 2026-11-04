# _*_coding:utf-8_*_
########################################
# ファイル名
#texture_replace.py
# 説明
#
#
# 作成日
#
########################################

import maya.cmds as cmds
import os

import s2000_tools.MS_lib.MSG2_P4Lib as MSG2_P4Lib
reload(MSG2_P4Lib)

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


def main(TARGET):
	MBFP=searchPath('D:/Projects/Gravite2/graphic/bg/scenes',TARGET)
	return MSG2_P4Lib.P4Status(PATH=MBFP)

