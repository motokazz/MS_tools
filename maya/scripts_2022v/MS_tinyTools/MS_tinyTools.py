# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_tinyTools.py
# 説明
#			
#			
# 作成日
#			
########################################
	
import maya.cmds as cmds

import os

import s2000_tools.MS_tinyTools.MS_checkInstance as MS_checkInstance
reload(MS_checkInstance)

import s2000_tools.MS_tinyTools.MS_fitVertexToGrid as MS_fitVertexToGrid
reload(MS_fitVertexToGrid)

import s2000_tools.MS_tinyTools.MS_nameConvert as MS_nameConvert
reload(MS_nameConvert)

import s2000_tools.MS_tinyTools.MS_G2BGSceneSetup as MS_G2BGSceneSetup
reload(MS_G2BGSceneSetup)

import s2000_tools.MS_tinyTools.MS_batchSetup as MS_batchSetup
reload(MS_batchSetup)

import s2000_tools.MS_tinyTools.MS_G2RenderUtil as MS_G2RenderUtil
reload(MS_G2RenderUtil)

import s2000_tools.MS_tinyTools.MS_G2lightUtil as MS_G2lightUtil
reload(MS_G2lightUtil)

import s2000_tools.MS_tinyTools.MS_removeNamespace as MS_removeNamespace
reload(MS_removeNamespace)

import s2000_tools.MS_tinyTools.MSG2_createMultiStructs as MSG2_createMultiStructs
reload(MSG2_createMultiStructs)

import s2000_tools.MS_tinyTools.MS_printTransform as MS_printTransform
reload(MS_printTransform)

import s2000_tools.MS_tinyTools.MSG2_checkoutTexture as MSG2_checkoutTexture
reload(MSG2_checkoutTexture)



def OPEN_EXPLOROR(DIR,MODE=''):
	DIR=DIR.replace('/','\\')
	
	if DIR[-1]=='\\':#行末がバックスラッシュの場合
		WINDOWS_PATH=DIR
	elif MODE=='file':#
		os.popen('explorer "%s"' % DIR)
		return
	else :#ファイルパスの場合
		WINDOWS_PATH='\\'.join(DIR.split('\\')[:-1])
	
	os.popen('explorer "%s"' % WINDOWS_PATH)
	

def UI():
	if cmds.window('MS_tinyTools_window',q=True,ex=True):
		cmds.deleteUI('MS_tinyTools_window')
	cmds.window('MS_tinyTools_window',rtf=True,s=True)
	cmds.columnLayout(adj=True)
	cmds.button(l='help',w=40,bgc=[0.5,0.5,0.8],c=lambda *args:OPEN_EXPLOROR(DIR='D:/Projects/Gravite2/tools/maya/maya2014/scripts/python/s2000_tools/MS_tinyTools/MS_tinyTools.docx',MODE='file'))
	cmds.setParent('..')
	MS_G2RenderUtil.LayoutA()
	MS_G2lightUtil.LayoutA()
	MS_checkInstance.LayoutA()
	MS_nameConvert.LayoutA()
	MS_fitVertexToGrid.LayoutA()
	MS_G2BGSceneSetup.LayoutA()
	MSG2_createMultiStructs.LayoutA()
	MS_removeNamespace.LayoutA()
	MS_printTransform.LayoutA()
	MSG2_checkoutTexture.LayoutA()
	#MS_batchSetup.LayoutA()

	cmds.window('MS_tinyTools_window',e=True,w=300,h=300)
	cmds.showWindow('MS_tinyTools_window')
	
