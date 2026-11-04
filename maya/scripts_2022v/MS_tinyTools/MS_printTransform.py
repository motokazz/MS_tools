# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_printTransform.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds


def main():
	SEL = cmds.ls(sl=True)
	for each in SEL:
		LOG=each+'\n'
		

		LOG+= 'Translate	:'
		LOG+= str(cmds.xform(each,q=True,t=True,ws=True))
		LOG+='\n'
		LOG+= 'Rotate	:'
		LOG+= str(cmds.xform(each,q=True,ro=True,ws=True))
		LOG+='\n'
		LOG+= 'Scale		:'
		LOG+= str(cmds.xform(each,q=True,s=True,ws=True))

		print LOG

def LayoutA():
	cmds.columnLayout('MS_printTransform.py _mainLayout',adj=True,ann=u'選択オブジェクトのトランスフォーム情報をプリントします。')
	cmds.separator()
	cmds.text(l='MS_printTransform.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='printTransform',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	