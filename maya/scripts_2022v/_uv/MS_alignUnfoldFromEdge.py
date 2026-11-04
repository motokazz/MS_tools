# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_alignUnfoldFromEdge.py
# 説明
#			選択エッジを元に、UVを整列
#			
# 作成日
#			
########################################

import maya.cmds as cmds


def MS_polySelectUVShell(SELUVS):
	RET=[]
	#selectUVShell
	cmds.select(SELUVS,r=True)
	cmds.polySelectConstraint(t=0x0010,m=2,sh=True,bo=False,pp=0)
	RET=cmds.filterExpand(sm=35)
	cmds.polySelectConstraint(dis=True)
	return RET

def listAverage(LIST=[]):
	return sum(LIST)/len(LIST)



def MS_alignUnfoldFromEdge():
	SEL = cmds.filterExpand(sm=[32,35],ex=True)
	MIDUVS = cmds.polyListComponentConversion(SEL[0],tuv=True)
	SELUVS=cmds.filterExpand(MIDUVS,sm=35,ex=True)
	cmds.polyEditUV(SELUVS[0],u=0.0,v=0.0,r=False)
	cmds.polyEditUV(SELUVS[1],u=1.0,v=0.0,r=False)

	UVSHELL = MS_polySelectUVShell(SELUVS)

	#初回選択UVの刈り込み
	cmds.select(UVSHELL,r=True)
	cmds.select(SELUVS,d=True)

	cmds.unfold(i=10000,ss=0.001,gb=0,gmb=0,pub=0,ps=0,oa=0,us=False)


	if sum(cmds.polyEditUV(UVSHELL,q=True)[1::2])<0:
		cmds.polyEditUV(UVSHELL,rot=True,pu=0.5,pv=0.0,angle=180)

def main():
	EDGES = cmds.filterExpand(sm=32,ex=True)
	for each in EDGES:
		cmds.select(each,r=True)
		MS_alignUnfoldFromEdge()

def LayoutA():
	cmds.columnLayout('MS_alignUnfoldFromEdge_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_alignUnfoldFromEdge',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	