# _*_coding:utf-8_*_
########################################
# ファイル名
#			DVY_VehicleRigger
# 説明
#			
#			
# 作成日
#			
########################################

import  os
import maya.mel as mel

def UI():
	currentfile = os.path.abspath(__file__)
	dir=os.path.dirname( currentfile ).replace('\\','/')+'/'

	files = os.listdir(dir)

	for each in files:
		if '.mel' in each:
			mel.eval('source "' +dir+each+'";')

	mel.eval('DVY_VehicleRigger();')


