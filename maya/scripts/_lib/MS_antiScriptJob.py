# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_antiScriptJob
# 説明
#			オートデスク・オンサイトミーティングでの案件
#			「スクリプトジョブをなるべく使わずに、オブジェクトの変更を知る方法」
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.OpenMaya as OpenMaya

def historyLog():
	
	def historyTestFunction(msg,messageType):
	    print messageType
	
	id = OpenMaya.MCommandMessage.addCommandCallback(historyTestFunction)
	# OpenMaya.MMessage.removeCallback(id)  # コールバックの削除。




def objactCallback():
	# コールバック本体
	# msg：アトリビュートに起こったイベントの種類
	# mplug：変更があったアトリビュート
	# otherMplug：接続しているアトリビュート
	# clientData：コールバック設定時に自分が設定したデータ
	def testFunction(msg, mplug, otherMplug, clientData):
	    print msg
	    print mplug.info()
	    print otherMplug.info()
	    print clientData
	    if msg & OpenMaya.MNodeMessage.kAttributeSet:
	        print "kAttributeSet"
	    if msg & OpenMaya.MNodeMessage.kConnectionMade:
	        print "kConnectionMade"
	    elif msg & OpenMaya.MNodeMessage.kConnectionBroken:
	        print "kConnectionBroken"
	        return
	    if msg & OpenMaya.MNodeMessage.kOtherPlugSet:
	        print "kOtherPlugSet"
	
	# 選択しているオブジェクトの取得
	selectionList = OpenMaya.MSelectionList()
	node = OpenMaya.MObject()
	OpenMaya.MGlobal.getActiveSelectionList(selectionList)
	selectionList.getDependNode(0, node)
	
	# clientDataを設定して、コールバックを作成。(ここで指定したclientDataはコールバック関数に渡される)
	clientData = "test"
	id2 = OpenMaya.MNodeMessage.addAttributeChangedCallback(node, testFunction, clientData) 
	# OpenMaya.MMessage.removeCallback(id2) # コールバックの削除




def layoutA():
	cmds.frameLayout('MS_antiScriptJob_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'MS_PYTHON_FORMAT',cll=True,cl=False)
	cmds.columnLayout()
	
	cmds.text(l='MS_antiScriptJob')
	cmds.textField('MS_antiScriptJob_textField_a',w=150,tx='')
	cmds.intField('MS_antiScriptJob_floatField_a',w=150,v=0)
	cmds.button(w=150,l=u'do',c=lambda *args:do())
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_antiScriptJob_main_window',q=True,ex=True):
		cmds.deleteUI('MS_antiScriptJob_main_window')
	cmds.window('MS_antiScriptJob_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_antiScriptJob_main_window')
	


