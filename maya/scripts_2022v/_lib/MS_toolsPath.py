# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_toolsPath.py
# 説明
#			ツールの実行パスを取得する
#			
# 作成日
#			
########################################


import sys

class MS_toolsPath:
	def __init__(self):
		self.fullPath = __file__
		self.pathArr=self.fullPath.replace('\\','/').split('/')
		self.currentPath = '/'.join(self.pathArr[0:-1])+'/'
		self.parentPath  = '/'.join(self.pathArr[0:-2])+'/'


	def getHRC(self,num=0):#自分がいるフォルダから、階層数を指定して親フォルダを取得
		return '/'.join(self.pathArr[0:-num])+'/'



