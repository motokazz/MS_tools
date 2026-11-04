# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_instancer
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import sys
import random

# BpundingBoxからいろいろ取得
def bbcalc(MODE='center',ROT=[0,0,0]):
	# BBCenter Rotation OriginScale BBScale CenterGaps
	TRN = [ 0.0 , 0.0 , 0.0 , 0.0 , 0.0 , 0.0 , 1.0 , 1.0 , 1.0 , 1.0 , 1.0 , 1.0 , 0.0 , 0.0 , 0.0]

	if not cmds.ls(sl=True):
		return TRN

	# get Rotation
	
	OTRN =  cmds.xform(q=True,t=True,ws=True)

	OROT = cmds.xform(q=True,ro=True,ws=True)
	cmds.xform(ro=ROT,os=True)
	BB =  cmds.xform(q=True,bb=True,ws=True)
	cmds.xform(ro=OROT,ws=True)


	if BB:
		TRN=[]

		if MODE=='origin':
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

def objectReplace(SOURCE=''):
	def RET(dummy=''):

		result = []

		TARGET = cmds.ls(sl=True,tr=True,l=True)

		#options
		VCOLOR_CHECK = cmds.checkBox('MS_instancer_VCOLOR',q=True,v=True)
		INST_CHECK = cmds.checkBox('MS_instancer_INSTANCE',q=True,v=True)
		SCALE_BY_BB = cmds.checkBox ('MS_instancer_ScaleByBoundingBox',q=True,v=True )
		
		for each in TARGET:
			# ditect target
			TARGET_PARENT=cmds.listRelatives(each,p=True,f=True)

			#duplicate
			if INST_CHECK:
				RESULT_OBJ=cmds.instance(SOURCE)
			else:
				RESULT_OBJ=cmds.duplicate(SOURCE,rc=True)
				#頂点カラーサンプル
				if VCOLOR_CHECK:
					VCOLORRGB=cmds.polyColorPerVertex(each+'.vtx[0]',q=True,rgb=True)
					cmds.polyColorPerVertex(RESULT_OBJ[0] , rgb=[VCOLORRGB[0],VCOLORRGB[1],VCOLORRGB[2]])

			# Scale mode

			if SCALE_BY_BB:	# BB
				#ターゲット移動値取得
				cmds.select(each,r=True)
				BB =  bbcalc()
				cmds.select(RESULT_OBJ,r=True)
				NBB =  bbcalc()

				# Translate
				cmds.xform(RESULT_OBJ,t=[BB[0],BB[1],BB[2]],ws=True)
				# Rotate
				cmds.xform(RESULT_OBJ,ro=[BB[3],BB[4],BB[5]],ws=True)
				# Scale

				BBX,BBY,BBZ = 1,1,1

				if BB[9] == 0 or NBB[9] == 0:
					BBX = 1
				else:
					BBX = BB[9]/NBB[9]

				if BB[10] == 0 or NBB[10] == 0:
					BBY = 1
				else:
					BBY = BB[10]/NBB[10]

				if BB[11] == 0 or NBB[11] == 0:
					BBZ = 1
				else:
					BBZ = BB[11]/NBB[11]	

				cmds.xform(RESULT_OBJ,s=[BBX,BBY,BBZ],ws=True)
				#cmds.move(-BB[12]-NBB[12],-BB[13]-NBB[13],-BB[14]-NBB[14],RESULT_OBJ,r=True,os=True)
				cmds.move(-NBB[12],-NBB[13],-NBB[14],RESULT_OBJ,xyz=True,r=True,os=True)
			else:
				#ターゲット移動値取得
				cmds.select(each,r=True)
				BB =  bbcalc(MODE='origin')

				# Translate
				cmds.xform(RESULT_OBJ,t=[BB[0],BB[1],BB[2]],ws=True)
				# Rotate
				cmds.xform(RESULT_OBJ,ro=[BB[3],BB[4],BB[5]],ws=True)
				# Scale				
				cmds.xform(RESULT_OBJ,s=[BB[6],BB[7],BB[8]],ws=True)

			cmds.setAttr( (RESULT_OBJ[0]+'.visibility') , cmds.getAttr (each+'.visibility'))


			#parent
			NEW_PARENT=cmds.listRelatives(RESULT_OBJ,p=True,f=True)
			if TARGET_PARENT:
				if len(TARGET_PARENT)>0:
					if NEW_PARENT:
						if not NEW_PARENT[0] == TARGET_PARENT[0]:
							cmds.parent(RESULT_OBJ[0],TARGET_PARENT[0])
							result.append(cmds.ls(sl=True,l=True)[0])
				else:
					cmds.parent(RESULT_OBJ[0],w=True)
					result.append(RESULT_OBJ[0])

			#result.append(cmds.ls(sl=True,l=True)[0])
			#元オブジェクトctrl キー押しながらで削除(swap)
			mods = cmds.getModifiers();
			if (mods & 4) > 0:cmds.delete(each)

			cmds.select(result,r=True)

				


			
	return RET

def instanceReplace(SOURCE=[]):
	#デュプリケーター本体
	SOURCE= cmds.textFieldGrp('MS_instancer_TFGTgt',q=True,tx=True).split(';')
	TARGET = cmds.ls(sl=True,tr=True,l=True)

	#options
	RANDCHECK = cmds.checkBox('MS_instancer_RandmizeObject',q=True,v=True)
	VCOLOR_CHECK = cmds.checkBox('MS_instancer_VCOLOR',q=True,v=True)
	INST_CHECK = cmds.checkBox('MS_instancer_INSTANCE',q=True,v=True)
	SCALE_BY_BB = cmds.checkBox ('MS_instancer_ScaleByBoundingBox',q=True,v=True )


	RESULT_OBJ = []

	for each in TARGET:
		#ランダムチェック
		if len(SOURCE)==1:
			RAND=0;
		elif RANDCHECK:
			RAND = random.randint(0,len(SOURCE)-1)
		else:
			RAND+=1

		#duplicate
		NOW_SOURCE=SOURCE[RAND]
		TARGET_PARENT=cmds.listRelatives(each,p=True,f=True)
		if INST_CHECK:
			RESULT_OBJ=cmds.instance(NOW_SOURCE)
		else:
			RESULT_OBJ=cmds.duplicate(NOW_SOURCE,rc=True)
			#頂点カラーサンプル
			if VCOLOR_CHECK:
				VCOLORRGB=cmds.polyColorPerVertex(each+'.vtx[0]',q=True,rgb=True)
				cmds.polyColorPerVertex(RESULT_OBJ[0] , rgb=[VCOLORRGB[0],VCOLORRGB[1],VCOLORRGB[2]])
			

		#ターゲット移動値取得
		
		cmds.select(each,r=True)
		BB =  bbcalc()
		cmds.select(RESULT_OBJ,r=True)
		NBB =  bbcalc()
		
		# Translate

		#cmds.xform(RESULT_OBJ,t=[BB[0]-NBB[0],BB[1]-NBB[1],BB[2]-NBB[2]],ws=True)
		cmds.xform(RESULT_OBJ,t=[BB[0],BB[1],BB[2]],ws=True)

		#trn = cmds.xform(each,q=True,t=True,ws=True,a=True)
		#cmds.xform(RESULT_OBJ[0],t=trn,ws=True)
		
		# Rotate
		cmds.xform(RESULT_OBJ,ro=[BB[3],BB[4],BB[5]],ws=True)

		# Scale mode

		if SCALE_BY_BB:	# BB
			cmds.xform(RESULT_OBJ,s=[BB[9]/NBB[9],BB[10]/NBB[10],BB[11]/NBB[11]],ws=True)
		else:
			cmds.xform(RESULT_OBJ,s=[BB[6],BB[7],BB[8]],ws=True)

		cmds.setAttr( (RESULT_OBJ[0]+'.visibility') , cmds.getAttr (each+'.visibility'))


		#parent
		NEW_PARENT=cmds.listRelatives(RESULT_OBJ,p=True,f=True)
		if TARGET_PARENT:
			if NEW_PARENT:
				if not NEW_PARENT[0] == TARGET_PARENT[0]:
					cmds.parent(RESULT_OBJ[0],TARGET_PARENT[0])
			else:
				cmds.parent(RESULT_OBJ[0],TARGET_PARENT[0])


		#元オブジェクトctrl キー押しながらで削除(swap)
		mods = cmds.getModifiers();
		if (mods & 4) > 0:cmds.delete(each)

def clickTargetList():
	#パーツリスト取得
	SEL = cmds.ls(sl=True,l=True,typ='transform')
	cmds.textFieldGrp('MS_instancer_TFGTgt',e=True,tx=';'.join(SEL))
	updateObjectList(SEL)

def addTargetList():
	PRE = cmds.textFieldGrp('MS_instancer_TFGTgt',q=True,tx=True)
	NOW = PRE.split(';')
	SEL = cmds.ls(sl=True,l=True,typ='transform')
	NOW.extend(SEL)
	cmds.textFieldGrp('MS_instancer_TFGTgt',e=True,tx=';'.join(NOW))
	updateObjectList(NOW)

def updateObjectList(SEL=[]):
	if cmds.scrollLayout('MS_instancer_objectList_scrollLayout',q=True,ex=True):
		cmds.deleteUI('MS_instancer_objectList_scrollLayout')
	cmds.scrollLayout('MS_instancer_objectList_scrollLayout',p='MS_instancer_objectList_mainLayout')
	for each in SEL:
		cmds.button(l=each.split('|')[-1],c=objectReplace(each))
	cmds.setParent('..')

# BBRotator
def BBRotator(ROT=[0,0,0]):
	BB =	bbcalc()
	NBB =  bbcalc(ROT=ROT)
	

	orign_translate = cmds.xform(q=True,t=True,ws=True)
	origin_bb = cmds.xform(q=True,bb=True,ws=True)
	origin_bbc=[(origin_bb[0]+origin_bb[3])*0.5,(origin_bb[1]+origin_bb[4])*0.5,(origin_bb[2]+origin_bb[5])*0.5]
	#
	cmds.xform(ro=ROT,r=True,os=True,cp=False)

	if ROT[0]>45 or ROT[0]<-45: #X
		cmds.xform(s=[BB[9]/NBB[9],BB[11]/NBB[11],BB[10]/NBB[10]],r=True)

	if ROT[1]>45 or ROT[1]<-45: #Y
		cmds.xform(s=[BB[11]/NBB[11],BB[10]/NBB[10],BB[9]/NBB[9]],r=True)

	if ROT[2]>45 or ROT[2]<-45: #Z
		cmds.xform(s=[BB[10]/NBB[10],BB[9]/NBB[9],BB[11]/NBB[11]],r=True)


	result_bb = cmds.xform(q=True,bb=True,ws=True)
	result_bbc = [(result_bb[0]+result_bb[3])*0.5,(result_bb[1]+result_bb[4])*0.5,(result_bb[2]+result_bb[5])*0.5]

	cmds.xform(t=[orign_translate[0]+origin_bbc[0]-result_bbc[0],orign_translate[1]+origin_bbc[1]-result_bbc[1],orign_translate[2]+origin_bbc[2]-result_bbc[2]],ws=True)

def pre_BBRotator(ROT=[0,0,0]):
	sel = cmds.ls(sl=True,l=True)
	
	for each in sel:
		cmds.select(each,r=True)
		BBRotator(ROT)
	cmds.select(sel,r=True)


def bestBBRotator():
	sel = cmds.ls(sl=True,l=True)
	
	for each in sel:
		cmds.select(each,r=True)
		bestBBRotator_core()
	cmds.select(sel,r=True)

def bestBBRotator_core():
	original_translation=cmds.xform(q=True,t=True,ws=True)
	original_rotation=cmds.xform(q=True,ro=True,ws=True)
	original_scale=cmds.xform(q=True,s=True,ws=True)
	#BB = bbcalc()
	rotation_axis=[[0,0,0],[90,0,0],[0,90,0],[0,0,90]]
	result_rotation=[0,0,0]
	
	MAX = 9999999999999.0
	for each in rotation_axis:

		BBRotator(ROT=each)

		gets = cmds.getAttr('.s')[0]
		
		now_max = gets[0]+gets[1]+gets[2]
		
		if  now_max < MAX:
			MAX=now_max
			result_rotation=each


		cmds.xform(t=original_translation,ws=True)
		cmds.xform(ro=original_rotation,ws=True)
		cmds.xform(s=original_scale,ws=True)
	
	BBRotator(ROT=result_rotation)

# UI
def Layout_BBRotator():
	cmds.frameLayout('MS_instancer_BBRotator_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='BBRotator',cll=True,cl=False)
	cmds.columnLayout('MS_instancer_BBRotator_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='BBRotator',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	
	cmds.rowLayout(nc=2,cw2=[100,200])

	#
	cmds.gridLayout(nc=2)
	cmds.button(l='x 90',c=lambda *args:pre_BBRotator(ROT=[90,0,0]))
	cmds.button(l='x-90',c=lambda *args:pre_BBRotator(ROT=[-90,0,0]))
	cmds.button(l='y 90',c=lambda *args:pre_BBRotator(ROT=[0,90,0]))
	cmds.button(l='y-90',c=lambda *args:pre_BBRotator(ROT=[0,-90,0]))
	cmds.button(l='z 90',c=lambda *args:pre_BBRotator(ROT=[0,0,90]))
	cmds.button(l='z-90',c=lambda *args:pre_BBRotator(ROT=[0,0,-90]))
	cmds.setParent('..')
	#
	cmds.button(l='bestBBRotator',h=80,c=lambda *args:bestBBRotator())
	cmds.setParent('..')

	cmds.setParent('..')
	cmds.setParent('..')	

def Layout_objectList():
	cmds.frameLayout('MS_instancer_objectList_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_instancer',cll=True,cl=False)
	cmds.columnLayout('MS_instancer_objectList_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='objectList',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	#
	cmds.scrollLayout('MS_instancer_objectList_scrollLayout')
	cmds.setParent('..')
	#
	cmds.setParent('..')
	cmds.setParent('..')

def LayoutA():
	cmds.frameLayout('MS_instancer_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_instancer',cll=True,cl=False)
	cmds.columnLayout('MS_instancer_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_instancer',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.button('MS_instancer_CLCTgt',l='parts',bgc=[1,1,1],w=200,al='center',c=lambda *args:clickTargetList())
	cmds.button(l='add',bgc=[0.7,0.8,1],w=200,al='center',c=lambda *args:addTargetList())

	cmds.textFieldGrp('MS_instancer_TFGTgt',en=False,cw=[1,200])
	
	cmds.separator(w=200)

	cmds.checkBox( 'MS_instancer_RandmizeObject',l='RandmizeObject',v=True)
	cmds.text(l='RotationMethod')
	cmds.radioButtonGrp( 'ROTMETHOD'
		,cw3=[50,70,70]
		,numberOfRadioButtons=3
		,labelArray3=['none','constraint','MSmethod']
		,sl =True
		)
	
	cmds.checkBox ('MS_instancer_VCOLOR',v=0 ,l='VERTX COLOR' )
	cmds.checkBox ('MS_instancer_INSTANCE',v=0 ,l='INSTANCE' )
	cmds.checkBox ('MS_instancer_ScaleByBoundingBox',v=0 ,l='ScaleByBoundingBox' )
	
	cmds.separator(w=200) 
	cmds.button (bgc=[ 0.9,1,0.9] ,al = 'center' ,l = 'DuplicateReplace' ,w=200 ,h = 20 ,c =lambda *args:instanceReplace(),ann = 'オブジェクト差し替え。Shiftキー押しながらで元オブジェクト残す')
	
	cmds.setParent('..')




	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_instancer_window',q=True,ex=True):
		cmds.deleteUI('MS_instancer_window')
	cmds.window('MS_instancer_window',rtf=True,s=True)
	
	LayoutA()
	Layout_objectList()
	Layout_BBRotator()

	cmds.showWindow('MS_instancer_window')
	