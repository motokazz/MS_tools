# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_textreUtil.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import os
#from PIL import Image


def rename(path='',source='',dist=''):
	#リネーム処理コア

	if not path or not source or not dist:
		return False

	try:
		os.rename( path+'/'+source , path+'/'+dist )
		return True
	except:
		return False


def main():
	#元情報取得
	fileTextureNode=cmds.ls(sl=True,typ=['file'])
	fullPath=cmds.getAttr(fileTextureNode[0]+'.fileTextureName')
	fullPathSeparate=fullPath.split('/')
	exportPath = ('/').join(fullPathSeparate[0:-1])
	textureName= fullPathSeparate[-1]
	textureExt = textureName.split('.')[-1]

	#変更後情報取得
	distName=cmds.textField('renametext',q=True,tx=True)

	if rename(exportPath,textureName,distName+'.'+textureExt):
		cmds.setAttr(fileTextureNode[0]+'.fileTextureName',distName+'.'+textureExt,type='string')
	else:
		print ('rename failed')
	print (fullPath,exportPath,textureName)

def LayoutA():
	cmds.columnLayout('MS_tools_mainLayout',adj=True)
	cmds.text(l='renameText')
	cmds.textField('renametext',cc=lambda *args:main())
	cmds.text(l=u'テクスチャノードを選択してtextFieldに入力するとテクスチャのリネームができる')
	#cmds.button(l='main',c=lambda *args:main())

	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')





