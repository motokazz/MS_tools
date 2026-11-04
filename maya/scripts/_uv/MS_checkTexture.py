# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_checkTexture.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import os

def preservedList(ORG,RESERVE=[]):
	if not RESERVE:
		preRESERVE=cmds.textFieldButtonGrp('MS_hahen_preserveList',q=True,tx=True)
		RESERVE=preRESERVE.split(';')
	for EACH in RESERVE:
		while EACH in ORG:ORG.remove(EACH)
	return ORG
	
def separateUVIslands(UVS):
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

def checkerTexturePath():#ダミーテクスチャはこのスクリプトパス内のdummy.png

	return '/'.join(__file__.split('\\\\')[0:-1])+'/dummy.png'



def main():
	OBJ=cmds.ls(sl=True)
	COMP=cmds.filterExpand(sm=[31,32,34,35])

	#UVIslandLists
	UVS=cmds.polyListComponentConversion(COMP,tuv=True)
	SUVI = separateUVIslands(UVS)

	for each in SUVI:
		TF=cmds.polyListComponentConversion(each[0],tf=True)
		print TF
		cmds.select(TF,r=True)
		cmds.hyperShade(smn=True)
		sel = cmds.ls(sl=True)
		print sel
		FTN = cmds.listConnections(sel[0]+'.color')
		if FTN:
			print getTextureSize(FTN[0])

	cmds.select(COMP,r=True)

def getTextureSize(FTN):
	#選択ファイルテクスチャノードからサイズを取得
	TEX_SIZE=cmds.getAttr(FTN+'.outSize')
	return TEX_SIZE

def LayoutA():
	cmds.columnLayout('MS_checkTexture.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_checkTexture.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	
main()
