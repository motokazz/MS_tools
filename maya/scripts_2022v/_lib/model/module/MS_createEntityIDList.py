# _*_coding:utf-8_*_
########################################
# ファイル名
#			MP_MS_createEntityIDList
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds
import maya.mel as mel
import os

import MS_module.MP_MS_entityList as entityList
reload(entityList)
	
	
##### define
	
EntityIDList='d:/Mproject/graphic/gimmick/doc/entity_location_list.csv'
	
	
	
	
def OPEN_EXPLOROR(DIR,MODE=''):
	DIR=DIR.replace('/','\\')
	
	if DIR[-1]=='\\':#行末がバックスラッシュの場合
		WINDOWS_PATH=DIR
	elif MODE=='file':#
		WINDOWS_PATH
	else :#ファイルパスの場合
		WINDOWS_PATH='\\'.join(DIR.split('\\')[:-1])
	
	os.popen('explorer "%s"' % WINDOWS_PATH)
	
	
	
	
	
############################
##### 飯田さんから拝借　～ #####
	
def ms_yu_createEntNode(entFile, newNode):

	##### プラグインチェッカー #####
	if not cmds.pluginInfo('ToroLocator.mll',q=True,loaded=True):
		cmds.loadPlugin('ToroLocator.mll')
	
	
	cmds.select(ado=True)
	preNodes = cmds.ls(selection=True)
	cmds.select(clear=True)
	
	command = 'LayoutoroCommand -r "' + entFile + '" ;' 
	mel.eval(command)
	cmds.select(ado=True)
	cmds.select(preNodes, deselect=True)
	postNodes = cmds.ls(selection=True)
	
	cmds.parent(postNodes, newNode)   
	cmds.select(newNode)
	
	try:
		cmds.addAttr(newNode + '.entity' , q=True, ex=True)
	except:	
		cmds.addAttr(longName='entity', dataType='string')
		cmds.setAttr(newNode + '.entity', entFile, type='string')

def importEntityFile(entFile='D:/Mproject/MGameData/models/BG/stage002/area03/env/d2_stage_builds.toro'):
	if not entFile:
		return False
	try:
		entNode = 'ent_' + (entFile.split('/')[-1]).split('.')[0]
		newNode = cmds.createNode( 'transform', n=entNode )
		ms_yu_createEntNode(entFile, newNode)
		return True
	except:
		print False
		return False
	
	
#####
def attrList(MODE='all'):
	shp=[
		'typeName'
		,'typeID'
		,'nickname'
		,'responeID'
		,'igcType'
	]
	trn=[
		'tx'
		,'ty'
		,'tz'
		,'rx'
		,'ry'
		,'rz'
	]
	if MODE=='all':
		return shp+trn
	if MODE=='shape':
		return shp
	if MODE=='transform':
		return trn


def clearList(ROW='ID',FILE_PATH=EntityIDList):
	ROW='stageID'+','+','.join(attrList())+'\n'
	f=open(FILE_PATH,'w')#'r'読み込み：'w'書き込み：'a'追記：'+'読み書き両方' 't'テキストモード：'b'バイナリーモード
	f.write(ROW)
	f.close()
	
	
def addList(ROW='ID,',FILE_PATH=EntityIDList):
	f=open(FILE_PATH,'a')#'r'読み込み：'w'書き込み：'a'追記：'+'読み書き両方' 't'テキストモード：'b'バイナリーモード
	f.write(ROW)
	f.close()
	
	
def analizeEntity(PATH):
	cmds.file(f=True,new=True)
	listTxt=''
	importEntityFile(entFile=PATH)
	LAYOUTORO_NODES=cmds.ls(type=['LayoutoroNode'],l=True)
	#MG_NODES=cmds.ls(type=['MGLocator'],l=True)
	splitPath=PATH.split('/')
	stageID=splitPath[5]+splitPath[6]
	for each in LAYOUTORO_NODES:
		DATALIST=[]
		DATALIST.append(stageID)
		for eachAttr in attrList('shape'):
			DATALIST.append(str(cmds.getAttr(each+'.'+eachAttr)))
		for eachAttr in attrList('transform'):
			node_trn=cmds.listRelatives(each,p=True,type='transform')[0]
			var=cmds.getAttr(node_trn+'.'+eachAttr)
			if -0.0001<var<0.0001:
				var=0
			DATALIST.append(str(var))
		listTxt+=','.join(DATALIST)+'\n'
	cmds.file(f=True,new=True)
	return listTxt
	
	
def do():
	clearList()
	entityLists=entityList.entityList()
	for each in entityLists:
		addList(analizeEntity(each))
	
	cmds.confirmDialog(m='createEntityIDList Finish\n')



def layoutA(
	LABEL='MP_MS_createEntityIDList'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.button(w=WIDTH-4,l=u'do',c=lambda *args:do())
	cmds.button(w=30,bgc=[0.6,0.7,0.8],l=u'e',c=lambda *args:OPEN_EXPLOROR(EntityIDList))
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MP_MS_createEntityIDList_main_window',q=True,ex=True):
		cmds.deleteUI('MP_MS_createEntityIDList_main_window')
	cmds.window('MP_MS_createEntityIDList_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MP_MS_createEntityIDList_main_window')
	

