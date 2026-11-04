# _*_coding:utf-8_*_
########################################
# ファイル名
#			unparentRootAndCol.py
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds

def main(TARGET_NAME):
	RT=cmds.ls(['*|root|low*','*|root|atgi_lod*'],tr=True)
	if RT:
		NRT=cmds.parent(RT[0],w=True)
		cmds.setAttr(NRT[0]+'.visibility',False)
		cmds.rename(NRT[0],'atgi_lod_reserved') 

