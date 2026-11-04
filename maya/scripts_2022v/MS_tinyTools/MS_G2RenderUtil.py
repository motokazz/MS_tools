# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_G2RenderUtil.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel
import sys,os

#execCheckList
import s2000_tools.MS_lib.MSG2_execCheck as MSG2_execCheck
reload(MSG2_execCheck)


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



class MS_toolsPath:
	def __init__(self):
		self.fullPath = __file__
		self.pathArr=self.fullPath.replace('\\','/').split('/')
		self.currentPath = '/'.join(self.pathArr[0:-1])+'/'
		self.parentPath  = '/'.join(self.pathArr[0:-2])+'/'


	def getHRC(self,num=0):#自分がいるフォルダから、階層数を指定して親フォルダを取得
		return '/'.join(self.pathArr[0:-num])+'/'


def SAVE(ROW,FILE_PATH):
	f=open(FILE_PATH,'w')#'r'読み込み：'w'書き込み：'a'追記：'+'読み書き両方' 't'テキストモード：'b'バイナリーモード
	f.write(ROW)
	f.close()

##### ファイルロード #####
def LOAD(FILE_PATH):
	f=open(FILE_PATH)
	DATA=[]
	for ROW in f:
		DATA.append(ROW)
	f.close()
	return DATA
	
#
TOOLPATHCLS=MS_toolsPath()
TOOLPATH = TOOLPATHCLS.currentPath+'G2RendererSetup.mel'




#セットアップファイルをロード
def loadSetup():
	MSG2_execCheck.execCheckSafe('MS_G2RenderUtil')#execCheckList
	mel.eval('G2RendererOptionBox;')
	if os.path.exists(TOOLPATH):
		mel.eval('source "%s";'%TOOLPATH)
	G2RenderSetup()
#現在のG2RendererGlobalsの設定を保存
def main():
	mel.eval('G2RendererOptionBox;')
	G2R=cmds.ls(type='G2RendererGlobals',l=True)
	ATTRS = cmds.listAttr(G2R[0],w=True,hd=True,se=True,v=True)
	COMMANDS=[]
	COMMANDS.append('string $G2RGS[]=`ls -type "G2RendererGlobals"`;')
	COMMANDS.append('string $G2R=$G2RGS[0];')
	COMMANDS.append('stringArrayRemoveAtIndex(0,$G2RGS);')
	COMMANDS.append('delete `listRelatives -p -f $G2RGS`;')

	for each in ATTRS:
		print G2R[0]+'.'+each

		try:
			VAR=cmds.getAttr(G2R[0]+'.'+each)
			TYPE=cmds.getAttr(G2R[0]+'.'+each,typ=True)
		except:
			continue

		if TYPE=='float3':
			continue

		elif TYPE=='float':
			COMMANDS.append('if (`attributeQuery -ex -node $G2R "%s"`){'%each)
			COMMANDS.append('setAttr ($G2R+".%s") %s;'%(each,VAR))
			COMMANDS.append('}')

		elif TYPE=='long':
			COMMANDS.append('if (`attributeQuery -ex -node $G2R "%s"`){'%each)
			COMMANDS.append('setAttr ($G2R+".%s") %s;'%(each,VAR))
			COMMANDS.append('}')

		elif TYPE=='enum':
			COMMANDS.append('if (`attributeQuery -ex -node $G2R "%s"`){'%each)
			COMMANDS.append('setAttr ($G2R+".%s") %s;'%(each,VAR))
			COMMANDS.append('}')

		elif TYPE=='bool':
			if VAR:
				VARSTR='true'
			else:
				VARSTR='false'
			COMMANDS.append('if (`attributeQuery -ex -node $G2R "%s"`){'%each)
			COMMANDS.append('setAttr ($G2R+".%s") %s;'%(each,VARSTR))
			COMMANDS.append('}')
			
	#print '\n'.join(COMMANDS)
	SAVE('\n'.join(COMMANDS),TOOLPATH)
	print G2R


#modelpanel4をG2レンダラーにする。
def G2RenderSetup():
	RENDER_NAME = 'vp2Renderer'
	RENDER_OVERRIDE = 'G2Renderer'
	cmds.modelEditor ('modelPanel4',edit=True,displayAppearance="smoothShaded",rnm=RENDER_NAME,rom=RENDER_OVERRIDE,displayTextures=True)

#UI
def LayoutA():
	cmds.columnLayout('MS_G2RenderUtil_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_G2RenderUtil',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.gridLayout(cw=100)
	cmds.button(l='saveSetup',w=100,bgc=[0.8,0.7,0.7],c=lambda *args:main(),ann=u'現在のG2レンダラーの設定を保存する。')
	cmds.button(l='loadSetup',w=100,bgc=[0.8,0.9,0.8],c=lambda *args:loadSetup(),ann=u'G2Rendererレンダラーの設定をロードし、同時にmodelpanel４をG2Renderにする。')
	eButton(TOOLPATH)
	cmds.setParent('..')
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
		