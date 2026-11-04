# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_progress.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

#プログレスバー
class MS_Progress:
	def __init__(self):
		pass

	def create(self,MAXVALUE=10):
		if MAXVALUE<1:
			MAXVALUE=1
		#プログレスウィンドウ
		if cmds.window('MS_ProgressWindow',ex=True):
			cmds.deleteUI('MS_ProgressWindow')
		if cmds.windowPref('MS_ProgressWindow',ex=True):
			cmds.windowPref('MS_ProgressWindow',r=True)
		cmds.window('MS_ProgressWindow',wh=[248,70],tlc=[414,516],tlb=True,s=True,t='Calculating')
		cmds.columnLayout()
		cmds.progressBar('MS_progress',minValue=0,maxValue=MAXVALUE,width=246)
		cmds.setParent ('..')
		cmds.showWindow ('MS_ProgressWindow')

	def add(self):
		cmds.progressBar('MS_progress',edit=True,s=1)

	def delete(self):
		cmds.deleteUI('MS_ProgressWindow')
