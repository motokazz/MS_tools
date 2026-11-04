# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_sceneCleanupForOutSource.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel

import os

DICT_OS_PATH={
	'XP13':'//Fs03/gravity2$/graphic/bg/outsource/from_SCE/vi15_xp12/G2XP12/Asset/'
	,'XP13Sample':'//Fs03/gravity2$/graphic/bg/outsource/from_SCE/vi15_xp12/G2XP12/Sample/'
}

def exportOSFolder(PACK=''):
	def ret(dummy=''):
		EXPATH = DICT_OS_PATH[PACK]
		if not os.path.exists(EXPATH):
			cmds.confirmDialog(m='notFoound exportPath')

		FULLPATH = cmds.file(q=True,sn=True)
		DIR = FULLPATH.split('/')[6:]
		EXFULLPATH = EXPATH+'/'.join(DIR)
		cmds.file(EXFULLPATH,force=True,options="v=0;",typ="mayaBinary",es=True)
	return ret

def publish_Basic():
	#シーン内オブジェクトのマテリアルを全部ランバート化してマテリアルのクリーンナップ
	MESH=cmds.ls(type='mesh')
	cmds.select(MESH,r=True)

	#カラーセットを消す必要あり
	#cmds.polyColorSet(MESH,delete=True,colorSet="colorSet")
	if cmds.checkBox('LAMBERT_ALL',q=True,v=True):
		cmds.sets(forceElement='initialShadingGroup',e=True)
	mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')

def layer_dont_make():
	DML=cmds.createDisplayLayer(name='dont_make',number=1,nr=True)
	cmds.setAttr(DML+'.visibility',True)
	cmds.setAttr(DML+'.displayType',1)
	cmds.setAttr(DML+'.color',0)


def main():
	pass

def LayoutA():
	cmds.columnLayout('MSG2_sceneCleanupForOutSource.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_sceneCleanupForOutSource.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.checkBox('LAMBERT_ALL',l='lambertAll',v=True)
	cmds.button(l='publish_Basic',c=lambda *args:publish_Basic())
	
	cmds.separator()

	cmds.text(l='layer_dont_make',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.text(l=u'dont_makeレイヤーを作成し、選択オブジェクトを入れる')
	cmds.button(l='layer_dont_make',c=lambda *args:layer_dont_make())

	cmds.separator()

	#exportOSFolder
	cmds.text(l='exportOSFolder',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.text(l=u'選択モデルを、開いているシーン名でアウトソース用のフォルダにエキスポート')
	cmds.gridLayout(nc=4,cw=100)
	#VI
	for each in DICT_OS_PATH.keys():
		#cmds.button(l=each,c=lambda *args:exportOSFolder(each))
		cmds.button(l=each,c=exportOSFolder(each))
	cmds.setParent('..')
	#

	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	

