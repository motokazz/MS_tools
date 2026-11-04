# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_filePathField
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import os
import sys
import importlib

#実行パス追加
#sys.path.append(os.path.dirname(__file__))

from . import MS_storeRecallUI
importlib.reload(MS_storeRecallUI)


##### エクスプローラーで開く系 #####
class explororUtil:
	dir=''
	def __init__(self,path=''):
		self.dir=path

	def pathNormalize(self):
		DIR=self.dir.replace('/','\\')
		if DIR[-1]=='\\':#行末がバックスラッシュの場合
			self.dir=DIR
		else :#ファイルパスの場合def while function:
			self.dir='\\'.join(DIR.split('\\')[:-1])
		
	def openExploror(self,path):
		self.dir=path
		self.pathNormalize()
		os.popen('explorer "%s"' % self.dir)
		

#####　標準

class filePathField:
	def __init__(self
		,controlName='MS_pathField'
		,label='filePath'
		,annotation='annotation'
		,useFileName=True
		,fileName=''
		,domainLayout='domainLayout'
		#for_fileDialog2
		,dialogStyle=2
		,caption='brouser'
		,startingDirectry='d:/'
		,fileFilter="Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
		,selectFileFilter='*.*'
		,fileMode=3
		,acceptMode=0
		,okCaption='SelectDir'
		,cancelCaption='cancel'
		,returnFilter=False
		#misc
		,isExist=True
		):
		self.domainLayout=domainLayout				#親のコントロール名。storeRcallで使われる。
		self.controlName=controlName				#メインコントロール名
		self.label=label							#ラベル
		self.annotation=annotation					#注釈
		self.useFileName=useFileName				#ファイル名のダイアログの編集可能状態のON/OFF
		self.fileName=fileName						#ファイル名

		#for_fileDialog2
		self.dialogStyle=2							#0=default:1=windows style:2=platform common style
		self.caption=caption						#dialog tytle
		self.startingDirectry=startingDirectry		#デフォルトのファイルパス
										
		self.fileFilter=fileFilter					#ダイアログ表示する時のファイルフィルター
		self.selectFileFilter=selectFileFilter		#初期ファイル フィルタを、選択するように指定します。ワイルドカード仕様全体ではなく、開始テキストのみを指定します。
		self.fileMode=fileMode						#ダイアログの表示モード：0 = isExist : 1=file : 2 = filedir : 3=dir : 4=filelist
		self.acceptMode=acceptMode					#ファイルを開くためのダイアログか、ファイルを保存するためのダイアログかを指定します。0=open:1=save
		self.okCaption=okCaption					#dialogStyle フラグを 2 に設定すると、ダイアログのボタンに OK または Accept のキャプションが表示されます。
		self.cancelCaption=cancelCaption			#dialogStyle フラグを 2 に設定すると、ダイアログのボタンに Cancel のキャプションが表示されます。
		self.returnFilter=returnFilter				#true の場合、選択したフィルタは選択したファイルとともに、文字配列の最後の項目として返されます。
		self.isExist=isExist						#fileMode　0 用


	def fileBrouser(self):#ファイルブラウザ
		FILE_PATH=cmds.fileDialog2(
			fileFilter=self.fileFilter
			,ds=self.dialogStyle
			,okc=self.okCaption
			,fm=self.fileMode
			,dir=self.startingDirectry
			)

		if self.fileMode==0:
			#fileMode 0 存在確認用
			self.isExist=FILE_PATH
			return self.isExist

		if FILE_PATH:
			#fileMode 1 2 3 4用
			if self.fileMode==1:
				self.startingDirectry = FILE_PATH[0]
				
			elif self.fileMode==2 or self.fileMode==3:
				self.startingDirectry = FILE_PATH[0] + '/'

			elif self.fileMode==4:
				self.startingDirectry = ':'.join(FILE_PATH)

			cmds.textField(self.controlName+'_FILE_PATH',e=True,fileName=self.startingDirectry)
			#
			MS_storeRecallUI.store(self.domainLayout)
	
	#UI

	def pathBrouser(self):
		cmds.columnLayout(self.controlName,ann=self.annotation,adj=True)
		cmds.rowLayout(nc=3 ,cw3=[100,80,20],adj=True)

		cmds.text(w=100,label=self.label,ann=u'ファイルを出力するパスを設定します')
		cmds.button(self.controlName+'Brouse',w=80,label='Brouse',c=lambda *args:self.fileBrouser())
		cmds.button(w=20,bgc=[0.6,0.8,0.9],label='e',c=lambda *args:self.openExploror())
		cmds.setParent('..')
		cmds.textField(self.controlName+'_FILE_PATH',w=200,en=0,fileName=self.startingDirectry)
		cmds.setParent('..')

		MS_storeRecallUI.recall(self.domainLayout)
		#パスの初期値を　startingDirectry　に格納
		self.startingDirectry=cmds.textField(self.controlName+'_FILE_PATH',q=True,tx=True)
		#self.fileName=cmds.textField(self.controlName+'_FILE_NAME',q=True,tx=True)


	def single(self):#ファイルダイアログ(fileDialog2)

		cmds.columnLayout(self.controlName,ann=self.annotation,adj=True)
		cmds.rowLayout(nc=3 ,cw3=[100,80,20],adj=True)

		cmds.text(w=100,label=self.label,ann=u'ファイルを出力するパスを設定します')
		cmds.button(self.controlName+'Brouse',w=80,label='Brouse',c=lambda *args:self.fileBrouser())
		cmds.button(w=20,bgc=[0.6,0.8,0.9],label='e',c=lambda *args:self.openExploror())
		cmds.setParent('..')
		cmds.textField(self.controlName+'_FILE_PATH',w=200,en=0,fileName=self.startingDirectry)
		cmds.checkBox(self.controlName+'_ac_'+self.controlName+'_FILE_NAME',l='useFileName',v=True,cc=lambda *args:self.useFileNameCheck())
		cmds.textField(self.controlName+'_FILE_NAME',w=200,en=self.useFileName,fileName=self.fileName)
		cmds.setParent('..')

		MS_storeRecallUI.recall(self.domainLayout)
		#パスの初期値を　startingDirectry　に格納
		self.startingDirectry=cmds.textField(self.controlName+'_FILE_PATH',q=True,tx=True)
		self.fileName=cmds.textField(self.controlName+'_FILE_NAME',q=True,tx=True)

	def useFileNameCheck(self):		#ファイルネームを使うか否かのフラグをself.useFileNameｊに格納。戻り値：self.useFileName
		if cmds.checkBox(self.controlName+'_ac_'+self.controlName+'_FILE_NAME',q=True,v=True):
			self.useFileName=True
		else:
			self.useFileName=False
		return self.useFileName

	def queryFileName(self):
		self.fileName=cmds.textField(self.controlName+'_FILE_NAME',q=True,tx=True)
		return self.fileName

	#util
	def openExploror(self):
		oe=explororUtil()
		oe.openExploror(self.startingDirectry)

#Sample
def layoutA():
	fpf=filePathField()
	cmds.columnLayout()
	fpf.fileMode=2
	fpf.single()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	layoutA()

	cmds.showWindow('MS_tools_window')
	

#UI()
