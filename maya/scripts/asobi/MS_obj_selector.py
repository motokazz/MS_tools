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


def main():
	result=[]
	search_name=cmds.textField('MS_obj_selector_textField_a',q=True,tx=True)
	sel = cmds.ls(type='transform',l=True)
	for each in sel:
		name=each.split('|')[-1]
		if search_name in name:
			result.append(each)
	cmds.select(result,r=True)





def LayoutA():
	cmds.frameLayout('MS_obj_selector_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_obj_selector',cll=True,cl=False)
	cmds.columnLayout('MS_obj_selector_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_obj_selector',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.textField('MS_obj_selector_textField_a')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_obj_selector_window',q=True,ex=True):
		cmds.deleteUI('MS_obj_selector_window')
	cmds.window('MS_obj_selector_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_obj_selector_window')
	