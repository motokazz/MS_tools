# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_p4_sceneTextureCheckout
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds


import MS_P4Lib


def main():
	f = cmds.ls(type='file')
	ftns=[]
	for each in f:

		ftns.append(cmds.getAttr(each+'.fileTextureName'))
	MS_P4Lib.P4CheckOut(ftns)


def LayoutA():
	cmds.frameLayout('MS_p4_sceneTextureCheckout_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_p4_sceneTextureCheckout',cll=True,cl=False)
	cmds.columnLayout('MS_p4_sceneTextureCheckout_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_p4_sceneTextureCheckout',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_p4_sceneTextureCheckout_window',q=True,ex=True):
		cmds.deleteUI('MS_p4_sceneTextureCheckout_window')
	cmds.window('MS_p4_sceneTextureCheckout_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_p4_sceneTextureCheckout_window')
