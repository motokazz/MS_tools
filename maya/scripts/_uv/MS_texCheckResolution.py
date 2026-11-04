# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_texCheckResolution.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

BUF=[]

def toOrgTex():
	global BUF
	for EACH in BUF:
		cmds.setAttr(EACH[0]+'.fileTextureName',EACH[1],type='string')
	#
	if cmds.button('MS_texCheckResolution_mainButton',ex=True):
		cmds.button('MS_texCheckResolution_mainButton',e=True,l='toResTex',bgc=[0.7,0.7,0.9],c=lambda *args:toResTex())

def toResTex(PATH='D:/Projects/Gravite2/tools/maya/maya2014/scripts/python/s2000_tools/MS_bestUVSize/reso_check',NAME='restex',APPENDNAME='ms',EXT='jpg'):
	storeBuffer()
	global BUF
	for EACH in BUF:
		RESTEX=PATH+'/'+NAME+'_'+str(int(EACH[2][0]))+'_'+str(int(EACH[2][1]))+'_'+APPENDNAME+'.'+EXT
		cmds.setAttr(EACH[0]+'.fileTextureName',RESTEX,type='string')
	#
	if cmds.button('MS_texCheckResolution_mainButton',ex=True):
		cmds.button('MS_texCheckResolution_mainButton',e=True,l='toOrgTex',bgc=[0.7,0.9,0.7],c=lambda *args:toOrgTex())

def storeBuffer():
	global BUF
	ftn=cmds.ls(type='file',l=True)
	for EACHFTN in ftn:
		TEXNAME=cmds.getAttr(EACHFTN+'.fileTextureName')
		TEXSIZE=cmds.getAttr(EACHFTN+'.outSize')
		BUF.append([EACHFTN,TEXNAME,TEXSIZE[0]])

def checkExit():
	toOrgTex()

def LayoutA():
	if cmds.columnLayout('MS_texCheckResolution_mainLayout',ex=True):
		cmds.deleteUI('MS_texCheckResolution_mainLayout')
	cmds.columnLayout('MS_texCheckResolution_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_texCheckResolution',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button('MS_texCheckResolution_mainButton',l='toResTex',bgc=[0.7,0.7,0.9],c=lambda *args:toResTex())
	cmds.separator()
	cmds.setParent('..')

	#ウィンドウ終了時にテクスチャを必ず元に戻す。
	cmds.scriptJob(uid=['MS_texCheckResolution_mainLayout',checkExit] )

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	