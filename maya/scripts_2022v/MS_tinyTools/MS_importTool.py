# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_importTool.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import os
import subprocess
import re
import glob

#川野さん、お借りしてます！
#import s1907_atg_change.main

#execCheckList
#import s2000_tools.MS_lib.MSG2_execCheck as MSG2_execCheck
#reload(MSG2_execCheck)
#MSG2_execCheck.execCheckSafe('MS_importTool')#execCheckList

#################
#  Plugin Check 
#################
#if not cmds.pluginInfo("GraviteLocatorNode.mll", q=1, loaded=1):
#	cmds.loadPlugin("GraviteLocatorNode.mll")

#################
# Initialize
#################
#ATGIPATH = 'D:/Projects/Gravite2/assets/bg/model'
THUMBNEILPATH='D:/Projects/Gravite2/graphic/bg/jam/thumbnail'
BGMBRoot = 'D:/Projects/Gravite2/graphic/bg/scenes'
DIRS={
	'work':['D:/work/gravitydaze2_work/parts','D:/work/gravitydaze2_work/parts']
	,'workVe':['D:/work/gravitydaze2_work/ve','D:/work/gravitydaze2_work/ve']
	,'JAM':['D:/Projects/Gravite2/graphic/bg/jam/thumbnail','D:/Projects/Gravite2/graphic/bg/scenes']
	,'JAM:_root':['D:/Projects/Gravite2/graphic/bg/jam/thumbnail','D:/Projects/Gravite2/graphic/bg/scenes/_root']
	,'JAM:architecture':['D:/Projects/Gravite2/graphic/bg/jam/thumbnail','D:/Projects/Gravite2/graphic/bg/scenes/architecture']
	,'JAM:billboard':['D:/Projects/Gravite2/graphic/bg/jam/thumbnail','D:/Projects/Gravite2/graphic/bg/scenes/billboard']
	,'JAM:building':['D:/Projects/Gravite2/graphic/bg/jam/thumbnail','D:/Projects/Gravite2/graphic/bg/scenes/building']
	,'JAM:fence':['D:/Projects/Gravite2/graphic/bg/jam/thumbnail','D:/Projects/Gravite2/graphic/bg/scenes/fence']
	,'JAM:furniture':['D:/Projects/Gravite2/graphic/bg/jam/thumbnail','D:/Projects/Gravite2/graphic/bg/scenes/furniture']
	,'JAM:item':['D:/Projects/Gravite2/graphic/bg/jam/thumbnail','D:/Projects/Gravite2/graphic/bg/scenes/item']
	,'JAM:objects':['D:/Projects/Gravite2/graphic/bg/jam/thumbnail','D:/Projects/Gravite2/graphic/bg/scenes/objects']
	,'JAM:organic':['D:/Projects/Gravite2/graphic/bg/jam/thumbnail','D:/Projects/Gravite2/graphic/bg/scenes/organic']
	,'JAM:other':['D:/Projects/Gravite2/graphic/bg/jam/thumbnail','D:/Projects/Gravite2/graphic/bg/scenes/other']
	,'JAM:sky':['D:/Projects/Gravite2/graphic/bg/jam/thumbnail','D:/Projects/Gravite2/graphic/bg/scenes/sky']
	,'JAM:terrain':['D:/Projects/Gravite2/graphic/bg/jam/thumbnail','D:/Projects/Gravite2/graphic/bg/scenes/terrain']
	,'JAM:window':['D:/Projects/Gravite2/graphic/bg/jam/thumbnail','D:/Projects/Gravite2/graphic/bg/scenes/window']
	}


#################
# P4
#################
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

def P4Status(PATH=''):
	userName=P4Info()
	command='p4 opened -a %s'%PATH
	line=cmdline(command)
	for eachline in line:
		if  userName in eachline:
			return 'checkout'
		elif '@' in eachline:
			return 'locked'
		else:
			return 'notcheckout'

def P4CheckOut(PATHLIST=[]):

	for each in PATHLIST:
		STRING=''
		if '.mb' in each:
			STRING=each.split('#')[-1].replace(' ','')+'...'
		elif 'GameData:' in each:
			STRING=each.split('#')[-1].replace(' ','')
		else:
			continue

		#P4Check
		P4Check=P4Status(each)
		if P4Check=='locked': #誰かがロックしている
			cmds.confirmDialog(m='file is locked',button=['confirm'],defaultButton='confirm')
			continue
		elif P4Check=='checkout': #チェックアウトされている
			continue
		else: #チェックアウトされていない
			DS=cmds.confirmDialog(m='Do you want P4 CheckOut?',button=['yes','No'],defaultButton='yes',cancelButton='No',dismissString='No')
			if DS=='No':
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
	
	#P4Status()
	

#################
# FILE IO
#################
def ImportMB(MBNAME):
	def RET(test=''):
		#BGMBRoot
		FPATH=searchPath(BGMBRoot,MBNAME)
		cmds.file(FPATH,i=True,options='v=0',f=True,ra=True)
	return RET

def OpenMB(MBNAME):
	def RET(test=''):
		#BGMBRoot
		FPATH=searchPath(BGMBRoot,MBNAME)
		sceneModfiedCheck()
		P4CheckOut([FPATH])
		cmds.file(FPATH,o=True,options='v=0',f=True)
	return RET


#シーン更新状況チェック
def sceneModfiedCheck():
	#scene modfied check
	if cmds.file(q=True,amf=True):
		DS=cmds.confirmDialog(m='Current Scene is Changed!\nPlease save scene.',button=['Save','No'],defaultButton='yes',cancelButton='No',dismissString='No')
		if DS=='No':
			return False
		else:
			cmds.file(save=True,options='v=0')
			return True
	return True
	
#################
# AtgiUtil
#################
#指定ノードを消す。
def deleteChildNodes(TOPNAME='',):
	preserveList=[]
	childs=cmds.listRelatives(TOPNAME,c=True,f=True)
	for each in childs:
		name=each.split('|')[-1]
		if 'root' in name:
			childs.remove(each)
			preserveList.append(each)

	cmds.delete(childs)
		
#Atgiを実体化
def atgiToMesh():
	TEMP_NAME='MS_importTool_temp_xxxx'
	SEL=cmds.ls(sl=True,l=True)
	for EACHSEL in SEL:
		TEMP_NAME='MS_importTool_temp_xxxx'
		PARENT=cmds.listRelatives(EACHSEL,p=True,f=True)

		#選択Atgiロケーターの座標を取得
		TRN=(0,0,0)
		ROT=(0,0,0)
		if SEL:
			TRN=xFormAverage(cmds.xform(EACHSEL,q=True,ws=True,t=True))
			ROT=cmds.xform(EACHSEL,q=True,ws=True,ro=True)

		#
		#if not cmds.nodeType(EACHSEL)=='GraviteAtgiLocatorNode':
		#	EACHSEL=cmds.listRelatives(EACHSEL,type='GraviteAtgiLocatorNode')[0]

		#選択AtgiファイルのMBパスを取得
		cmds.select(EACHSEL,r=True)
		AtgiFile=cmds.getAttr('.atgiFilename')

		AtgiName=AtgiFile.split('/')[-1].split('\\')[-1].split('.')[-2]
		FPATH=searchPath(BGMBRoot,AtgiName)
		try:
			cmds.file(FPATH,i=True,rdn=True,rpr="crash",dns=True,type="mayaBinary",options="v=0",loadReferenceDepth="none",gr=True,gn=TEMP_NAME)
			deleteChildNodes(TEMP_NAME)

		except:
			return
		#
		cmds.xform(TEMP_NAME,t=TRN)
		cmds.xform(TEMP_NAME,ro=ROT)
		cmds.select(TEMP_NAME,r=True)
		if PARENT:
			TEMP_NAME=cmds.parent(TEMP_NAME,PARENT)
		#
		cmds.rename(TEMP_NAME,AtgiName+'_01')


	cmds.delete(SEL)

#シーン内のAtgiを全部選択
def selectAtgi():
	Nodes=[]
	Shapes=cmds.ls(s=True)
	for each in Shapes:
		if cmds.nodeType(each)=='GraviteAtgiLocatorNode':
			Trn = cmds.listRelatives(ap=True,typ='transform')
			Nodes.append(Trn[0])
	cmds.select(Nodes,r=True)

#空のAtgiノードを作成
def xFormAverage(xf):
	#xform が連続した戻り値リスト（[[0,0,0],[1,1,1],[2,2,2],[3,3,3]...])を返してくるので、それを平均化する。
	x=0.0
	y=0.0
	z=0.0
	n=0
	RET=[0.0,0.0,0.0]

	while xf:
		x+=xf.pop(0)
		y+=xf.pop(0)
		z+=xf.pop(0)
		n+=1

	if x and n:
		RET[0]=x/n
	else:
		RET[0]=0
	if y and n:
		RET[1]=y/n
	else:
		RET[1]=0
	if z and n:
		RET[2]=z/n
	else:
		RET[2]=0
	return RET

def createAtgiNode():
	SEL=cmds.ls(sl=True)
	TRN=(0,0,0)
	ROT=(0,0,0)
	if SEL:
		TRN=xFormAverage(cmds.xform(SEL[0],q=True,ws=True,t=True))
		ROT=cmds.xform(SEL[0],q=True,ws=True,ro=True)
	NODE = cmds.createNode('GraviteAtgiLocatorNode')
	NODETRNS = cmds.listRelatives(NODE,ap=True,type='transform')
	cmds.xform(NODETRNS,t=TRN)
	cmds.xform(NODETRNS,ro=ROT)
	cmds.select(NODETRNS,r=True)
	return NODE

def MS_importMB(FILENAME):
	TEMPNAME='MS_importTool_temp_xxxx'
	FPATH=searchPath(BGMBRoot,FILENAME)
	cmds.file(FPATH,i=True,options='v=0',f=True,shd=True,gr=True,gn=TEMPNAME)
	SN=cmds.rename(TEMPNAME,FILENAME)
	cmds.select(SN,r=True)
	SEL=cmds.ls(SN,sl=True,l=True)
	return SEL

	
#サムネイルリストからの実行コマンド
def swapfileThumbneil(FILENAME):
	def RET(dummy=''):
		
		NEWATGI=''
		SEL=cmds.ls(sl=True,type='transform',l=True)
		
		IMPORTED=MS_importMB(FILENAME)

		if not SEL:
			#選択無し
			return

		for EACHSEL in SEL:

			#TRN=cmds.xform(EACHSEL,q=True,t=True,ws=True)
			
			ROT=cmds.xform(EACHSEL,q=True,ro=True,ws=True)
			SCL=cmds.xform(EACHSEL,q=True,s=True,ws=True)

			#BBTRN
			BB=cmds.xform(EACHSEL,q=True,bb=True,ws=True)
			TRN=[sum(BB[0::3])*0.5,sum(BB[1::3])*0.5,sum(BB[2::3])*0.5]
			
			cmds.duplicate(IMPORTED)
			DUPED=cmds.ls(sl=True,l=True)
			cmds.xform(DUPED,t=TRN,ro=ROT,s=SCL,ws=True)

			#ワイヤーフレームカラー

			#リネーム処理

			#ctrlキーが押されているときの処理
			mods = cmds.getModifiers()
			if (mods & 4) > 0:#+ctrl
				PAR=cmds.listRelatives(EACHSEL,ap=True,f=True)
				cmds.parent(DUPED,PAR[0])
				cmds.delete(EACHSEL)
		cmds.delete(IMPORTED)

	return RET
	
def printString(STR):
	def RET(dummy=''):
		if cmds.scrollField('MS_batch_export_atgi_list',ex=True):
			cmds.scrollField('MS_batch_export_atgi_list',e=True,insertText=STR+'\n',insertionPosition=0)
		if cmds.scrollField('MS_batch_List',ex=True):
			cmds.scrollField('MS_batch_List',e=True,insertText=STR+'\n',insertionPosition=0)
		print STR
	return RET


#指定パスからの相対パスを返す　例）module/MS_primitives.py
def searchPath(searchPath,searchFile='',searchExt='mb'):
	print searchFile+'.'+searchExt
	for (root,dir,files) in os.walk(searchPath):
		#発見時の処理
		for f in files:
			fname=f.split('.')[0]
			if (searchFile+'.'+searchExt) == f:
				root=root.replace('\\','/').replace('//','/')
				return root+'/'+f
	return ''


###############
# AtgiSumbneil
###############
def createRefleshCommands(MIN=0,MAX=100):
	def ret(dummy=''):
		print 'push'
		refleshfileThumbneil(MIN,MAX)
	return ret


def refleshfileThumbneil(MIN=0,MAX=100):
	ATGILIST=createList(MIN,MAX)
	if cmds.gridLayout('MS_importTool_fileThumbneil',q=True,ex=True):
		cmds.deleteUI('MS_importTool_fileThumbneil')
	cmds.gridLayout('MS_importTool_fileThumbneil',nc=4,nr=6,cw=120,ch=125,p='MS_importTool_fileThumbneil_scrollLayout')
	for each in ATGILIST:
		cmds.columnLayout(adj=True)
		#
		if each=='XXXX_NEXT_XXXX':
			cmds.button(l='NEXT',w=120,h=90,c=createRefleshCommands(100,100+MAX))
		#
		else:
			
			#name
			cmds.button(l=each,h=16,c=printString(each))
			
			#壊れモデル名前サムネール用に変更
			THUMNAME=each.replace('_bk','').replace('_db','').replace('_dy','')
			#icon
			cmds.iconTextButton(style='iconOnly', w=120,h=90,image1=THUMBNEILPATH+'/'+THUMNAME+'.jpg', label=each , c=swapfileThumbneil(each))
			#execbutton
			cmds.rowLayout(nc=2)
			cmds.button(l='open',w=55,h=15,bgc=[0.6,0.9,0.6],c=OpenMB(each))
			cmds.button(l='import',w=55,h=15,bgc=[0.6,0.6,0.9],c=ImportMB(each))
			cmds.setParent('..')
			#
		cmds.setParent('..')
	cmds.setParent('..')

#################
# Directory Template
#################

def setDir(NAME='JAM'):
	def setDirRet(dummy=''):
		global THUMBNEILPATH
		global BGMBRoot
		THUMBNEILPATH=DIRS[NAME][0]
		BGMBRoot=DIRS[NAME][1]

		refleshfileThumbneil()
	return setDirRet


###############
# FileList
###############
#Atgiを検索したリスト
def createIgnoreWord():
	IGNOREWORDS=['_col.','_sdw.','_low.','_occ.']#無視するワード、;で区切って複数指定可能
	if not cmds.checkBox('MS_importTool_ignoreWords_checkbrk',q=True,v=True):
		IGNOREWORDS.append('_db.')
		IGNOREWORDS.append('_bk.')
		IGNOREWORDS.append('_dy.')
		IGNOREWORDS.append('_brk_')
	return IGNOREWORDS

def getAtgiList(
	SEARCHWORDS=''	#検索語
	,IGNOREWORDS=['_col.','_sdw.','_low.','_occ.','_db.','_bk.','_dy.','_brk_']#無視するワード、;で区切って複数指定可能
	,BASE_PATH_MODE='THUMBNEIL'
	,MIN=0
	,MAX=100
	):
	IGNOREWORDS=createIgnoreWord()
	RET=[]

	if BASE_PATH_MODE=='MBROOT':
		DIR = glob.glob(BGMBRoot+'/*%s*.mb'%SEARCHWORDS)
	elif BASE_PATH_MODE=='THUMBNEIL':
		DIR = glob.glob(THUMBNEILPATH+'/*%s*.jpg'%SEARCHWORDS)
	
	i=MIN
	for eachDIR in DIR:
		#無視するワードチェック
		IGNORECHECK=False
		for eachIW in IGNOREWORDS:
			if not eachIW:
				continue
			elif eachIW in eachDIR :
				IGNORECHECK=True
				break
		if IGNORECHECK:
			continue

		PRE=eachDIR.replace('\\','/')
		RET.append(PRE)
		i+=1
		if i>MAX:
			RET.append('XXXX_NEXT_XXXX')
			break
	return RET

def createList(MIN=0,MAX=100):
	SEARCHWORDS=cmds.textField('MS_importTool_searchWord',q=True,tx=True)
	IGNOREWORDS=cmds.textField('MS_importTool_ignoreWords',q=True,tx=True).split(';')
	ATGILIST=getAtgiList(SEARCHWORDS,IGNOREWORDS,MIN=MIN,MAX=MAX)
	ATGINAMELIST=[]
	for each in ATGILIST:
		if each=='XXXX_NEXT_XXXX':
			ATGINAMELIST.append('XXXX_NEXT_XXXX')
		else:
			PRE=re.split('/|\\\\',each)
			if len(PRE)>1:
				ATGINAME=PRE[-1].split('.')[0]
				ATGINAMELIST.append(ATGINAME)

	return ATGINAMELIST


#################
# Store Recall
#################
def store():
	PREFIX='MS_importTool'
	CONTROLNAME='MS_importTool_searchWord'
	NAME=PREFIX+CONTROLNAME
	if cmds.control(CONTROLNAME,ex=True):
		cmds.optionVar(stringValue=[NAME,cmds.textField(CONTROLNAME,q=True,tx=True)])

def recall():
	PREFIX='MS_importTool'
	CONTROLNAME='MS_importTool_searchWord'
	NAME=PREFIX+CONTROLNAME
	if cmds.optionVar(exists=NAME):
		cmds.textField(CONTROLNAME,e=True,tx=cmds.optionVar(q=NAME))

###############
# UI
###############

#UIリフレッシュ
def storeAndGetList():
	store()
	refleshfileThumbneil()

def dirsButton():
	cmds.gridLayout(nc=8,cw=80)
	for eachKW in DIRS.keys():
		cmds.button(l=eachKW,w=80,c=setDir(eachKW))
	cmds.setParent('..')

#Atgiリストのレイアウト
def atgiList():
	IGNOREWORDS='_col.;_sdw.;_low.;_occ.;_db.;_bk.;_dy.;_brk_'
	cmds.columnLayout(adj=True)
	cmds.text(l='MS_importTool',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	#
	cmds.rowLayout(nc=4,cw4=[50,150,80,80])
	cmds.text(l='SeatchWords')
	cmds.textField('MS_importTool_searchWord',tx='_ms_',cc=lambda *args:storeAndGetList())
	cmds.button(l='work',c=lambda *args:setDir('work'))
	cmds.button(l='JAM',c=lambda *args:setDir('JAM'))
	cmds.setParent('..')

	dirsButton()
	#
	cmds.rowLayout(nc=4,cw4=[50,150,50,150])
	cmds.text(l='ignoreWords')
	cmds.textField('MS_importTool_ignoreWords',tx=IGNOREWORDS,cc=lambda *args:storeAndGetList())
	cmds.checkBox('MS_importTool_ignoreWords_checkbrk',l='brk',v=False,cc=lambda *args:storeAndGetList())

	cmds.setParent('..')

	cmds.button(l='atgi to mesh',c=lambda *args:atgiToMesh())
	#cmds.button(l='mesh to atgi',c=lambda *args:s1907_atg_change.main.to_atg())

	cmds.setParent('..')

#Atgiサムネイルのレイアウト
def fileThumbneil():
	cmds.columnLayout(adj=True)
	cmds.scrollLayout('MS_importTool_fileThumbneil_scrollLayout',h=500)
	cmds.setParent('..')
	cmds.setParent('..')

#外部ツール用レイアウト
def LayoutA():
	cmds.columnLayout('MS_importTool_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_importTool',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='MS_importTool',c=lambda *args:UI())
	cmds.separator()
	cmds.setParent('..')


def UI():
	if cmds.window('MS_importTool_window',q=True,ex=True):
		cmds.deleteUI('MS_importTool_window')
	cmds.window('MS_importTool_window',rtf=True,s=True)
	
	atgiList()
	fileThumbneil()

	cmds.showWindow('MS_importTool_window')
	recall()
	storeAndGetList()

