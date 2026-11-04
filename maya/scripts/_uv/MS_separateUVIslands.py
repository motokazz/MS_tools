# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_separateUVIslands.py
# 説明
#			UVアイランドごとのUVリストを返す。
#			戻り値:[[アイランドのUVリスト１],[アイランドのUVリスト2],...]
# 作成日
#			
########################################

import maya.cmds as cmds

def preservedList(ORG,RESERVE=[]):
	for EACH in RESERVE:
		while EACH in ORG:ORG.remove(EACH)
	return ORG
		
def main(UVS):
	#UVアイランドごとのUVリストを返す。
	#戻り値:[[アイランドのUVリスト１],[アイランドのUVリスト2],...]
	RET=[]
	cmds.select(UVS,r=True)
	cmds.select(cmds.polyListComponentConversion(tuv=True),r=True)
	UVS_EX=cmds.filterExpand(sm=35)
	while UVS_EX:
		cmds.select(UVS_EX[0])
		cmds.polySelectConstraint(t=0x0010,m=2,sh=True,bo=False,pp=0)
		TEMP=cmds.filterExpand(sm=35)
		UVS_EX=preservedList(UVS_EX,TEMP)
		RET.append(TEMP)
	cmds.polySelectConstraint(dis=True)
	return RET
