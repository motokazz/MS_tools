# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_shelfMaster
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel

def MS_createShelfButton(shelfButtonName='',selectedShelfId=[]):



	val_icon='USERMENUICONFLIPBOOKS.BMP'
	
	commands=''
	commands=commands+'{\n'
	commands=commands+'if(`window -exists MS_shelf`){deleteUI MS_shelf;}\n'
	
	commands=commands+'window -title \"MS_shelf\" MS_shelf;\n'
	commands=commands+'shelfTabLayout -image \"smallTrash.xpm\" -imageVisible true;\n'
	commands=commands+'\n'
	
	i=0
	for i in selectedShelfId:
		
		shelfName = cmds.optionVar('shelfName'+i,q=True)
		shelfFile = cmds.optionVar('shelfFile'+i,q=True)
		
		commands=commands+'shelfLayout "+$shelfName+";\n'
		commands=commands+shelfFile+';\n'
		commands=commands+'setParent ..;\n'
		commands=commands+'\n'
	
	commands=commands+'\n'
	commands=commands+'showWindow MS_shelf\n'
	commands=commands+'\n'
	commands=commands+'\n'

	print commands
	
	if cmds.window('MS_melpalette',e=True):
		cmds.deleteUI ('MS_melpalette')
	

	cmds.window('MS_melpalette',title='MS_melpalette')
		
	cmds.columnLayout()
	
	cmds.shelfTabLayout('mainShelfTab',image='smallTrash.xpm',imageVisible = True)

	cmds.shelfLayout('WorkWindow')

	
	cmds.shelfButton(
		enableCommandRepeat=1
		,enable = 1
		,width = 34
		,height = 34
		,manage = 1
		,visible = 1
		,preventOverride = 0
		#-annotation val_annotation
		,align = 'center'
		,label = shelfButtonName
		,labelOffset = 0
		,font = 'tinyBoldLabelFont'
		,imageOverlayLabel = shelfButtonName
		,image = val_icon
		#-image1 = val_icon
		,style = 'iconAndTextHorizontal'
		,marginWidth = 1
		,marginHeight = 1
		,command = commands
		,actionIsSubstitute = 0
		)
	

 	cmds.showWindow(MS_melpalette)
 	

def MS_shelf():
	
	nShelves = cmds.optionVar(q='numShelves')

	if cmds.window('MS_shelf',q=True,ex=True):
		cmds.deleteUI('MS_shelf')
	cmds.window('MS_shelf',t='MS_shelf')

	#cmds.columnLayout()

	cmds.shelfTabLayout(image='smallTrash.xpm',imageVisible=True)

	for i in range(0,nShelves):
		if not cmds.checkBox( 'chk' + str(i) ,q=True,v=True):
			continue

		shelfName = cmds.optionVar(q='shelfName'+str(i))
		shelfFile = cmds.optionVar(q='shelfFile'+str(i))

		cmds.shelfLayout( shelfName + str(i) )
		mel.eval(shelfFile+';\n')
		print shelfFile
		cmds.setParent('..')

	#cmds.setParent('..')
	
	cmds.showWindow('MS_shelf')



def main():
	pass

def LayoutShelfForm():
	cmds.columnLayout()
	nShelves = cmds.optionVar(q='numShelves')
	for i in range(0,nShelves):
		shelfName = cmds.optionVar(q='shelfName'+str(i))
		shelfFile = cmds.optionVar(q='shelfFile'+str(i))
		cmds.checkBox('chk'+str(i),l=shelfName)
	cmds.setParent('..')

def LayoutA():
	cmds.frameLayout('MS_shelfMaster_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_shelfMaster',cll=True,cl=False)
	cmds.columnLayout('MS_shelfMaster_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_shelfMaster',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:MS_shelf())
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():

	if cmds.window('MS_shelfMaster_window',q=True,ex=True):
		cmds.deleteUI('MS_shelfMaster_window')
	cmds.window('MS_shelfMaster_window',rtf=True,s=True)

	cmds.columnLayout()

	LayoutA()
	LayoutShelfForm()
	
	cmds.setParent('..')
	
	cmds.showWindow('MS_shelfMaster_window')
	