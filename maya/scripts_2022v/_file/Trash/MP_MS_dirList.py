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
import sys
import os
import subprocess
import re

#sys.path.append('D:/MS_tools/maya/scripts/mayapy/knack')

import s2000_tools.MS_lib.MS_CSVImportDict as MS_CSVImportDict
reload(MS_CSVImportDict) 

import s2000_tools.MS_lib.MS_fileExport as MS_fileExport
reload(MS_fileExport)

#import s2000_tools.knack.MS_objRangeCurring as MS_objRangeCurring
#reload(MS_objRangeCurring)

import s2000_tools.MS_lib.MS_copyClipboard as MS_copyClipboard
reload(MS_copyClipboard)


#execCheckList
import s2000_tools.MS_lib.MSG2_execCheck as MSG2_execCheck
reload(MSG2_execCheck)
MSG2_execCheck.execCheckSafe('MP_MS_dirList.py')

ROOTDIR='D:/Projects/Gravite2'


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
	
	

def P4Status(LISTUI='MP_MS_gimmickPathList'):
	return
	userName=P4Info()
	print userName
	if cmds.scrollLayout('MP_MS_dirList_layoutP4Status_scrollLayout',q=True,ex=True):
		cmds.deleteUI('MP_MS_dirList_layoutP4Status_scrollLayout')
	cmds.scrollLayout('MP_MS_dirList_layoutP4Status_scrollLayout',h=200,p='MP_MS_dirList_layoutP4Status')
	
	ORGSTRING=cmds.textScrollList(LISTUI,q=True,ai=True)
	for each in ORGSTRING:
		STRING=''
		if 'MB  :' in each or 'TORO:' in each:
			STRING=each.split('#')[-1].replace(' ','')+'...'
		elif 'GameData:' in each:
			STRING=each.split('#')[-1].replace(' ','')
		else:
			continue
		
		#opend
		command='p4 opened -a %s'%STRING
		line=cmdline(command)
		for eachline in line:
			if  userName in eachline:
				cmds.text(l=eachline,bgc=[0.7,0.8,0.8],p='MP_MS_dirList_layoutP4Status_scrollLayout')
				print eachline
			elif '@' in eachline:
				cmds.text(l=eachline,bgc=[0.8,0.7,0.7],p='MP_MS_dirList_layoutP4Status_scrollLayout')
			else:
				print 'lock others or not checkout : '
				cmds.text(l=eachline,p='MP_MS_dirList_layoutP4Status_scrollLayout')
				print eachline
	#finish
	print '---P4Status complete---'
	
	
def onProgress():
	cmds.text('MP_MS_dirList_layoutP4Status_progress',e=True,w=100,l='working',bgc=[0.9,0.3,0.3])
	
def endProgress():
	cmds.text('MP_MS_dirList_layoutP4Status_progress',e=True,w=100,l='ok',bgc=[0.3,0.3,0.3])
	
def P4CheckOut(LISTUI='MP_MS_gimmickPathList'):
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
		#sync
		command='p4 sync %s'%STRING
		line=cmdline(command)
		print line
		#lock
		command='p4 lock %s'%STRING
		line=cmdline(command)
		print line
		#edit
		command='p4 edit -c default %s'%STRING
		line=cmdline(command)
		print line
	#finish
	print '---p4checkout complete---'
	
	P4Status()
	
	
def P4CheckIn(LISTUI='MP_MS_gimmickPathList'):
	return
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
	
##### 飯田さんから拝借　～ #####
	
def ms_yu_getData(PATH='D:/Mproject/MGameData/models/BG/'):
	entFile = cmds.fileDialog(m=0, dm=PATH+'*.toro')
	if not entFile:
		return
	entNode = 'ent_' + (entFile.split('/')[-1]).split('.')[0]
	newNode = cmds.createNode( 'transform', n=entNode )
	MP_MS_searchEntityID.ms_yu_createEntNode(entFile, newNode)
	
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
		PATH=ROOTDIR+'/'+STRING
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
	
def searchEntityIDinScene():#シーン内からオブジェクトIDで指定したノードを選択
	RESULTNODE=[]
	SEARCH_ID=cmds.textField('GIMMICK_ID',q=True,tx=True)
	
	RESULTNODE=MP_MS_searchEntityID.searchScene(SEARCH_ID)
	
	if RESULTNODE:
		cmds.select(RESULTNODE,r=True)
	else:
		return
	
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
	
##### IDからパス検索
	
##### ステージIDからパス検索
	
def ditectStagePathFromID(ID='',OPENMODE=False):
	#Stage
	STAGE_MB_ROOT_PATH='D:/Mproject/graphic/bg/stage/'
	DICT_STAGE={
		'01':'stage001/'
		,'02':'stage002/'
		,'03':'stage003/'
		,'04':'stage004/'
		,'05':'stage005/'
		,'06':'stage006/'
		,'07':'stage007/'
		,'08':'stage008/'
		,'09':'stage009/'
		,'10':'stage010/'
		,'11':'stage011/'
		,'12':'stage012/'
		,'13':'stage013/'
	}
	
	DICT_STAGE_AREA={
		'a':'area_a/'
		,'b':'area_b/'
		,'c':'area_c/'
		,'d':'area_d/'
	}
	#Light&Post
	STAGE_LIGHT_ROOT_PATH='D:/Mproject/graphic/post/light/'
	DICT_LIGHT={
		'01':'bg_01'
		,'02':'bg_02'
		,'03':'bg_03'
		,'04':'bg_04'
		,'05':'bg_05'
		,'06':'bg_06'
		,'07':'bg_07'
		,'08':'bg_08'
		,'09':'bg_09'
		,'10':'bg_10'
		,'11':'bg_11'
		,'12':'bg_12'
		,'13':'bg_13'
	}
	
	DICT_LIGHT_AREA={
		'a':'_a/'
		,'b':'_b/'
		,'c':'_c/'
		,'d':'_d/'
	}
	
	
	
	
	
	
	#Entity
	STAGE_ENTITY_ROOT_PATH='D:/Mproject/mgamedata/models/bg/'
	DICT_ENTITY_AREA={
		'a':'area00/'
		,'b':'area01/'
		,'c':'area02/'
		,'d':'area03/'
	}
	DICT_ENTITY_CATHEGORY={
		'cam':'cam/'
		,'fg':'prop/'
		,'bg':'env/'
	}
	LIST=[]
	LIST.append(' %s' % ID)
	LIST.append('   stage  :#%s' % STAGE_MB_ROOT_PATH+DICT_STAGE[ID[2:4]]+DICT_STAGE_AREA[ID[-1]])
	LIST.append('   entity:#%s' % STAGE_ENTITY_ROOT_PATH+DICT_STAGE[ID[2:4]]+DICT_ENTITY_AREA[ID[-1]]+DICT_ENTITY_CATHEGORY['fg'])
	LIST.append('   light  :#%s' % STAGE_LIGHT_ROOT_PATH+DICT_LIGHT[ID[2:4]]+'/'+DICT_LIGHT[ID[2:4]]+DICT_LIGHT_AREA[ID[-1]])
	
	return LIST
	
##### ギミックIDからパス検索
	
def ditectGimmickPathFromID(ID=0,OPENMODE=False):
	if not ID:
		ID=cmds.textField('GIMMICK_ID',q=True,tx=True).replace(' ','')
	ID_FOLDER=str(ID)[0:2]+'00/'
	
	#MBAPTH
	GIMMICK_MB_PATH='D:/Mproject/graphic/fg/character/gimmick/'
	MB_ID_PATH=GIMMICK_MB_PATH+ID_FOLDER
	MBLIST = os.listdir(MB_ID_PATH)
	GIMMICK_NAME=''
	for EACH in MBLIST:
		if str(ID) in EACH:
			GIMMICK_NAME=EACH
			break
	
	if not GIMMICK_NAME:
		print 'not Match'
		gimmickPathList(['not Match'])
		return
	
	MB_GIMMICK_PATH=MB_ID_PATH+GIMMICK_NAME+'/'
	
	#TOROPATH
	GIMMICK_TORO_PATH='D:/Mproject/mdata/character/gimmick/'
	TORO_ID_PATH=GIMMICK_TORO_PATH+ID_FOLDER
	TORO_GIMMICK_PATH=TORO_ID_PATH+GIMMICK_NAME+'/'
	
	if not os.path.exists(TORO_GIMMICK_PATH):
		TORO_GIMMICK_PATH='nothing'
	
	
	#finalToroFile
	FINAL_TORO_PATH='nothing'
	CHARA_PROJECT=TORO_GIMMICK_PATH+GIMMICK_NAME+'.csv'
	if os.path.exists(CHARA_PROJECT):
		DICT=MS_CSVImportDict.indexColumn(CHARA_PROJECT)
		FINAL_TORO_PATH=DICT['#export'][0][0].replace('\\','/')
		if os.path.exists(FINAL_TORO_PATH):
			FINAL_TORO_PATH=FINAL_TORO_PATH.lower()
			FINAL_TORO_PATH=FINAL_TORO_PATH.replace('d:/mproject','D:/Mproject')
	
	#optionVar
	cmds.optionVar(stringValue=['MP_MS_GIMMICK_ID',str(ID)])
	cmds.optionVar(stringValue=['MP_MS_DIR_FILE_NAME',GIMMICK_NAME])
	cmds.optionVar(stringValue=['MP_MS_DIR_MB',MB_GIMMICK_PATH])
	cmds.optionVar(stringValue=['MP_MS_DIR_TORO',TORO_GIMMICK_PATH])
	
	#gimmickPathList
	LIST=[]
	LIST.append(' %s' % GIMMICK_NAME)
	LIST.append('   MB  :#%s' % MB_GIMMICK_PATH)
	LIST.append('   TORO:#%s' % TORO_GIMMICK_PATH)
	LIST.append('   GameData:#%s' % FINAL_TORO_PATH)
	print LIST
	
	#stageID
	if re.search('st\d{2}_[a-d]',GIMMICK_NAME):#stageID
		LIST+=['------------------------------------------------------------------------------------------------']
		LIST+=ditectStagePathFromID(re.search('st\d{2}_[a-d]',GIMMICK_NAME).group(0))
	
	#
	gimmickPathList(LIST)
	#
	
	setProject(MB_GIMMICK_PATH)
	if OPENMODE:
		mel.eval('projectViewer Open;')

class mpPath:
	
	def __init__(self,sid):
		self.sid=sid
		self.mb		='d:/Mproject/graphic/'
		self.mdata	='d:/Mproject/mdata/'
		self.toro		='d:/Mproject/mgamedata/models/'
		self.stage	='d:/Mproject/graphic/bg/stage/'
		self.entity	='d:/Mproject/mgamedata/models/bg/'
		
		search()
		
	def search():
		DIC={
			'vehicle'			:['d:/Mproject/graphic/bg/object/vehicle/','','d:/Mproject/mgamedata/models/instance/','','']
			,'gimmicksample'	:['d:/Mproject/graphic/misc/','','d:/Mproject/mgamedata/models/test/map_gimmicktest/','','']
			,'enemy'			:['d:/Mproject/graphic/fg/character/enemy/','d:/Mproject/mdata/character/enemy','d:/Mproject/mgamedata/m	odels/character/enemy','','']
		}
		list=DIC[self.sid]
		if list:
			self.mb=list[0]
			self.mdata=list[1]
			self.toro=list[2]
			self.stage=list[3]
			self.entity=list[4]
	def mb():
		return self.mb
	def mdata():
		return self.mdata
	def toro():
		return self.toro
	def stage():
		return self.stage
	def entity():
		return self.entity
		
	def keys():
		return dict.keys()
		
		
		
		
def uniquePathTest(sid=''):
	LIST=[]
	path=mpPath
	LIST.append('MB :#'+path.mb(sid))
	LIST.append('TORO :#'+path.toro(sid))
	gimmickPathList(LIST)
	#setProject(MB_PATH)

def getSceneName():
	#シーン名
	SN=cmds.file(q=True,sn=True)
	ARRAY=SN.replace('.','/').split('/')
	if SN:
		FILE_NAME=ARRAY[-2]
	else:
		FILE_NAME='new_scene'
	return FILE_NAME
	
def uniquePath(ID=''):
	LIST=[]
	DIC={
		'vehicle'			:['d:/Mproject/graphic/bg/object/vehicle/','','d:/Mproject/mgamedata/models/instance/','','']
		,'gimmicksample'	:['d:/Mproject/graphic/misc/','','d:/Mproject/mgamedata/models/test/map_gimmicktest/','','']
		,'enemy'			:['d:/Mproject/graphic/fg/character/enemy/','d:/Mproject/mdata/character/enemy','d:/Mproject/mgamedata/models/character/enemy','','']
	}
	DATA_NAME=getSceneName()
	MB_PATH=DIC[ID][0]
	TORO_PATH=DIC[ID][2]
	FINAL_TORO_PATH=TORO_PATH+DATA_NAME+'.toro'
	cmds.optionVar(stringValue=['MP_MS_DIR_FILE_NAME',DATA_NAME])
	cmds.optionVar(stringValue=['MP_MS_DIR_MB',MB_PATH])
	cmds.optionVar(stringValue=['MP_MS_DIR_TORO',TORO_PATH])
	LIST.append('   MB :#'+MB_PATH)
	LIST.append('   TORO :#'+TORO_PATH)
	LIST.append('   GameData:#%s' % FINAL_TORO_PATH)
	gimmickPathList(LIST)
	setProject(MB_PATH)
	
	
#####
def pre_ditectGimmickPathFromID():
	ID=cmds.textField('GIMMICK_ID',q=True,tx=True).replace(' ','')
	if not ID:
		return
	

	
	#オープンモード
	if cmds.checkBox('OPENMODE',q=True,v=False):
		OPENMODE=True
	else:
		OPENMODE=False
	
	#スーテージID検索モード
	if re.search('st\d{2}_[a-d]',ID):#st【2桁数字】_【a~d】だったら
		ID2=re.search('st\d{2}_[a-d]',ID).group(0)
		if len(ID2)<5:
			gimmickPathList(['--- invailed stageID ---','  stageID : st##_[a-d]','  ex) st01_a'])
			return
		LIST=ditectStagePathFromID(ID=ID2,OPENMODE=OPENMODE)
		gimmickPathList(LIST)
	elif not re.search('\d{4}',ID):#４桁数字じゃなかったら
		uniquePath(ID)
		return
	else:
		P4Revert()#現在のパスリストチェックアウト状態を戻す
		LIST=ditectGimmickPathFromID(ID=ID,OPENMODE=OPENMODE)
		P4CheckOut()
	
#####UI
	
def recallGimmickID():#ギミックIDストア
	NAME='MP_MS_GIMMICK_ID'
	CONTROL_NAME='GIMMICK_ID'
	if cmds.optionVar(exists=NAME):
		cmds.textField(CONTROL_NAME,e=True,tx=cmds.optionVar(q=NAME))
	
def gimmickPathList(LIST):#パスリストUI構築
	if cmds.textScrollList('MP_MS_gimmickPathList',ex=True):
		cmds.deleteUI('MP_MS_gimmickPathList')
	
	cmds.textScrollList('MP_MS_gimmickPathList'
		,w=200
		,numberOfRows=8
		,append=LIST
		,p='MP_MS_gimmickPathList_columnLayout'
		,allowMultiSelection=False
		,doubleClickCommand=lambda *args:openExploror(LISTUI='MP_MS_gimmickPathList',ADDROOT=False)
		)
	
def layoutGimmickID():
	cmds.frameLayout('MP_MS_dirList_frameLayoutB'
		,bgc=[0.2,0.2,0.2]
		,fn='boldLabelFont'
		,l=u'ditectGimmickPathFromID'
		,cll=True
		,cl=False
		,ann=help()
		)
	cmds.columnLayout(adj=True)#col0
	cmds.rowLayout(nc=3)#row1
	#
	cmds.columnLayout(adj=True)#col1
	#
	cmds.rowLayout(nc=2)#row2
	cmds.textField('GIMMICK_ID',tx='9000',cc=lambda *args:pre_ditectGimmickPathFromID())
	cmds.checkBox('OPENMODE',v=False)
	cmds.setParent('..')#row2
	
	cmds.text(l='GimmickID : ####    stageID : st##_[a~d]',al='left')
	cmds.setParent('..')#col1
	#
	###ユーティリティー
	cmds.columnLayout(adj=True)#col2
	cmds.button(l='searchEntityIDinScene',c=lambda *args:searchEntityIDinScene())
	#
	cmds.rowLayout(nc=4)#row3
#	cmds.iconTextButton( style='iconOnly', w=32,image1='distanceDim.png', label='MS_objRangeCurring',c=lambda *args:MS_objRangeCurring.UI())
	cmds.setParent('..')#row3
	#
	cmds.setParent('..')#col2
	
	#
	cmds.columnLayout(adj=True)
	cmds.button(l='open Model',w=100,bgc=[0.7,0.8,0.7],c=lambda *args:openWildCard('_model.mb'))
	cmds.button(l='open Motion',w=100,bgc=[0.7,0.7,0.8],c=lambda *args:openWildCard('_motion.mb'))
	cmds.setParent('..')
	
	cmds.setParent('..')#row1
	
	
	###パスリスト
	cmds.columnLayout('MP_MS_gimmickPathList_columnLayout',adj=True)
	cmds.button(l='pathListToClipboard',w=100,h=20,c=lambda *args:pathListToClipbord())
	cmds.textScrollList('MP_MS_gimmickPathList',p='MP_MS_gimmickPathList_columnLayout',h=80)
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.setParent('..')#col0
	recallGimmickID()
	ditectGimmickPathFromID(OPENMODE=False)
	
	
	
##### UI
	
	
def UI():
	if cmds.window('MP_MS_dirList_main_window',q=True,ex=True):
		cmds.deleteUI('MP_MS_dirList_main_window')
	cmds.window('MP_MS_dirList_main_window',rtf=True,s=True)
	cmds.columnLayout(adj=True)
	
	layoutGimmickID()
	layoutP4Status()
	
	cmds.setParent('..')
	cmds.showWindow('MP_MS_dirList_main_window')
	#P4
	#P4Status()
	
def MP_MS_dirList():
	UI()
	
	
	
