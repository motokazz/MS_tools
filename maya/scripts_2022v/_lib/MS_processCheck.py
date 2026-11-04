# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_processCheck.py
# 説明
#			アプリケーション起動確認
# 作成日
#			
########################################

import os
import maya.mel as mel

def getRun(APP):
	
	#RUNNING=os.popen('tasklist').read()
	RUNNING=mel.eval('system"tasklist"')
	if APP in RUNNING:
		return True
	else:
		return False







