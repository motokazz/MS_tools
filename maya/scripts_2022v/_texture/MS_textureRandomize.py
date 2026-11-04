# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_textureRandomize
# 説明
#
# 作成日
########################################

import maya.cmds as cmds
import glob
import random
import importlib

import _lib.MS_fileExport as MS_fileExport
importlib.reload(MS_fileExport)


def repath(path=''):
	fnode=cmds.ls(sl=True,type='file')
	if not fnode:
		return
	if not path:
		path=MS_fileExport.single('MS_textureRandomize_dir',Q=True)

	for each in fnode:
		ftn=cmds.getAttr(each+'.fileTextureName')
		filepath = path.replace('\\','/') + ftn.split('/')[-1].split('\\')[-1]
		print (filepath)
		#filepath=textures[random.randint(0,len(textures)-1)].replace('\\','/')
		cmds.setAttr(each+'.fileTextureName',filepath,type='string')


def RANDOMIZE(path=''):
	fnode=cmds.ls(sl=True,type='file')
	if not fnode:
		return
	if not path:
		path=MS_fileExport.single('MS_textureRandomize_dir',Q=True)
	ncv=cmds.textField('MS_textureRandomize_textField_a',q=True,tx=True)
	ext=cmds.textField('MS_textureRandomize_textField_b',q=True,tx=True)

	textures=glob.glob(path+'*'+ncv+'*.'+ext)

	#
	for each in fnode:
		filepath=textures[random.randint(0,len(textures)-1)].replace('\\','/')
		cmds.setAttr(each+'.fileTextureName',filepath,type='string')

def NEXT():
	fnode=cmds.ls(sl=True,type='file')
	if not fnode:
		return
	path=MS_fileExport.single('MS_textureRandomize_dir',Q=True)
	ncv=cmds.textField('MS_textureRandomize_textField_a',q=True,tx=True)
	ext=cmds.textField('MS_textureRandomize_textField_b',q=True,tx=True)
	textures=glob.glob(path+'*'+ncv+'.'+ext)
	print (textures)
	for each in fnode:
		CURRENT=cmds.getAttr(each+'.fileTextureName')
		#search
		IDX=textures.index(CURRENT.replace('/','\\'))

		if IDX<(len(textures)-1):
			filepath=textures[IDX+1]
		else:
			filepath=textures[0]

		cmds.setAttr(each+'.fileTextureName',filepath,type='string')

def PREV():
	fnode=cmds.ls(sl=True,type='file')
	if not fnode:
		return
	path=MS_fileExport.single('MS_textureRandomize_dir',Q=True)
	ncv=cmds.textField('MS_textureRandomize_textField_a',q=True,tx=True)
	ext=cmds.textField('MS_textureRandomize_textField_b',q=True,tx=True)
	textures=glob.glob(path+'*'+ncv+'.'+ext)
	print (textures)
	for each in fnode:
		CURRENT=cmds.getAttr(each+'.fileTextureName')
		#search
		IDX=textures.index(CURRENT.replace('/','\\'))

		if IDX>0:
			filepath=textures[IDX-1]
		else:
			filepath=textures[len(textures)]

		cmds.setAttr(each+'.fileTextureName',filepath,type='string')


def layoutA(
	LABEL='MS_textureRandomize'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()

	cmds.text(l=LABEL)

	MS_fileExport.single('MS_textureRandomize_dir',FILENAME='D:/Projects/Gravite2/graphic/bg/textures',MODE='dir')

	cmds.button(l=u'Repath',c=lambda *args:repath())

	cmds.text(l='searchWord')
	cmds.textField(LABEL+'_textField_a',w=WIDTH-4,tx='_c')
	cmds.text(l='searchExt')
	cmds.textField(LABEL+'_textField_b',w=WIDTH-4,tx='tif')

	cmds.button(w=WIDTH-4,l=u'RANDOMIZE',c=lambda *args:RANDOMIZE())

	#
	cmds.gridLayout(nc=4)

	cmds.button(l=u'decal',c=lambda *args:RANDOMIZE('D:/Projects/Gravite2/graphic/bg/textures/decal/'))
	cmds.button(l=u'ground',c=lambda *args:RANDOMIZE('D:/Projects/Gravite2/graphic/bg/textures/ground/'))
	cmds.button(l=u'metal',c=lambda *args:RANDOMIZE('D:/Projects/Gravite2/graphic/bg/textures/metal/'))
	cmds.button(l=u'object',c=lambda *args:RANDOMIZE('D:/Projects/Gravite2/graphic/bg/textures/object/'))
	cmds.button(l=u'organic',c=lambda *args:RANDOMIZE('D:/Projects/Gravite2/graphic/bg/textures/organic/'))
	cmds.button(l=u'rock',c=lambda *args:RANDOMIZE('D:/Projects/Gravite2/graphic/bg/textures/rock/'))
	cmds.button(l=u'roof',c=lambda *args:RANDOMIZE('D:/Projects/Gravite2/graphic/bg/textures/roof/'))
	cmds.button(l=u'sign',c=lambda *args:RANDOMIZE('D:/Projects/Gravite2/graphic/bg/textures/sign/'))
	cmds.button(l=u'sky',c=lambda *args:RANDOMIZE('D:/Projects/Gravite2/graphic/bg/textures/sky/'))
	cmds.button(l=u'vehicle',c=lambda *args:RANDOMIZE('D:/Projects/Gravite2/graphic/bg/textures/vehicle/'))
	cmds.button(l=u'wall',c=lambda *args:RANDOMIZE('D:/Projects/Gravite2/graphic/bg/textures/wall/'))
	cmds.button(l=u'window',c=lambda *args:RANDOMIZE('D:/Projects/Gravite2/graphic/bg/textures/window/'))
	cmds.button(l=u'effect',c=lambda *args:RANDOMIZE('D:/Projects/Gravite2/graphic/effect/textures/'))
	cmds.setParent('..')

	cmds.rowLayout(nc=2)
	cmds.button(w=WIDTH*0.5-4,l=u'PREV',c=lambda *args:PREV())
	cmds.button(w=WIDTH*0.5-4,l=u'NEXT',c=lambda *args:NEXT())
	cmds.setParent('..')
	#
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_textureRandomize_main_window',q=True,ex=True):
		cmds.deleteUI('MS_textureRandomize_main_window')
	cmds.window('MS_textureRandomize_main_window',rtf=True,s=True)

	layoutA()

	cmds.showWindow('MS_textureRandomize_main_window')
