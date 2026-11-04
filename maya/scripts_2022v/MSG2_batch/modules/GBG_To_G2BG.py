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


import s2000_tools.MS_tinyTools.MS_G2ShaderUtil as MS_G2ShaderUtil
reload(MS_G2ShaderUtil)

def main(TARGET_NAME):
	LOG=''
	GBG=cmds.ls(type='G_BG_Main')
	G2BG=cmds.ls(type='G2_BG_Main')
	i=0
	for each in GBG:

		MS_G2ShaderUtil.matBtoMatA(G2BG[i],each)
		if len(G2BG)<i:
			i+=1
	MS_G2ShaderUtil.shaderClean()
	return LOG

