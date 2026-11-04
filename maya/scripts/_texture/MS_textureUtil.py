# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_textreUtil.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import MS_textureRename
reload(MS_textureRename)

import MS_textureRandomize
reload(MS_textureRandomize)



def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	MS_textureRename.LayoutA()
	MS_textureRandomize.layoutA()
	
	cmds.showWindow('MS_tools_window')





