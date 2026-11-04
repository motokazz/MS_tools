# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_exportMb
# 説明
#			
# 作成日
#			
########################################
import maya.cmds as cmds

import MS_exporter
reload(MS_exporter)

#追加モジュール
import MS_swatchMaker
reload(MS_swatchMaker)

#################
#プラグインのロード
#################
#if not cmds.pluginInfo('objExport.mll',q=True,loaded=True):
#	cmds.loadPlugin('objExport.mll')

################
#エキスポーター定義
#################
Exporter=MS_exporter.GUI('MA_mup_bb')

#エキスポートコマンドの中に記述されるファイルタイプ。つづりに注意。
Exporter.fileType='mayaAscii'

#見出しのラベルカラー
Exporter.mainLabelColor=[0.6,0.8,0.9]

#デバッグ設定、Trueだと出力コマンドだけ返す。
Exporter.debug=False 

#################
#オプション定義
#################

#タイプ個別オプションの名前
Exporter.optionLayout.layoutName='includeOption'

#オプション設定
Exporter.optionLayout.list=[
		#['controlName','label','value','extra1','extra2','annotation']
		['History','History',True,'ch','extra2','annotation']
		,['Channels','Channels',True,'chn','extra2','annotation']
		,['Expressions','Expressions',True,'exp','extra2','annotation']
		,['Constraints','Constraints',True,'con','extra2','annotation']
		,['TextureInfo','TextureInfo',True,'sh','extra2','annotation']
		]

#################
#事前・事後処理
#################
TempList=[]
#事前に行いたい処理を書く
def preGlobalCommand():
	pass
#オブジェクトごとの事前処理など
def preEachCommand():
	global TempList
	return
	
	TempList=[]
	#ワールドに出して原点におく
	for each in Exporter.nodes:
		List=[]

		try:
			TYPE=cmds.nodeType(cmds.listRelatives(each,s=True)[0])
		except:
			TYPE='group'

		if TYPE == 'JsPfxRigidBody':
			continue

		#merge
		MESHES = cmds.ls(each,dag=True,type='mesh',sl=True,l=True)
		cmds.duplicate(MESHES)
		DUPED = cmds.ls(sl=True,l=True)

		if len(MESHES)>1:
			UNITED = cmds.polyUnite(DUPED)
		else:
			UNITED = DUPED

		TempList.append(UNITED)
		
		return
		##
		try:
			cmds.polyTriangulate(each)
		except:
			pass

		'''
		PreParent = cmds.listRelatives(each,ap=True,f=True)

		if PreParent:	
			List.append(PreParent[0])
			try:
				each=cmds.parent(each,w=True)
			except:
				pass
		else:
			List.append('')
		
		List.append(cmds.xform(UNITED,q=True,t=True,ws=True))
		List.append(cmds.xform(UNITED,q=True,ro=True,ws=True))
		List.append(cmds.xform(UNITED,q=True,bb=True,ws=True))
		cmds.xform(UNITED,t=[0,0,0],ro=[0,0,0],ws=True)


		if not TYPE == 'JsPfxRigidBody':
			cmds.makeIdentity(each,apply=True,t=0,r=0,s=1,n=0,pn=1)
		try:
			cmds.polyTriangulate(each)
		except:
			pass
		'''
		TempList.append(List)
	pass
	
#オブジェクトごとの事後処理など
def postEachCommand():
	
	global TempList

	#cmds.delete(TempList)
	
	pass

#事後に行いたい処理を書く
def postGlobalCommand():	
	pass

Exporter.preGlobalCommand=preGlobalCommand
Exporter.postGlobalCommand=postGlobalCommand
Exporter.preEachCommand=preEachCommand
Exporter.postEachCommand=postEachCommand

##################################
def layoutA():
	Exporter.layoutA()
	return Exporter.layoutName

def UI():
	Exporter.UI()

