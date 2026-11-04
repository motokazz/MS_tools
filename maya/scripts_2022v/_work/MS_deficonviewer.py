# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_deficonviewer
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds
from _lib import MS_copyClipboard as MS_copyClipboard

def iconList():
	def cc(name):
		def ret(dummy=''):
			print (name)
		return ret

	if cmds.flowLayout('MS_deficonviewer_flowLayout',q=True,ex=True):
		cmds.deleteUI('MS_deficonviewer_flowLayout')
	cmds.flowLayout('MS_deficonviewer_flowLayout',h=3500,cs=1,wrap=True,p='MS_deficonviewer_scrollLayout')


	search_word = cmds.textField('MS_deficonviewer_search_word',q=True,tx=True)
	pngList = cmds.resourceManager(nameFilter ='*' + search_word+"*.png")
	for png in pngList:
		cmds.iconTextButton(w=200,h=32,l=png.replace('.png',''),st='iconAndTextHorizontal',al='left',i=png,ann=png,c=cc(png))
	cmds.setParent('..')

def layoutIcons():

	form=cmds.formLayout()

	scroll=cmds.scrollLayout('MS_deficonviewer_scrollLayout',cr=True,mcw=200)

	cmds.setParent('..')
	cmds.setParent('..')
	cmds.formLayout(form,e=True
		,af=[
			(scroll,"top",60)
			,(scroll,"left",0)
			,(scroll,"bottom",0)
			,(scroll,"right",0)
			]
		)

def main():
	pass

def LayoutA():
	cmds.frameLayout('MS_deficonviewer_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_deficonviewer',cll=True,cl=False)
	cmds.columnLayout('MS_deficonviewer_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_deficonviewer',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.textField('MS_deficonviewer_search_word',cc=lambda *args:iconList())
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_deficonviewer_window',q=True,ex=True):
		cmds.deleteUI('MS_deficonviewer_window')
	cmds.window('MS_deficonviewer_window',rtf=True,s=True)
	
	layoutIcons()
	LayoutA()

	cmds.showWindow('MS_deficonviewer_window')
	