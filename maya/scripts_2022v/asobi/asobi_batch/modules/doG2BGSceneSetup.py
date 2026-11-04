# _*_coding:utf-8_*_
########################################
# ファイル名
#			doG2BGSceneSetup.py
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds

import s2000_tools.MS_tinyTools.MS_G2BGSceneSetup as MS_G2BGSceneSetup
reload(MS_G2BGSceneSetup)

def main(TARGET_NAME):
	LOG=''
	OBJ=''
	
	if cmds.objExists('|root'):
		OBJ='|root'
	else:
		OBJS=cmds.ls('|*')
		for each in OBJS:
			if len(cmds.ls(each,dag=True,type='mesh')):
				OBJ=each
				break

	if OBJ:
		cmds.select(OBJ,r=True)
		MS_G2BGSceneSetup.G2BGSceneSetup()

	LOG+=OBJ
	return LOG
