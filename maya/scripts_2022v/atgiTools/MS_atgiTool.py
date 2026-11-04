# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_atgiTool.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel
import os
import subprocess
import re
import glob
import random

#川野さん、お借りしてます！
import s1907_atg_change.main

import s2000_tools.MS_lib.MS_copyClipboard as MS_copyClipboard
reload(MS_copyClipboard)

import s2000_tools.MSG2_atgiTools.MSG2_atgiLocatorToLocator as MSG2_atgiLocatorToLocator
reload(MSG2_atgiLocatorToLocator)

import s2000_tools.MSG2_atgiTools.MSG2_assetsUtil as MSG2_assetsUtil
reload(MSG2_assetsUtil)


#execCheckList
import s2000_tools.MS_lib.MSG2_execCheck as MSG2_execCheck
reload(MSG2_execCheck)
MSG2_execCheck.execCheckSafe('MSG2_atgiTool')#execCheckList

#################
#  Plugin Check 
#################
if not cmds.pluginInfo("GraviteLocatorNode.mll", q=1, loaded=1):
	cmds.loadPlugin("GraviteLocatorNode.mll")

#################
# Initialize
#################
ATGIPATH = 'D:/Projects/Gravite2/assets/bg/model'
THUMBNEILPATH='D:/Projects/Gravite2/graphic/bg/jam/thumbnail'
BGMBRoot = 'D:/Projects/Gravite2/graphic/bg/scenes'


DICT_PATH={
	'bg':['D:/Projects/Gravite2/assets/bg/model','D:/Projects/Gravite2/graphic/bg/jam/thumbnail','D:/Projects/Gravite2/graphic/bg/scenes']
	,'effect':['D:/Projects/Gravite2/assets/effect/model','D:/Projects/Gravite2/graphic/effect/jam/thumbnail','D:/Projects/Gravite2/graphic/effect/scenes']
}

def change_PATH(KEY='bg'):
	global ATGIPATH 
	global THUMBNEILPATH
	global BGMBRoot
	ATGIPATH = DICT_PATH[KEY][0]
	THUMBNEILPATH=DICT_PATH[KEY][1]
	BGMBRoot = DICT_PATH[KEY][2]
	refleshAtgiThumbneil()

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
	
def P4CheckOutForButton(MBNAME):
	def RET(test=''):
		#BGMBRoot
		FPATH=searchPath(BGMBRoot,MBNAME)
		P4CheckOut([FPATH])
	return RET


#################
# Shelf Util
#################
def toShelfIcon(TOOL_NAME,COMMAND,ICON,ANNO):

	def toCastString(str):#evalにキャストするためのコマンドを作成する
		str=str.replace('"','\'')
		str=str.replace('\r\n','\\\\\\\\r\\\\\\\\n')
		str=str.replace('\n','\\\\\\\\n')
		return str

	PYCOM=''
	precom=COMMAND.split('\r\n')

	for each in precom:
		if each:
			com=toCastString(each)
			PYCOM+='python(\\\"%s\\\");\\\r\\\n' % com
	TAB=mel.eval("global string $gShelfTopLevel; $temp=$gShelfTopLevel;")

	#ANNO=toCastString(ANNO)


	SELECTED_TAB=cmds.shelfTabLayout(TAB,q=True,st=True)
	SHELFCOM=(
		u'global string $gShelfTopLevel; $temp=$gShelfTopLevel;\n'
		u'$selectedTab=`shelfTabLayout -q -st $temp`;\n'
		+u'shelfButton '
		+u'-p $selectedTab'
		+u' -image1 \"'+ICON+u'\"'
		+u' -imageOverlayLabel \"'+TOOL_NAME+u'\"'
		+u' -ann \"'+TOOL_NAME+u'\"'
		+u' -command \"'+PYCOM+u'\"'
		+u';'
		)

	return SHELFCOM

def toShelf_import(MBNAME,ICON='D:/Projects/Gravite2/tools/maya/maya2014/scripts/python/s2000_tools/MSG2_atgiTools/MSG2_atgi.bmp'):
	FPATH=searchPath(BGMBRoot,MBNAME)
	ATGIFILEPATH = ATGIPATH+'/'+MBNAME+'.atgi'
	def RET(test=''):
		COMMAND=''
		COMMAND+='import maya.cmds as cmds\r\n'
		COMMAND+='import s2000_tools.MSG2_atgiTools.MSG2_atgiTool as MSG2_atgiTool\r\n'
		COMMAND+='ATGINODE=MSG2_atgiTool.createAtgiNode()\r\n'
		COMMAND+='cmds.setAttr(ATGINODE + ".atgiFilename","%s",type="string")\r\n'%ATGIFILEPATH
		COMMAND+='cmds.rename(cmds.listRelatives(ATGINODE,p=True)[0],"%s")\r\n'%MBNAME
		MELCOM=toShelfIcon(MBNAME,COMMAND,ICON,ANNO='')
		mel.eval(MELCOM)
	return RET

#################
# FILE IO
#################

def ImportMB(MBNAME):
	def RET(test=''):
		#BGMBRoot
		FPATH=searchPath(BGMBRoot,MBNAME)
		cmds.file(FPATH,i=True,options='v=0',f=True)
	return RET

def OpenMB(MBNAME):
	def RET(test=''):
		#BGMBRoot
		FPATH=searchPath(BGMBRoot,MBNAME)

		#シーン更新状況チェック
		if cmds.file(q=True,sn=True):
			if cmds.file(q=True,amf=True):
				DS=cmds.confirmDialog(m='Current Scene is Changed!\nPlease save scene.',button=['Save','No'],defaultButton='yes',dismissString='No')
				if DS=='No':
					DS2=cmds.confirmDialog(m='Work Not Save! \nContinue?.',button=['forceOpen','Cancel'],defaultButton='forceOpen',dismissString='Cancel')
					if DS2=='Cancel':
						return False
				else:
					cmds.file(save=True,options='v=0')

		#P4関連

		try:
			P4CheckOut([FPATH])
		except:
			cmds.confirmDialog(m='Perforce Error . ')

		cmds.file(FPATH,o=True,options='v=0',f=True)

	return RET

#シーン更新状況チェック
def sceneModfiedCheck():
	#scene modfied check
	if cmds.file(q=True,amf=True):
		DS=cmds.confirmDialog(m='Current Scene is Changed!\nPlease save scene.',button=['Save','No','Cancel'],defaultButton='yes',cancelButton='Cancel',dismissString='No')
		if DS=='No':
			return False
		else:
			cmds.file(save=True,options='v=0')
			return True
	return True
	

#################
# AtgiUtil
#################

#シーン内の全ATGIをリロード
def reloadAtgiAll():
	ATGI=cmds.ls(type='GraviteAtgiLocatorNode',l=True)
	for each in ATGI:
	    mel.eval('AEGraviteAtgiReloadCmd %s.atgiFilename;'%each)
	    
#ファンクショナルリネーマー
def functionalRenamer_GraviteAtgiLocatorNode(MODE='ALL'):
	SEL = cmds.ls(sl=True,l=True)
	#
	#if not SEL:
	#	SEL=cmds.ls(type='GraviteAtgiLocatorNode')
	#else:
	#	SEL = cmds.listRelatives(SEL,type='GraviteAtgiLocatorNode',f=True)

	
	for EACH in SEL:
		# if cmds.attributeQuery('atgiFilename',node=EACH,ex=True):

		SHAPE=cmds.listRelatives(EACH,s=True,f=True)
		if SHAPE:
			TYPE=cmds.nodeType(SHAPE)
		else:
			TYPE='group'

		if TYPE=='GraviteAtgiLocatorNode':
			ATGI_FILENAME=cmds.getAttr(EACH+'.atgiFilename')
			NAME=ATGI_FILENAME.split('/')[-1].split('\\')[-1].split('.')[0]
			#TRN=cmds.listRelatives(EACH,p=True,f=True)[0]
		else:
			NAME='_'.join(EACH.split('|')[-1].split('_')[0:-1])

		#
		CHECK=True
		i=1
		while (CHECK):
			if cmds.objExists(NAME+'_'+str(i).zfill(2)) and not EACH.split('|')[-1]==(NAME+'_'+str(i).zfill(2)):
				i+=1
			else:
				CHECK=False

		#
		cmds.rename(EACH,NAME+'_'+str(i).zfill(2))
		i+=1


#指定パスからの相対パスを返す　例）module/MS_primitives.py
def searchPath(searchPath,searchFile='',searchExt='mb'):
	#print searchFile+'.'+searchExt
	for (root,dir,files) in os.walk(searchPath):
		#発見時の処理
		for f in files:
			fname=f.split('.')[0]
			if (searchFile+'.'+searchExt) == f:
				root=root.replace('\\','/').replace('//','/')
				return root+'/'+f
	return False

#指定ノードを消す。
def deleteChildNodes(TOPNAME='',PRESERVE_WORDS=['root','col']):
	preserveList=[]
	deleteList=[]
	childs=cmds.listRelatives(TOPNAME,c=True,f=True)

	for each in childs:
		CHECK=False
		for EACH_PRESERVE_WORDS in PRESERVE_WORDS:
			if EACH_PRESERVE_WORDS in each:
				CHECK=True
		if CHECK:
			preserveList.append(each)
		else:
			deleteList.append(each)

	if deleteList:
		cmds.delete(deleteList)

	return preserveList

#ATTRIBUTE設定から、ノードを探す
def searchFromATTR(TOPNAME='',ATTR='',VAR=0):
	TEMP=[]
	MESH=cmds.ls(TOPNAME,tr=True,dag=True,l=True)
	for each in MESH:
		if cmds.attributeQuery(ATTR,node=each,ex=True):
			GETVAR = cmds.getAttr(each+'.'+ATTR)
			if GETVAR == VAR:
				TEMP.append(each)
	
	RET=cmds.group(em=True,n='MS_TEMPGROUP_ZZZZ')

	if TEMP:
		cmds.parent(TEMP,RET)
	
	return RET

#Atgiを実体化
def atgiToMesh(PRESERVE_WORDS=['root','col']):
	ATGIS=cmds.ls(sl=True,l=True)
	RET=[]
	LOADED={}

	for EACHSEL in ATGIS:
		TEMP_NAME='MS_atgiTool_temp_xxxx'

		if cmds.objExists(TEMP_NAME):
			cmds.delete(TEMP_NAME)
		#
		PARENT=cmds.listRelatives(EACHSEL,p=True,f=True)

		#選択Atgiロケーターの座標を取得
		TRN=cmds.xform(EACHSEL,q=True,ws=True,t=True)
		ROT=cmds.xform(EACHSEL,q=True,ws=True,ro=True)

		#選択AtgiファイルのMBパスを取得
		cmds.select(EACHSEL,r=True)
		AtgiFile=cmds.getAttr('.atgiFilename')
		AtgiName=AtgiFile.split('/')[-1].split('\\')[-1].split('.')[-2]
		
		#もう読み込んである物をチェック。
		CHECK_LOADED=False
		for EACHKEY in LOADED.keys():
			if AtgiName == EACHKEY:
				CHECK_LOADED=True
				break

		#読み込み処理
		if CHECK_LOADED:
			TEMP_NAME=cmds.duplicate(LOADED[EACHKEY])[0]
			TEMP_NAME=cmds.ls(TEMP_NAME,l=True)
		else:
			FPATH=searchPath(BGMBRoot,AtgiName)
			if not FPATH:
				#ファイル無かったらスキップ
				print 'MBFile not found ! %s'%AtgiName
				continue

			cmds.file(FPATH,i=True,rdn=True,rpr="crash",dns=True,type="mayaBinary",options="v=0",loadReferenceDepth="none",gr=True,gn=TEMP_NAME,shd=True,prompt=False)
			cmds.xform(TEMP_NAME,piv=[0,0,0])
			PRE=deleteChildNodes(TEMP_NAME,PRESERVE_WORDS)
		
		#Translate
		cmds.xform(TEMP_NAME,t=TRN,ws=True)
		cmds.xform(TEMP_NAME,ro=ROT,ws=True)



		#sorting
		if not cmds.objExists('|imported_root'):
			cmds.group(em=True,n='imported_root')

		if not cmds.objExists('|imported_col'):
			cmds.group(em=True,n='imported_col')

		if not cmds.objExists('|imported_atgi'):
			cmds.group(em=True,n='imported_atgi')


		IR=cmds.ls(TEMP_NAME+'|root*')
		if IR:
			#Atgisort
			IA=cmds.ls(IR[0]+'|atgi*')
			if IA:
				IAM=cmds.listRelatives(IA,c=True,f=True)
				if IAM:
					cmds.parent(IAM,'imported_atgi')

			#ModelSort
			IRM=cmds.listRelatives(IR,c=True,f=True)
			if IRM:
				cmds.parent(IRM,'imported_root')

		IC=cmds.ls(TEMP_NAME+'|col*')
		if IC:
			ICM=cmds.listRelatives(IC,c=True,f=True)
			if ICM:
				cmds.parent(ICM,'imported_col')

		cmds.delete(TEMP_NAME)

		
		'''
		#Rename
		RENAMED=cmds.rename(TEMP_NAME,AtgiName+'_01')


		RENPARENT=cmds.listRelatives(RENAMED,p=True,f=True)
		if not PARENT == RENPARENT:
			RENAMED=cmds.parent(RENAMED,PARENT[0])

		RET.append(cmds.ls(RENAMED,dag=True,lf=True,l=True)[0])

		#読み込み済みファイル格納
		if not CHECK_LOADED:
			LOADED.setdefault(AtgiName,cmds.ls(RENAMED,l=True)[0])
		'''

		cmds.delete(EACHSEL)
		
	#cmds.delete(ATGIS)
	
	MELCOM='''
		{
		source "C:/Program Files/Autodesk/Maya2014/scripts/startup/cleanUpScene.mel";
		deleteUnusedNurbsSurfaces();
		deleteEmptyGroups();
		deleteEmptyLayers("Display");
		deleteEmptyLayers("Render");
		deleteUnusedConstraints;
		deleteUnusedPairBlends;
		deleteUnusedSets;
		deleteUnusedExpressions;
		//deleteUnusedInUnusedHierarchy;
		deleteUnknownNodes;
		}
		'''
	mel.eval(MELCOM)
	mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')

	return RET

def atgiToMeshFromAttr(ATTR='',VAR=0):
	ATGIS=cmds.ls(sl=True,l=True)
	RET=[]
	LOADED={}
	TEMP_NAME='MS_atgiTool_temp_xxxx'

	if cmds.objExists(TEMP_NAME):
		cmds.delete(TEMP_NAME)

	for EACHSEL in ATGIS:
		#存在確認
		if not cmds.objExists(EACHSEL):
			continue
		#型チェック
		SHAPE=cmds.listRelatives(EACHSEL,s=True,f=True)
		if not SHAPE:
			continue
		if not cmds.nodeType(SHAPE)=='GraviteAtgiLocatorNode':
			continue

		#親特定
		PARENT=cmds.listRelatives(EACHSEL,p=True,f=True)

		#選択Atgiロケーターの座標を取得
		TRN=cmds.xform(EACHSEL,q=True,ws=True,t=True)
		ROT=cmds.xform(EACHSEL,q=True,ws=True,ro=True)

		#選択AtgiファイルのMBパスを取得
		cmds.select(EACHSEL,r=True)
		AtgiFile=cmds.getAttr('.atgiFilename')
		AtgiName=AtgiFile.split('/')[-1].split('\\')[-1].split('.')[-2]
		
		#もう読み込んである物をチェック。
		CHECK_LOADED=False
		for EACHKEY in LOADED.keys():
			if AtgiName == EACHKEY:
				CHECK_LOADED=True
				break

		#読み込み処理
		if CHECK_LOADED:
			ROOTNAME=cmds.duplicate(LOADED[EACHKEY])[0]
			ROOTNAME=cmds.ls(ROOTNAME,l=True)[0]
		else:
			FPATH=searchPath(BGMBRoot,AtgiName)
			if not FPATH:
				#ファイル無かったらスキップ
				print 'MBFile not found ! %s'%AtgiName
				continue

			#cmds.file(FPATH,i=True,rdn=True,rpr="crash",dns=True,type="mayaBinary",options="v=0",loadReferenceDepth="none",gr=True,gn=TEMP_NAME,shd=['displayLayers','shadingNetworks','renderLayersByName','renderLayersById'],prompt=False)
			cmds.file(FPATH,i=1,rdn=1,rpr="crash",dns=1,type="mayaBinary",options="v=0",loadReferenceDepth="none",gr=1,gn=TEMP_NAME)
			#オブジェクト刈り込み
			ROOTNAME=searchFromATTR(TEMP_NAME,ATTR,VAR)
			cmds.delete(TEMP_NAME)
			#mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
		#
		RENAMED=cmds.rename(ROOTNAME,AtgiName+'_01')
		RENPARENT=cmds.listRelatives(RENAMED,p=True,f=True)
		if not PARENT == RENPARENT:
			RENAMED=cmds.parent(RENAMED,PARENT[0])
		#
		cmds.xform(RENAMED,t=TRN,ws=True)
		cmds.xform(RENAMED,ro=ROT,ws=True)

		RET.append(cmds.ls(RENAMED,dag=True,lf=True,l=True)[0])

		#読み込み済みファイル格納
		if not CHECK_LOADED:
			LOADED.setdefault(AtgiName,cmds.ls(RENAMED,l=True)[0])

		cmds.delete(EACHSEL)
		
	#cmds.delete(ATGIS)
	MELCOM='''
		{
		source "C:/Program Files/Autodesk/Maya2011/scripts/startup/cleanUpScene.mel";
		deleteUnusedNurbsSurfaces();
		deleteEmptyGroups();
		deleteEmptyLayers("Display");
		deleteEmptyLayers("Render");
		deleteUnusedConstraints;
		deleteUnusedPairBlends;
		deleteUnusedSets;
		deleteUnusedExpressions;
		//deleteUnusedInUnusedHierarchy;
		deleteUnknownNodes;
		}
		'''
	#mel.eval(MELCOM)
	return RET


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

def createAtgiNode(SELTRN=''):
	TRN=(0,0,0)
	ROT=(0,0,0)
	if SELTRN:
		PRETRN=cmds.xform(SELTRN,q=True,ws=True,t=True)
		TRN=xFormAverage(PRETRN)
		ROT=cmds.xform(SELTRN,q=True,ws=True,ro=True)
	elif cmds.filterExpand(sm=[31,32,34]):
		PRETRN=cmds.xform(q=True,ws=True,t=True)
		TRN=xFormAverage(PRETRN)
		#ROT=cmds.xform(SELTRN,q=True,ws=True,ro=True)

	NODE = cmds.createNode('GraviteAtgiLocatorNode')
	NODETRNS = cmds.listRelatives(NODE,ap=True,type='transform')
	cmds.xform(NODETRNS,t=TRN)
	cmds.xform(NODETRNS,ro=ROT)
	cmds.select(NODETRNS,r=True)
	return NODE

def atgiCreator(ATGINAME,TRN='',COMP=[]):
	global ATGIPATH
	mods = cmds.getModifiers()
	if (mods & 1) > 0 or COMP:
		#Shiftキーを押しながらで強制ATGI新規作成モード
		NODE=createAtgiNode(TRN)
		ATGINODE = cmds.listRelatives(ad=True,type='GraviteAtgiLocatorNode')[0]

	elif cmds.nodeType(TRN) == 'GraviteAtgiLocatorNode':
		#Atgi生選択中
		ATGINODE = TRN

	elif cmds.nodeType(cmds.listRelatives(TRN,s=True,f=True)) == 'GraviteAtgiLocatorNode':
		#子供がAtgi選択中
		ATGINODE = cmds.listRelatives(TRN,ad=True,type='GraviteAtgiLocatorNode',f=True)[0]

	elif not cmds.nodeType(cmds.listRelatives(TRN,s=True,f=True)) == 'GraviteAtgiLocatorNode':
		#Atgi以外を選択中
		NODE=createAtgiNode(TRN)
		ATGINODE = cmds.listRelatives(ad=True,type='GraviteAtgiLocatorNode')[0]
	else:
		#全てに引っかからない
		return

	ATGIFILEPATH = ATGIPATH+'/'+ATGINAME+'.atgi'
	print ATGINODE
	cmds.setAttr(ATGINODE + '.atgiFilename',ATGIFILEPATH,type='string')

	#ワイヤーフレームカラー
	cmds.color(ATGINODE,ud=2)

	#リネーム処理
	PNODE=cmds.listRelatives(ATGINODE,p=True,f=True)
	NEWATGI=cmds.rename(PNODE,ATGINAME+'_01')
	NEWATGI=cmds.ls(NEWATGI,l=True)

	#ctrlキーが押されているときの処理
	if NEWATGI:
		mods = cmds.getModifiers()
		if (mods & 4) > 0:#+ctrl
			PAR=cmds.listRelatives(EACHSEL,ap=True,f=True)
			cmds.parent(NEWATGI,PAR[0])
			cmds.delete(EACHSEL)
	return NEWATGI

#サムネイルリストからの実行コマンド
def swapAtgiThumbneil(ATGINAME):
	def RET(dummy=''):
		COMP=cmds.filterExpand(sm=[31,32,34])
		if COMP:
			atgiCreator(ATGINAME,COMP=COMP)
			return
		SEL=cmds.ls(sl=True,tr=True,l=True)

		NEWATGI=''
		if not SEL:
			#選択無し
			SEL=[createAtgiNode()]

		for EACHSEL in SEL:
			atgiCreator(ATGINAME,EACHSEL)

	return RET
	
def printString(STR):
	def RET(dummy=''):
		SCROLLFIELDS=['MS_batch_export_atgi_list'
			,'MS_batch_List'
			,'MSG2_atgi_send_to_win_run_ATGIS'
			,'MSG2_check_atgi_located_seachWord'
			,'MSG2_check_hkx_seachWord'
			]
		for each in SCROLLFIELDS:
			if cmds.scrollField(each,ex=True):
				cmds.scrollField(each,e=True,insertText=STR+'\n',insertionPosition=0)
		MS_copyClipboard.copyClipboard(STR)
		print STR
	return RET

#シーン内のAtgiを全部選択
def selectAtgi():
	Nodes=[]
	Shapes=cmds.ls(s=True)
	for each in Shapes:
		if cmds.nodeType(each)=='GraviteAtgiLocatorNode':
			Trn = cmds.listRelatives(ap=True,typ='transform',f=True)
			Nodes.append(Trn[0])
	cmds.select(Nodes,r=True)

#atgiFilename指定選択
def searchAndSelectAtgi():
	SW=cmds.textField('MS_atgiTool_searchAndSelectAtgi',q=True,tx=True)
	ATGIS = cmds.ls(type='GraviteAtgiLocatorNode',l=True)
	Nodes=[]
	for each in ATGIS:
		if cmds.attributeQuery('atgiFilename',node=each,ex=True):
			if SW in cmds.getAttr(each+'.atgiFilename'):
				Trn = cmds.listRelatives(each,ap=True,typ='transform',f=True)
				Nodes.append(Trn[0])

	cmds.select(Nodes,r=True)

#atgiFilenameデッドリンク選択
def searchAtgiDeadLink():
	ATGIS = cmds.ls(type='GraviteAtgiLocatorNode',l=True)
	Nodes=[]
	for each in ATGIS:
		if cmds.attributeQuery('atgiFilename',node=each,ex=True):
			PATH = cmds.getAttr(each+'.atgiFilename')
			if not os.path.exists(PATH):
				Trn = cmds.listRelatives(each,ap=True,typ='transform',f=True)
				Nodes.append(Trn[0])
	if Nodes:
		cmds.select(Nodes,r=True)

###############
# AtgiThumbneil
###############

def refleshAtgiThumbneil(RANDOMSELECT=0,MIN=0,MAX=100):
	
	ATGILIST=createList(RANDOMSELECT=RANDOMSELECT,MIN=MIN,MAX=MAX)

	if not ATGILIST:
		return

	if cmds.gridLayout('MS_atgiTool_atgiThumbneil',q=True,ex=True):
		cmds.deleteUI('MS_atgiTool_atgiThumbneil')
	cmds.gridLayout('MS_atgiTool_atgiThumbneil',nc=4,nr=6,cw=120,ch=125,p='MS_atgiTool_atgiThumbneil_scrollLayout')
	for each in ATGILIST:

		if each in 'MAX':
			cmds.button(l='NEXT',w=30,h=15,bgc=[0.6,0.9,0.6],c=lambda *args:refleshAtgiThumbneil(RANDOMSELECT=RANDOMSELECT,MIN=(MIN+100),MAX=(MAX+100)))
			continue
		if each in 'FOWARD':
			cmds.button(l='FOWARD',w=30,h=15,bgc=[0.6,0.9,0.6],c=lambda *args:refleshAtgiThumbneil(RANDOMSELECT=RANDOMSELECT,MIN=(MIN-100),MAX=(MAX-100)))
			continue

		cmds.columnLayout(adj=True)
		#name
		if '_brk' in each:
			cmds.button(l=each,bgc=[0.9,0.5,0.5],h=16,c=printString(each))
		else:
			cmds.button(l=each,h=16,c=printString(each))

		#壊れモデル名前サムネール用に変更
		THUMNAME=each.replace('_bk','').replace('_db','').replace('_dy','')

		#icon
		ICON=THUMBNEILPATH+'/'+THUMNAME+'.jpg'
		cmds.iconTextButton(style='iconOnly', w=120,h=90,image1=ICON, label=each , c=swapAtgiThumbneil(each))

		#execbutton
		cmds.rowLayout(nc=4,cw4=[30,30,35,20],cl4=['center','center','center','center'],columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0),(4, 'both', 0)])
		cmds.button(l='open',w=30,h=15,bgc=[0.6,0.9,0.6],c=OpenMB(each))
		cmds.button(l='import',w=30,h=15,bgc=[0.6,0.6,0.9],c=ImportMB(each))
		cmds.text('')
		cmds.button(l='x',h=15,bgc=[0.9,0.6,0.6],c=MSG2_assetsUtil.main(each))
		cmds.setParent('..')
		#
		cmds.setParent('..')
	cmds.setParent('..')

###############
# AtgiList
###############
#Atgiを検索したリスト
def createIgnoreWord():
	IGNOREWORDS=['_col.','_sdw.','_low.','_occ.']#無視するワード、;で区切って複数指定可能
	#if not cmds.checkBox('MS_atgiTool_ignoreWords_checkbrk',q=True,v=True):
	IGNOREWORDS=cmds.textField('MS_atgiTool_ignoreWords',q=True,tx=True).split(';')
	return IGNOREWORDS

def getAtgiList(
	SEARCHWORDS=''	#検索語
	,IGNOREWORDS=['_col.','_sdw.','_low.','_occ.','_db.','_bk.','_dy.','_brk_']#無視するワード、;で区切って複数指定可能
	,RANDOMSELECT=0
	,MIN=0
	,MAX=100
	):
	
	IGNOREWORDS=createIgnoreWord()
	RET=[]

	DIR = glob.glob(ATGIPATH+'/*%s*.atgi'%SEARCHWORDS)

	# RANDOMSELECT
	if RANDOMSELECT>0:
		DIR=random.sample(DIR,RANDOMSELECT)

	#RANGE
	if MIN<0:
		MIN=0
	if len(DIR)<=MAX:
		MAX=len(DIR)
	#
	if MIN>0:
		RET.append(u'FOWARD')
	for i in range(MIN,MAX):

		PRE=DIR[i].replace('\\','/')

		#無視するワードチェック
		IGNORECHECK=False
		for eachIW in IGNOREWORDS:
			if not eachIW:
				continue
			elif eachIW in DIR[i] :
				IGNORECHECK=True
				break

		if IGNORECHECK:
			continue

		#壊れ物チェック
		BRK=''
		for eachBKW in  ['_bk.','_db.','_dy.','_md01.']:
			if eachBKW in DIR[i]:
				BRK=PRE.replace('\\','/').replace(eachBKW,'.')

		#壊れ物あったら追加
		if BRK:
			if not BRK in RET:
				RET.append(BRK)

		#かぶりなければリストに追加
		if not PRE in RET:
			RET.append(PRE)

		#表示最大数チェック
		if i>=(MAX-1):
			RET.append(u'MAX')
			break
	return RET

def createList(RANDOMSELECT=0,MIN=0,MAX=100):
	SEARCHWORDS=cmds.textField('MS_atgiTool_searchWord',q=True,tx=True)
	IGNOREWORDS=cmds.textField('MS_atgiTool_ignoreWords',q=True,tx=True).split(';')

	#
	if SEARCHWORDS=='' and RANDOMSELECT==0:
		return False

	ATGILIST=getAtgiList(SEARCHWORDS,IGNOREWORDS,RANDOMSELECT,MIN,MAX)

	ATGINAMELIST=[]
	for each in ATGILIST:
		if each == 'MAX' or  each == 'FOWARD':
			ATGINAMELIST.append(each)

		PRE=re.split('/|\\\\',each)
		if len(PRE)>1:
			ATGINAME=PRE[-1].split('.')[0]
			ATGINAMELIST.append(ATGINAME)

	return ATGINAMELIST


#################
# Store Recall
#################
def store():
	PREFIX='MS_atgiTool'
	CONTROLNAME='MS_atgiTool_searchWord'
	NAME=PREFIX+CONTROLNAME
	if cmds.control(CONTROLNAME,ex=True):
		cmds.optionVar(stringValue=[NAME,cmds.textField(CONTROLNAME,q=True,tx=True)])

def recall():
	PREFIX='MS_atgiTool'
	CONTROLNAME='MS_atgiTool_searchWord'
	NAME=PREFIX+CONTROLNAME
	if cmds.optionVar(exists=NAME):
		cmds.textField(CONTROLNAME,e=True,tx=cmds.optionVar(q=NAME))

###############
# UI
###############

#UIリフレッシュ
def storeAndGetList():
	store()
	refleshAtgiThumbneil()

def atgiUtil():
	cmds.columnLayout(adj=True)
	cmds.text(l='Util',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.gridLayout(nc=4,cw=125)
	cmds.button(l='atgi to mesh',c=lambda *args:atgiToMesh())
	cmds.button(l='atgi to meshLODLow',c=lambda *args:atgiToMeshFromAttr('LodLevelMin',5))
	cmds.button(l='mesh to atgi',c=lambda *args:s1907_atg_change.main.to_atg())
	cmds.button(l='functionalRenamer',c=lambda *args:functionalRenamer_GraviteAtgiLocatorNode())
	cmds.text(l='searchWord')
	cmds.textField('MS_atgiTool_searchAndSelectAtgi',tx='',cc=lambda *args:searchAndSelectAtgi())
	cmds.text(l='')
	cmds.text(l='')
	cmds.button(l='reloadAtgiAll',c=lambda *args:reloadAtgiAll())
	cmds.button(l='searchAtgiDeadLink',c=lambda *args:searchAtgiDeadLink())
	cmds.setParent('..')

#Atgiリストのレイアウト
def atgiList():
	IGNOREWORDS='_col.;_sdw.;_low.;_occ.;'
	cmds.columnLayout(adj=True)
	cmds.text(l='MS_atgiTool',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	#
	cmds.gridLayout(nc=4,cw=100)
	cmds.text(l='SeatchWords',w=50)
	cmds.textField('MS_atgiTool_searchWord',tx='_ms_',cc=lambda *args:storeAndGetList(),w=150)
	cmds.button('bg',c=lambda *args:change_PATH('bg'))
	cmds.button('effect',c=lambda *args:change_PATH('effect'))
	cmds.setParent('..')
	#
	cmds.gridLayout(nc=4,cw=100,ch=16)
	cmds.button(l='random 5',c=lambda *args:refleshAtgiThumbneil(RANDOMSELECT=5))
	cmds.button(l='random 10',c=lambda *args:refleshAtgiThumbneil(RANDOMSELECT=10))
	cmds.button(l='random 25',c=lambda *args:refleshAtgiThumbneil(RANDOMSELECT=25))
	cmds.button(l='random 50',c=lambda *args:refleshAtgiThumbneil(RANDOMSELECT=50))
	cmds.setParent('..')
	#
	cmds.rowLayout(nc=4,cw4=[50,400,50,150])
	cmds.text(l='ignoreWords')
	cmds.textField('MS_atgiTool_ignoreWords',w=400,tx=IGNOREWORDS,cc=lambda *args:storeAndGetList())
	cmds.checkBox('MS_atgiTool_ignoreWords_checkbrk',l='brk',v=False,cc=lambda *args:storeAndGetList())

	cmds.setParent('..')

	cmds.setParent('..')

#Atgiサムネイルのレイアウト
def atgiThumbneil():
	cmds.columnLayout(adj=True)
	cmds.scrollLayout('MS_atgiTool_atgiThumbneil_scrollLayout',h=500)
	cmds.setParent('..')
	cmds.setParent('..')

#外部ツール用レイアウト
def LayoutA():
	cmds.columnLayout('MS_atgiTool_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_atgiTool',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='MS_atgiTool',c=lambda *args:UI())
	cmds.separator()
	cmds.setParent('..')


def UI():
	if cmds.window('MS_atgiTool_window',q=True,ex=True):
		cmds.deleteUI('MS_atgiTool_window')
	cmds.window('MS_atgiTool_window',rtf=True,s=True)
	
	atgiList()
	atgiThumbneil()
	atgiUtil()
	MSG2_atgiLocatorToLocator.LayoutA()
	cmds.showWindow('MS_atgiTool_window')
	recall()
	storeAndGetList()

	