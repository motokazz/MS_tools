# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_exportFbx
# 説明
#			UNITY用に編集
# 作成日
#			
########################################
import maya.cmds as cmds
import maya.mel as mel
import importlib

import MS_exporter
importlib.reload(MS_exporter)

#追加モジュール
import MS_convertSmoothMesh
importlib.reload(MS_convertSmoothMesh)

import MS_swatchMaker
importlib.reload(MS_swatchMaker)

#################
#プラグインのロード
#################
if not cmds.pluginInfo('fbxmaya.mll',q=True,loaded=True):
	cmds.loadPlugin('fbxmaya.mll')

#################
#エキスポーター定義
#################
Exporter=MS_exporter.GUI('MS_FBXexport')

#エキスポートコマンドの中に記述されるファイルタイプ。つづりに注意。
Exporter.fileType='FBX export'

#見出しのラベルカラー
Exporter.mainLabelColor=[0.6,0.6,0.9]

#デバッグ設定、Trueだと出力コマンドだけ返す。
Exporter.debug=False 

#################
#オプション定義
#################

#タイプ個別オプションの名前
Exporter.optionLayout.layoutName='FBXexportOption'

#オプション設定
Exporter.optionLayout.list=[
		#['controlName','label','value','extra1','extra2','annotation']
		['groups','groups',True,'groups','extra2','annotation']
		,['pointGroups','pointGroups',True,'ptgroups','extra2','annotation']
		,['materials','materials',True,'materials','extra2','annotation']
		,['smoothing','smoothing',True,'smoothing','extra2','annotation']
		,['normals','normals',True,'normals','extra2','annotation']
		]

#オプションに追加したいコントロールはここに書く
def ExLayout(): 
	cmds.button(l='Edit preset ...',c=lambda *args:mel.eval('FBXUICallBack -1 editExportPresetInNewWindow fbx;'))
Exporter.optionLayout.extraLayout=ExLayout

#################
#事前・事後処理
#################
pc=MS_convertSmoothMesh.convertSmoothMesh()

#事前に行いたい処理を書く
def preGlobalCommand():
	pass

#オブジェクトごとの事前処理など
def preEachCommand():
	pass
	#スクリーンショット作成　※現在は本体側MS_exporter
	#MS_swatchMaker.objSwatchMaker(Exporter.nodes, Exporter.filePath,Exporter.fileName)

	#スムースメッシュをポリゴンに
	#pc.meshes=Exporter.tempArray
	#pc.toPoly()
	#Exporter.tempArray=pc.result

	
#オブジェクトごとの事後処理など
def postEachCommand():
	pass

	#スムースメッシュをポリゴンにを削除
	#pc.clean()

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
	pc.OptionLayout()

def UI():
	Exporter.UI()
