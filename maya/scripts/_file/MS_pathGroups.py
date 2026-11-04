# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_pathGroups
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds
import pickle

import _file.MS_filePathUI as MS_filePathUI
reload (MS_filePathUI)





class pathGroups():
	name='default'
	path_a = ['jpg','']
	path_b = ['mb','']
	path_c = ['ext','']
	path_d = ['ext','']
	path_e = ['ext','']

def main():
	path=__file__+'/pickle'
	with open(path,'rb') as f:
		ret = pickle.load(f)
	ret.name

	pg=pathGroups
	pg.name=cmds.textField('MS_pathGroups_name',q=True,tx=True)
	pg.path_a[1] = cmds.textField('thunbneil_FILE_PATH',q=True,tx=True)
	pg.path_b[1] = cmds.textField('mb_FILE_PATH',q=True,tx=True)
	pg.path_c[1] = cmds.textField('atgi_FILE_PATH',q=True,tx=True)


	with open(path,'wb') as f:
		pickle.dump(data,f)

def LayoutA():
	cmds.frameLayout('MS_pathGroups_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_pathGroups',cll=True,cl=False)
	cmds.columnLayout('MS_pathGroups_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_pathGroups',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.textField('MS_pathGroups_name')
	loa('thunbneil')
	loa('mb')
	loa('atgi')

	cmds.button(l='submit',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def loa(name=''):
	fpf = MS_filePathUI.filePathField()
	fpf.controlName=name
	fpf.label=name
	fpf.fileMode=3
	fpf.dialogStyle=1
	return fpf.pathBrouser_lineLayout()

def UI():
	if cmds.window('MS_pathGroups_window',q=True,ex=True):
		cmds.deleteUI('MS_pathGroups_window')
	cmds.window('MS_pathGroups_window',rtf=True,s=True)
	LayoutA()

	cmds.showWindow('MS_pathGroups_window')
	