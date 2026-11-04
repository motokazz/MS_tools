# _*_coding:shift-jis_*_
########################################
# ファイル名
#			MS_forceSyncTexturefileFromP4
# 説明
#			
# 作成日\n#			
########################################
import subprocess
import os
import maya.cmds as cmds
import re

tempfile='d:/Mproject/gtools/MS_forceSyncTexturefileFromP4.txt'
newfile='d:/Mproject/gtools/MS_forceSyncTexturefileFromP4_new.txt'


def load(filepath):
	f=open(filepath)
	data=[]
	for row in f:
		data.append(row.decode())
	f.close
	return data

def OPEN_EXPLOROR(DIR,MODE=''):
	DIR=DIR.replace('/','\\')
	
	if DIR[-1]=='\\':#行末がバックスラッシュの場合
		WINDOWS_PATH=DIR
	elif MODE=='file':#
		WINDOWS_PATH
	else :#ファイルパスの場合
		WINDOWS_PATH='\\'.join(DIR.split('\\')[:-1])
	
	os.popen('explorer "%s"' % WINDOWS_PATH)


def save(row,filepath):
	f=open(filepath,'w')#'r'読み込み：'w'書き込み：'a'追記：'+'読み書き両方' 't'テキストモード：'b'バイナリーモード
	for each in row:
		f.write(each.encode('shift-jis'))
		print each
	f.close()
	
def UNIQUE(LIST):
	#リストから重複要素を取り除く。
	return sorted(set(LIST),key=LIST.index)
	
def searchClient(list):
	for each in list:
		if 'Client:	' in each:
			ret=each.replace('Client:','')
			ret=ret.replace(' ','')
			ret=ret.replace('\n','')
			ret=ret.replace('\r','')
			ret=ret.replace('\t','')
			return ret
	return False
	
def cmdline(cmdline):
	logstr=[]
	p=subprocess.Popen(cmdline, shell=True, stdin=subprocess.PIPE,
						 stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
						 )
	(stdouterr, stdin) = (p.stdout, p.stdin)  # 
	print "-" * 80  # 区切り表示(開始)
	while True:
		line = stdouterr.readline()  # 改行を含んで行を読み込む
		if not line:
			break
		print line.rstrip()  # 後ろの改行を消して出力
		logstr.append(line.rstrip())
	print "-" * 80  # 区切り表示(終了)
	logstr.append("-" * 80)
	ret = p.wait()  # 戻り値が入る
	print "Return code: %d" % ret
	logstr.append("Return code: %d" % ret)
	return logstr
	
def P4backRevision(PATH):
	#リビジョンを指定数戻す
	backRev=cmds.intField('MS_forceSyncTexturefileFromP4_Rev',q=True,v=True)
	rev=P4headRev(PATH)
	if re.search('\D',str(rev)):
		return 'nothing'
	getRev= int(rev)-backRev
	if getRev<1:
		getRev=1
	progress(['back Revision to'+str(getRev)])
	return getRev
	
def P4headRev(PATH=''):
	#最新リビジョンチェック
	if not PATH:
		return
	msg=cmdline("p4 fstat -T \"headRev\" %s"%PATH)
	progress(msg)
	rev=msg[0].split()[-1]
	return rev
	

def P4newWorkSpace(FTN_PATHLIST=[]):
	#ワークスペースにパスを追加
	if not FTN_PATHLIST:
		return
	
	#p4workspace 2 tempfile
	msg=cmdline("p4 client -o > %s"%tempfile)
	progress(msg)
	datas=load(tempfile)
	
	#ditectClient
	client=searchClient(datas)
	if not client:
		print 'can`t Find Clients Name!'
		return
	
	#replaceWorkspaceMapping
	newpath=[]
	renamedUniques=[]
	for each in FTN_PATHLIST:
		#
		depoPath=each
		#
		clientPath=each.replace('//mproject','//'+client)
		clientPath=clientPath.replace('//Mproject','//'+client)
		clientPath=clientPath.replace('//MProject','//'+client)
		#
		newpath.append('\t'+depoPath+' '+clientPath+'\r\n')
		renamedUniques.append(each.replace('//mproject','//Mproject'))
	newdata=datas+newpath
	save(newdata,newfile)
	
	msg=cmdline("p4 client -i < %s"%newfile)
	progress(msg)
	
	return renamedUniques
	
	
def P4workSpaceRevert():
	#ワークスペースを元に戻す
	#P4 revert WorkspaceMapping
	msg=cmdline("p4 client -i < %s"%tempfile)
	progress(msg)
	
	
def P4forceSync(FTN_PATHLIST=[]):
	#強制ワークスペース追加と取得
	if not FTN_PATHLIST:
		return
	
	renamedUniques=P4newWorkSpace(FTN_PATHLIST)
	
	#P4sync
	for each in renamedUniques:
		each=each.replace('//','d:/')
		rev=P4backRevision(each)#リビジョン取得
		if rev=='nothing':
			progress(['Cant find path.'])
			continue
		msg=cmdline("p4 sync -s %s"%each+'#'+str(rev))
		progress(msg)
		
	P4workSpaceRevert()
	
	return 
	
def P4revCheck(FTN_PATHLIST=[]):
	#リビジョンチェック
	if not FTN_PATHLIST:
		return
	
	renamedUniques=P4newWorkSpace(FTN_PATHLIST)
	
	#P4sync
	for each in renamedUniques:
		each=each.replace('//','d:/')
		P4headRev(each)
		
	P4workSpaceRevert()
	
	return 
	
def invailedPathFixer(path):
	#fix invailedString
	path=path.replace('\\','/')
	path=path.replace('//','/')
	
	#fix drive
	path=path.replace('d:','/')
	path=path.replace('D:','/')
	path=path.replace('v:','//Mproject')
	path=path.replace('V:','//Mproject')
	
	#fix rootpath
	path=path.replace('/mproject','/Mproject')
	path=path.replace('/mProject','/Mproject')
	path=path.replace('/MProject','/Mproject')
	#fix extension
	path=path.replace('.jpg','.tif')
	
	return path
	
def pathFixMirrorTexture(path):
	path=path.replace('V:','d:/Mproject')
	path=path.replace('v:','d:/Mproject')
	path=path.replace('.jpg','.tif')
	return path
	
def syncFtn(MODE='all'):
	progressNew()
	
	nodes=[]
	if MODE=='all':
		nodes=cmds.ls(type='file')
	elif MODE=='selected':
		nodes=cmds.ls(sl=True,type='file')
	elif MODE=='textField':
		nodes=getPath(q=True)
	
	if not nodes:
		progress(['Not found fileTextureNodes','=======FINISH======='])
		return
	
	#createNewlist
	texpaths=[]
	for each in nodes:
		try:
			ftn=cmds.getAttr(each+'.fileTextureName')
			ftn=invailedPathFixer(ftn)
			texpaths.append(ftn)
		except:
			continue
			
	uniques=UNIQUE(texpaths)
	
	P4forceSync(uniques)
	
	#reloadTextures
	for each in nodes:
		ftn=cmds.getAttr(each+'.fileTextureName')
		#for yamabe tool
		ftn=pathFixMirrorTexture(ftn)
		cmds.setAttr(each+'.fileTextureName',ftn,type='string')
		
	progress(['=======FINISH======='])


def progressNew():
	if cmds.textScrollList('MS_forceSyncTexturefileFromP4_log',q=True,ex=True):
		cmds.deleteUI('MS_forceSyncTexturefileFromP4_log')
	cmds.textScrollList('MS_forceSyncTexturefileFromP4_log',p='MS_forceSyncTexturefileFromP4_log_parent')
	cmds.textScrollList('MS_forceSyncTexturefileFromP4_log',e=True,append='=== forceSyncP4 start ===')
	
	
def progress(MSG=[]):
	for each in MSG:
		cmds.textScrollList('MS_forceSyncTexturefileFromP4_log',e=True,append=each)
	
def getPath(q=False):
	if q:
		str=cmds.textField('MS_forceSyncTexturefileFromP4_pathField',q=True,tx=True)
		if str:
			ret=str.split(',')
			return ret
		else:
			return []
	node=cmds.ls(sl=True,type='file')
	
	list=[]
	if node:
		for each in node:
			list.append(cmds.getAttr(each+'.fileTextureName'))
	cmds.textField('MS_forceSyncTexturefileFromP4_pathField',e=True,tx=','.join(list))
	
	
def layoutA(
	LABEL='MS_forceSyncTexturefileFromP4'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.rowLayout(nc=4)
	cmds.button(w=60,h=60,l=u'Force\nP4 Sync\nTextures\nAll',bgc=[0.7,0.8,0.7],c=lambda *args:syncFtn())
	cmds.button(w=60,h=60,l=u'Force\nP4 Sync\nTextures\nSelected',bgc=[0.7,0.8,0.8],c=lambda *args:syncFtn(MODE='selected'))
	
	cmds.columnLayout()
	cmds.text(l='backRevision')
	cmds.intField('MS_forceSyncTexturefileFromP4_Rev',w=60,v=0)
	cmds.setParent('..')
	
	cmds.setParent('..')
	
	cmds.separator(w=210)
	
	cmds.rowLayout(nc=2)
	cmds.button(w=60,h=60,l=u'Force\nP4 Sync\nTextures\nTextField',bgc=[0.7,0.7,0.8],c=lambda *args:syncFtn(MODE='textField'))
	cmds.columnLayout()
	cmds.text(l='path')
	cmds.textField('MS_forceSyncTexturefileFromP4_pathField',w=150)
	cmds.button(l='getPath',bgc=[0.7,0.7,0.7],w=150,h=20,c=lambda *args:getPath())
	cmds.setParent('..')
	
	cmds.setParent('..')
	cmds.separator(w=210)
	
	cmds.columnLayout('MS_forceSyncTexturefileFromP4_log_parent')
	cmds.textScrollList('MS_forceSyncTexturefileFromP4_log',w=210)
	cmds.setParent('..')
	cmds.button(l='open Mirror Folder',bgc=[0.6,0.8,0.9],w=210,c=lambda *args:OPEN_EXPLOROR(DIR='v:/graphic/bg/texture/'))
	cmds.separator(w=210)
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_forceSyncTexturefileFromP4_main_window',q=True,ex=True):
		cmds.deleteUI('MS_forceSyncTexturefileFromP4_main_window')
	cmds.window('MS_forceSyncTexturefileFromP4_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_forceSyncTexturefileFromP4_main_window')
	cmds.window('MS_forceSyncTexturefileFromP4_main_window',e=True,w=217,h=400)
	

