# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_copyToCollision.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

#execCheckList
import s2000_tools.MS_lib.MSG2_execCheck as MSG2_execCheck
reload(MSG2_execCheck)


def main():
	RET=[]

	MSG2_execCheck.execCheckSafe('MS_copyToCollision')#execCheckList
	OBJ=cmds.ls(sl=True,l=True)

	for each in OBJ:
		P = cmds.ls(each,l=True)
		PP=P[0].split('|')[1]
		DUPED=cmds.duplicate(each)
		#子供を消す
		try:
			cmds.delete(DUPED[1:-1])
		except:
			pass
			
		#DUPED=cmds.ls(sl=True,l=True)
		PCOL = PP+'|col'
		PARENTED=cmds.parent(DUPED[0],PCOL)
		#PARENTED=cmds.ls(sl=True,l=True)
		RET.extend(PARENTED)
		
	return RET


def LayoutA():
	cmds.columnLayout('MS_copyToCollision.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_copyToCollision.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	