# _*_coding:utf-8_*_
########################################
# �t�@�C����
#			MS_renamer.py
# ����
#			
# �쐬��
#			
########################################

import maya.cmds as cmds

def renameToSceneName():
	cmds.textField('MS_renamer_newname',e=True,tx=cmds.file(q=True,sn=True).split('/')[-1].split('.')[0])

def ns_pasted__():
	cmds.textField('MS_renamer_orgname',e=True,tx='pasted__')
	cmds.textField('MS_renamer_newname',e=True,tx='')

def replace():
	orgname = cmds.textField('MS_renamer_orgname',q=True,tx=True)
	newname = cmds.textField('MS_renamer_newname',q=True,tx=True)
	KETA = cmds.intField('MS_renamer_KETA',q=True,v=True)
	NUM=0
	uids = cmds.ls(sl=True,uid=True)
	for EACH in uids:
		current_longname = cmds.ls(EACH,l=True)[0]
		current_shortname = cmds.ls(EACH)[0]
		if orgname=='':
			result_name=newname
		else:
			result_name = current_shortname.replace(orgname,newname)

		if KETA:
			cmds.rename(current_longname,result_name+str(NUM).zfill(KETA))
		else:
			cmds.rename(current_longname,result_name)
		NUM+=1
		

def LayoutUtil():
	cmds.frameLayout('MS_renamer_util_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='util',cll=True,cl=False)
	cmds.columnLayout('MS_renamer_util_mainLayout',adj=True)

	cmds.separator()
	cmds.text(l='util',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.gridLayout(nc=4,cw=100)
	cmds.button (l='SceneName',c=lambda *args:renameToSceneName())
	cmds.button (l='pasted__',c=lambda *args:ns_pasted__())
	cmds.setParent('..')

	cmds.separator()
	
	cmds.setParent('..')
	cmds.setParent('..')

def LayoutA():
	cmds.frameLayout('MS_renamer_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_renamer',cll=True,cl=False)
	cmds.columnLayout('MS_renamer_mainLayout',adj=True)

	cmds.separator()
	cmds.text(l='MS_renamer',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.rowLayout(nc=4,cw4=[150,20,150,20])
	cmds.text(l='source name')
	cmds.text(l='')
	cmds.text(l='dist name')
	cmds.text(l='KETA')
	cmds.setParent('..')

	cmds.rowLayout(nc=4,cw4=[150,20,150,20])
	cmds.textField('MS_renamer_orgname',w=150,tx='')
	cmds.text(l='=>')
	cmds.textField('MS_renamer_newname',w=150,tx='')
	cmds.intField('MS_renamer_KETA',w=20,v=0)
	cmds.setParent('..')

	cmds.button (l='Rename',c=lambda *args:replace())
	cmds.separator()
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_renamer_window',q=True,ex=True):
		cmds.deleteUI('MS_renamer_window')
	cmds.window('MS_renamer_window',rtf=True,s=True)
	
	LayoutA()
	
	LayoutUtil()

	cmds.showWindow('MS_renamer_window')
	
UI()
