# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_loadPlugin.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

def PLUGINS():
	RET=[
		'Gravite2Shader.mll'
		,'GraviteLocatorNode.mll'
		,'GraviteMayaToAtgi.mll'
		#,'GraviteShader.mll'
		#,'JFtFloat3SeqNode.mll'
		#,'JFtStrSeqNode.mll'
		#,'JfcpCmd.py'
		#,'LMUVFitter.mll'
		#,'sntCopyWeights.mll'
		#,'sntExportSkinWeights.mll'
		,'hctMayaSceneExport.mll'
	]
	return RET

def main():
	for each in PLUGINS():
		if not cmds.pluginInfo(each,q=True,loaded=True):
			cmds.loadPlugin(each)
