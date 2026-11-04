# _*_coding:utf-8_*_
########################################
# ファイル名
#			hkxFixer.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

def main(TARGET_NAME):
	LOG=''
	COL=cmds.ls('|col',dag=True,type='hkNodeShape')
	if COL:
		SHAPE_TYPE = cmds.getAttr(COL[0]+'.shapeType')
		if SHAPE_TYPE==6:
			if cmds.getAttr(COL[0]+'.changeExtraRadius'):
				cmds.setAttr(COL[0]+'.changeExtraRadius',False)
				LOG=' changeExtraRadius => False '

	return LOG
