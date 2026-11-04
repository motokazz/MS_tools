import maya.cmds as cmds




def main():
	pass

def LayoutA():
	cmds.columnLayout('MS_test.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_test.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	