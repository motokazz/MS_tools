# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_lemon_motion_exporter
# 説明
#
#
# 作成日
#
########################################

import maya.cmds as cmds
import  maya.mel as mel
import os
import importlib

import _lemon.motion_baker as motion_baker
importlib.reload(motion_baker)

import _lemon.MS_lemon_P4Lib as MS_lemon_P4Lib
importlib.reload(MS_lemon_P4Lib)


class MS_lemon_motion_exporter:
	def __init__(self):
		# Define ####################################

		self.scene_name = cmds.file(q=True, sn=True).split('/')[-1].split('.')[0]

		#正規出力パス
		self.ExportPath = 'M:/Assets/LemonArt/Chara/common/anim'

		#プリセット名
		self.PresetName = 'Lemon_anim'#正しいプリセット名
		self.PresetName_bak = 'New Lemon_anim'#古いプリセット名

		self.FBX_version = 'FBX201800'
		self.Valid_Suffix = ['_in', '_loop', '_out']#正しいSuffix


		# Var ####################
		self.AutoFix = False
		self.GameExporterNodes = cmds.ls(typ='gameFbxExporter')
		self.GameExporterNodeUsing = ''
		self.message = []
		self.baked=False
		self.AnimClips = []
		##################

	def initialize(self):
		cmds.scrollField('MS_lemon_motion_exporter_log', e=True, cl=True)

	def CheckPreset(self):  # ditect Prest Used

		PresetVailed=False
		#正規プリセット名存在確認
		for each in self.GameExporterNodes:
			if cmds.getAttr(each + ".presetName") == self.PresetName:
				self.GameExporterNodeUsing=each
				PresetVailed=True
				break

		#過去に使われていたプリセット名しか無いとき、正規の名前にリネーム
		if not PresetVailed:
			for each in self.GameExporterNodes:
				if cmds.getAttr(each + ".presetName") == self.PresetName_bak:
					if self.AutoFix:
						cmds.setAttr(each + ".presetName", self.PresetName, type='string')
						self.message.append(u'OK : Preset リネーム　=> ' + self.PresetName_bak )
						self.GameExporterNodeUsing = each
						PresetVailed = True
					else:
						self.message.append(u'NG : 古い名前のPreset = ' + self.PresetName_bak)
					break

		# PresetCheck
		if PresetVailed:
			self.message.append('OK : Preset = '+self.PresetName)
			return True
		else:
			self.message.append(u'NG : Presetが無い = ' + self.PresetName )
			return False


	def CheckAnimationClips(self):  # check AnimationClips

		AllClipsValid=True
		animClipsExist=False

		self.AnimClips = []

		#アニメーションクリップ取得
		if cmds.getAttr(self.GameExporterNodeUsing + '.ac',size=True) > 1:#アニメーションクリップが複数ある
			animClips = cmds.getAttr(self.GameExporterNodeUsing + '.ac[*].acn')
			animClipsExist = True
			print ('multi')
		else:#アニメーションクリップは一つ
			print('single')
			animClips = [cmds.getAttr( self.GameExporterNodeUsing + '.ac[0].acn')]
			animClipsExist=True

		if not animClipsExist:
			self.message.append(u'NG : AnimationClipが無い')
			return False

		#クリップ名チェック
		i = 0
		for each in animClips:
			print('c'+each)
			# check filename & suffix
			ClipName_Valid = False

			#

			if self.scene_name == each:#シーン名と一致
				ClipName_Valid = True
			else:

				for each_Valid_Suffix in self.Valid_Suffix:
					# シーン名と一致、かつ正規のSuffix
					if each == self.scene_name+each_Valid_Suffix:
						ClipName_Valid = True
						break
					#大文字小文字チェック
					elif each.lower().endswith(each_Valid_Suffix):
						if self.AutoFix:
							cmds.setAttr(self.GameExporterNodeUsing + '.ac[' + str(i) + '].acn', self.scene_name + each_Valid_Suffix,type='string')
							self.message.append(u'OK : ClipName 修正\n  ' + each + ' => ' + self.scene_name + each_Valid_Suffix)
							ClipName_Valid = True
							break
						else:
							self.message.append('NG : ClipName = ' + each)

			i+=1

			#

			if ClipName_Valid:
				self.message.append('OK : clipname = ' + each)
				self.AnimClips.append(each)
			else:
				AllClipsValid = False
				self.message.append('NG : clipname = ' + each)


		if AllClipsValid:
			self.message.append('OK : All Animation Clips')
		else:
			self.message.append('NG : NG Clip Exist !')
		return AllClipsValid


	def CheckVersion(self):
		Var = cmds.getAttr(self.GameExporterNodeUsing + '.fv')
		if Var == self.FBX_version:
			self.message.append('OK : FBX_version = ' + self.FBX_version )
			return True
		elif self.AutoFix:
			cmds.setAttr(self.GameExporterNodeUsing + '.fv', self.FBX_version, type='string')
			self.message.append('OK : set FBX_version = '+self.FBX_version )
			return True
		else:
			self.message.append('NG : FBX_version = ' + Var )
			return False


	def CheckExportPath(self):

		Var = cmds.getAttr(self.GameExporterNodeUsing + '.exportPath')
		if Var == self.ExportPath:
			self.message.append('OK : ExportPath = ' + Var)
			return True
		elif self.AutoFix:
			cmds.setAttr(self.GameExporterNodeUsing + '.exportPath', self.ExportPath, type='string')
			self.message.append('OK : set ExportPath = ' + self.ExportPath)
			return True
		else:
			self.message.append('NG : ExportPath = ' + Var)
			return False

	# exec ##############################################################################################################

	def Check_All(self,
			exec_CheckAnimationClips = True
			,exec_SetupSettings = True
			,exec_motion_baker = False
			,auto_fix = False
		):

		#
		self.AutoFix = auto_fix

		initialize()

		CheckProgress=[]
		if CheckPreset():
			CheckProgress.append(True)
			if exec_CheckAnimationClips:
				CheckProgress.append(CheckAnimationClips())

			if exec_SetupSettings:
				CheckProgress.append(CheckVersion())
				CheckProgress.append(CheckExportPath())
		else:
			CheckProgress.append(False)


		#全部OK判定
		if False in CheckProgress:
			#一個でもNGがあったらここで処理を中断########################################
			self.message.append('xxx All Check NG xxx')
			#cmds.confirmDialog(m='\n'.join(self.message))
			cmds.scrollField('MS_lemon_motion_exporter_log',e=True,it='\n'.join(self.message))
			return False

		else:
			# 全部OK ##############################################################
			self.message.append('ooo All Check OK ooo')
			cmds.button('MS_lemon_motion_exporter_bakeButton',e=True,en=True, bgc=[0.5,0.7,0.5])
			#cmds.confirmDialog(m='\n'.join(self.message))
			cmds.scrollField('MS_lemon_motion_exporter_log',e=True, it='\n'.join(self.message))
			return True

def GameFbxExporter():
	if cmds.window('gameExporterWindow',q=True,ex=True):
		cmds.deleteUI('gameExporterWindow')
	mel.eval('gameFbxExporter()')



def bake_motion():

	if cmds.file(q=True,modified=True):
		cmds.confirmDialog(m=u'ベイク前にシーンを保存してください')
		return

	global baked
	motion_baker.exec_motion_baker()
	cmds.button('MS_lemon_motion_exporter_bakeButton', e=True, en=False,bgc=[0.4,0.3,0.3])
	cmds.button('MS_lemon_motion_exporter_GameFbxExporter', e=True, bgc=[0.5, 0.7, 0.7])


# P4 ##################################################


WALKED_DATA=[]

def walked(SEARCH_PATH):
	global WALKED_DATA
	WALKED_DATA=[]
	for (root,dir,files) in os.walk(SEARCH_PATH):
		WALKED_DATA.append([root,files])


def searchPath(SEARCH_PATH,SEARCH_FILE='',TARGET_EXT='py'):
	global WALKED_DATA
	for EACH in WALKED_DATA:
		if (SEARCH_FILE + '.' +TARGET_EXT).lower() in list(map(str.lower,EACH[1])):
			root = EACH[0].replace('\\', '/').replace('//', '/')
			return root+'/'+SEARCH_FILE + '.fbx'
	return False

def p4_CheckStatus():
	P4MasterPath = '//Lemon/Master/'
	P4ArtPath = '//LemonArtist/Master/'

	Check_All()

	#MA
	ma_scene_path = P4ArtPath+cmds.file(q=True, sn=True).split(':/')[-1]

	#FBX
	walked('M:/Assets/LemonArt')
	for each in self.AnimClips:
		fbx_path = searchPath(SEARCH_PATH='L:/Assets/LemonArt', SEARCH_FILE=each, TARGET_EXT='fbx')
		if fbx_path:
			unity_asset_path = P4MasterPath + fbx_path.replace('M:/', '')


	#print (unity_asset_path)
	#print (ma_scene_path)

	#print (MS_lemon_P4Lib.P4Info())
	#print (MS_lemon_P4Lib.P4Status(PATH=unity_asset_path))
	#print (MS_lemon_P4Lib.P4headRev(PATH=unity_asset_path))
	print (MS_lemon_P4Lib.P4CheckOut(PATHLIST=[unity_asset_path], ENABLE_DIALOG=True))

# Script job ######################################################################################################
def job():
	jobNum = cmds.scriptJob(e=["SceneOpened",lambda *args:job_newscene()],parent='MS_lemon_motion_exporter_window',protected=True)

def job_newscene():
	initialize()
	UI()

# UI ##############################################################################################################


def LayoutC():
	cmds.frameLayout(l='MS_lemon_motion_exporter', cl=True, cll=False, bgc=[0.4, 0.4, 0.4])
	cmds.separator()
	#
	cmds.columnLayout(adj=True)

	###
	cmds.rowLayout(nc=2,cw2=[100,200],ct2=['left','both'],ad2=2,rat=[1,'top',0])


	###### left #####
	cmds.columnLayout(adj=True)
	LayoutA()
	LayoutB()
	cmds.setParent('..')


	###### right #####
	cmds.columnLayout(adj=True)
	# ログ用 #
	cmds.scrollField('MS_lemon_motion_exporter_log',ed=False,h=300)
	cmds.setParent('..')


	cmds.setParent('..')
	###

	cmds.setParent('..')
	#
	cmds.separator()
	cmds.setParent('..')

def LayoutB():
	cmds.frameLayout(l='util', cl=True, cll=True, bgc=[0.4, 0.4, 0.4])
	cmds.separator()
	#
	cmds.columnLayout(adj=True)
	cmds.button( l='fix_preset', c=lambda *args: Check_All(exec_CheckAnimationClips = False ,exec_SetupSettings = False))
	cmds.button( l='fix_AnimationClips', c=lambda *args: Check_All(exec_CheckAnimationClips = True ,exec_SetupSettings = False))
	cmds.button(l='SetupSettings', c=lambda *args: Check_All(exec_CheckAnimationClips=False, exec_SetupSettings=True))
	cmds.button(l='P4', c=lambda *args: p4_CheckStatus())
	cmds.setParent('..')
	#
	cmds.separator()
	cmds.setParent('..')


def LayoutA():
	cmds.frameLayout(l='', cl=True, cll=False, bgc=[0.4, 0.4, 0.4])
	cmds.separator()
	#
	cmds.columnLayout(adj=True)

	cmds.checkBox('MS_lemon_motion_exporter_autofix',l='Auto fix',v=False,visible=False)
	cmds.button(l='check_All', c=lambda *args: Check_All())
	cmds.button(l='FIX_All', c=lambda *args: Check_All(auto_fix=True))
	cmds.button('MS_lemon_motion_exporter_bakeButton',l='bake motion',en=False, c=lambda *args: bake_motion(),ann=u'全てのチェックがOKにならないと、ベイク出来ません')
	cmds.button('MS_lemon_motion_exporter_GameFbxExporter',l='GameFbxExporter', c=lambda *args: GameFbxExporter())
	cmds.setParent('..')
	#
	cmds.separator()
	cmds.setParent('..')


def UI():
	if cmds.window('MS_lemon_motion_exporter_window', q=True, ex=True):
		cmds.deleteUI('MS_lemon_motion_exporter_window')
	cmds.window('MS_lemon_motion_exporter_window', rtf=True, s=True)

	##LayoutA()
	##LayoutB()
	LayoutC()
	cmds.showWindow('MS_lemon_motion_exporter_window')

	job()

