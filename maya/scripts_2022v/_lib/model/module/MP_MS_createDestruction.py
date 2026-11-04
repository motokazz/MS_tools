# _*_coding:utf-8_*_
########################################
# ファイル名
#			MP_MS_createDestruction
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds
	
	
def selectMeshTransform():
	nodes=cmds.ls(sl=True,type='transform',l=True)
	meshes=cmds.listRelatives(nodes,ad=True,type='mesh',f=True)
	list=[]
	for each in meshes:
	    trn=cmds.listRelatives(each,p=True,type='transform')
	    print trn
	    list.append(trn[0])
	return list
	
	
def configueVisible():
	if cmds.objExists('gp_obj'):
		cmds.setAttr('gp_obj.visibility',True)
	if cmds.objExists('gp_brk'):
		cmds.setAttr('gp_brk.visibility',False)
	
def addDestruction(NODE):
	
	if not cmds.attributeQuery('destruction',n=NODE,ex=True):
		cmds.addAttr(NODE,at='bool',longName='destruction')
	cmds.setAttr(NODE+'.destruction',True,keyable=True)
	
	
def parent_gp_obj(nodes):
	if not cmds.objExists('gp_obj'):
		cmds.group(n='gp_obj',empty=True)
	
	GP_OBJ=cmds.ls('gp_obj',l=True)
	cmds.parent(nodes,GP_OBJ[0])
	if cmds.objExists('scale_fix'):
		try:
			cmds.parent(GP_OBJ[0],'scale_fix')
		except:
			print 'OK'
	
def do():
	
	brknodes=selectMeshTransform()
	
	for each in brknodes:
		addDestruction(each)
	
	
	duped=cmds.duplicate()
	try:
		unparented=cmds.parent(duped[0],w=True)
	except:
		unparented=duped[0]
	
	united=cmds.polyUnite(unparented,ch=False)
	
	cmds.delete(unparented)
	
	cmds.rename(united[0],unparented[0])
	
	addDestruction(unparented[0])
	
	parent_gp_obj(unparented[0])
	
	configueVisible()
	


def layoutA(
	LABEL='MP_MS_createDestruction'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.text(l=' 1.selectParts \n (able to hrc selection) \n 2.go')
	cmds.button(w=200,h=100,bgc=[0.8,0.6,0.6],l=u'createDestruction!',c=lambda *args:do())
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MP_MS_createDestruction_main_window',q=True,ex=True):
		cmds.deleteUI('MP_MS_createDestruction_main_window')
	cmds.window('MP_MS_createDestruction_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MP_MS_createDestruction_main_window')
	

