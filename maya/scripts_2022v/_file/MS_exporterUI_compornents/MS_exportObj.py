# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_exportObj
# 説明
#			
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
if not cmds.pluginInfo('objExport.mll',q=True,loaded=True):
	cmds.loadPlugin('objExport.mll')

################
#エキスポーター定義
#################
Exporter=MS_exporter.GUI('MS_OBJexport')

#エキスポートコマンドの中に記述されるファイルタイプ。つづりに注意。
Exporter.fileType='OBJexport'

#見出しのラベルカラー
Exporter.mainLabelColor=[0.8,0.9,0.6]

#デバッグ設定、Trueだと出力コマンドだけ返す。
Exporter.debug=False 

#################
#オプション定義
#################

#タイプ個別オプションの名前
Exporter.optionLayout.layoutName='OBJexportOption'

#オプション設定
Exporter.optionLayout.list=[
		#['controlName','label','value','extra1','extra2','annotation']
		['groups','groups',True,'groups','extra2','annotation']
		,['pointGroups','pointGroups',True,'ptgroups','extra2','annotation']
		,['materials','materials',True,'materials','extra2','annotation']
		,['smoothing','smoothing',True,'smoothing','extra2','annotation']
		,['normals','normals',True,'normals','extra2','annotation']
		]

#################
#事前・事後処理
#################
pc=MS_convertSmoothMesh.convertSmoothMesh()

#事前に行いたい処理を書く
def preGlobalCommand():
	pass

#オブジェクトごとの事前処理など
def preEachCommand():

	#スムースメッシュをポリゴンに
	pc.meshes=Exporter.tempArray
	pc.toPoly()
	Exporter.tempArray=pc.result

	#念のためマテリアルをデフォルトにしておく
	#cmds.sets(Exporter.tempArray,e=True,forceElement='initialShadingGroup')

#オブジェクトごとの事後処理など
def postEachCommand():
	#スムースメッシュをポリゴンにを削除
	pc.clean()

#事後に行いたい処理を書く
def postGlobalCommand():
	pass

Exporter.preGlobalCommand=preGlobalCommand
Exporter.preEachCommand=preEachCommand
Exporter.postEachCommand=postEachCommand
Exporter.postGlobalCommand=postGlobalCommand

##################################
def layoutA():
	Exporter.layoutA()
	pc.OptionLayout()

def UI():
	Exporter.UI()
