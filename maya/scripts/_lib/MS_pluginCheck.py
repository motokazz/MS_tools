# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_pluginCheck.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds


def loadPlugin():
	if not cmds.pluginInfo('mpPhysicsNode.py',q=True,loaded=True):
		cmds.loadPlugin('mpPhysicsNode.py')

