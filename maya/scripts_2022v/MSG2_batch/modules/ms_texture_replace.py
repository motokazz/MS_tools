# _*_coding:utf-8_*_
########################################
# ファイル名
#			ms_texture_replace.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds


def main(TARGET):
	G2BG=cmds.ls(type='G2_BG_Main')
	for each in G2BG:
		COL = cmds.listConnections(each+'.color')
		if COL:
			FTN=cmds.getAttr(COL[0]+'.fileTextureName')
			if not 'wall_xp_18_c.tif' in FTN:
				continue

		CON = cmds.listConnections(each+'.normal')
		if CON:
			try:
				cmds.disconnectAttr(CON[0]+'.outColor',each+'.normal')
			except:
				pass
		#2
		COL = cmds.listConnections(each+'.color2')
		if COL:
			FTN=cmds.getAttr(COL[0]+'.fileTextureName')
			if not 'wall_xp_18_c.tif' in FTN:
				continue

		CON = cmds.listConnections(each+'.normal2')
		if CON:
			try:
				cmds.disconnectAttr(CON[0]+'.outColor',each+'.normal2')
			except:
				pass
	        