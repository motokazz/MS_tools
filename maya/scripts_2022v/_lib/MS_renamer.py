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

def put_textField(source='',dist='',keta=0,suffix=''):
	cmds.textField('MS_renamer_orgname',e=True,tx=source)
	cmds.textField('MS_renamer_newname', e=True, tx=dist)
	cmds.intField('MS_renamer_KETA', e=True, v=keta)
	cmds.textField('MS_renamer_suffix', e=True, tx=suffix)


def replace():
	PREFIX = cmds.textField('MS_renamer_prefix',q=True,tx=True)
	orgname = cmds.textField('MS_renamer_orgname',q=True,tx=True)
	newname = cmds.textField('MS_renamer_newname',q=True,tx=True)
	KETA = cmds.intField('MS_renamer_KETA',q=True,v=True)
	SUFFIX = cmds.textField('MS_renamer_suffix',q=True,tx=True)

	NUM=0
	uids = cmds.ls(sl=True,uid=True)
	for EACH in uids:
		result_name=''
		current_longname = cmds.ls(EACH,l=True)[0]
		current_shortname = cmds.ls(EACH)[0]

		if PREFIX:
			result_name+=PREFIX

		if orgname=='' and newname == '':
			result_name += current_shortname
		elif orgname == '':
			result_name += newname
		else:
			result_name += current_shortname.replace(orgname,newname).split('|')[-1]

		if KETA:
			result_name+=str(NUM).zfill(KETA)
		NUM+=1

		if SUFFIX:
			result_name+=SUFFIX

		cmds.rename(current_longname, result_name)

def LayoutUtil():
	cmds.frameLayout('MS_renamer_util_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='util',cll=True,cl=False)
	cmds.columnLayout('MS_renamer_util_mainLayout',adj=True)

	cmds.separator()
	cmds.text(l='util',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.gridLayout(nc=4,cw=100)
	cmds.button (l='SceneName',c=lambda *args:renameToSceneName())
	cmds.button (l='pasted__',c=lambda *args:ns_pasted__())
	cmds.button (l='FBXASC046',c=lambda *args:put_textField('FBXASC046','_'))
	cmds.setParent('..')

	cmds.separator()
	
	cmds.setParent('..')
	cmds.setParent('..')

def LayoutA():
	cmds.frameLayout('MS_renamer_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_renamer',cll=True,cl=False)
	cmds.columnLayout('MS_renamer_mainLayout',adj=True)

	cmds.separator()
	cmds.text(l='MS_renamer',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.rowLayout(nc=6,cw6=[150,150,20,150,20,30])
	cmds.text(l='prefix')
	cmds.text(l='source name')
	cmds.text(l='')
	cmds.text(l='dist name')
	cmds.text(l='KETA')
	cmds.text(l='suffix')
	cmds.setParent('..')

	cmds.rowLayout(nc=6,cw6=[150,150,20,150,20,30])
	cmds.textField('MS_renamer_prefix',w=150,tx='',ann=u'プレフィックス')
	cmds.textField('MS_renamer_orgname',w=150,tx='',ann=u'置換文字列。空白で名前付けなおし')
	cmds.text(l='=>')
	cmds.textField('MS_renamer_newname',w=150,tx='',ann=u'新しい名前')
	cmds.intField('MS_renamer_KETA',w=20,v=0,ann=u'末尾の数字桁数')
	cmds.textField('MS_renamer_suffix',w=150,tx='',ann=u'サフィックス')
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
