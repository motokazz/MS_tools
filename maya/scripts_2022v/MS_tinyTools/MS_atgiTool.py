# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_atgiTool.py
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

#川野さん、お借りしてます！
import s1907_atg_change.main

#execCheckList
import s2000_tools.MS_lib.MSG2_execCheck as MSG2_execCheck
reload(MSG2_execCheck)
MSG2_execCheck.execCheckSafe('MS_atgiTool')#execCheckList

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
		cmds.file(FPATH,i=True,options='v=0',f=True)
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

#シーン内の全ATGIをリロード
def reloadAtgi():
	ATGI=cmds.ls(type='GraviteAtgiLocatorNode',l=True)
	for each in ATGI:
		mel.eval('AEGraviteAtgiReloadCmd %s.atgiFilename;'%each)




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
	TEMP_NAME='MS_atgiTool_temp_xxxx'
	SEL=cmds.ls(sl=True,l=True)
	for EACHSEL in SEL:
		TEMP_NAME='MS_atgiTool_temp_xxxx'
		PARENT=cmds.listRelatives(EACHSEL,p=True,f=True)
		#
		TRN=(0,0,0)
		ROT=(0,0,0)
		if SEL:
			TRN=xFormAverage(cmds.xform(EACHSEL,q=True,ws=True,t=True))
			ROT=cmds.xform(EACHSEL,q=True,ws=True,ro=True)

		#
		if not cmds.nodeType(EACHSEL)=='GraviteAtgiLocatorNode':
			EACHSEL=cmds.listRelatives(EACHSEL,type='GraviteAtgiLocatorNode')[0]
		AtgiFile=cmds.getAttr(EACHSEL+'.atgiFilename')
		AtgiName=AtgiFile.split('/')[-1].split('||')[-1].split('.')[-2]
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
	return NODETRNS

#Atgiの中身を書き換える
def swapAtgi():
	SEL=cmds.ls(sl=True,l=True)
	global ATGIPATH
	ATGINAME=cmds.textScrollList('MS_atgiTool_atgiList',q=True,si=True)[0]
	ATGINODE = cmds.listRelatives(ad=True,type='GraviteAtgiLocatorNode')
	ATGIFILEPATH = ATGIPATH+'/'+ATGINAME+'.atgi'
	cmds.setAttr(ATGINODE[0] + '.atgiFilename',ATGIFILEPATH,type='string')
	cmds.rename(ATGINODE[0],ATGINAME)

#サムネイルリストからの実行コマンド
def swapAtgiThumbneil(ATGINAME):
	def RET(dummy=''):
		global ATGIPATH
		SEL=cmds.ls(sl=True,l=True)
		NEWATGI=''
		if not SEL:
			#選択無し
			createAtgiNode()
			ATGINODE = cmds.listRelatives(ad=True,type='GraviteAtgiLocatorNode')

		elif not cmds.nodeType(cmds.listRelatives(SEL,s=True,f=True)) == 'GraviteAtgiLocatorNode':
			#Atgi以外を選択中
			createAtgiNode()
			ATGINODE = cmds.listRelatives(ad=True,type='GraviteAtgiLocatorNode')
		else:
			#Atgi選択中
			ATGINODE = SEL
		ATGIFILEPATH = ATGIPATH+'/'+ATGINAME+'.atgi'
		for each in ATGINODE:
			cmds.setAttr(each + '.atgiFilename',ATGIFILEPATH,type='string')
			cmds.color(each,ud=2)
			PNODE=cmds.listRelatives(each,p=True,f=True)
			NEWATGI=cmds.rename(PNODE,ATGINAME+'_01')
		if NEWATGI:
			mods = cmds.getModifiers()
			if (mods & 4) > 0:#+ctrl
				PAR=cmds.listRelatives(SEL[0],ap=True,f=True)
				cmds.parent(NEWATGI,PAR[0])
				cmds.delete(SEL)


	return RET
	
def searchPath(searchPath,searchFile=''):#指定パスからの相対パスを返す　例）module/MS_primitives.py
	for (root,dir,files) in os.walk(searchPath):
		for f in files:
			fname=f.split('.')[0]
			if searchFile == fname:
				root=root.replace('\\','/').replace('//','/')
				return root+'/'+f
	return ''


###############
# AtgiSumbneil
###############

def refleshAtgiThumbneil():
	ATGILIST=createList()
	if cmds.gridLayout('MS_atgiTool_atgiThumbneil',q=True,ex=True):
		cmds.deleteUI('MS_atgiTool_atgiThumbneil')
	cmds.gridLayout('MS_atgiTool_atgiThumbneil',nc=4,nr=6,cw=120,ch=125,p='MS_atgiTool_atgiThumbneil_scrollLayout')
	for each in ATGILIST:
		cmds.columnLayout()
		#name
		cmds.text(l=each)

		#壊れモデル名前サムネール用に変更
		THUMNAME=each.replace('_bk','').replace('_db','').replace('_dy','')
		#icon
		cmds.iconTextButton(style='iconOnly', w=120,h=90,image1=THUMBNEILPATH+'/'+THUMNAME+'.jpg', label=each , c=swapAtgiThumbneil(each))
		#execbutton
		cmds.rowLayout(nc=2)
		cmds.button(l='open',w=55,h=15,bgc=[0.6,0.9,0.6],c=OpenMB(each))
		cmds.button(l='import',w=55,h=15,bgc=[0.6,0.6,0.9],c=ImportMB(each))
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
	if not cmds.checkBox('MS_atgiTool_ignoreWords_checkbrk',q=True,v=True):
		IGNOREWORDS.append('_db.')
		IGNOREWORDS.append('_bk.')
		IGNOREWORDS.append('_dy.')
		IGNOREWORDS.append('_brk_')
	return IGNOREWORDS

def getAtgiList(
	SEARCHWORDS=''	#検索語
	,IGNOREWORDS=['_col.','_sdw.','_low.','_occ.','_db.','_bk.','_dy.','_brk_']#無視するワード、;で区切って複数指定可能
	):
	IGNOREWORDS=createIgnoreWord()
	RET=[]
	DIR = glob.glob(ATGIPATH+'/*%s*.atgi'%SEARCHWORDS)
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
		#
		PRE=eachDIR.replace('\\','/')
		RET.append(PRE)

	return RET

def createList():
	SEARCHWORDS=cmds.textField('MS_atgiTool_searchWord',q=True,tx=True)
	IGNOREWORDS=cmds.textField('MS_atgiTool_ignoreWords',q=True,tx=True).split(';')
	ATGILIST=getAtgiList(SEARCHWORDS,IGNOREWORDS)
	ATGINAMELIST=[]
	for each in ATGILIST:
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

#Atgiリストのレイアウト
def atgiList():
	IGNOREWORDS='_col.;_sdw.;_low.;_occ.;_db.;_bk.;_dy.;_brk_'
	cmds.columnLayout(adj=True)
	cmds.text(l='MS_atgiTool',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	#
	cmds.rowLayout(nc=2,cw2=[50,150])
	cmds.text(l='SeatchWords')
	cmds.textField('MS_atgiTool_searchWord',tx='_ms_',cc=lambda *args:storeAndGetList())
	cmds.setParent('..')
	#
	cmds.rowLayout(nc=4,cw4=[50,150,50,150])
	cmds.text(l='ignoreWords')
	cmds.textField('MS_atgiTool_ignoreWords',tx=IGNOREWORDS,cc=lambda *args:storeAndGetList())
	cmds.checkBox('MS_atgiTool_ignoreWords_checkbrk',l='brk',v=False,cc=lambda *args:storeAndGetList())

	cmds.setParent('..')

	cmds.button(l='atgi to mesh',c=lambda *args:atgiToMesh())
	cmds.button(l='mesh to atgi',c=lambda *args:s1907_atg_change.main.to_atg())

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
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	atgiList()
	atgiThumbneil()

	cmds.showWindow('MS_tools_window')
	recall()
	storeAndGetList()

	