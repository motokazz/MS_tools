# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_UILib
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds
	
	
def selectionFilter(type):
	NODES=[]
	if type:
		NODES=cmds.ls(sl=True,type=type,l=True)
	else:
		NODES=cmds.ls(sl=True,l=True)
	return NODES
	
	
#####UI
def nodeList(UI_NAME,q=False,w=200,h=20,type=[]):
	if q:
		TX	=cmds.textField(UI_NAME,q=True,tx=True)
		if TX:
			LIST	=TX.split(';')
		else:
			LIST=[]
		return LIST
	
	def createList():
		NODES=selectionFilter(type)
		cmds.textField(UI_NAME,e=True,tx=';'.join(NODES))
		
	def addList():
		NODES=selectionFilter(type)
		TX=cmds.textField(UI_NAME,q=True,tx=True)
		if TX:
			LIST=TX.split(';')
		else:
			LIST=[]
		RET=list(set(LIST+NODES))
		cmds.textField(UI_NAME,e=True,tx=';'.join(RET))
		
	def removeList():
		NODES=selectionFilter(type)
		TX=cmds.textField(UI_NAME,q=True,tx=True)
		LIST=TX.split(';')
		for EACH in NODES:
			while EACH in LIST:LIST.remove(EACH)
		cmds.textField(UI_NAME,e=True,tx=';'.join(LIST))
		
	def clearList():
		cmds.textField(UI_NAME,e=True,tx='')
		
	def query():
		TX	=cmds.textField(UI_NAME,q=True,tx=True)
		if TX:
			LIST	=TX.split(';')
		else:
			LIST=[]
		return LIST
	
	def LO(UI_NAME):
		cmds.columnLayout(UI_NAME+'mainColumn')
		cmds.text(l=UI_NAME)
		cmds.textField(UI_NAME,w=w,tx='')
		cmds.rowLayout(nc=4)
		cmds.button(w=40,l=u'create',c=lambda *args:createList())
		cmds.button(w=40,l=u'add',c=lambda *args:addList())
		cmds.button(w=40,l=u'remove',c=lambda *args:removeList())
		cmds.button(w=40,l=u'clear',c=lambda *args:clearList())
		cmds.setParent('..')
		cmds.setParent('..')
	
	if not cmds.control(UI_NAME+'mainColumn',q=True,ex=True):
		LO(UI_NAME)
	
	print UI_NAME
	
	
def UI():
	if cmds.window('MS_UILib_main_window',q=True,ex=True):
		cmds.deleteUI('MS_UILib_main_window')
	cmds.window('MS_UILib_main_window',rtf=True,s=True)
	
	nodeList('sample')
	
	cmds.showWindow('MS_UILib_main_window')
	


