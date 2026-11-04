# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_swapNearestParent
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds
	
import MS_module.MS_UILib as MS_UILib
reload(MS_UILib)

import MS_module.MS_swapParent as swapParent
reload(swapParent)
	
import MS_Lib
reload(MS_Lib)
	
	
def do():
	SRC	=	MS_UILib.nodeList('MS_swapParent_source',q=True)
	DST	=	MS_UILib.nodeList('MS_swapParent_dist',q=True)
	nearest=MS_Lib.nearest(SRC,DST)
	
	for each in nearest:
		swapParent.swapParent(each[0],each[1])
	
	

	
def layoutA(
	LABEL='MS_swapParent'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	MS_UILib.nodeList('MS_swapParent_source',type='transform')
	MS_UILib.nodeList('MS_swapParent_dist',type='transform')
	
	cmds.button(w=WIDTH-4,l=u'do',c=lambda *args:do())
	
	cmds.separator(w=200)
	
	cmds.button(w=WIDTH-4,l=u'swap 2 objects',c=lambda *args:swapParent.sample())
	
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_swapParent_main_window',q=True,ex=True):
		cmds.deleteUI('MS_swapParent_main_window')
	cmds.window('MS_swapParent_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_swapParent_main_window')
	
