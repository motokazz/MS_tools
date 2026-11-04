# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_pipeUV.py
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds

def addList():
	COMP=cmds.filterExpand(ex=True,sm=[35])
	if not COMP:
		clearList()
		return
	AI=cmds.textScrollList('MS_PIPEUV_list',q=True,ai=True)
		
	if not AI:
		AI=''
	clearList()
	
	for EACH in AI:
		if EACH in COMP:
			cmds.textScrollList('MS_PIPEUV_list',e=True,append=EACH)
	for EACH in COMP:
		if not EACH in AI:
			cmds.textScrollList('MS_PIPEUV_list',e=True,append=EACH)


def clearList():
	cmds.textScrollList('MS_PIPEUV_list',e=True,ra=True)

def jobPipeUV():
	jobNum = cmds.scriptJob(e=["SelectionChanged",THIS_SCRIPT+".addList()"],parent='MS_bestUVSize_main_window',protected=True)

def pipeUV():
	#EDGES=cmds.filterExpand(sm=32)
	UVS=cmds.textScrollList('MS_PIPEUV_list',q=True,ai=True)
	TOTAL_EDGE_LENGTH=0.0
	EDGE_LIST=[]
	
	for EACH in range(len(UVS)-1):
		TOTAL_EDGE_LENGTH+=getUVLength([UVS[EACH],UVS[EACH+1]])
	
	BEFOR_V=0.0
	cmds.polyEditUV(UVS[0],r=False,u=0.0,v=BEFOR_V)
	for EACH in range(len(UVS)-1):
		UVPOS=getUVLength([UVS[EACH],UVS[EACH+1]])/TOTAL_EDGE_LENGTH
		cmds.polyEditUV(UVS[EACH+1],r=False,u=0.0,v=UVPOS)
		print UVS[EACH]

def layoutPipeUV():
	cmds.frameLayout('PIPEUV',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'PIPEUV',cll=True,cl=True)
	cmds.columnLayout()
	cmds.button(w=150,l=u'PIPEUV',c=lambda *args:pipeUV())
	cmds.separator(w=200)
	cmds.button(w=150,l=u'addlist',c=lambda *args:addList())
	cmds.textScrollList('MS_PIPEUV_list',h=100)
	cmds.button(w=150,l=u'clearlist',c=lambda *args:clearList())
	cmds.setParent('..')
	cmds.setParent('..')
	
def LayoutA():
	cmds.columnLayout('MS_tools_mainLayout',adj=True)

	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	