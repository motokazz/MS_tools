# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_explororUtil
# 説明
#			
# 作成日
#			
########################################
import maya.cmds as cmds
import os

class explororUtil:
	dir=''
	def __init__(self,path=''):
		self.dir=path

	def pathNormalize(self):#認識できるパス記述は'/'じゃなくて'\\'
		self.dir = self.dir.replace('/','\\')

	def openExploror(self,path):#ディレクトリを開く
		self.dir=path
		self.pathNormalize()
		if not self.dir[-1]=='\\':
			self.dir='\\'.join(self.dir.split('\\')[:-1])
		os.popen('explorer "%s"' % self.dir)

	def openFile(self,path):#ファイルをアプリケーションで開く
		self.dir=path
		self.pathNormalize()
		os.popen('explorer "%s"' % self.dir)
		

def eButton(path='D:/',w=16,h=16,bgc=[0.75,0.85,0.9],label='e',ann='open Folder'):#ディレクトリを開くボタン作成
	oe=explororUtil()
	cmds.button(w=w,h=h,bgc=bgc,label=label,ann=ann,c=lambda *args:oe.openExploror(path))

def oButton(path='D:/',w=16,h=16,bgc=[0.8,0.8,0.75],label='o',ann='open File'):#指定ファイルを開くためのボタン作成
	oe=explororUtil()
	cmds.button(w=w,h=h,bgc=bgc,label=label,ann=ann,c=lambda *args:oe.openFile(path))

