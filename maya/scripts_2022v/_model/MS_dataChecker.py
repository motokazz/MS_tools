# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_dataChecker.py
# 説明
#			
#			
# 作成日
#			
########################################
	
import maya.cmds as cmds
import maya.mel as mel

import math

import MSG2_LODTools.MS_polyUnite as MS_polyUnite
reload(MS_polyUnite)

import dfx_polyCalc
reload(dfx_polyCalc)

#import s2000_tools.MSG2_sceneCleanup_compornents.MSG2_loadPlugin as MSG2_loadPlugin
#reload(MSG2_loadPlugin)

#################
# LOAD PLUGIN
#################
#MSG2_loadPlugin.main()


#################
# IO
#################
def SAVE(ROW=[],FILE_PATH=''):
	f=open(FILE_PATH,'w')#'r'読み込み：'w'書き込み：'a'追記：'+'読み書き両方' 't'テキストモード：'b'バイナリーモード
	for each in ROW:
		f.write(each+'\n')
	f.close()


#################
# polyCalc
#################

def HULL(TARGETS=[],MAX_VTX=60):
	for each in TARGETS:
		cmds.select(each,r=True)
		print each
		mel.eval('hkCmdCreateConvexHull -mv %s'%MAX_VTX)
	return cmds.ls(dag=True,tr=True)[-1]

def calcPolyScale():
	CPS=dfx_polyCalc.calcPolyScale()
	scaleResult=[]
	targetList = cmds.ls(sl=True)
	for x in targetList:					
		scaleResult.append(CPS.doIt_PolyScale(x))

	print scaleResult

def calcPolyScaleCombinedHull(NODES=[]):
	cmds.duplicate(NODES)
	DUPED=cmds.ls(sl=True,l=True)
	#メッシュが一個だったときの処理
	MESH=cmds.ls(DUPED,type='mesh',dag=True,l=True)

	if not len(MESH):
		return 0
	elif len(MESH)==1:
		CONBINED=cmds.listRelatives(MESH,p=True,f=True)
	elif len(MESH)>1:
		cmds.select(DUPED,r=True)
		CONBINED=cmds.polyUnite(ch=False)

	cmds.select(CONBINED,r=True)

	HULL_OBJ=HULL([CONBINED])

	cmds.select(HULL_OBJ,r=True)

	CPS=dfx_polyCalc.calcPolyScale()
	scaleResult=[]
	targetList = cmds.ls(sl=True)
	for x in targetList:					
		scaleResult.append(CPS.doIt_PolyScale(x))

	cmds.delete(CONBINED)
	cmds.delete(HULL_OBJ)

	try:
		cmds.delete(DUPED)
	except:
		pass

	print math.sqrt(scaleResult[0])
	#print math.sqrt(scaleResult[0])
	return math.sqrt(scaleResult[0])

#################
# BBVolume
#################

def BBMesure_multi(OBJS):
	if not OBJS:
		return [1,1,1]
	#ポリゴンバウンディングボックス面積
	BB=BBMulti(OBJS)
	RET=[(BB[3]-BB[0]),(BB[4]-BB[1]),(BB[5]-BB[2])]
	return RET

def BBVolume_multi(OBJS):
	RET=0
	for EACH in OBJS:
		try:
			P=cmds.listRelatives(EACH,p=True)[0]
			BB=cmds.xform(P,q=True,ws=True,bb=True,a=True)
			bbsize=[(BB[3]-BB[0]),(BB[4]-BB[1]),(BB[5]-BB[2])]
			bbvolm=math.sqrt(math.sqrt(bbsize[0]*bbsize[1]*bbsize[2]))
			RET+=bbvolm
		except:
			pass
	return RET

#複数のオブジェクトのバウンディングボックスを返す。
def BBMulti(OBJS):
	BB=cmds.xform(OBJS[0],q=True,ws=True,bb=True,a=True)
	for each in OBJS[1:]:#マルチ選択対応
		preBB=cmds.xform(each,q=True,ws=True,bb=True,a=True)
		if preBB[0]<BB[0]:BB[0]=preBB[0]
		if preBB[1]<BB[1]:BB[1]=preBB[1]
		if preBB[2]<BB[2]:BB[2]=preBB[2]
		if preBB[3]>BB[3]:BB[3]=preBB[3]
		if preBB[4]>BB[4]:BB[4]=preBB[4]
		if preBB[5]>BB[5]:BB[5]=preBB[5]
		print preBB
	return BB

def atgiBB(OBJS):
	ATGI=cmds.listRelatives(type='GraviteAtgiLocatorNode',f=True)


#################
# 工数計算
#################

def kousu(bbvolm=1.0):
	if bbvolm>400:return 5
	if bbvolm>300:return 4
	if bbvolm>200:return 3
	if bbvolm>100:return 2
	return 1

def kousuMODEL(TOTAL):
	return ((TOTAL*0.6*4)//1)*0.25

def kousuUV(TOTAL):
	if TOTAL<1:
		return 'T'
	if TOTAL<2:
		return 'S'
	if TOTAL<5:
		return 'M'
	if TOTAL<10:
		return 'L'
	if TOTAL<15:
		return 'X'

	return 'XX'

def kousuTEX(TOTAL):
	if TOTAL<1:
		return 'T'
	if TOTAL<2:
		return 'S'
	if TOTAL<5:
		return 'M'
	if TOTAL<10:
		return 'L'
	if TOTAL<15:
		return 'X'
	if TOTAL<20:
		return 'XX'
	if TOTAL<40:
		return '3X'
	if TOTAL<50:
		return '4X'
	return '5X'

def kousuOPTTEX(TOTAL):
	if TOTAL<2:
		return 'T'
	if TOTAL<5:
		return 'S'
	if TOTAL<10:
		return 'M'
	if TOTAL<15:
		return 'L'
	return 'X'

def kousuLOD(TOTAL):
	return ''

def kousuZ(TOTAL):
	if TOTAL<20:
		return 'M'
	return 'L'

def kousuCOL(TOTAL):
	if TOTAL<2:
		return 'T'
	if TOTAL<5:
		return 'S'
	if TOTAL<10:
		return 'M'
	if TOTAL<15:
		return 'L'
	if TOTAL<20:
		return 'X'

	return 'XX'


def kousuFromBBVM(BBVM):
	#180は1日を最低換算
	return (BBVM)*0.01

#################
# MAIN
#################



def dataChecker():
	sel=cmds.ls(sl=True,l=True)
	id=0
	dat=['id,name,bbVolume','zantei']

	MODEL_SIMPLENESS=cmds.floatField('MODEL_SIMPLENESS',q=True,v=True)

	for each in sel:
		name=each.split('|')[-1]

		#マルチ選択用、子供が複数ぶら下がっているときのためにマルチBBを使う。
		#TRN=[]
		#MESHES=cmds.ls(each,sl=True,dag=True,type='mesh')
		#for eachMesh in MESHES:
		#	TRN.append(cmds.listRelatives(eachMesh,p=True,f=True)[0])

		#bbvolm
		#BB=BBMulti(TRN)
		#bbsize=[(BB[3]-BB[0]),(BB[4]-BB[1]),(BB[5]-BB[2])]
		#bbvolm=math.sqrt(math.sqrt(bbsize[0]*bbsize[1]*bbsize[2]))

		#vtxcnt=cmds.polyEvaluate(each,v=True)
		#dat.append(str(id)+','+name+','+str(bbsize[0])+','+str(bbsize[0])+','+str(bbsize[0])+','+str(bbvolm)+','+str(vtxcnt))

		#BBVolm_multi
		#BBVM=BBVolume_multi(MESHES)

		#工数自動作成
		#KOUSU=kousu(bbvolm)
		#TOTAL=kousuFromBBVM(BBVM)

		#TOTAL=math.pow(calcPolyScaleCombinedHull(),2)*0.00000015*MODEL_SIMPLENESS
		TOTAL=calcPolyScaleCombinedHull(each)*0.002*MODEL_SIMPLENESS

		#dat.append(str(id)+','+name+','+str(bbvolm)+','+str(KOUSU)+','+'|'+','+str(BBVM)+','+str(TOTAL))
		print name+'\t'+str(TOTAL)
		dat.append(str(id)+'\t'+name+'\t'+str(kousuMODEL(TOTAL))+'\t'+kousuUV(TOTAL)+'\t'+kousuTEX(TOTAL)+'\t'+kousuOPTTEX(TOTAL)+'\t'+kousuLOD(TOTAL)+'\t'+kousuZ(TOTAL)+'\t'+kousuCOL(TOTAL))
		id+=1
		
	objcount=len(sel)

	for each in dat:
		print each
		
	#return dat
	SAVE(dat,'D:/MS_tools/maya/scripts/_model/MS_dataChecker.csv')

def LayoutA():
	cmds.columnLayout('MS_tools_mainLayout',adj=True)

	#cmds.text(l=u'リピートレベル')
	#cmds.floatField('MODEL_REPEAT_LEVEL',v=1)

	cmds.text(l=u'単純さ')
	cmds.floatField('MODEL_SIMPLENESS',v=1)
	
	#cmds.text(l=u'質感の種類')
	#cmds.floatField('MATERIAL_SIMPLENESS',v=1)

	#cmds.text(l=u'質感の種類')
	#cmds.floatField('MATERIAL_SIMPLENESS',v=1)

	cmds.button(l='dataChecker',c=lambda *args:dataChecker())
	
	cmds.separator(w=200)
	cmds.button(l='calcPolyScaleCombinedHull',c=lambda *args:calcPolyScaleCombinedHull())
	cmds.button(l='calcPolyScale',c=lambda *args:calcPolyScale())

	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	

