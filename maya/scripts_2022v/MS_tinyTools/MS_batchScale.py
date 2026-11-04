# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_batchSetup.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import MS_tinyTools_compornents.MS_batchScene as MS_batchScene
reload(MS_batchScene)

import MS_tinyTools_compornents.MS_G2BGSceneSetup as MS_G2BGSceneSetup
reload(MS_G2BGSceneSetup)

def newPreCommand():
	MESH = cmds.listRelatives('|root',ad=True,type='mesh')
	TRN = cmds.listRelatives(MESH,ap=True)
	if TRN:
		cmds.parent(TRN,w=True)
		cmds.xform(TRN,s=[1.3,1.3,1.3],ws=True)
		cmds.makeIdentity(TRN,a=True,s=True)
	OBJS=['|root','|sdw','|low','|col']
	for each in OBJS:
		if cmds.objExists(each):
			cmds.delete(each)
	MS_G2BGSceneSetup.G2BGSceneSetup()


def main():
	MS_batchScene.preCommand = newPreCommand
	MS_batchScene.UI()

def LayoutA():
	cmds.columnLayout('MS_batchSetup_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_batchSetup',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	main()
	