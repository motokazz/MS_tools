# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_railCreator.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds


import MSG2_atgiTools.MSG2_atgiLoader as MSG2_atgiLoader
reload(MSG2_atgiLoader)

#################
#  Plugin Check 
#################
#if not cmds.pluginInfo("GraviteLocatorNode.mll", q=1, loaded=1):
#	cmds.loadPlugin("GraviteLocatorNode.mll")

#################
# Initialize
#################
ATGIPATH = 'D:/Projects/Gravite2/assets/bg/model'
THUMBNEILPATH='D:/Projects/Gravite2/graphic/bg/jam/thumbnail'
BGMBRoot = 'D:/Projects/Gravite2/graphic/bg/scenes'

def createAtgiNode(SELTRN=''):
	TRN=(0,0,0)
	ROT=(0,0,0)
	if SELTRN:
		TRN=cmds.xform(SELTRN,q=True,ws=True,t=True)
		ROT=cmds.xform(SELTRN,q=True,ws=True,ro=True)
	NODE = cmds.createNode('GraviteAtgiLocatorNode')
	NODETRNS = cmds.listRelatives(NODE,ap=True,type='transform')
	cmds.xform(NODETRNS,t=TRN)
	cmds.xform(NODETRNS,ro=ROT)
	cmds.select(NODETRNS,r=True)
	return NODE

def changeAtgi(ATGINODE,ATGINAME):
	ATGIFILEPATH = ATGIPATH+'/'+ATGINAME+'.atgi'
	cmds.setAttr(ATGINODE + '.atgiFilename',ATGIFILEPATH,type='string')

	#ワイヤーフレームカラー
	cmds.color(ATGINODE,ud=2)

	#リネーム処理
	PNODE=cmds.listRelatives(ATGINODE,p=True,f=True)
	NEWATGI=cmds.rename(PNODE,ATGINAME+'_01')
	NEWATGI=cmds.ls(NEWATGI,l=True)

'''
PIPE_DICT_org={
	'_a':[0.0, 0.0, 200.0, 0.0, 0.0, 0.0]
	,'_la':[-3.5419762820087687e-15, -117.15728752538098, 282.84271247461896, 45.000000000000036, -0.0, 0.0]
	,'_lb':[-82.84271247461913, -82.84271247461896, 282.8427124746191, 35.26438968275468, -30.00000000000003, -9.735610317245364]
	,'_lc':[-117.15728752538098, 1.4347629716474392e-14, 282.842712474619, 0.0, -45.000000000000014, 0.0]
	,'_ld':[-82.84271247461902, 82.84271247461899, 282.842712474619, -35.26438968275471, -30.000000000000043, 9.735610317245309]
	,'_le':[2.95561199046703e-14, 117.15728752538092, 282.84271247461896, -45.000000000000036, -0.0, 0.0]
	,'_lf':[82.84271247461902, 82.84271247461896, 282.842712474619, -35.26438968275466, 30.000000000000018, -9.735610317245344]
	,'_lg':[117.15728752538098, 0.0, 282.842712474619, 0.0, 45.000000000000014, 0.0]
	,'_lh':[82.84271247461896, -82.84271247461902, 282.84271247461885, 35.26438968275479, 30.00000000000006, 9.735610317244904]
	,'_ma':[-1.7709881410043844e-15, -58.57864376269049, 141.42135623730948, 45.000000000000036, -0.0, 0.0]
	,'_mb':[-41.42135623730957, -41.42135623730948, 141.42135623730954, 35.26438968275468, -30.00000000000003, -9.735610317245364]
	,'_mc':[-58.57864376269049, 7.173814858237196e-15, 141.4213562373095, 0.0, -45.000000000000014, 0.0]
	,'_md':[-41.42135623730951, 41.421356237309496, 141.4213562373095, -35.26438968275471, -30.000000000000043, 9.735610317245309]
	,'_me':[1.477805995233515e-14, 58.57864376269046, 141.42135623730948, -45.000000000000036, -0.0, 0.0]
	,'_mf':[41.42135623730951, 41.42135623730948, 141.4213562373095, -35.26438968275466, 30.000000000000018, -9.735610317245344]
	,'_mg':[58.57864376269049, 0.0, 141.4213562373095, 0.0, 45.000000000000014, 0.0]
	,'_mh':[41.42135623730948, -41.42135623730951, 141.42135623730942, 35.264389682754754, 30.00000000000008, 9.735610317245095]
}
'''

PIPE_DICT={
	'_a':[0.0, 0.0, 200.0, 0.0, 0.0, 0.0]
	,'_la':[-3.5419762820087687e-15, -117.15728752538098, 282.84271247461896, 45.000000000000036, -0.0, 0.0]
	,'_lb':[-82.84271247461913, -82.84271247461896, 282.8427124746191, 29.8375664783138, -35.39626013732807, 0.2808856075610086]
	,'_lc':[-117.15728752538098, 1.4347629716474392e-14, 282.842712474619, 0.0, -45.000000000000014, 0.0]
	,'_ld':[-82.84271247461902, 82.84271247461899, 282.842712474619, -29.8375664783138, -35.39626013732807, 0.2808856075610086]
	,'_le':[2.95561199046703e-14, 117.15728752538092, 282.84271247461896, -45.000000000000036, -0.0, 0.0]
	,'_lf':[82.84271247461902, 82.84271247461896, 282.842712474619, -29.8375664783138, 35.39626013732807, -0.2808856075610086]
	,'_lg':[117.15728752538098, 0.0, 282.842712474619, 0.0, 45.000000000000014, 0.0]
	,'_lh':[82.84271247461896, -82.84271247461902, 282.84271247461885, 29.8375664783138, 35.39626013732807, 0.2808856075610086]
	,'_ma':[-1.7709881410043844e-15, -58.57864376269049, 141.42135623730948, 45.000000000000036, -0.0, 0.0]
	,'_mb':[-41.42135623730957, -41.42135623730948, 141.42135623730954, 29.8375664783138, -35.39626013732807, 0.2808856075610086]
	,'_mc':[-58.57864376269049, 7.173814858237196e-15, 141.4213562373095, 0.0, -45.000000000000014, 0.0]
	,'_md':[-41.42135623730951, 41.421356237309496, 141.4213562373095, -29.8375664783138, -35.39626013732807, -0.2808856075610086]
	,'_me':[1.477805995233515e-14, 58.57864376269046, 141.42135623730948, -45.000000000000036, -0.0, 0.0]
	,'_mf':[41.42135623730951, 41.42135623730948, 141.4213562373095, -29.8375664783138, 35.39626013732807, -0.2808856075610086]
	,'_mg':[58.57864376269049, 0.0, 141.4213562373095, 0.0, 45.000000000000014, 0.0]
	,'_mh':[41.42135623730948, -41.42135623730951, 141.42135623730942, 29.8375664783138, 35.39626013732807, -0.2808856075610086]
}

def createP(PIPEID):
	#パイプ名定義
	ATGI_PIPE_NAME=cmds.textField('MSG2_railTools_baseRailPartsName',q=True,tx=True)
	#
	SEL=cmds.ls(sl=True,l=True)

	ATGINODE=createAtgiNode(SEL[0])
	for key in PIPE_DICT.keys():
		if key in SEL[0]:
			ATGITR=cmds.listRelatives(ATGINODE,p=True,f=True)[0]
			ATGITR=cmds.parent(ATGITR,SEL)
			cmds.xform(ATGITR,t=[PIPE_DICT[key][0]*20,PIPE_DICT[key][1]*20,PIPE_DICT[key][2]*20],r=True)
			cmds.xform(ATGITR,ro=[PIPE_DICT[key][3],PIPE_DICT[key][4],PIPE_DICT[key][5]],r=True)
			cmds.parent(ATGITR,w=True)

	changeAtgi(ATGINODE,ATGI_PIPE_NAME+'_'+PIPEID)

def createNew(PIPEID):
	#パイプ名定義
	ATGI_PIPE_NAME=cmds.textField('MSG2_railTools_baseRailPartsName',q=True,tx=True)
	#
	ATGINODE=createAtgiNode()
	changeAtgi(ATGINODE,ATGI_PIPE_NAME+'_'+PIPEID)

def parallelParts(PID):
	#パイプ名定義
	ATGI_PIPE_NAME=cmds.textField('MSG2_railTools_baseRailPartsName',q=True,tx=True)

	SEL=cmds.ls(sl=True,l=True)
	SELATGINODE=cmds.listRelatives(SEL[0],type='GraviteAtgiLocatorNode')
	ATGIFILENAME=cmds.getAttr(SELATGINODE[0]+'.atgiFilename')
	PIPEID=ATGIFILENAME.split('.')[0].split('_')[-1]

	ATGINODE=createAtgiNode(SEL[0])

	changeAtgi(ATGINODE,ATGI_PIPE_NAME+'_'+PID+'_'+PIPEID)

def create(PIPEID):
	#何も選択されていないとき
	SEL=cmds.ls(sl=True)
	if not SEL:
		createNew(PIPEID)

	mods = cmds.getModifiers()
	if (mods & 1) > 0:
		#Shiftキーを押しながらで強制ATGI新規作成モード
		createP(PIPEID)
	else:
		#changeAtgi(ATGINODE,ATGI_PIPE_NAME+'_'+PIPEID)
		ATGI_PIPE_NAME=cmds.textField('MSG2_railTools_baseRailPartsName',q=True,tx=True)
		MSG2_atgiLoader.main(ATGI_PIPE_NAME+'_'+PIPEID)
	#

def previewCamera():
	SEL = cmds.ls(sl=True)
	RIG = '|locator1'
	XFTR = cmds.xform(SEL,q=True,t=True,ws=True)
	#XFRO = cmds.xform(SEL,q=True,ro=True,ws=True)
	XFRX = cmds.getAttr(SEL[0]+'.rx')
	XFRY = cmds.getAttr(SEL[0]+'.ry')
	XFRZ = cmds.getAttr(SEL[0]+'.rz')

	cmds.xform(RIG,t=XFTR,ws=True)
	cmds.setAttr(RIG+'.rx',XFRX)
	cmds.setAttr(RIG+'.ry',XFRY)
	cmds.setAttr(RIG+'.rz',XFRZ)
	

#################
# Store Recall
#################
def store():
	PREFIX='MSG2_railTools'
	CONTROLNAME='MSG2_railTools_baseRailPartsName'
	NAME=PREFIX+CONTROLNAME
	if cmds.control(CONTROLNAME,ex=True):
		cmds.optionVar(stringValue=[NAME,cmds.textField(CONTROLNAME,q=True,tx=True)])

def recall():
	PREFIX='MSG2_railTools'
	CONTROLNAME='MSG2_railTools_baseRailPartsName'
	NAME=PREFIX+CONTROLNAME
	if cmds.optionVar(exists=NAME):
		cmds.textField(CONTROLNAME,e=True,tx=cmds.optionVar(q=NAME))
		
###############
# UI
###############

def LayoutParallelParts():
	cmds.columnLayout(adj=True)
	cmds.button(l='n',c=lambda *args:parallelParts('n'))
	cmds.button(l='bw',c=lambda *args:parallelParts('bw'))
	cmds.button(l='wb',c=lambda *args:parallelParts('wb'))
	cmds.button(l='bwb',c=lambda *args:parallelParts('bwb'))
	cmds.button(l='wbw',c=lambda *args:parallelParts('wbw'))
	cmds.setParent('..')


def LayoutButtons():
	cmds.gridLayout(nc=5)
	#
	cmds.button(l='lf',c=lambda *args:create('lf'))
	cmds.text(l='')
	cmds.button(l='le',c=lambda *args:create('le'))
	cmds.text(l='')
	cmds.button(l='ld',c=lambda *args:create('ld'))
	#
	cmds.text(l='')
	cmds.button(l='mf',c=lambda *args:create('mf'))
	cmds.button(l='me',c=lambda *args:create('me'))
	cmds.button(l='md',c=lambda *args:create('md'))
	cmds.text(l='')
	#
	cmds.button(l='lg',c=lambda *args:create('lg'))
	cmds.button(l='mg',c=lambda *args:create('mg'))
	cmds.button(l='a',c=lambda *args:create('a'))
	cmds.button(l='mc',c=lambda *args:create('mc'))
	cmds.button(l='lc',c=lambda *args:create('lc'))
	#
	cmds.text(l='')
	cmds.button(l='mh',c=lambda *args:create('mh'))
	cmds.button(l='ma',c=lambda *args:create('ma'))
	cmds.button(l='mb',c=lambda *args:create('mb'))
	cmds.text(l='')
	#
	cmds.button(l='lh',c=lambda *args:create('lh'))
	cmds.text(l='')
	cmds.button(l='la',c=lambda *args:create('la'))
	cmds.text(l='')
	cmds.button(l='lb',c=lambda *args:create('lb'))
	#
	cmds.setParent('..')


def LayoutA():
	cmds.columnLayout('MSG2_railCreator_mainLayout',adj=True,bgc=[0.3,0.35,0.3])
	cmds.separator()
	cmds.text(l='MSG2_railCreator',bgc=[0.8,0.9,0.8],fn='boldLabelFont')
	cmds.text(l='baseRailPartsName')
	cmds.textField('MSG2_railTools_baseRailPartsName',tx='az6_pipe',cc=lambda *args:store())
	LayoutButtons()
	LayoutParallelParts()
	cmds.separator()
	cmds.setParent('..')
	recall()

def UI():
	if cmds.window('MSG2_railTools_window',q=True,ex=True):
		cmds.deleteUI('MSG2_railTools_window')
	cmds.window('MSG2_railTools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MSG2_railTools_window')

	recall()
	
