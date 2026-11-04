# -*- coding:utf-8 -*-
########################################
# ファイル名
#			MS_exporter
# 説明
#			シーン名エキスポート、ノード個別命名エキスポート、
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel
import sys
import os
import importlib

sys.path.append(os.path.dirname(__file__))

import MS_filePathUI
importlib.reload(MS_filePathUI)

#追加モジュール
import MS_swatchMaker
importlib.reload(MS_swatchMaker)

import MS_storeRecallUI as MS_storeRecallUI
importlib.reload(MS_storeRecallUI)

####################
#エキスポートコアクラス
####################

class fileExport:
	def __init__(self
		,filePath='d:/'
		,fileName='temp'
		,nodes=[]
		,option='v=0'
		,generalOption='-de'
		,referenceOption='-pr'
		,fileType='mayaBinary'
		,isSelection = '-ea'
		,debug=False
		):
		self.filePath = filePath
		self.fileName = fileName
		self.nodes = nodes
		self.option = option
		self.generalOption = generalOption
		self.referenceOption = referenceOption
		self.fileType = fileType
		self.isSelection = isSelection
		self.debug=debug

		#テンポラリプロパティ

		self.tempStr=''
		self.tempArray=[]


	#######################
	#ユーティリティ
	#######################

	#ファイル名の正規化
	def fileNameNormalize(self):
		if self.fileName:
			#リファレンス関連のネームスペース対応
			self.fileName=self.fileName.replace(':','_')
			self.fileName=self.fileName.split('|')[-1]

			#シーン名の拡張子を削除
			try:
				temp = self.fileName.replace('.','/').split('/')
				self.fileName=temp[-2]
			except:
				pass
		else:
			self.fileName='new_scene'

		if self.filePath:
			#リファレンス関連のネームスペース対応
			self.filePath=self.filePath.replace('\\','/')

	#######################
	#実行コマンド
	#######################

	#エキスポートコマンド作成
	def createCommand(self):
		self.fileNameNormalize()

		if self.fileType == 'FBX export':
			self.command = ('file -force -options "fbx" -typ "FBX export" -pr -es '
				+ '"' + self.filePath + self.fileName + '"'
				)
		else:
			self.command=('file -force '
				+ '-options \"' + self.option +'\" '
				+ '-typ \"' + self.fileType + '\" '
				+ self.generalOption +' '
				+ self.referenceOption +' '
				+ self.isSelection +' '
				+ '-ch 0 -chn 0 -con 0 -exp 0 '
				+ '\"' + self.filePath + self.fileName + '\"'
				)

	#エキスポート実行
	def export(self):
		self.createCommand()
		print (self.command)
		if not self.debug:
			mel.eval(self.command)


####################
#オプションをつくるたためのクラス
####################

#オプション作成コアクラス
class optionLayout:	#layoutName=layoutName,cll=collapsed,list=[['controlName','label','value','extra1','extra2','annotation']]
	
	def __init__(self
		,layoutName='createCheckBoxsLayout'
		,cll=True
		,list=[['controlName','label','value','extra1','extra2','annotation']]
		):
		self.layoutName=layoutName
		self.cll=cll
		self.list=list
		self.optionString=''


	def store(self):
		print ('store command dummy')

	def extraLayout(self): #オプションの中に追加したいコントロールはここに書く
		pass

	def layout(self):
		cmds.frameLayout('MS_'+self.layoutName,l=self.layoutName,cl=True,cll=self.cll)
		cmds.columnLayout(adj=True)
		for each in self.list:
			if isinstance(each[2],bool):
				cmds.checkBox(each[0],l=each[1],v=each[2],ann=each[4])
		self.extraLayout()#追加レイアウト
		cmds.setParent('..')
		cmds.setParent('..')


	def query(self):
		temp =[]
		for each in self.list:
			if isinstance(each[2],bool):
				if cmds.checkBox(each[0],q=True,v=True):
					temp.append(each[3]+'=1')
				else:
					temp.append(each[3]+'=0')
		self.optionString=';'.join(temp)
		return self.optionString

#GeneralOptions：MAYAネイティブオプション　オプションの作り方が特殊なため個別にクラス化
class generalOption(optionLayout):
	def __init__(self,*av):
		optionLayout.__init__(self,*av)

		self.layoutName='generalOption'
		self.optionString='-de 1'
		self.list=[
			#['controlName','label','value','extra1','extra2','annotation']
			['defaultFileExtensions','defaultFileExtensions',True,'-de 1','extra2','defaultFileExtensions']
		]

	def query(self):
		temp =[]
		for each in self.list:
			if isinstance(each[2],bool):
				if cmds.checkBox(each[0],q=True,v=True):
					temp.append(each[3])
		self.optionString=' '.join(temp)
		return self.optionString

class referenceOption(optionLayout):
	def __init__(self,*av):
		optionLayout.__init__(self,*av)

		self.layoutName='referenceOption'
		self.optionString='-pr'
		self.list=[
			#['controlName','label','value','extra1','extra2','annotation']
			['PreserveReferences','preserve references',True,'-pr','extra2','preserve references']
			,['ExportUnloadProxys','Export unloaded proxies',False,'-eur','extra2','Export unloaded proxies']
			#,'exp'	:[False,'Keep only a Reference','Keep only a Reference']
			#,'namespace'	:[False,'Use name spaces','Use name spaces']
			]
	def query(self):
		temp =[]
		for each in self.list:
			if isinstance(each[2],bool):
				if cmds.checkBox(each[0],q=True,v=True):
					temp.append(each[3])
		self.optionString=' '.join(temp)
		return self.optionString

####################
# GUIクラス
####################
class GUI(fileExport):
	def __init__(self,layoutName,fileType='mayaBinary',optionLayout=optionLayout(),*av):

		fileExport.__init__(self,*av)
		#
		self.fex=fileExport()
		self.go=generalOption()
		self.ro=referenceOption()
		#
		self.layoutName=layoutName	#メインレイアウト名
		self.fileType=fileType	#ファイルタイプ指定
		self.optionLayout=optionLayout	#個別オプション指定
		self.mainLabelColor=[0.9,0.9,0.9]

		#Swatchのカメラ設定
		self.swatchEnable = False
		#self.swatchCamSets=[[0,0,0,-20,30,0],[0,0,0,-20,120,0],[0,0,0,-20,210,0],[0,0,0,-20,300,0],[0,0,0,-70,30,0],[0,0,0,70,30,0]]
		self.swatchCamSets=[[0,0,0,-20,30,0]]

		#storeRecall設定
		self.storeRecall=True
		self.filePathField=MS_filePathUI.filePathField(layoutName+'MS_exporter',fileMode=3,domainLayout=layoutName)

	##############
	#事前・事後処理
	##############

	def preGlobalCommand(self):#事前処理用ダミー関数
		print ('executed preGlobalCommand')

	def postGlobalCommand(self):#事後処理用ダミー関数
		print ('executed postGlobalCommand')

	def preEachCommand(self):#オブジェクトごとの事前処理など
 		print ('executed preEachCommand')

	def postEachCommand(self):#オブジェクトごとの事後処理など
		print ('executed postEachCommand')

	##############
	#UIからGet関連
	##############

	#オプション文字列取得
	def getOptions(self):
		self.option=self.optionLayout.query()
		self.generalOption=self.go.query()
		self.referenceOption=self.ro.query()
		self.swatchEnable=cmds.checkBox('createThumbneil',q=True,v=True)
	
	####################
	#タイプ別エキスポート実行
	####################

	def exportAll(self):#シーンエキスポート
		#
		self.preGlobalCommand()					#包括事前コマンド
		#
		self.isSelection='-ea'

		self.filePath=self.filePathField.startingDirectry
		if self.filePathField.useFileNameCheck():		#useFileName=True:通常シーンエキスポート
			self.fileName=self.filePathField.queryFileName()
		else:
			self.fileName=cmds.file(q=True,sn=True)		#useFileName=False:保存されているシーン名でシーンエキスポート

		self.getOptions()
		#
		self.preEachCommand()					#直前コマンド
		self.export()
		self.postEachCommand()					#直後コマンド

		self.postGlobalCommand()				#包括事後コマンド
		
		#スクリーンショット作成
		if self.swatchEnable:
			#MS_swatchMaker.objSwatchMaker( [] , self.filePath , self.fileName , CAMSETS=self.swatchCamSets , RENDER_NAME = 'vp2Renderer' , RENDER_OVERRIDE = '')

			#Lemon
			MS_swatchMaker.objSwatchMaker([], 'L:/BG/thumbnail/', self.fileName, CAMSETS=self.swatchCamSets,RENDER_NAME='vp2Renderer', RENDER_OVERRIDE='')

	def exportSelection(self):#ノード個別命名エキスポート、

		self.preGlobalCommand()					#包括事前コマンド

		self.nodes=cmds.ls(sl=True)
		if not self.nodes:
			return
			
		self.isSelection='-es'

		self.filePath=self.filePathField.startingDirectry

		self.getOptions()

		
		#
		if self.filePathField.useFileNameCheck():		#useFileName=True:通常選択エキスポート
			
			self.fileName=self.filePathField.queryFileName()
			self.tempArray=self.nodes				#ノードセレクションに使われる。preEachCommandで書き換えたいため
			self.preEachCommand()				#直前コマンド
			cmds.select(self.tempArray,r=True)
			self.export()

			self.postEachCommand()				#直後コマンド

			#スクリーンショット作成
			if self.swatchEnable:
				#MS_swatchMaker.objSwatchMaker( self.nodes , self.filePath , self.fileName , CAMSETS=self.swatchCamSets , RENDER_NAME = 'vp2Renderer' , RENDER_OVERRIDE = '')
				#Lemon
				MS_swatchMaker.objSwatchMaker(self.nodes, 'L:/BG/thumbnail/', self.fileName, CAMSETS=self.swatchCamSets,RENDER_NAME='vp2Renderer', RENDER_OVERRIDE='')
		else:
			for each in self.nodes:							#useFileName=False:ノード個別命名エキスポート、
				self.fileName=each				#ファイル名に使われる
				self.tempArray=[each]				#ノードセレクションに使われる。preEachCommandで書き換えたいため
				#
				self.preEachCommand()			#直前コマンド
				#
				cmds.select(self.tempArray[0],r=True)
				self.export()
				
				#スクリーンショット作成
				if self.swatchEnable:	
					#MS_swatchMaker.objSwatchMaker( [each] , self.filePath , self.fileName , CAMSETS=self.swatchCamSets , RENDER_NAME = 'vp2Renderer' , RENDER_OVERRIDE = '' , REFFERENCE_MODEL = 'D:/Projects/Gravite2/assets/bg/model/kitten_notex.atgi')
					# Lemon
					MS_swatchMaker.objSwatchMaker([each], 'L:/BG/thumbnail/', self.fileName,CAMSETS=self.swatchCamSets, RENDER_NAME='vp2Renderer',RENDER_OVERRIDE='')
				#
				self.postEachCommand()			#直後コマンド
		#
		self.postGlobalCommand()				#包括事後コマンド


	####################
	#UI
	####################


	def layoutA(self):
		#mainLayout
		cmds.columnLayout(self.layoutName,adj=True)#レイアウトメインの親
		cmds.text(l=self.fileType,bgc=self.mainLabelColor,fn='boldLabelFont')
		
		#fileDialog
		self.filePathField.single()
		
		#buttons
		cmds.columnLayout(self.layoutName+'EX',adj=True)
		
		cmds.gridLayout( numberOfColumns=2, cellWidthHeight=(100, 50) ,p=self.layoutName+'EX')
		cmds.button(l='eachobj\nSeparate',bgc=[0.6,0.8,0.6],c=lambda *args:self.exportSelection())
		cmds.button(l='scene',bgc=[0.7,0.6,0.9],c=lambda *args:self.exportAll())
		cmds.setParent('..')

		cmds.checkBox('createThumbneil',v=False)

		cmds.setParent('..')

		#exportOptions
		cmds.columnLayout(adj=True)

		self.go.layout()
		self.ro.layout()
		self.optionLayout.layout()
		cmds.setParent('..')
		#
		cmds.setParent('..')

		MS_storeRecallUI.recall(self.layoutName)
		MS_storeRecallUI.ccOn(self.layoutName)

		return self.layoutName

	def UI(self):
		if cmds.window('MS_tools_window',q=True,ex=True):
			cmds.deleteUI('MS_tools_window')
		cmds.window('MS_tools_window',rtf=True,s=True)

		#
		self.layoutA()

		cmds.showWindow('MS_tools_window')













