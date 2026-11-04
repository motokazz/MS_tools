# _*_coding:utf-8_*_
########################################
# ファイル名
#			checkAtgiBB.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import s2000_tools.MSG2_atgiTools.MSG2_atgiTool as MSG2_atgiTool
reload(MSG2_atgiTool)


def main(ARGS=''):
	SEL=MSG2_atgiTool.createAtgiNode()
	ATGI=MSG2_atgiTool.atgiCreator(ARGS,SEL)
	XF=cmds.xform(ATGI,q=True,bb=True)
	#return [str(XF[3]-XF[0]),str(XF[4]-XF[1]),str(XF[5]-XF[2])]
	return '0,0,0'
