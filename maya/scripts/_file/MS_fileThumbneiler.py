# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_fileThumbneiler
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import random
import glob
import re
import os
import subprocess
import csv

# atgi Tools
import atgiTools

import _lib.MS_copyClipboard as MS_copyClipboard
reload(MS_copyClipboard)

''' asobi util
# asobi utils
import muple.utility as util
import muple.importer as imp


def set_lox_attributes(node, lox, odx = None):
	try:
		attributes = imp.loxes[lox]['Attributes']
		if odx != None:
			odx_attr = filter(lambda a:a['Name'] == 'Odx', attributes)
			odx_attr[0]['Value'] = odx
		util.set_attributes(node, attributes)
		util.add_common_attribute(node, add_as_template=False)
	except:
		pass
'''


#設定CSVのパス
setting_path = os.path.dirname(__file__).replace('\\','/')+'/MS_fileThumbneiler.csv'

#パスリスト初期化
THUMBNEILPATH='d:/'
BGMBRoot='d:/'
ATGIPATH ='d:/'

###############
# import path list
###############
#パスリストをインポートする
DICT_PATH={}
with open(setting_path,'r') as f:
	reader = csv.reader(f)
	header = next(reader)
	i=0
	for each in header:
		if each == 'name':key=i
		if each == 'thumbneil':thumbnail=i
		if each == 'mb':mb=i
		if each == 'atgi':atgi=i
		i+=1
	for each in reader:
		DICT_PATH.setdefault(each[key],[each[thumbnail],each[mb],each[atgi]])

#パスリストを基に、パスを設置
def change_PATH(KEY='bg'):

	global THUMBNEILPATH
	global BGMBRoot
	global ATGIPATH

	THUMBNEILPATH=DICT_PATH[KEY][0]
	BGMBRoot = DICT_PATH[KEY][1]
	ATGIPATH = DICT_PATH[KEY][2]

	create_thumbneil()
	store()


###############
# thumbList
###############
def listOdx():
	ATTR='Odx'
	ret =[]
	ad = cmds.ls(type='transform',l=True)

	for each in ad:
		if cmds.attributeQuery(ATTR,node = each,ex=True):
			odx=cmds.getAttr(each + '.' + ATTR)
			if not odx in ret:
				ret.append(odx)
	return ret

def create_thumbneil(RANDOMSELECT=0,MIN=0,MAX=100):
	
	#リスト作成
	def createList(RANDOMSELECT=0,MIN=0,MAX=100):
		#　検索ワード取得
		SEARCHWORDS=cmds.textField('MS_fileThumbneiler_searchWord',q=True,tx=True)
		IGNOREWORDS=cmds.textField('MS_fileThumbneiler_ignoreWords',q=True,tx=True).split(';')

		if SEARCHWORDS=='' and RANDOMSELECT==0:
			return listOdx()
			#return False

		#　リスト作成
		THUMBLIST=getThumbList(SEARCHWORDS,IGNOREWORDS,RANDOMSELECT,MIN,MAX)

		THUMBNAMELIST=[]
		for each in THUMBLIST:
			if each == 'MAX' or  each == 'FOWARD':
				THUMBNAMELIST.append(each)

			PRE=re.split('/|\\\\',each)
			if len(PRE)>1:
				THUMBNAME=PRE[-1].split('.')[0]
				THUMBNAMELIST.append(THUMBNAME)

		return THUMBNAMELIST
		
	#Thumbを検索したリスト
	def getThumbList(
		SEARCHWORDS=''	#検索語
		,IGNOREWORDS=['_col.','_sdw.','_low.','_occ.','_db.','_bk.','_dy.','_brk_']#無視するワード、;で区切って複数指定可能
		,RANDOMSELECT=0
		,MIN=0
		,MAX=100
		):
		
		RET=[]

		DIR = glob.glob(THUMBNEILPATH+'/*%s*.jpg'%SEARCHWORDS)

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

	#各チップ内のレイアウト
	def chip_layout(name):
		cmds.columnLayout(adj=True)

		##################
		#上段
		##################

		#　名前表示ボタン
		cmds.button(l=name,h=16,c=printString(name),ann=name)

		##################
		# 中段
		##################

		#　壊れモデル名前サムネール用に変更
		THUMNAME=name.replace('_bk','').replace('_db','').replace('_dy','')
		
		#　サムネイル作成
		cmds.iconTextButton(
			style='iconOnly'
			, w=120
			,h=90
			,image1=THUMBNEILPATH+'/'+THUMNAME+'.jpg'
			, label=name
			,c=thumbneil_command(name)
			)

		##################
		# 下段
		##################

		# Execbutton
		cmds.rowLayout(nc=4,cw4=[28,28,28,28],cl4=['center','center','center','center'],columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0),(4, 'both', 0)])
		cmds.button(l='open',w=28,h=15,c=OpenMB(name))
		cmds.button(l='import',w=28,h=15,c=ImportMB(name))
		cmds.button(l='',w=28,h=15,c=y_command(name))
		cmds.button(l='',w=28,h=15,c=x_command(name))
		cmds.setParent('..')
		#
		cmds.setParent('..')

	#
	THUMBLIST=createList(RANDOMSELECT=RANDOMSELECT,MIN=MIN,MAX=MAX)

	if not THUMBLIST:
		return

	if cmds.gridLayout('MS_fileThumbneiler_atgiThumbneil',q=True,ex=True):
		cmds.deleteUI('MS_fileThumbneiler_atgiThumbneil')
	cmds.gridLayout('MS_fileThumbneiler_atgiThumbneil',nc=4,nr=6,cw=120,ch=125,p='MS_fileThumbneiler_thumbneil_scrollLayout')

	for each in THUMBLIST:
		cmds.button('MS_fileThumbneiler_misc_button_a',e=True,l='')
		cmds.button('MS_fileThumbneiler_misc_button_d',e=True,l='')
		
		if each in 'MAX':
			cmds.button('MS_fileThumbneiler_misc_button_d',e=True,l='=>',c=lambda *args:create_thumbneil(RANDOMSELECT=RANDOMSELECT,MIN=(MIN+100),MAX=(MAX+100)))
			continue

		if each in 'FOWARD':
			cmds.button('MS_fileThumbneiler_misc_button_a',e=True,l='<=',c=lambda *args:create_thumbneil(RANDOMSELECT=RANDOMSELECT,MIN=(MIN-100),MAX=(MAX-100)))
			continue



		chip_layout(each)

	cmds.setParent('..')


#################
# button commands
#################

# 上段
# 文字列をコピー＆表示
def printString(STR):
	def RET(dummy=''):
		SCROLLFIELDS=['MS_batch_export_atgi_list'
			,'MS_batch_List'
			,'MSG2_atgi_send_to_win_run_THUMBS'
			,'MSG2_check_atgi_located_seachWord'
			,'MSG2_check_hkx_seachWord'
			]
		for each in SCROLLFIELDS:
			if cmds.scrollField(each,ex=True):
				cmds.scrollField(each,e=True,insertText=STR+'\n',insertionPosition=0)
		MS_copyClipboard.copyClipboard(STR)
		print STR
	return RET

# 中段
# サムネイル
def thumbneil_command(MBNAME):
	def RET(dummy=''):
		scale_options = cmds.radioButtonGrp('MS_fileThumbneiler_scaleOptions', q=True ,sl=True)

		#DELFLAG ctrlキー押されてたら消す
		mods = cmds.getModifiers()
		if (mods & 4) > 0: DELETE_source_FLAG=True
		else:DELETE_source_FLAG=False

		#selection
		sel = cmds.ls(sl=True,l=True)

		#BGMBRoot

		######################################
		#load (if needed)
		#######################################
		
		RN=[]
		new=[]

		loaded = False
		
		# if scene already loaded MBNAME obj:今のシーンの中に同じ名前のオブジェクトがあったらそれをコピー

		exist = cmds.ls(MBNAME,tr=True,l=True)

		if len(exist)>0:
			RN = cmds.duplicate(exist[0])
			loaded = True

		#下記優先順位でファイルサーチ＆読み込み。※とりあえずAtgi優先
		else:
			if not ATGIPATH == '':#ATGI
				FPATH=searchPath(ATGIPATH,MBNAME,searchExt='atgi')
			if not FPATH:#FBX
				FPATH=searchPath(BGMBRoot,MBNAME,searchExt='fbx')
			if not FPATH:#OBJ
				FPATH=searchPath(BGMBRoot,MBNAME,searchExt='obj')
			if not FPATH:# MB or MA
				FPATH=searchPath(BGMBRoot,MBNAME)

		# atgi
		if not loaded:

			if FPATH:
				if '.atgi' in FPATH:
					RN = [atgiTools.createAtgiLocatorNode(FPATH)]

					# asobi : set_lox_attributes
					# set_lox_attributes(RN[0], 'art_bg' , MBNAME)

				else:
					RN = cmds.file(FPATH,i=True,options='v=0',f=True,dns=True,rnn=True)
					RN = cmds.ls(RN,typ='transform')

				# rename to MBNAME
				RN[0]=cmds.rename(RN[0],MBNAME)


			else:
				print 'file not found'
				return
			
		#reset transform
		cmds.setAttr(RN[0]+'.tx',0)
		cmds.setAttr(RN[0]+'.ty',0)
		cmds.setAttr(RN[0]+'.tz',0)
		cmds.setAttr(RN[0]+'.rx',0)
		cmds.setAttr(RN[0]+'.ry',0)
		cmds.setAttr(RN[0]+'.rz',0)
		cmds.setAttr(RN[0]+'.sx',1)
		cmds.setAttr(RN[0]+'.sy',1)
		cmds.setAttr(RN[0]+'.sz',1)


		# selection

		if len(sel)>0:
			for each in sel:
				

				#######################################
				#duplicate 
				#######################################

				# Store parentnode
				TARGET_PARENT=cmds.listRelatives(each,p=True,f=True)
				
				# Duplicate source

				duped = cmds.duplicate(RN[0])
				try:
					duped = cmds.parent(duped[0],w=True)
				except:
					pass
				cmds.setAttr(duped[0]+'.visibility',True)

				# Ditect translate
				translateMode = cmds.radioButtonGrp('MS_fileThumbneiler_translateOptions',q=True,sl=True)
				
				if translateMode == 1:
					cmds.select(each,r=True)
					BB =  bbcalc(MODE='source')
					cmds.select(duped,r=True)
					NBB =  bbcalc(MODE='source')
				elif translateMode == 2:
					cmds.select(each,r=True)
					BB =  bbcalc(MODE='center')
					cmds.select(duped,r=True)
					NBB =  bbcalc(MODE='center')
				
				# do Translate

				cmds.xform(t=[BB[0],BB[1],BB[2]],ws=True)
					
				# do Rotate
				cmds.xform(ro=[BB[3],BB[4],BB[5]],ws=True)

				# do Scale by mode
				if scale_options == 1:	# none
					cmds.xform(s=[1,1,1],ws=True)

				if scale_options == 2:	# BB
					cmds.xform(s=[BB[9]/NBB[9],BB[10]/NBB[10],BB[11]/NBB[11]],ws=True)

				if scale_options == 3:	# sourceScale
					cmds.xform(s=[BB[6],BB[7],BB[8]],ws=True)



				# del source
				#check
				unti_delete_flag = False
				if cmds.attributeQuery('LoxFile',node = each,ex=True):
					if not cmds.getAttr(each+'.LoxFile') == 'art_bg':
						unti_delete_flag = True
						print 'skipped , It`s not art_bg: '+each
						

				if cmds.listRelatives(each,c=True,f=True,typ='transform'):
					unti_delete_flag = True
					print 'skipped , has childlen: '+each
					

				if DELETE_source_FLAG and not unti_delete_flag:
					cmds.delete(each)
				else:
					# Offset
					offsetMode = cmds.radioCollection('MS_fileThumbneiler_offsetMode',q=True,sl=True)
					
					if offsetMode == 'x_add':cmds.move((BB[9]+NBB[9])*0.5,x=True,os=True,r=True)
					if offsetMode == 'x_dec':cmds.move(-(BB[9]+NBB[9])*0.5,x=True,os=True,r=True)
					if offsetMode == 'y_add':cmds.move((BB[10]+NBB[10])*0.5,y=True,os=True,r=True)
					if offsetMode == 'y_dec':cmds.move(-(BB[10]+NBB[10])*0.5,y=True,os=True,r=True)
					if offsetMode == 'z_add':cmds.move((BB[11]+NBB[11])*0.5,z=True,os=True,r=True)
					if offsetMode == 'z_dec':cmds.move(-(BB[11]+NBB[11])*0.5,z=True,os=True,r=True)
				
				
				#parent

				temp=[]

				if TARGET_PARENT:
					temp = cmds.parent(duped[0],TARGET_PARENT[0])
				else:
					try:
						temp = cmds.parent(duped[0],w=True)
					except:
						temp = duped

				# copy Attr

				new.append(temp[0])

		else:
			new.append(cmds.duplicate(RN[0])[0])
		cmds.delete(RN[0])

		# selectNewObj
		SelectionMode = cmds.radioButtonGrp('MS_fileThumbneiler_selectionMode', q=True ,sl=True)
		if SelectionMode == 1:cmds.select(cl=True)
		if SelectionMode == 2:cmds.select(sel,r=True)
		if SelectionMode == 3:cmds.select(new,r=True)
		
		# for fix rename 20200615
		for each in new:
			cmds.rename(each,MBNAME)

	return RET

# 下段
# コマンドボタン
def OpenMB(MBNAME):
	def RET(dummy=''):
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

		cmds.file(FPATH,o=True,options='v=0',f=True,dns=True)

	return RET

def ImportMB(MBNAME):
	def RET(dummy=''):
		#BGMBRoot
		FPATH=searchPath(BGMBRoot,MBNAME)
		if not FPATH:
			FPATH=searchPath(BGMBRoot,MBNAME,searchExt='obj')
		if not FPATH:
			FPATH=searchPath(BGMBRoot,MBNAME,searchExt='fbx')

		if FPATH:
			cmds.file(FPATH,i=True,options='v=0',f=True,dns=True)
		else:
			print 'file not found'
	return RET

def y_command(*args):
	def RET(dummy=''):
		print args
		pass
	return RET

def x_command(*args):
	def RET(dummy=''):
		print args
		pass
	return RET


# 指定パスからの相対パスを返す　例）module/MS_primitives.py
def searchPath(searchPath,searchFile='',searchExt='ma'):
	#print searchFile+'.'+searchExt
	for (root,dir,files) in os.walk(searchPath):
		#発見時の処理
		for f in files:
			fname=f.split('.')[0]
			if (searchFile+'.'+searchExt) == f:
				root=root.replace('\\','/').replace('//','/')
				return root+'/'+f
	return False

# BpundingBoxからいろいろ取得
def bbcalc(MODE='center',ROT=[0,0,0]):
	# BBCenter Rotation sourceScale BBScale CenterGaps
	TRN = [ 0.0 , 0.0 , 0.0 , 0.0 , 0.0 , 0.0 , 1.0 , 1.0 , 1.0 , 1.0 , 1.0 , 1.0 , 0.0 , 0.0 , 0.0]

	if not cmds.ls(sl=True):
		return TRN

	# get Rotation
	
	OTRN =  cmds.xform(q=True,t=True,ws=True)

	OROT = cmds.xform(q=True,ro=True,ws=True)
	cmds. xform(ro=ROT,ws=True)
	BB =  cmds.xform(q=True,bb=True,ws=True)
	cmds. xform(ro=OROT,ws=True)


	if BB:
		TRN=[]

		if MODE=='source':
			OTRN = cmds.xform(q=True,t=True,ws=True)
			TRN.extend(OTRN)
		elif MODE=='center':
			TRN.append((BB[0]+BB[3])*0.5)
			TRN.append((BB[1]+BB[4])*0.5)
			TRN.append((BB[2]+BB[5])*0.5)
		elif MODE=='XPositive':
			TRN.append(BB[3])
			TRN.append((BB[1]+BB[4])*0.5)
			TRN.append((BB[2]+BB[5])*0.5)
		elif MODE=='XNegative':
			TRN.append(BB[0])
			TRN.append((BB[1]+BB[4])*0.5)
			TRN.append((BB[2]+BB[5])*0.5)
		elif MODE=='YPositive':
			TRN.append((BB[0]+BB[3])*0.5)
			TRN.append(BB[4])
			TRN.append((BB[2]+BB[5])*0.5)
		elif MODE=='YNegative':
			TRN.append((BB[0]+BB[3])*0.5)
			TRN.append(BB[1])
			TRN.append((BB[2]+BB[5])*0.5)
		elif MODE=='ZPositive':
			TRN.append((BB[0]+BB[3])*0.5)
			TRN.append((BB[1]+BB[4])*0.5)
			TRN.append(BB[5])
		elif MODE=='ZNegative':
			TRN.append((BB[0]+BB[3])*0.5)
			TRN.append((BB[1]+BB[4])*0.5)
			TRN.append(BB[2])
		elif MODE=='compornent':
			BB=cmds.polyEvaluate(COMP,bc=True)
			TRN.append((BB[0][1]+BB[0][0])*0.5)
			TRN.append((BB[1][1]+BB[1][0])*0.5)
			TRN.append((BB[2][1]+BB[2][0])*0.5)

		# ditectRot

		TRN.extend(cmds.xform(q=True,ro=True,ws=True))

		# ditectScale
		TRN.extend(cmds.xform(q=True,s=True,ws=True))

		# append BBsize

		TRN.append(abs(BB[0]-BB[3]))
		TRN.append(abs(BB[1]-BB[4]))
		TRN.append(abs(BB[2]-BB[5]))

		# append center gaps
		TRN.append(TRN[0]-OTRN[0])
		TRN.append(TRN[1]-OTRN[1])
		TRN.append(TRN[2]-OTRN[2])

	#return 
	return TRN


###############
# UI
###############

# Store Recall
#################
def store():
	PREFIX='MS_fileThumbneiler'
	CONTROLNAME='MS_fileThumbneiler_searchWord'
	NAME=PREFIX+CONTROLNAME
	if cmds.control(CONTROLNAME,ex=True):
		cmds.optionVar(stringValue=[
			NAME
			,cmds.textField(CONTROLNAME,q=True,tx=True)
			+';'+cmds.optionMenu('MS_fileThumbneiler_presets',q=True,v=True)
			])

def recall():
	PREFIX='MS_fileThumbneiler'
	CONTROLNAME='MS_fileThumbneiler_searchWord'
	NAME=PREFIX+CONTROLNAME
	if cmds.optionVar(exists=NAME):

		VAR=cmds.optionVar(q=NAME).split(';')

		if cmds.control('MS_fileThumbneiler_searchWord',ex=True):
			cmds.textField('MS_fileThumbneiler_searchWord',e=True,tx=VAR[0])

		if cmds.control('MS_fileThumbneiler_presets',ex=True):
			cmds.optionMenu('MS_fileThumbneiler_presets',e=True,v=VAR[1])
			change_PATH(VAR[1])

#UIリフレッシュ
#################

def storeAndGetList():
	store()
	create_thumbneil()

def atgiUtil():
	cmds.columnLayout(adj=True)
	cmds.text(l='Util',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.gridLayout(nc=4,cw=125)
	cmds.button(l='atgi to mesh',c=lambda *args:atgiToMesh())
	cmds.button(l='atgi to meshLODLow',c=lambda *args:atgiToMeshFromAttr('LodLevelMin',5))
	cmds.button(l='mesh to atgi',c=lambda *args:s1907_atg_change.main.to_atg())
	cmds.button(l='functionalRenamer',c=lambda *args:functionalRenamer_GraviteThumbLocatorNode())
	cmds.text(l='searchWord')
	cmds.textField('MS_fileThumbneiler_searchAndSelectThumb',tx='',cc=lambda *args:searchAndSelectThumb())
	cmds.text(l='')
	cmds.text(l='')
	cmds.button(l='reloadThumbAll',c=lambda *args:reloadThumbAll())
	cmds.button(l='searchThumbDeadLink',c=lambda *args:searchThumbDeadLink())
	cmds.setParent('..')

#iリストのレイアウト
#################
def Layout_header():
	IGNOREWORDS='_col.;_sdw.;_low.;_occ.;'
	cmds.columnLayout(adj=True)
	cmds.text(l='MS_fileThumbneiler',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.gridLayout(nc=5,cw=100)
	#SearchWords
	
	cmds.text(l='SeatchWords',w=50)
	cmds.textField('MS_fileThumbneiler_searchWord',tx='_ms_',cc=lambda *args:storeAndGetList(),w=150)

	#Presets
	cmds.text(l='Presets')
	cmds.optionMenu('MS_fileThumbneiler_presets',cc=change_PATH)
	for each in DICT_PATH.keys():
		cmds.menuItem( label=each)

	cmds.button(l='openSetup',c=lambda *args:os.popen('explorer "%s"' % setting_path.replace('/','\\')))

	cmds.setParent('..')

	# Random Selection
	cmds.gridLayout(nc=4,cw=100,ch=16)
	cmds.button(l='random 5',c=lambda *args:create_thumbneil(RANDOMSELECT=5))
	cmds.button(l='random 10',c=lambda *args:create_thumbneil(RANDOMSELECT=10))
	cmds.button(l='random 25',c=lambda *args:create_thumbneil(RANDOMSELECT=25))
	cmds.button(l='random 50',c=lambda *args:create_thumbneil(RANDOMSELECT=50))
	cmds.setParent('..')

	# Ignore Words
	cmds.rowLayout(nc=4,cw4=[50,400,50,150])
	cmds.text(l='ignoreWords')
	cmds.textField('MS_fileThumbneiler_ignoreWords',w=400,tx=IGNOREWORDS,cc=lambda *args:storeAndGetList())
	cmds.setParent('..')

	# Transform mode
	cmds.radioButtonGrp('MS_fileThumbneiler_translateOptions', label='Translate Method', cw3=[100,60,60] , labelArray2=['source', 'BBCenter'], numberOfRadioButtons=2 ,sl=1)
	cmds.separator(w=200)

	# Scale Mode
	cmds.radioButtonGrp('MS_fileThumbneiler_scaleOptions', label='Scale Method', cw4=[100,60,60,60] , labelArray3=['None', 'BB', 'source Scale'], numberOfRadioButtons=3 ,sl=3)
	cmds.separator(w=200)
	# Selection Mode
	cmds.radioButtonGrp('MS_fileThumbneiler_selectionMode',  label='Selection Mode', cw4=[100,60,60,60] , labelArray3=['None' , 'Selected' , 'Created' ], numberOfRadioButtons=3 ,sl=3)

	cmds.separator(w=200)

	# Offset Mode
	cmds.rowLayout(nc=2,cw2=[100,200],ct2=['right','left'])
	cmds.text(l='offsetMode')
	cmds.gridLayout(nc=4,cw=50,ch=16)
	cmds.radioCollection('MS_fileThumbneiler_offsetMode')
	cmds.text(l='')	
	cmds.radioButton( 'z_dec',label='z-' )
	cmds.text(l='')	
	cmds.radioButton( 'y_add',label='y+' )

	cmds.radioButton( 'x_dec',label='x-' )
	cmds.radioButton( 'none',label='none' )
	cmds.radioButton( 'x_add',label='x+' )
	cmds.text(l='')	

	cmds.text(l='')	
	cmds.radioButton( 'z_add',label='z+' )
	cmds.text(l='')	
	cmds.radioButton( 'y_dec',label='y-' )
	cmds.setParent('..')
	cmds.radioCollection('MS_fileThumbneiler_offsetMode',e=True,sl='none')
	cmds.setParent('..')
	#
	cmds.setParent('..')

#Thumbサムネイルのレイアウト
def Layout_thumbneil():
	cmds.columnLayout('MS_fileThumbneiler_misc',adj=True)
	cmds.gridLayout(nc=4,cw=122,ch=16)
	cmds.button('MS_fileThumbneiler_misc_button_a',l='',h=16)
	cmds.button('MS_fileThumbneiler_misc_button_b',l='',h=16)
	cmds.button('MS_fileThumbneiler_misc_button_c',l='',h=16)
	cmds.button('MS_fileThumbneiler_misc_button_d',l='',h=16)
	cmds.setParent('..')
	cmds.setParent('..')

	cmds.columnLayout(adj=True)
	cmds.scrollLayout('MS_fileThumbneiler_thumbneil_scrollLayout',h=500)
	cmds.setParent('..')
	cmds.setParent('..')

#外部ツール用レイアウト
#################
def Layout_footer():
	cmds.frameLayout('MS_fileThumbneiler_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_fileThumbneiler',cll=True,cl=False)
	cmds.columnLayout('MS_fileThumbneiler_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_fileThumbneiler',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='MS_fileThumbneiler',c=lambda *args:UI())
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

# メインレイアウト
#################
def UI():
	if cmds.window('MS_fileThumbneiler_window',q=True,ex=True):
		cmds.deleteUI('MS_fileThumbneiler_window')
	cmds.window('MS_fileThumbneiler_window',rtf=True,s=True)
	
	Layout_header()
	Layout_thumbneil()
	cmds.text(l='ctrl + thumbneil  =  swap mode')
	cmds.showWindow('MS_fileThumbneiler_window')

	recall()
	storeAndGetList()



