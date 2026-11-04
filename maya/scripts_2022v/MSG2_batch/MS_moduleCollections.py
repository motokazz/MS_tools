# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_moduleCollections.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import os

MODULE_PATH='D:/Projects/Gravite2/tools/maya/maya2014/scripts/python/s2000_tools/MSG2_batch/modules'

def execMod(NAME):
	LOG=[]
	exec('import s2000_tools.MSG2_batch.modules.'+NAME+' as '+NAME)
	exec('reload('+NAME+')')
	LOG.append(exec(NAME+'.main('+FILENAME+')'))
	

def main():
	RET=[]
	FILES=os.listdir(MODULE_PATH)
	for EACH in FILES:
		if '__init__' in EACH:continue
		if '.pyc' in EACH:continue
		NAME=EACH.replace('.py','')
		RET.append(NAME)
	return RET

def LOEX():
	ARR=main()
	cmds.columnLayout('LOEX')
	for EACH in ARR:
		cmds.checkBox(EACH,l=EACH,v=True)
	cmds.setParent('..')


def LayoutA():
	cmds.columnLayout('MS_moduleCollections.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_moduleCollections.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()

	LOEX()

	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	
UI()