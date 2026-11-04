# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_switchVisible.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

switch=True
switchVisible_a=['|root|mesh']
switchVisible_b=['||col']

def store_a():
	global switchVisible_a
	switchVisible_a=cmds.ls(sl=True,l=True)
	cmds.textField('MS_switchVisible_a',e=True,tx=','.join(switchVisible_a))

def store_b():
	global switchVisible_b
	switchVisible_b=cmds.ls(sl=True,l=True)
	cmds.textField('MS_switchVisible_b',e=True,tx=','.join(switchVisible_b))

def showBoth():
	
	SEL=cmds.ls(sl=True,l=True)

	cmds.hide(all=True)
	cmds.showHidden(switchVisible_a,a=True)
	cmds.showHidden(switchVisible_b,a=True)
	
	cmds.select(SEL,r=True)

def main():
	
	SEL=cmds.ls(sl=True,l=True)

	global switch
	if switch:
		cmds.hide(all=True)
		cmds.showHidden(switchVisible_a,a=True)
		switch=False
	else:
		cmds.hide(all=True)
		cmds.showHidden(switchVisible_b,a=True)
		switch=True

	cmds.select(SEL,r=True)

def LayoutA():
	cmds.columnLayout('MS_switchVisible.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_switchVisible.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.textField('MS_switchVisible_a',tx='|root|mesh',en=False)
	cmds.button(l='store_a',c=lambda *args:store_a())
	cmds.textField('MS_switchVisible_b',tx='|col',en=False)
	cmds.button(l='store_b',c=lambda *args:store_b())

	cmds.gridLayout(nc=2,cw=80)
	cmds.button(l='switch',c=lambda *args:main())
	cmds.button(l='showBoth',c=lambda *args:showBoth())
	cmds.setParent('..')
	
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	