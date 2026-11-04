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
	RT=cmds.ls('*|root*',tr=True)
	NRT=cmds.parent(RT[0],w=True)
	cmds.rename(NRT[0],'root') 
	CL=cmds.ls('*|col*',tr=True)
	NCL=cmds.parent(CL[0],w=True)
	cmds.rename(NCL[0],'col')
