# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_LODTool.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm

import subprocess
import os
import shutil

#import gravite_ui

import MSG2_LODreduce
reload(MSG2_LODreduce)

import MSG2_LODPreview
reload(MSG2_LODPreview)

import MS_polyUnite
reload(MS_polyUnite)

import MS_BBfilter
reload (MS_BBfilter)




#################
# LOAD PLUGINS
#################
'''
def PLUGINS():
	RET=[
		'Gravite2Shader.mll'
		,'GraviteLocatorNode.mll'
		,'GraviteMayaToAtgi.mll'
		,'hctMayaSceneExport.mll'
	]
	return RET

for each in PLUGINS():
	if not cmds.pluginInfo(each,q=True,loaded=True):
		cmds.loadPlugin(each)
'''

#################
# DEFINES
#################

#WorkFolderPath
TEMP_WORK_FOLDER = 'D:/work'
TEMP_FILE_NAME = TEMP_WORK_FOLDER+'/MS_LODTool_temp.mb'
TEMP_LOD_TEXTURE_FILE_PATH = TEMP_WORK_FOLDER+'/MS_LODTool_temp'

#G2Path
LOD_TEXTURE_EXPORT_PATH='D:/Projects/Gravite2/graphic/bg/textures/_lod'
BGMBRoot = 'D:/Projects/Gravite2/graphic/bg/scenes'

ASSETS_PATH='D:/Projects/Gravite2/assets/common/texture'
ASSETS_LOCAL_PATH='D:/Projects/Gravite2/assets_local'

#################
# CHECK TEMP WORK FOLDER
#################

if not os.path.exists(TEMP_WORK_FOLDER):
	os.mkdir(TEMP_WORK_FOLDER)
	cmds.confirmDialog(m=u'このツールを動かすのに必要なフォルダ\n　%s\nを作成しました。'%TEMP_WORK_FOLDER)



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

def P4headRev(PATH=''):
	#最新リビジョンチェック
	if not PATH:
		return
	msg=cmdline("p4 fstat -T \"headRev\" %s"%PATH)
	rev=msg[0].split()[-1]

	if rev=='file(s).':#存在しないファイルはFalseを返す。
		rev=False
	return rev
	
def P4Status(PATH=''):
	#ローカルファイルかどうかチェック
	if not P4headRev(PATH):
		return 'localFile'

	#ユーザーネーム取得
	userName=P4Info()

	#チェックアウト情報
	line=cmdline('p4 opened -a %s'%PATH)
	for eachline in line:
		if  userName in eachline:
			return 'checkout'
		elif '@' in eachline:
			return 'locked'
		else:
			return 'notcheckout'

def P4CheckOut(PATHLIST=[]):
	checkFlag=True #正常にチェックアウト出来ないファイルがあったらFalse
	for each in PATHLIST:
		STRING=each.replace(' ','')+'...'
		#P4Check
		P4Check=P4Status(each)
		
		if P4Check=='localFile':#ローカルにしか存在しないファイル
			continue

		elif P4Check=='checkout': #チェックアウトされている
			continue

		elif P4Check=='locked': #誰かがロックしている
			cmds.confirmDialog(m='file is locked',button=['confirm'],defaultButton='confirm')
			checkFlag=False
			continue

		else: #チェックアウトされていない
			DS=cmds.confirmDialog(m='%s\nDo you want P4 CheckOut?'%each,button=['yes','No'],defaultButton='yes',cancelButton='No',dismissString='No')
			if DS=='No':
				checkFlag=False
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
	
	return checkFlag
	#P4Status()
	
#################
# ATGI
#################
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
	return False

'''
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
'''

#指定ノードを消す。
def deleteChildNodes(TOPNAME='',):
	preserveList=[]
	childs=cmds.listRelatives(TOPNAME,c=True,f=True)
	for each in childs:
		name=each.split('|')[-1]
		if 'root' in name:
			childs.remove(each)
			preserveList.append(each)

	if childs:
		cmds.delete(childs)
	return preserveList
	
#Atgiを実体化
def atgiToMesh(ATGIS=[]):
	RET=[]
	LOADED={}
	TEMP_NAME='MS_atgiTool_temp_xxxx'

	if cmds.objExists(TEMP_NAME):
		cmds.delete(TEMP_NAME)

	for EACHSEL in ATGIS:
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
			ROOTNAME=cmds.ls(ROOTNAME,l=True)
		else:
			FPATH=searchPath(BGMBRoot,AtgiName) 
			if not FPATH:
				#ファイル無かったらスキップ
				print 'MBFile not found ! %s'%AtgiName
				continue

			cmds.file(FPATH,i=True,rdn=True,rpr="crash",dns=True,type="mayaBinary",options="v=0",loadReferenceDepth="none",gr=True,gn=TEMP_NAME,shd=True,prompt=False)
			PRE=deleteChildNodes(TEMP_NAME)
			ROOTNAME=cmds.parent(PRE,w=True)
			cmds.delete(TEMP_NAME)
			mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')

		#リネームと親子付け
		RENAMED=cmds.rename(ROOTNAME[0],AtgiName+'_01')
		RENPARENT=cmds.listRelatives(RENAMED,p=True,f=True)
		if not PARENT == RENPARENT:
			RENAMED=cmds.parent(RENAMED,PARENT[0])

		#移動
		cmds.xform(RENAMED,t=TRN,ws=True)
		cmds.xform(RENAMED,ro=ROT,ws=True)

		#戻り値を作る
		RET.append(cmds.ls(RENAMED,s=True,dag=True,lf=True,l=True)[0])

		#読み込み済みファイル格納
		if not CHECK_LOADED:
			LOADED.setdefault(AtgiName,cmds.ls(RENAMED,l=True)[0])

		cmds.delete(EACHSEL)
		
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
	#cmds.delete(ATGIS)
	return RET

#################
# UTIL
#################
def shaderChanger(shdName='G2_BG_Main',FROM ='selection'):
	RET=[]

	#### selectionmode ###
	if FROM =='selection':
		nodes=cmds.ls(sl=True,l=True)
	elif FROM =='allGBG':
		nodes=cmds.ls(type='G_BG_Main',l=True)
	elif FROM =='allG2BG':
		nodes=cmds.ls(type='G2_BG_Main',l=True)
	elif FROM =='alllambert':
		nodes=cmds.ls(type='lambert',l=True)

	### core ###
	for each in nodes:

		if each == 'lambert1':
			continue

		success=False
		con = cmds.listConnections(each+'.color')
		sg = cmds.listConnections(each+'.outColor')
		if sg:#空のシェーディンググループ対応
			sgs = cmds.sets(sg[0],q=True)
		else:
			continue
		#
		shd = cmds.shadingNode(shdName,asShader=True)

		certified=[]#発見できないオブジェクトを排斥したリストを作成する
		if sgs:
			for eachsgs in sgs:
				if cmds.objExists(eachsgs):
					certified.append(eachsgs)
				else:
					print each

			cmds.select(certified,r=True)
			try:
				cmds.hyperShade(a=shd)
				RET.append(shd)
				#RET+='success : '+each+' to '+shd+'\n'
			except:
				#RET+='failed : '+each+' to '+shd+'\n'
				pass

			try:
				cmds.connectAttr(con[0]+'.outColor',shd+'.color')
				cmds.connectAttr(shd+'.outColor',sg[0]+'.surfaceShader')
				success=True
				
			except:
				pass

			#
			if shdName=='G2_BG_Main' and cmds.nodeType(each)=='G_BG_Main':
				try:
					copyParamGToG2(each,shd)
				except:
					pass


	return RET

#################
# TEXTURE
#################
#LODテクスチャをアサイン、既にテクスチャがある場合、リロード
def assignLodMaterialTexture(TARGETMESH=[],LOD_TEXTURE_FILE_PATH=''):
	#すでにLODテクスチャを使ってるかチェック
	def checkLODTextureExist(LOD_TEXTURE_FILE_PATH=''):
		FTN=cmds.ls(type='file')
		for EACH in FTN:
			FTNN=cmds.getAttr(EACH+'.fileTextureName')
			if FTNN==LOD_TEXTURE_FILE_PATH:
				cmds.setAttr(EACH+".fileTextureName",LOD_TEXTURE_FILE_PATH,type="string")
				return True
		return False

	if checkLODTextureExist(LOD_TEXTURE_FILE_PATH):
		return False

	shd = cmds.shadingNode('G2_BG_Main',asShader=True)
	FTN=cmds.shadingNode('file',asTexture=True)
	cmds.setAttr(FTN+'.fileTextureName',LOD_TEXTURE_FILE_PATH,type='string')
	cmds.connectAttr(FTN+'.outColor',shd+'.color')
	#
	cmds.select(TARGETMESH,r=True)
	cmds.hyperShade(a=shd)

#テンポラリ出力したテクスチャを正規のフォルダにコピー
def copyTextureToReg(CURRENT_SCENE):
	
	NAME=CURRENT_SCENE.split('/')[-1].split('.')[0]
	#ローカルファイルチェック
	LOD_TEXTURE_FILE_PATH=LOD_TEXTURE_EXPORT_PATH+'/lod_'+NAME+'_c'
	if not P4CheckOut([LOD_TEXTURE_FILE_PATH+'.tif']):
		return 'CANCELED ! : %s :TextureFileCheckoutFailed'%LOD_TEXTURE_FILE_PATH+'.tif'
	shutil.copyfile(TEMP_LOD_TEXTURE_FILE_PATH+'.tif',LOD_TEXTURE_FILE_PATH+'.tif')

	'''
	#ASSETSファイルチェック
	LOD_TEXTURE_ASSETS_FILE_PATH=ASSETS_PATH+'/lod_'+NAME+'_c'
	if not P4CheckOut([LOD_TEXTURE_FILE_PATH+'.tif']):
		return 'CANCELED ! : %s :TextureFileCheckoutFailed'%LOD_TEXTURE_FILE_PATH+'.tif'
	shutil.copyfile(TEMP_LOD_TEXTURE_FILE_PATH+'.tif',LOD_TEXTURE_ASSETS_FILE_PATH+'.tif')
	'''

	TEXTURES=cmds.ls(type='file')
	for each in TEXTURES:
		if cmds.getAttr(each+'.fileTextureName')==(TEMP_LOD_TEXTURE_FILE_PATH+'.tif'):
			cmds.setAttr(each+'.fileTextureName',LOD_TEXTURE_FILE_PATH+'.tif',type='string')

#################
# CHECKER
#################
#シーン更新状況チェック
def sceneModfiedCheck():
	#scene modfied check
	if cmds.file(q=True,amf=True):
		DS=cmds.confirmDialog(m='Current Scene is Changed!\nPlease save scene.',button=['Save','No'],defaultButton='yes',cancelButton='No',dismissString='No')
		if DS=='No':
			DSB=cmds.confirmDialog(m='Continue?\n If continue current work is lost.',button=['Yes','No'],defaultButton='yes',cancelButton='No',dismissString='No')
			if DSB=='No':
				return False
			else:
				return True
		else:
			cmds.file(save=True,options='v=0')
			return True
	return True

#################
# MAIN
#################
	#バウンディングボックスからテクスチャサイズ取得
def getTextureSizeFromBB(TARGET):
	BB=MS_BBfilter.BBMesure_new(TARGET)
	if 	 BB<100000000:TEX_RES=64
	elif BB<10000000000:TEX_RES=128
	elif BB<1000000000000:TEX_RES=256
	elif BB<100000000000000:TEX_RES=512
	else :TEX_RES=1024
	return TEX_RES

def ditectSourceAndTarget(SOURCES_LOD_MAX=4):
	SEL = cmds.ls('root',tr=True,dag=True,l=True)
	SOURCES=[]
	TARGETS=[]
	for each in SEL:
		if not cmds.listRelatives(each,s=True):
			continue
		if cmds.attributeQuery('LodLevelMax',n=each,ex=True):
			if cmds.getAttr(each+'.LodLevelMax')<=SOURCES_LOD_MAX:
				SHAPE=cmds.listRelatives(each,s=True)
				SOURCES.extend(SHAPE)
			if cmds.getAttr(each+'.LodLevelMin')>=(SOURCES_LOD_MAX+1):
				SHAPE=cmds.listRelatives(each,s=True)
				TARGETS.extend(SHAPE)
	return SOURCES,TARGETS

def MS_surfaceSampler(TARGETS=[],SOURCES=[],FILEPATH='D:/work/baked_c',MAPWIDTH=512,MAPHEIGHT=512,SEARCH_OFFSET=0,MAX_SEARCH_DISTANCE=0):
	cmds.surfaceSampler(
		target=TARGETS
		,uvSet='map1'
		,searchOffset=SEARCH_OFFSET
		,maxSearchDistance=MAX_SEARCH_DISTANCE
		,searchCage=''
		,source=SOURCES
		,mapOutput='diffuseRGB'
		,mapWidth=MAPWIDTH
		,mapHeight=MAPHEIGHT
		,max=1
		,mapSpace='tangent'
		,mapMaterials=1
		,shadows=1
		,filename=FILEPATH
		,fileFormat='tif'
		,superSampling=1
		,filterType=0
		,filterSize=3
		,overscan=100
		,searchMethod=0
		,useGeometryNormals=1
		,ignoreMirroredFaces=0
		,flipU=0
		,flipV=0
		)

def main(MAPWIDTH=512,MAPHEIGHT=512,ATGI_ENABLE=False,SOURCES_LOD_MAX=4):

	CURRENT_SCENE=cmds.file(q=True,sn=True)

	#テンポラリセーブ
	cmds.file( rename=TEMP_FILE_NAME )
	cmds.file(save=True,options='v=0')

	#SAVEしてから作業
	SOURCES,TARGETS = ditectSourceAndTarget(SOURCES_LOD_MAX)

	#素材チェック
	if not SOURCES or not TARGETS:
		cmds.confirmDialog(m='WARRNING !\ncant find SOURCE or TARGET.')
		#シーンを元のパス情報に戻す
		cmds.file( rename=CURRENT_SCENE )
		return 'ERROR ! : %s :cant find SOURCE or TARGET'%CURRENT_SCENE

	#ATGIをコンバート
	if ATGI_ENABLE:
		SHAPE = cmds.ls('root',type='GraviteAtgiLocatorNode',dag=True,lf=True,l=True)
		if SHAPE:
			ATGIS = cmds.listRelatives(SHAPE,ad=True,p=True,f=True)
			ATGI_FORM_MESH=atgiToMesh(ATGIS)
			SOURCES.extend(ATGI_FORM_MESH)

	#シェーダーチェンジ
	NEW = shaderChanger(shdName='lambert',FROM ='allG2BG')


	#テクスチャベイクする。
	SEARCH_OFFSET=cmds.floatField('MSG2_LODTool_SEARCH_OFFSET',q=True,v=True)
	MAX_SEARCH_DISTANCE=cmds.floatField('MSG2_LODTool_MAX_SEARCH_DISTANCE',q=True,v=True)
	try:
		MS_surfaceSampler(TARGETS,SOURCES,TEMP_LOD_TEXTURE_FILE_PATH,MAPWIDTH,MAPHEIGHT,SEARCH_OFFSET,MAX_SEARCH_DISTANCE)
	except:
		print 'ERROR : MS_surfaceSampler'
		print TARGETS
		print SOURCES

	#SAVEしておいたSCENEを呼び出す。
	cmds.file(TEMP_FILE_NAME,o=True,options='v=0',f=True)

	#シーンを元のパス情報に戻す
	cmds.file( rename=CURRENT_SCENE )
	
	#開いたシーンに対して、作ったテクスチャを刺す。
	assignLodMaterialTexture(TARGETMESH=TARGETS,LOD_TEXTURE_FILE_PATH=TEMP_LOD_TEXTURE_FILE_PATH+'.tif')

	#テンポラリ出力のテクスチャを正規フォルダにコピー
	copyTextureToReg(CURRENT_SCENE)
	
	#gravite_uiもし開いてるとテンポラリ出力しちゃうので再構築
	#################
	# 拝借gravite_ui
	#################
	# ウィンドウのハンドル名
	#TOPWINDOW_HANDLE_NAME = 'GraviteExportUIWindow'
	#if pm.window(TOPWINDOW_HANDLE_NAME, exists=True):
	#	gravite_ui.open_ui()

	return 'SUCCESS ! : %s '%CURRENT_SCENE
def removeExceptionsFromSelection(OBJS):
	RET=[]
	for each in OBJS:
		if cmds.polyColorSet(each,q=True,acs=True): #ColorSetあり
			continue
		if 'pre_atgi' in each: #pre_atgi
			continue
		if 'keep_conbine' in each:
			continue
		RET.append(each)
	return RET

def super():
	#root low　があったら消す。
	if cmds.objExists('|root|low'):
		cmds.delete('|root|low')

	SEL=removeExceptionsFromSelection(cmds.ls('root',tr=True,dag=True,l=True))
	
	if not SEL:
		cmds.confirmDialog(m=u'SUPER：セパレート対象が見つかりませんでした')
		return 
	cmds.select(SEL,r=True)

	#root以下のモデルをセパレート
	TEMP=MS_polyUnite.main(MS_polyUnite.MS_polySeparate)
	
	#root以下のモデルをバウンディングボックスでグループ分けしてコンバイン、LOD設定付加
	if not MS_BBfilter.main():
		cmds.confirmDialog(m=u'SUPER：BBグループ作成対象が見つかりませんでした')
		return 

	#LOD設定を元にリデュースモデルを作成
	REDUCED = MSG2_LODreduce.main()
	if not REDUCED:
		cmds.confirmDialog(m=u'SUPER：ローメッシュ作成対象が見つかりませんでした')
		return

	#LODテクスチャ焼きこみ、テンポラリ出力
	TEX_RES=getTextureSizeFromBB(REDUCED)
	main(TEX_RES,TEX_RES)


#################
# UI
#################
def LayoutA():
	cmds.columnLayout('MSG2_LODTool_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_LOD_bake',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	#MeshLODReduce
	cmds.text(l='meshLOD')
	cmds.gridLayout(nc=6)
	cmds.button(l='64',bgc=[0.7,0.8,0.7],c=lambda *args:main(MAPWIDTH=64,MAPHEIGHT=64,ATGI_ENABLE=True,SOURCES_LOD_MAX=4))
	cmds.button(l='128',bgc=[0.7,0.8,0.7],c=lambda *args:main(MAPWIDTH=128,MAPHEIGHT=128,ATGI_ENABLE=True,SOURCES_LOD_MAX=4))
	cmds.button(l='256',bgc=[0.7,0.8,0.7],c=lambda *args:main(MAPWIDTH=256,MAPHEIGHT=256,ATGI_ENABLE=True,SOURCES_LOD_MAX=4))
	cmds.button(l='512',bgc=[0.7,0.8,0.7],c=lambda *args:main(MAPWIDTH=512,MAPHEIGHT=512,ATGI_ENABLE=True,SOURCES_LOD_MAX=4))
	cmds.button(l='1024',bgc=[0.7,0.8,0.7],c=lambda *args:main(MAPWIDTH=1024,MAPHEIGHT=1024,ATGI_ENABLE=True,SOURCES_LOD_MAX=4))
	cmds.button(l='2048',bgc=[0.7,0.8,0.7],c=lambda *args:main(MAPWIDTH=2048,MAPHEIGHT=2048,ATGI_ENABLE=True,SOURCES_LOD_MAX=4))
	cmds.setParent('..')

	#LowMeshReduce
	cmds.text(l='meshLOD with no ATGI')
	cmds.gridLayout(nc=6)
	cmds.button(l='64',bgc=[0.8,0.7,0.8],c=lambda *args:main(MAPWIDTH=64,MAPHEIGHT=64,ATGI_ENABLE=False,SOURCES_LOD_MAX=4))
	cmds.button(l='128',bgc=[0.8,0.7,0.8],c=lambda *args:main(MAPWIDTH=128,MAPHEIGHT=128,ATGI_ENABLE=False,SOURCES_LOD_MAX=4))
	cmds.button(l='256',bgc=[0.8,0.7,0.8],c=lambda *args:main(MAPWIDTH=256,MAPHEIGHT=256,ATGI_ENABLE=False,SOURCES_LOD_MAX=4))
	cmds.button(l='512',bgc=[0.8,0.7,0.8],c=lambda *args:main(MAPWIDTH=512,MAPHEIGHT=512,ATGI_ENABLE=False,SOURCES_LOD_MAX=4))
	cmds.button(l='1024',bgc=[0.8,0.7,0.8],c=lambda *args:main(MAPWIDTH=1024,MAPHEIGHT=1024,ATGI_ENABLE=False,SOURCES_LOD_MAX=4))
	cmds.button(l='2048',bgc=[0.8,0.7,0.8],c=lambda *args:main(MAPWIDTH=2048,MAPHEIGHT=2048,ATGI_ENABLE=False,SOURCES_LOD_MAX=4))
	cmds.setParent('..')


	#LowMeshReduce
	cmds.text(l='for LowMesh')
	cmds.gridLayout(nc=6)
	cmds.button(l='64',bgc=[0.7,0.7,0.8],c=lambda *args:main(MAPWIDTH=64,MAPHEIGHT=64,ATGI_ENABLE=False,SOURCES_LOD_MAX=7))
	cmds.button(l='128',bgc=[0.7,0.7,0.8],c=lambda *args:main(MAPWIDTH=128,MAPHEIGHT=128,ATGI_ENABLE=False,SOURCES_LOD_MAX=7))
	cmds.button(l='256',bgc=[0.7,0.7,0.8],c=lambda *args:main(MAPWIDTH=256,MAPHEIGHT=256,ATGI_ENABLE=False,SOURCES_LOD_MAX=7))
	cmds.button(l='512',bgc=[0.7,0.7,0.8],c=lambda *args:main(MAPWIDTH=512,MAPHEIGHT=512,ATGI_ENABLE=False,SOURCES_LOD_MAX=7))
	cmds.button(l='1024',bgc=[0.7,0.7,0.8],c=lambda *args:main(MAPWIDTH=1024,MAPHEIGHT=1024,ATGI_ENABLE=False,SOURCES_LOD_MAX=7))
	cmds.button(l='2048',bgc=[0.7,0.7,0.8],c=lambda *args:main(MAPWIDTH=2048,MAPHEIGHT=2048,ATGI_ENABLE=False,SOURCES_LOD_MAX=7))
	cmds.setParent('..')

	cmds.rowLayout(nc=2,cw2=[65,50],ann=u'ソース サーフェスを検索するときのスタート ポイントとして使用する、固定オフセットをターゲットサーフェスから指定します。\nこの値は、所定のターゲットに検索ケージが指定されていない場合のみ使用します。\nこのフラグを含む場合は、すべてのターゲットに 1 度は含める必要があります。')
	cmds.text(l='offset')
	cmds.floatField('MSG2_LODTool_SEARCH_OFFSET',v=10)
	cmds.setParent('..')

	cmds.rowLayout(nc=2,cw2=[65,50],ann=u'ソース サーフェスを検索するターゲットサーフェスからの最大距離を制御します。\n値「0」は、無制限を示します。\n生成したマップにオブジェクトの反対側のアーティファクトが含まれる場合は、この値をオブジェクトの半径とほぼ同じ距離に設定してください。\nこのフラグを含む場合は、すべてのターゲットに 1 度は含める必要があります。')
	cmds.text(l='distance')
	cmds.floatField('MSG2_LODTool_MAX_SEARCH_DISTANCE',v=0)
	cmds.setParent('..')

	cmds.button(l='super',bgc=[0.8,0.7,0.7],c=lambda *args:super())


	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MSG2_LODTool_window',q=True,ex=True):
		cmds.deleteUI('MSG2_LODTool_window')
	cmds.window('MSG2_LODTool_window',rtf=True,s=True)
	MS_polyUnite.LayoutA()
	MS_BBfilter.LayoutA()
	MSG2_LODreduce.LayoutA()
	LayoutA()
	MSG2_LODPreview.LayoutA()


	cmds.window('MSG2_LODTool_window',e=True,w=80,h=40)
	cmds.showWindow('MSG2_LODTool_window')
	
