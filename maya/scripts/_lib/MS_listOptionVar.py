# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_listOptionVar
# 説明
#			OptionVarのリスト関連のユーティリティ
# 作成日
#			
########################################


import maya.cmds as cmds
	
def toolHelp(MODE='Query'):
	RET=u'''

「MS_listOptionVar」

～変数リスト～
ツールを起動するとMAYAに登録されているoptionVer変数が全てリストされています。
「optionVar検索後」に検索したい文字列を入力し、Enterで決定すると、リストが作り替えられます。

～操作～
リスト項目ダブルクリック　＝　その変数にどのような値が入っているか調べられます。
SHFT+クリック　＝　項目の複数選択が可能です。
Deleteキー　＝　リストで選択されている変数を削除します。

	'''
	if MODE=='Dialog':
		cmds.confirmDialog(m=RET)
		return
	
	return RET
	
def get(SEARCH_STRING):
	RET=[]
	OPTION_VAR=cmds.optionVar(l=True)
	for EACH in OPTION_VAR:
		if SEARCH_STRING in EACH:
			RET.append(EACH)
	return RET
	
def createList(SEARCH_STRING):
	cmds.optionVar(stringValue=['MS_listOptionVar_textField_a',SEARCH_STRING])#ここでSTORE
	LIST=get(SEARCH_STRING)
	if cmds.textScrollList('MS_listOptionVar_scrollList_a',ex=True):
		cmds.textScrollList('MS_listOptionVar_scrollList_a',e=True,removeAll=True)
	cmds.textScrollList('MS_listOptionVar_scrollList_a'
		,e=True
		,append=LIST
		,p='MS_listOptionVar_paneLayout'
		,allowMultiSelection=True
		,doubleClickCommand=lambda *args:query()
		,deleteKeyCommand=lambda *args:remove()
		)
		
		
def remove():
	OPTION_VAR_NAME=cmds.textScrollList('MS_listOptionVar_scrollList_a',q=True,selectItem=True)
	MESSAGE=''
	for EACH in OPTION_VAR_NAME:
		MESSAGE+=EACH+'\n'
	CONFIRM=cmds.confirmDialog(
		m=MESSAGE+u' を削除してもよろしいですか？'
		,icn='warning'
		,button=['Yes','No']
		,dismissString='No'
		)
	if CONFIRM=='Yes':
		for EACH in OPTION_VAR_NAME:
			cmds.optionVar(rm=EACH)
			print 'removed '+EACH
		cmds.confirmDialog(m=MESSAGE+u'削除しました')
	else:
		print 'command canceled'
	SEARCH_STRING=cmds.textField('MS_listOptionVar_textField_a',q=True,tx=True)
	createList(SEARCH_STRING)
	
def query():
	OPTION_VAR_NAME=cmds.textScrollList('MS_listOptionVar_scrollList_a',q=True,selectItem=True)
	for EACH in OPTION_VAR_NAME:
		VAR=cmds.optionVar(q=EACH)
		if not isinstance(VAR, unicode):
			VAR=str(VAR)
		cmds.confirmDialog(t=EACH,m=EACH+' = '+VAR)
	
	
def recall():
	if not cmds.optionVar(ex='MS_listOptionVar_textField_a'):
		return
	VAR=cmds.optionVar(q='MS_listOptionVar_textField_a')
	cmds.textField('MS_listOptionVar_textField_a',e=True,tx=VAR)
	
	
def layoutA():
	cmds.frameLayout('MS_listOptionVar_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'MS_listOptionVar',cll=True,cl=False)
	
	
	cmds.columnLayout(adj=True)
	
	cmds.rowLayout(nc=2,cw2=[170,30],rat=[2,'both',0])
	cmds.columnLayout(h=40)
	cmds.text(l=u'optionVar検索語')
	cmds.textField('MS_listOptionVar_textField_a',w=150,tx='',cc=lambda *args:createList(cmds.textField('MS_listOptionVar_textField_a',q=True,tx=True)))
	cmds.setParent('..')
	cmds.button(l=u'ヘルプ',c=lambda *args:toolHelp('Dialog'))
	cmds.setParent('..')
	
	
	cmds.paneLayout('MS_listOptionVar_paneLayout')
	cmds.textScrollList('MS_listOptionVar_scrollList_a',p='MS_listOptionVar_paneLayout')
	cmds.setParent('..')
	
	
	cmds.setParent('..')
	
	
def UI():
	if cmds.window('MS_listOptionVar_main_window',q=True,ex=True):
		cmds.deleteUI('MS_listOptionVar_main_window')
	cmds.window('MS_listOptionVar_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_listOptionVar_main_window')
	recall()
	createList(cmds.textField('MS_listOptionVar_textField_a',q=True,tx=True))

def MS_listOptionVar():
	UI()



