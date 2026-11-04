# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_BBfilter.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import MS_polyUnite
reload(MS_polyUnite)


#### 	BBUTIL ###

def BBMesure(FACE,MIN=1):
	#ポリゴンバウンディングボックス面積
	BB=cmds.xform(FACE,q=True,bb=True,ws=False)
	X=(BB[3]-BB[0])
	Y=(BB[4]-BB[1])
	Z=(BB[5]-BB[2])

	if X<MIN:X=MIN
	if Y<MIN:Y=MIN
	if Z<MIN:Z=MIN

	RET=(X*Y*Z)
	return RET

def getFaces(COMP):#フェース選択
	FACE=cmds.polyListComponentConversion(COMP,tf=True)
	if not FACE:
		return False
	cmds.select(FACE,r=True)
	result=cmds.filterExpand(FACE,ex=True,sm=34)
	return result
	
def BBMesure_new(OBJ,MIN=1):
	if not OBJ:
		return [1,1,1]
	FACE=getFaces(OBJ)
	if not FACE:
		return False
	#ポリゴンバウンディングボックス面積
	cmds.select(FACE,r=True)
	BB=cmds.polyEvaluate(bc=True)
	
	X=(BB[0][1]-BB[0][0])
	Y=(BB[1][1]-BB[1][0])
	Z=(BB[2][1]-BB[2][0])

	if X<MIN:X=MIN
	if Y<MIN:Y=MIN
	if Z<MIN:Z=MIN

	RET=(X*Y*Z)
	
	return RET

def atgiBB(ATGI):
	SHAPE=cmds.listRelatives(ATGI,s=True)
	BBMIN = cmds.getAttr(SHAPE[0]+'.boundingBoxMin')
	BBMAX = cmds.getAttr(SHAPE[0]+'.boundingBoxMax')
	RET=((BBMAX[0][0]-BBMIN[0][0])*(BBMAX[0][1]-BBMIN[0][1])*(BBMAX[0][2]-BBMIN[0][2]))
	return RET

def bbsize(OBJ):
	DICT={}
	for EACH in OBJ:
		NUM=0
		if not cmds.objExists(EACH):
			continue

		#Atgiロケータチェック
		if cmds.nodeType(EACH)=='mesh':
			if cmds.nodeType(EACH)=='mesh':#メッシュ選択防止
				EACH=cmds.listRelatives(EACH,p=True,type='transform',f=True)[0]
			NUM = BBMesure(EACH)
		else:
			SHAPE=cmds.listRelatives(EACH,s=True,f=True)
			if SHAPE:
				if cmds.nodeType(SHAPE[0])=='GraviteAtgiLocatorNode' or cmds.nodeType(EACH)=='GraviteAtgiLocatorNode':
					#NUM = atgiBB(EACH)
					continue
				elif cmds.nodeType(SHAPE[0])=='mesh':
					NUM = BBMesure(EACH)
		
		if not NUM in DICT.keys():
			DICT[NUM]=[]
		DICT[NUM].append(EACH)
	return DICT
	
def bbfilter(OBJ,MIN=-1,MAX=-1):
	print 'bb'
	
	DICT=bbsize(OBJ)
	#print DICT
	LIST=[]
	for EACHKEY in DICT.keys():
		if MIN<0 and MAX<0:#単純にメッシュオブジェクト全部を返す
			LIST.extend(DICT[EACHKEY])
		elif float(EACHKEY)>=MIN and MAX<0:#最小値のみ考慮
			LIST.extend(DICT[EACHKEY])
		elif MIN<0 and float(EACHKEY)<=MAX:#最大値のみ考慮
			LIST.extend(DICT[EACHKEY])
		elif float(EACHKEY)>=MIN and float(EACHKEY)<=MAX:#最小値、最大値を考慮
			LIST.extend(DICT[EACHKEY])

	#print LIST
	cmds.select(clear=True)
	if LIST:
		cmds.select(LIST,r=True)
	print LIST
	return LIST
	

#### 	ATTR UTIL ###

def setLODAttr(TARGETS=[],MAX=2,MIN=1):
	for each in TARGETS:
		if not cmds.attributeQuery("LodLevelMax",node=each,ex=True):
			cmds.addAttr(each,ln="LodLevelMax",at='long')
		if not cmds.attributeQuery("LodLevelMin",node=each,ex=True):
			cmds.addAttr(each,ln="LodLevelMin",at='long')
		cmds.setAttr(each+".LodLevelMax",MAX)
		cmds.setAttr(each+".LodLevelMin",MIN)

		if MAX==2 and MIN==1:
			cmds.color(each,ud=3)
		elif MAX==3 and MIN==1:
			cmds.color(each,ud=3)
		elif MAX==4 and MIN==1:
			cmds.color(each,ud=6)
		elif MAX==5 and MIN==1:
			cmds.color(each,ud=6)
		elif MAX==6 and MIN==1:
			cmds.color(each,ud=8)
		elif MAX==7 and MIN==1:
			cmds.color(each,ud=8)

		elif MAX==8 and MIN==3:
			cmds.color(each,ud=4)
		elif MAX==8 and MIN==4:
			cmds.color(each,ud=4)
		elif MAX==8 and MIN==5:
			cmds.color(each,ud=5)
		elif MAX==8 and MIN==6:
			cmds.color(each,ud=5)
		elif MAX==8 and MIN==7:
			cmds.color(each,ud=7)

def removeExceptionsFromSelection(OBJS,FILTER_WORDS=['pre_atgi','keep_conbine','|low','|high']):
	RET=[]
	EXP=[]
	for each in OBJS:
		if not cmds.objExists(each):
			continue

		if cmds.polyColorSet(each,q=True,acs=True): #ColorSetあり
			EXP.append(each)
			continue

		#FILTER_WORDS
		for EACH_FILTER_WORD in FILTER_WORDS:
			if EACH_FILTER_WORD in each: #pre_atgi
				EXP.append(each)
				continue

		RET.append(each)
	return RET



#################
# MAIN
#################
def createConbine(SEL=[],NAME='lodNear0',LODATTR_MIN=1,LODATTR_MAX=2,VMIN=0,VMAX=1000,):
	#root内のモデルの指定BBボリューム内のもデルをコンバイン
	RESULT=[]
	bbfilter(SEL,MIN=VMIN,MAX=VMAX)
	try:
		
		SEL=cmds.ls(sl=True,l=True)
		
		if not SEL:
			return

		if len(SEL)>1:
			UNITED=MS_polyUnite.MS_superPolyUnite()
			i=0
			for i in range(len(UNITED)):
				if cmds.listRelatives(UNITED[i],p=True):
					UNITED[i]=cmds.parent(UNITED[i],w=True)
				UNITED[i]=cmds.rename(UNITED[i],NAME)
		else:
			if cmds.listRelatives(SEL,p=True):
				UNITED=cmds.parent(SEL,w=True)
			else:
				UNITED=SEL
			cmds.rename(UNITED,NAME)
			UNITED=cmds.ls(sl=True,l=True)

		setLODAttr(UNITED,LODATTR_MAX,LODATTR_MIN)

		RESULT.extend(UNITED)

	except:
		pass

	return RESULT

def createDupConbine(NAME='lodNear0',LODATTR_MIN=1,LODATTR_MAX=2,VMIN=0,VMAX=1000,):
	#root内のモデルの指定BBボリューム内のもデルをデュプリケートしてコンバイン
	RESULT=[]
	try:
		SEL=cmds.ls('root',lf=True,dag=True,type='mesh',l=True)
		bbfilter(SEL,MIN=VMIN,MAX=VMAX)
		cmds.duplicate()
		SEL=cmds.ls(sl=True,l=True)
		if len(SEL)>2:
			UNITED=MS_polyUnite.MS_superPolyUnite()
			i=0
			for i in range(len(UNITED)):
				if cmds.listRelatives(UNITED[i],p=True):
					UNITED[i]=cmds.parent(UNITED[i],w=True)
				UNITED[i]=cmds.rename(UNITED[i],NAME)
		else:
			UNITED=cmds.parent(SEL,w=True)
			cmds.rename(UNITED,NAME)
			UNITED=cmds.ls(sl=True,l=True)

		setLODAttr(UNITED,LODATTR_MAX,LODATTR_MIN)

		RESULT.extend(UNITED)

	except:
		pass

	return RESULT

def createMeshLOD_Grouping(OBJ=[]):
	#createGroups
	if not cmds.objExists('|root'):
		cmds.group(em=True,n='root')
	if not cmds.objExists('|root|high'):
		cmds.group(em=True,n='high')
		cmds.parent('|high','root')

	cmds.parent(OBJ,'|root|high')

def createMeshLOD_lowGrouping(OBJ=[]):
	#createGroups
	if not cmds.objExists('|root'):
		cmds.group(em=True,n='root')
	if not cmds.objExists('|root|low'):
		cmds.group(em=True,n='templow')
		cmds.parent('|templow','root')
		cmds.rename('|root|templow','low')

	if cmds.listRelatives(OBJ,p=True,f=True):
		if cmds.listRelatives(OBJ,p=True,f=True)[0]=='|root|low':
			return

	cmds.parent(OBJ,'|root|low')

def createLowModel_Grouping(OBJ=[]):
	#createGroups
	if not cmds.objExists('|low'):
		cmds.group(em=True,n='low')

	cmds.parent(OBJ,'|low')

def setAttrToAtgi(SELECTIONMODE='root'):
	if SELECTIONMODE=='selection':
		SEL=cmds.ls(sl=True,tr=True,dag=True,type='GraviteAtgiLocatorNode',l=True)
	else:
		SEL=cmds.ls(SELECTIONMODE,tr=True,dag=True,type='GraviteAtgiLocatorNode',l=True)

	for each in SEL:
		SHAPE=cmds.listRelatives(each,s=True,f=True)
		if SHAPE:
			if cmds.nodeType(SHAPE[0])=='GraviteAtgiLocatorNode':
				setLODAttr([each],6,1)

def forceCreation(NAME='lod_near0',LODATTR_MIN=1,LODATTR_MAX=8):
	SEL=cmds.ls(sl=True,lf=True,dag=True,type='mesh',l=True)
	COMB=createConbine(SEL,NAME,LODATTR_MIN,LODATTR_MAX,VMIN=0,VMAX=9999999999999999999999999999999999999)
	if COMB:
		createMeshLOD_Grouping(COMB)

def forceLowModel():
	UNITED=MS_polyUnite.MS_superPolyUnite()
	setLODAttr(UNITED,8,5)
	UNITED=cmds.rename(UNITED,'lod_lowmesh')
	createMeshLOD_lowGrouping(UNITED)
	
def main(SELECTIONMODE='root'):
	RESULT=[]
	SEL=cmds.ls(sl=True)
	if SELECTIONMODE=='selection':
		SEL=removeExceptionsFromSelection(cmds.ls(SEL,sl=True,lf=True,dag=True,type='mesh',l=True),FILTER_WORDS=[])
	else:
		SEL=removeExceptionsFromSelection(cmds.ls(SELECTIONMODE,lf=True,dag=True,type='mesh',l=True))
	#
	COMB=createConbine(SEL,NAME='lod_near0',LODATTR_MIN=1,LODATTR_MAX=2,VMIN=0,VMAX=1000)
	if COMB:RESULT.extend(COMB)
	#
	COMB=createConbine(SEL,NAME='lod_middle0',LODATTR_MIN=1,LODATTR_MAX=4,VMIN=0,VMAX=1000000)
	if COMB:RESULT.extend(COMB)
	#
	COMB=createConbine(SEL,NAME='lod_far0',LODATTR_MIN=1,LODATTR_MAX=4,VMIN=0,VMAX=9999999999999999999999999999999999999)
	if COMB:RESULT.extend(COMB)

	setAttrToAtgi()

	if RESULT:
		createMeshLOD_Grouping(RESULT)
		return True
	else:
		return False

def superLOD(SELECTIONMODE='root'):
	RESULT=[]
	if SELECTIONMODE=='selection':
		SEL=removeExceptionsFromSelection(cmds.ls(sl=True,lf=True,dag=True,type='mesh',l=True))
	else:
		SEL=removeExceptionsFromSelection(cmds.ls(SELECTIONMODE,lf=True,dag=True,type='mesh',l=True))

	COMB=createConbine(SEL,NAME='lod_12lv0',LODATTR_MIN=1,LODATTR_MAX=2,VMIN=0,VMAX=1000)
	if COMB:RESULT.extend(COMB)
	COMB=createConbine(SEL,NAME='lod_13lv0',LODATTR_MIN=1,LODATTR_MAX=3,VMIN=0,VMAX=2000)
	if COMB:RESULT.extend(COMB)
	COMB=createConbine(SEL,NAME='lod_14lv0',LODATTR_MIN=1,LODATTR_MAX=4,VMIN=0,VMAX=4000)
	if COMB:RESULT.extend(COMB)
	COMB=createConbine(SEL,NAME='lod_15lv0',LODATTR_MIN=1,LODATTR_MAX=5,VMIN=0,VMAX=8000)
	if COMB:RESULT.extend(COMB)
	COMB=createConbine(SEL,NAME='lod_16lv0',LODATTR_MIN=1,LODATTR_MAX=6,VMIN=0,VMAX=10000)
	if COMB:RESULT.extend(COMB)

	COMB=createConbine(SEL,NAME='lod_170lv0',LODATTR_MIN=1,LODATTR_MAX=7,VMIN=0,VMAX=25000)
	if COMB:RESULT.extend(COMB)
	COMB=createConbine(SEL,NAME='lod_171lv0',LODATTR_MIN=1,LODATTR_MAX=7,VMIN=0,VMAX=50000)
	if COMB:RESULT.extend(COMB)
	COMB=createConbine(SEL,NAME='lod_172lv0',LODATTR_MIN=1,LODATTR_MAX=7,VMIN=0,VMAX=100000)
	if COMB:RESULT.extend(COMB)

	COMB=createConbine(SEL,NAME='lod_180lv0',LODATTR_MIN=1,LODATTR_MAX=8,VMIN=0,VMAX=250000)
	if COMB:RESULT.extend(COMB)
	COMB=createConbine(SEL,NAME='lod_181lv0',LODATTR_MIN=1,LODATTR_MAX=8,VMIN=0,VMAX=500000)
	if COMB:RESULT.extend(COMB)
	COMB=createConbine(SEL,NAME='lod_182lv0',LODATTR_MIN=1,LODATTR_MAX=8,VMIN=0,VMAX=1000000)
	if COMB:RESULT.extend(COMB)
	COMB=createConbine(SEL,NAME='lod_183lv0',LODATTR_MIN=1,LODATTR_MAX=8,VMIN=0,VMAX=2500000)
	if COMB:RESULT.extend(COMB)
	COMB=createConbine(SEL,NAME='lod_184lv0',LODATTR_MIN=1,LODATTR_MAX=8,VMIN=0,VMAX=5000000)
	if COMB:RESULT.extend(COMB)
	COMB=createConbine(SEL,NAME='lod_185lv0',LODATTR_MIN=1,LODATTR_MAX=8,VMIN=0,VMAX=10000000)
	if COMB:RESULT.extend(COMB)
	COMB=createConbine(SEL,NAME='lod_186lv0',LODATTR_MIN=1,LODATTR_MAX=8,VMIN=0,VMAX=25000000)
	if COMB:RESULT.extend(COMB)
	COMB=createConbine(SEL,NAME='lod_187lv0',LODATTR_MIN=1,LODATTR_MAX=8,VMIN=0,VMAX=50000000)
	if COMB:RESULT.extend(COMB)
	COMB=createConbine(SEL,NAME='lod_188lv0',LODATTR_MIN=1,LODATTR_MAX=8,VMIN=0,VMAX=100000000)
	if COMB:RESULT.extend(COMB)
	COMB=createConbine(SEL,NAME='lod_189lv0',LODATTR_MIN=1,LODATTR_MAX=8,VMIN=0,VMAX=9999999999999999999999999999999999999)
	if COMB:RESULT.extend(COMB)

	createMeshLOD_Grouping(RESULT)

	setAttrToAtgi()

def createLowModel():
	RESULT=[]
	RESULT.extend(createDupConbine(NAME='lod_lowmodel',LODATTR_MIN=1,LODATTR_MAX=2,VMIN=100000,VMAX=9999999999999999999999999999999999999))
	createLowModel_Grouping(RESULT)

def autoSetLODToSelection():
	SEL=cmds.ls(sl=True,tr=True,dag=True,type='mesh',l=True)
	for each in SEL:
		try:
			SIZE=BBMesure(each)
			if SIZE<1000:
				setLODAttr([each],2,1)
			else:
				setLODAttr([each],4,1)
		except:
			continue

#################
# UI
#################

def LayoutB():
	cmds.columnLayout('MS_BBfilter.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_BBfilter.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.gridLayout(nc=7)
	cmds.text(l='LOD1,2')
	cmds.text(l='LOD1,3')
	cmds.text(l='LOD1,4')
	cmds.text(l='LOD1,5')
	cmds.text(l='LOD1,6')
	cmds.text(l='LOD1,7')
	cmds.text(l='LOD1,8')
	#
	cmds.checkBox()
	cmds.checkBox()
	cmds.checkBox()
	cmds.checkBox()
	cmds.checkBox()
	cmds.checkBox()
	cmds.checkBox()
	#
	cmds.floatField()
	cmds.floatField()
	cmds.floatField()
	cmds.floatField()
	cmds.floatField()
	cmds.floatField()
	cmds.floatField()
	#
	cmds.button(l='getBBVolume')
	cmds.button(l='getBBVolume')
	cmds.button(l='getBBVolume')
	cmds.button(l='getBBVolume')
	cmds.button(l='getBBVolume')
	cmds.button(l='getBBVolume')
	cmds.button(l='getBBVolume')
	
	cmds.separator()
	cmds.setParent('..')

def Layout_manual():
	cmds.columnLayout('MS_BBfilter.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='manualConbine',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.rowLayout(nc=2,cw2=[100,100])
	#
	cmds.columnLayout(adj=True)
	cmds.button(l='near(1,2)',bgc=[0.4095,0.63,0.189],c=lambda *args:forceCreation(NAME='lod_near0',LODATTR_MIN=1,LODATTR_MAX=2))
	cmds.button(l='middle(1,4)',bgc=[0.189,0.4051,0.63],c=lambda *args:forceCreation(NAME='lod_middle0',LODATTR_MIN=1,LODATTR_MAX=4))
	cmds.button(l='far(1,6)',bgc=[0.63,0.189,0.41391],c=lambda *args:forceCreation(NAME='lod_far0',LODATTR_MIN=1,LODATTR_MAX=4))
	cmds.button(l='atgi(1,6)',bgc=[0.63,0.189,0.41391],c=lambda *args:setAttrToAtgi(SELECTIONMODE='selection'))
	cmds.setParent('..')
	#
	cmds.columnLayout(adj=True)
	#cmds.button(l='LowModel(5,8)',bgc=[0.189,0.63,0.3654],c=lambda *args:forceLowModel())
	cmds.button(l='LowModel(5,8)',bgc=[0.189,0.63,0.63],c=lambda *args:forceLowModel())
	#cmds.button(l='LowModel(5,8)',bgc=[0.43596,0.189,0.63],c=lambda *args:forceLowModel())
	cmds.setParent('..')
	#
	cmds.setParent('..')

	cmds.setParent('..')

def LayoutA():
	cmds.columnLayout('MS_BBfilter.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_BBfilter.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.gridLayout(nc=2,cw=100)
	cmds.button(l='meshLOD',c=lambda *args:main(SELECTIONMODE='selection'),ann=u'選択オブジェクト群をLOD３段階に自動コンバイン\nコンバイン制限20000頂点')
	cmds.button(l='superLOD',c=lambda *args:superLOD(SELECTIONMODE='selection'),ann=u'選択オブジェクト群をLOD8段階に自動コンバイン\nコンバイン制限20000頂点')
	#cmds.button(l='LOWMODEL',c=lambda *args:createLowModel())
	cmds.setParent('..')
	cmds.separator()
	cmds.button(l='autoSetLOD To Selection From BB',c=lambda *args:autoSetLODToSelection())

	cmds.setParent('..')

	Layout_manual()

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	
