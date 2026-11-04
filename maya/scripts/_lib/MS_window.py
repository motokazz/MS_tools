# -*- coding:utf-8 -*-
########################################
# ファイル名
#			MS_window
# 説明
#			ウィンドウを作る
# 作成日\n#			
########################################

import maya.cmds as cmds

class main:
	def __init__(self,windowName='MS_tools_window',forceSize=False,w=200,h=400):
		self.windowName=windowName
		self.mainLayout=windowName+'_main'
		self.forceSize=forceSize
		self.w=w
		self.h=h


	def hiddenUI(self):
		if cmds.window(self.windowName,q=True,ex=True):
			cmds.deleteUI(self.windowName)
		cmds.window(self.windowName,rtf=True,s=True,w=self.w,h=self.h)

		self.mainLyout()


	def mainLyout(self):
		cmds.columnLayout(self.mainLayout,adj=True,p=self.windowName)
		self.layoutA()
		cmds.setParent('..')
	
	def layoutA(self):
		cmds.text('sample')

	def reflesh(self):
		#if not cmds.window(self.windowName,q=True,ex=True):
		#	self.UI()
		if cmds.columnLayout(self.mainLayout,q=True,ex=True):
			cmds.deleteUI(self.mainLayout)
		self.mainLyout()
		self.UI()

	def close(self):
		if cmds.window(self.windowName,q=True,ex=True):
			cmds.deleteUI(self.windowName)

	def UI(self):
		if cmds.window(self.windowName,q=True,ex=True):
			cmds.deleteUI(self.windowName)
		cmds.window(self.windowName,rtf=True,s=True,w=self.w,h=self.h)

		self.mainLyout()

		cmds.showWindow(self.windowName)
