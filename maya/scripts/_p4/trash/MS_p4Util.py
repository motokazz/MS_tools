# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_p4Util.py
# 説明
#			
#			
# 作成日
#			
########################################

# -*- coding: sjis -*-
########################################
# ファイル名
#			MP_MS_dirList
# 説明
#			作業用パスの管理＆設定
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel
import os
import subprocess
import re

import s2000_tools.MS_lib.MS_CSVImportDict as MS_CSVImportDict
reload(MS_CSVImportDict)

#import s2000_tools.MS_lib.MS_fileExport
#reload(MS_fileExport)


#import s2000_tools.MS_lib.MS_objRangeCurring as MS_objRangeCurring
#reload(MS_objRangeCurring)

#import s2000_tools.MS_lib.MP_MS_convertCharaProject
#reload(MP_MS_convertCharaProject)

import s2000_tools.MS_lib.MS_copyClipboard as MS_copyClipboard
reload(MS_copyClipboard)



#execCheckList
#import s2000_tools.MS_lib.MS_execCheck as MS_execCheck
#reload(MS_execCheck)
#MS_execCheck.execCheckSafe('MP_MS_dirList.py')


G2Root='d:/Projects/Gravite2'


def help(CONTENT=''):
	RET=''
	if CONTENT=='':RET=u'''
概要：作業用パスの管理＆設定
設定用CSVファイルを元に、シンボル名で作業に関連するディレクトリを管理します。
ディレクトリパスや、事前・事後スクリプトの登録など、を環境変数に登録する機能も有り、ほかのツールで引用可能になります。
'''
	if CONTENT=='brouser':RET=u'''
設定用CSVファイルを選択します。
'''
	if CONTENT=='index':RET=u'''
設定用CSVファイル内の項目が全てカテゴリ化可能です。
'''
	if CONTENT=='cathegory':RET=u'''
ここでカテゴリを選択します。
'''
	if CONTENT=='name':RET=u'''
ここでシンボル名をを選択します。
シンボル名をダブルクリックすると、環境変数に各種パス情報が設定されます。
'''	
	if CONTENT=='content':RET=u'''
ここにコンテンツ内容が表示されます。
ディレクトリパス表示がある項目をダブルクリックすると、エクスプローラーでパスを表示します。
'''
	return RET.replace('\n\n','')

#####P4Commands
	
	
def cmdline(cmdline):
	
	logtex=[]
	
	p=subprocess.Popen(cmdline, shell=True, stdin=subprocess.PIPE,
						 stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
						 )
	(stdouterr, stdin) = (p.stdout, p.stdin)  # 
	print "-" * 80  # 区切り表示(開始)
	while True:
		line = stdouterr.readline()  # 改行を含んで行を読み込む
		if not line:
			break
		logtex.append(line.rstrip())  # 後ろの改行を消して出力
	print "-" * 80  # 区切り表示(終了)
	ret = p.wait()  # 戻り値が入る
	print "Return code: %d" % ret
	
	return logtex

def P4Info():#ユーザー名返す
	command='p4 info'
	line=cmdline(command)
	for each in line:
		if 'User name:' in each:
			name=each.replace('User name:','')
			name=name.replace(' ','')
			name=name.replace('\r','')
			name=name.replace('\n','')
			name=name.replace('\t','')
	
	return name
	
	

def P4Status(FILELIST=[]):
	
	userName=P4Info()
	print userName

	for each in FILELIST:
		#opend
		command='p4 opened -a %s'%each
		line=cmdline(command)
		for eachline in line:
			if  userName in eachline:
				print userName
				print eachline
			elif '@' in eachline:
				print '@'
				print eachline
			else:
				print 'lock others or not checkout : '
				#cmds.text(l=eachline,p='MP_MS_dirList_layoutP4Status_scrollLayout')
				print eachline
	#finish
	print '---P4Status complete---'
	
	
def onProgress():
	cmds.text('MP_MS_dirList_layoutP4Status_progress',e=True,w=100,l='working',bgc=[0.9,0.3,0.3])
	
def endProgress():
	cmds.text('MP_MS_dirList_layoutP4Status_progress',e=True,w=100,l='ok',bgc=[0.3,0.3,0.3])
	
def P4CheckOut(FILELIST=[]):
	
	for EACHFILE in FILELIST:
		#sync
		command='p4 sync %s'%EACHFILE
		line=cmdline(command)
		print line
		#lock
		command='p4 lock %s'%EACHFILE
		line=cmdline(command)
		print line
		#edit
		command='p4 edit -c default %s'%EACHFILE
		line=cmdline(command)
		print line
	#finish
	print '---p4checkout complete---'
	
	#P4Status()
	
	
def P4CheckIn(LISTUI='MP_MS_gimmickPathList'):
	
	#scene modfied check
	if not sceneModfiedCheck():
		return
	#submit comment
	SUBMIT_COMMENT=cmds.textField('MP_MS_dirList_submitComment',q=True,tx=True)
	if not SUBMIT_COMMENT:
		cmds.confirmDialog(m=' submit comment is empty !')
		return
	
	
	ORGSTRING=cmds.textScrollList(LISTUI,q=True,ai=True)
	
	for each in ORGSTRING:
		STRING=''
		if 'MB  :' in each or 'TORO:' in each:
			STRING=each.split('#')[-1].replace(' ','')+'...'
		elif 'GameData:' in each:
			STRING=each.split('#')[-1].replace(' ','')
		else:
			continue
		command='p4 revert -a -k %s'%STRING
		line=cmdline(command)
		print line
		command='p4 unlock %s'%STRING
		line=cmdline(command)
		print line
		command='p4 submit -f submitunchanged -d "'+str(SUBMIT_COMMENT.encode('shift-jis'))+'" '+str(STRING)
		line=cmdline(command)
		print line
	#finish
	print '---p4checkin complete---'
	
	P4Status()
	
def P4Revert(LISTUI='MP_MS_gimmickPathList'):
	ORGSTRING=cmds.textScrollList(LISTUI,q=True,ai=True)
	
	for each in ORGSTRING:
		STRING=''
		if 'MB  :' in each or 'TORO:' in each:
			STRING=each.split('#')[-1].replace(' ','')+'...'
		elif 'GameData:' in each:
			STRING=each.split('#')[-1].replace(' ','')
		else:
			continue
		command='p4 revert -a -k %s'%STRING
		line=cmdline(command)
		for eachline in line:
			print eachline
	#finish
	print '---p4revert complete---'
	
	P4Status()
	
	
def storeP4Status():
	comment=cmds.textField('MP_MS_dirList_submitComment',q=True,tx=True)
	cmds.optionVar(stringValue=['MP_MS_dirList_submitComment',comment])
	
def recallP4Status():
	if cmds.optionVar(exists='MP_MS_dirList_submitComment'):
		cmds.textField('MP_MS_dirList_submitComment',e=True,tx=cmds.optionVar(q='MP_MS_dirList_submitComment'))
	
def layoutP4Status():
	#
	cmds.columnLayout()
	cmds.rowLayout(nc=5,cw5=[100,100,100,100,100],adj=True)
	cmds.button(l='P4stastuscheck',w=100,c=lambda *args:P4Status())
	cmds.button(l='P4CheckOut',w=100,bgc=[0.7,0.8,0.7],c=lambda *args:P4CheckOut())
	cmds.button(l='P4CheckIn',w=100,bgc=[0.8,0.7,0.7],c=lambda *args:P4CheckIn())
	cmds.button(l='P4Revert',w=100,c=lambda *args:P4Revert())
	cmds.text('MP_MS_dirList_layoutP4Status_progress',l='progress',bgc=[0.3,0.3,0.3])
	cmds.setParent('..')
	cmds.setParent('..')
	#
	cmds.textField('MP_MS_dirList_submitComment',w=400,tx='submit from MP_MS_dirList',cc=lambda *args:storeP4Status())
	#
	cmds.columnLayout('MP_MS_dirList_layoutP4Status',adj=True)
	cmds.scrollLayout('MP_MS_dirList_layoutP4Status_scrollLayout',h=200)
	
	
	
	cmds.setParent('..')
	cmds.setParent('..')
	
	recallP4Status()
	
##### ユーティリティ
def pathListToClipbord():
	LISTUI='MP_MS_gimmickPathList'
	ORGSTRING=cmds.textScrollList(LISTUI,q=True,ai=True)
	TEXT='\n'.join(ORGSTRING)
	MS_copyClipboard.copyClipboard(TEXT)
	
def openExploror(PATH='',LISTUI='MP_MS_gimmickPathList',ADDROOT=True):
	ORGSTRING=cmds.textScrollList(LISTUI,q=True,si=True)[0]
	STRING=cmds.textScrollList(LISTUI,q=True,si=True)[0].split('#')[-1].replace(' ','')
	if not STRING:
		return
	
	if not STRING[-1]=='/' and not '.toro' in STRING:
		PRE_STRING=STRING
		STRING='/'.join(PRE_STRING.split('/')[0:-1])+'/'
	if ADDROOT:
		PATH=G2Root+'/'+STRING
	else:
		PATH=STRING
	
	if 'GameData:' in ORGSTRING:
		command='D:\Mproject\ToroTool.exe %s'%PATH
		print command
		subprocess.Popen(command, shell=False)
		#print cmdline(command)
	elif 'entity:' in ORGSTRING:
		ms_yu_getData(PATH)
	else:
		MS_fileExport.OPEN_EXPLOROR(PATH)

def sceneModfiedCheck():
	#scene modfied check
	if cmds.file(q=True,amf=True):
		DS=cmds.confirmDialog(m='Current Scene is Changed!\nPlease save scene.',button=['Save','No'],defaultButton='yes',cancelButton='No',dismissString='No')
		if DS=='No':
			DS2=cmds.confirmDialog(m='Current Scene is NotSaved!\nContinue?.',button=['Yes','No'],defaultButton='yes',cancelButton='No',dismissString='No')
			if DS2=='No':
				return False
			else:
				return True
		else:
			cmds.file(save=True,options='v=0')
			return True
	return True
	
	
def openWildCard(SEARCH_WORD):
	if not sceneModfiedCheck():
		return
	path=cmds.optionVar(q='MP_MS_DIR_MB')
	filename=path.split('/')[-2]+SEARCH_WORD
	print filename
	filelist=os.listdir(path)
	for each in filelist:
		if filename in each:
			cmds.file(path+each,o=True,options='v=0',f=True)
			return
	
def setProject(PATH):#MAYAプロジェクト設定
	mel.eval('setProject "%s"' % PATH)
	



########################

def main():
	FTN=cmds.getAttr('.fileTextureName')
	print FTN
	P4CheckOut([FTN])

def pre_P4status():
	FTN=cmds.getAttr('.fileTextureName')
	P4Status([FTN])
	
def LayoutA():
	cmds.columnLayout('MS_p4Util_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_p4Util',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.button(l='P4Status',c=lambda *args:pre_P4status())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	
UI()