# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_exportMb4Gravity
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
Exporter=MS_exporter.GUI('MS_MBGRexport')

#エキスポートコマンドの中に記述されるファイルタイプ。つづりに注意。
Exporter.fileType='mayaBinary'

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
	TempList=[]
	#ワールドに出して原点におく
	for each in Exporter.nodes:
		List=[]
		List.append(each)

		PreParent = cmds.listRelatives(each,ap=True,f=True)

		if PreParent:	
			List.append(PreParent[0])
			try:
				each=cmds.parent(each,w=True)
			except:
				pass
		else:
			List.append('')

		
		List.append(cmds.xform(each,q=True,t=True,ws=True))
		List.append(cmds.xform(each,q=True,ro=True,ws=True))
		List.append(cmds.xform(each,q=True,bb=True,ws=True))
		cmds.xform(each,t=[0,0,0],ro=[0,0,0],ws=True)
		cmds.makeIdentity(each,apply=True,t=0,r=0,s=1,n=0,pn=1)

		TempList.append(List)


	pass
	
#オブジェクトごとの事後処理など
def postEachCommand():
	global TempList
	#ワールドに出したのを元に戻す
	for each in TempList:
		print each
		cmds.xform(each[0],t=[each[2][0],each[2][1],each[2][2]],ro=[each[3][0],each[3][1],each[3][2]],ws=True)
		if each[1]:
			cmds.parent(each[0],each[1],r=True)

		#スクリーンショット作成
		MS_swatchMaker.objSwatchMaker( [each] , self.filePath , each , RENDER_NAME = 'vp2Renderer' , RENDER_OVERRIDE = 'G2Renderer' , REFFERENCE_MODEL = 'D:/Projects/Gravite2/assets/bg/model/kitten_notex.atgi')

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

