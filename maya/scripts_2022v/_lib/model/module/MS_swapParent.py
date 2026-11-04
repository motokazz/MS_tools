# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_swapParent
# 説明	
#			２つの選択されたノードの親を交換する
# 作成日\n#			
########################################
import maya.cmds as cmds


def swapParent(NODE_A,NODE_B):
	P0=cmds.listRelatives(NODE_A,p=True,f=True)
	P1=cmds.listRelatives(NODE_B,p=True,f=True)
	print P0,P1
	
	if P1:
		cmds.parent(NODE_A,P1)
	else:
		cmds.parent(NODE_A,w=True)
			
	if P0:
		cmds.parent(NODE_B,P0)
	else:
		cmds.parent(NODE_B,w=True)
	
def sample():
	OBJ=cmds.ls(sl=True,l=True)
	swapParent(OBJ[0],OBJ[1])
	
