# _*_coding:utf-8_*_
########################################
# ファイル名
#			launchMayaFPS.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel

def UI():
	if not cmds.pluginInfo("MayaFPS_2014x64Demo.mll", q=1, loaded=1):
		cmds.loadPlugin("MayaFPS_2014x64Demo.mll")
	else:
		mel.eval('mayafps -settings')


