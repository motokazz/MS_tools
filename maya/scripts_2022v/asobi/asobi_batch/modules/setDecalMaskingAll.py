# _*_coding:utf-8_*_
########################################
# ファイル名
#			setDecalMaskingAll.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

def main(TARGET,VAR=True):
	sel = cmds.ls(type='G2_BG_Main')
	for each in sel:
		cmds.setAttr(each+'.decalMasking',VAR)

