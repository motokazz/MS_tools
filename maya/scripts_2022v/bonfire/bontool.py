# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_obj_selector
# 説明
#
#
# 作成日
#
########################################
import maya.cmds as cmds

def Rename(STR):
	cmds.rename(STR)


def LayoutA():
	cmds.frameLayout('MS_bontool_frameLayout', w=217, bgc=[0.2, 0.2, 0.2], fn='boldLabelFont',
					 l='MS_bontool', cll=True, cl=False)
	cmds.columnLayout('MS_bontool_mainLayout', adj=True)
	cmds.separator()
	cmds.text(l='MS_bontool', bgc=[0.9, 0.9, 0.9], fn='boldLabelFont')
	cmds.button(l='mesh_Head_Opt', c=lambda *args: Rename('mesh_Head_Opt'))
	cmds.button(l='mesh_Hair', c=lambda *args: Rename('mesh_Hair'))
	cmds.button(l='mesh_Face', c=lambda *args: Rename('mesh_Face'))
	cmds.button(l='mesh_Back_Opt', c=lambda *args: Rename('mesh_Back_Opt'))
	cmds.button(l='mesh_Body', c=lambda *args: Rename('mesh_Body'))
	cmds.button(l='mesh_L_Arm', c=lambda *args: Rename('mesh_L_Arm'))
	cmds.button(l='mesh_R_Arm', c=lambda *args: Rename('mesh_R_Arm'))
	cmds.button(l='mesh_L_Leg', c=lambda *args: Rename('mesh_L_Leg'))
	cmds.button(l='mesh_R_Leg', c=lambda *args: Rename('mesh_R_Leg'))
	cmds.button(l='mesh_L_Shoes', c=lambda *args: Rename('mesh_L_Shoes'))
	cmds.button(l='mesh_R_Shoes', c=lambda *args: Rename('mesh_R_Shoes'))

	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')


def UI():
	if cmds.window('MS_bontool_window', q=True, ex=True):
		cmds.deleteUI('MS_bontool_window')
	cmds.window('MS_bontool_window', rtf=True, s=True)

	LayoutA()

	cmds.showWindow('MS_bontool_window')

