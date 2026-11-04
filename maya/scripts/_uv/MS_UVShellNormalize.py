# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_UVShellNormalize.py
# 説明
#			離れた位置にできてしまったUVシェルを0,1のページ内に引き寄せる
#			
# 作成日
#			
########################################
import maya.cmds as cmds
import math

import MS_separateUVIslands
reload(MS_separateUVIslands)

##### UVShell move to 0,1
def main():
	SEL=cmds.ls(sl=True)
	UVIL = MS_separateUVIslands.main(SEL)
	for each in UVIL:
		PU=cmds.polyEditUVShell(each[0],q=True)
		cmds.select(each,r=True)
		cmds.polyEditUVShell(u=-math.floor(PU[0]),v=-math.floor(PU[1]))
