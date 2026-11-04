# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_insertLocator
# 説明
#			オブジェクトの親にロケーターを挿入
# 作成日
#			
########################################

import maya.cmds as cmds
	
def do():
	ATTR_LIST=['tx','ty','tz','rx','ry','rz','sx','sy','sz']
	OBJ=cmds.ls(sl=True)
	for EACH_OBJ in OBJ:
		ATTR_VAR=[]
		for EACH_ATTR in ATTR_LIST:
			ATTR_VAR.append([EACH_ATTR,cmds.getAttr(EACH_OBJ+'.'+EACH_ATTR)])

		PARENT=cmds.listRelatives(EACH_OBJ,p=True)
		LOC=cmds.spaceLocator()[0]
		#親がある場合と無い場合を振り分け
		if PARENT:
			WOBJ=cmds.parent(EACH_OBJ,w=True)[0]
			LOC=cmds.parent(LOC,PARENT[0])[0]
			COBJ=cmds.parent(WOBJ,LOC)[0]
		else:
			COBJ=cmds.parent(EACH_OBJ,LOC)[0]
			
		for EACH_ATTR_VAR in ATTR_VAR:
			cmds.setAttr(LOC+'.'+EACH_ATTR_VAR[0],EACH_ATTR_VAR[1])
		cmds.rename(LOC,EACH_OBJ+'_loc')
		
		cmds.setAttr(COBJ+'.tx',0)
		cmds.setAttr(COBJ+'.ty',0)
		cmds.setAttr(COBJ+'.tz',0)
	
		cmds.setAttr(COBJ+'.rx',0)
		cmds.setAttr(COBJ+'.ry',0)
		cmds.setAttr(COBJ+'.rz',0)
		
		cmds.setAttr(COBJ+'.sx',1)
		cmds.setAttr(COBJ+'.sy',1)
		cmds.setAttr(COBJ+'.sz',1)
	
def layoutA():
	cmds.frameLayout('MS_insertLocator_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'MS_insertLocator',cll=True,cl=False)
	cmds.columnLayout()
	
	cmds.button(w=150,l=u'do',c=lambda *args:do())
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_insertLocator_main_window',q=True,ex=True):
		cmds.deleteUI('MS_insertLocator_main_window')
	cmds.window('MS_insertLocator_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_insertLocator_main_window')
	


