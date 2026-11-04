# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_uniqueName.py
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds

def uniqueName():
	NODES=cmds.ls(type='transform',sn=True)
	NODES.reverse()
	for EACH in NODES:
		TMP=cmds.ls(EACH.split('|')[-1],l=True)
		if len(TMP)>1:
			cmds.rename(EACH,EACH.split('|')[-1]+str(len(TMP)-1))



