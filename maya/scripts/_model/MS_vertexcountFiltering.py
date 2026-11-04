# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_vertexcountFiltering
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import _lib.MS_distance as MS_distance
reload(MS_distance)

##### utility
	
##### mesureTool
	

def getEdgeLength():
	EDG=cmds.filterExpand(sm=32)
	LEN=0
	for each in EDG:
		V=cmds.polyListComponentConversion(each,tv=True)
		LEN+=MS_distance.distance(V[0],V[1])
	return LEN

def BBMesure(FACE):
	#ポリゴンバウンディングボックス面積
	BB=cmds.xform(FACE,q=True,bb=True,ws=False)
	RET=((BB[3]-BB[0])*(BB[4]-BB[1])*(BB[5]-BB[2]))
	return RET

def getFaces(COMP):#フェース選択
	#print COMP
	FACE=cmds.polyListComponentConversion(COMP,tf=True)
	cmds.select(FACE,r=True)
	result=cmds.filterExpand(FACE,ex=True,sm=34)
	return result
	
def BBMesure_new(OBJ,MIN=5):
	if not OBJ:
		return [1,1,1]
	FACE=getFaces(OBJ)
	#ポリゴンバウンディングボックス面積
	cmds.select(FACE,r=True)
	BB=cmds.polyEvaluate(bc=True)
	
	X=(BB[0][1]-BB[0][0])
	Y=(BB[1][1]-BB[1][0])
	Z=(BB[2][1]-BB[2][0])
	if X<MIN:X=1
	if Y<MIN:Y=1
	if Z<MIN:Z=1

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
		#Atgiロケータチェック
		SHAPE=cmds.listRelatives(EACH,s=True,f=True)
		if SHAPE:
			if 'AtgiLocator' in cmds.nodeType(SHAPE[0]) or 'AtgiLocator' in cmds.nodeType(EACH):
				NUM = atgiBB(EACH)
			elif cmds.nodeType(SHAPE[0])=='mesh':
				if cmds.nodeType(EACH)=='mesh':#メッシュ選択防止
					EACH=cmds.listRelatives(EACH,p=True,type='transform')[0]
				NUM = BBMesure_new(EACH)

		if not NUM in DICT.keys():
			DICT[NUM]=[]
		DICT[NUM].append(EACH)
	return DICT
	
def bbfilter():
	
	OBJ=cmds.ls(sl=True,l=True)
	if not OBJ:
		OBJ=cmds.ls(hl=True,l=True)
	if not OBJ:
		OBJ=cmds.ls(l=True,v=True,typ='mesh')
	if not OBJ:
		return
	#print OBJ
	MIN_VALUE=cmds.floatField('MS_vertexcountFiltering_bbmin',q=True,v=True)
	MAX_VALUE=cmds.floatField('MS_vertexcountFiltering_bbmax',q=True,v=True)
	DICT=bbsize(OBJ)
	#print DICT
	LIST=[]
	for EACHKEY in DICT.keys():
		if float(EACHKEY)>=MIN_VALUE and float(EACHKEY)<=MAX_VALUE:
			LIST.extend(DICT[EACHKEY])
	#print LIST
	cmds.select(clear=True)
	if LIST:
		cmds.select(LIST,r=True)
	
def getBBsize():
	OBJ=cmds.ls(sl=True)
	if not OBJ:
		OBJ=cmds.ls(hl=True)
	if not OBJ:
		return
	NUM=bbsize(OBJ)
	#cmds.floatField('MS_vertexcountFiltering_bbmin',e=True,v=NUM.keys()[0])
	cmds.floatField('MS_vertexcountFiltering_bbmax',e=True,v=NUM.keys()[0])
	
##### objcount
	
def objCount():
	OBJ=cmds.ls(sl=True)
	print len(OBJ)
	cmds.textField('MS_vertexcountFiltering_count',e=True,tx=str(len(OBJ)))
	
def layoutCount():
	cmds.columnLayout()
	cmds.text(l='Count',w=200,bgc=[0.8,0.8,0.8])
	cmds.button(l='objCount',w=200,c=lambda *args:objCount())
	cmds.textField('MS_vertexcountFiltering_count',w=200)
	cmds.setParent('..')
	
	
##### functional renamer
	
def renameHiOrLow():
	NODE=cmds.ls(sl=True)
	if len(NODE)<2:
		return
	if cmds.polyEvaluate(NODE[0],v=True)<cmds.polyEvaluate(NODE[1],v=True):
		LOWNODE=NODE[0]
		HIGHNODE=NODE[1]
	else:
		LOWNODE=NODE[1]
		HIGHNODE=NODE[0]
	RENAME_STRING=cmds.textField('MS_vertexcountFiltering_rename',q=True,tx=True)
	cmds.rename(LOWNODE,RENAME_STRING.replace(' ','')+'_l')
	cmds.rename(HIGHNODE,RENAME_STRING.replace(' ','')+'_h')
	
def groupHiAndLow():
	NODE=cmds.ls(sl=True)
	if not cmds.objExists('|low_pts'):
		GRP=cmds.group(empty=True)
		cmds.rename(GRP,'low_pts')
	
	if not cmds.objExists('|high_pts'):
		GRP=cmds.group(empty=True)
		cmds.rename(GRP,'high_pts')
	
	for EACH in NODE:
		if EACH[-2:]=='_l':
			cmds.parent(EACH,'low_pts')
		if EACH[-2:]=='_h':
			cmds.parent(EACH,'high_pts')
	
	
def layoutRenamer(
	LABEL='renamer'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.columnLayout()
	cmds.text(l='functionalRenamer',w=200,bgc=[0.8,0.8,0.8])
	cmds.textField('MS_vertexcountFiltering_rename',w=WIDTH-4)
	cmds.button(w=WIDTH-4,l=u'機能リネーム',c=lambda *args:renameHiOrLow())
	cmds.button(w=WIDTH-4,l=u'ハイ・ロー・グルーピング',c=lambda *args:groupHiAndLow())
	
	cmds.setParent('..')
	cmds.setParent('..')
	
	
##### vertexcountFiltering
	
def vertexcountFiltering(MIN=0,MAX=100):
	
	OBJ=cmds.ls(v=True)
	NEWOBJ=[]
	for EACH in OBJ:
		NUM=cmds.polyEvaluate(EACH,v=True)
		if NUM>=MIN and NUM<=MAX:
			if cmds.nodeType(EACH)=='mesh':#メッシュ選択防止
				NEWOBJ.append(cmds.listRelatives(EACH,p=True,type='transform')[0])
			else:
				NEWOBJ.append(EACH)
	return NEWOBJ

def vertexcount(OBJ):
	DICT={}
	for EACH in OBJ:
		NUM=cmds.polyEvaluate(EACH,v=True)
		if not NUM in DICT.keys():
			DICT[NUM]=[]
		DICT[NUM].append(EACH)
	return DICT
	
##### sort outliner
	
def sortOutliner(METHOD='select'):
	OBJ=cmds.ls(sl=True,l=True)
	
	reverse = cmds.checkBox('MS_vertexcountFiltering_sort_reverse',q=True,v=True)

	if len(OBJ)<2:
		return
	if METHOD=='name':#名前順ソート
		SORTED=nameSort(OBJ)
	elif METHOD=='bb':#バウンディングボックス順ソート
		SORTED=bbSort(OBJ)
	elif METHOD=='distance':#ターゲットからの距離順ソート
		TARGET=cmds.textFieldGrp('TARGET',q=True,tx=True)
		SORTED=distanceSort(OBJ,TARGET=TARGET)
	elif METHOD=='attr':
		SORTED=attrSort(OBJ)
	elif METHOD=='attrDialog':
		SORTED=attrSortFromDialog(OBJ)
	elif METHOD=='vertexCount':
		SORTED=vertexCountSort(OBJ)
	else:#選択順ソート
		SORTED=OBJ

	if reverse:
		SORTED.reverse()

	cmds.select(SORTED,r=True)
	PARENTS=cmds.listRelatives(SORTED,p=True,f=True)
	GRP=cmds.group(SORTED)
	if PARENTS:
		cmds.ungroup(GRP,p=PARENTS[0])
	else:
		cmds.ungroup(GRP,w=True)

	
#attrSort
	
##### チャンネル取得 #####
def getChannel():
	ATTR=[]
	SHA=[]
	COMP_ATTR=[]
	#sma=True,sha=True,sol=True,mol=True,hol=True)
	try:
		ATTR.extend(cmds.channelBox('mainChannelBox',q=True,sma=True))
	except TypeError:
		pass
	
	try:
		SHA.extend(cmds.channelBox('mainChannelBox',q=True,ssa=True))
	except TypeError:
		pass
	'''
	try:
		COMP_ATTR.extend(cmds.textScrollList('attribute_scrollList',q=True,selectItem=True))
	except TypeError:
		pass
	except RuntimeError:
		pass

	if ATTR:
		cmds.textField('CHANNEL',e=True,tx=':'.join(ATTR))
		
	if SHA:
		cmds.textField('CHANNEL_SHA',e=True,tx=':'.join(SHA))
	if COMP_ATTR:
		cmds.textField('COMP_ATTR',e=True,tx=':'.join(COMP_ATTR))
	'''
	return ATTR+SHA
	
def attrSort(LIST,REVERSE=False):#指定アトリビュートでソート済みリスト作成
	SRC=[]
	ATTR=getChannel()#
	if not ATTR:
		return
	for EACH in LIST:
		VALUE=cmds.getAttr('%s.%s'%(EACH,ATTR[0]))
		SRC.append([EACH,VALUE])
	return sorter(SRC,COLUMN=1,REVERSE=REVERSE)
	
def attrSortFromDialog(LIST,REVERSE=False):#ダイアログで指定したアトリビュートでソート済みリスト作成
	SRC=[]
	ATTR=cmds.textField('MS_vertexcountFiltering_attribute',q=True,tx=True)
	if not ATTR:
		return
		
	for EACH in LIST:
		if cmds.attributeQuery(ATTR,n=EACH,ex=True):
			VALUE=cmds.getAttr('%s.%s'%(EACH,ATTR))
		else:
			try:
				SHAPE=cmds.listRelatives(EACH,s=True)
				VALUE=cmds.getAttr('%s.%s'%(SHAPE[0],ATTR))
			except:
				print 'error'
				VALUE=0
		SRC.append([EACH,VALUE])
	return sorter(SRC,COLUMN=1,REVERSE=REVERSE)
	
#distanceSort
	
def distanceSort(LIST,TARGET='',REVERSE=False):#ターゲットとの距離でソート済みリスト作成
	SRC=[]
	if not TARGET:
		return
	for EACH in LIST:
		RANGE=MS_distance.distance(TARGET,EACH,mode='BBCenter')#
		SRC.append([EACH,RANGE])
	return sorter(SRC,COLUMN=1,REVERSE=REVERSE)
	
#BBsort
	
def bbSort(LIST,REVERSE=False):#バウンディングボックスサイズ順でソート済みリスト作成
	SRC=[]
	for EACH in LIST:
		#Atgiロケータチェック
		SHAPE=cmds.listRelatives(EACH,s=True,f=True)
		if cmds.nodeType(SHAPE[0])=='GraviteAtgiLocatorNode' or cmds.nodeType(EACH)=='GraviteAtgiLocatorNode':
			AREA = atgiBB(EACH)
		#Atgiで無い場合
		else:
			AREA=BBMesure_new(EACH)

		SRC.append([EACH,AREA])
	return sorter(SRC,COLUMN=1,REVERSE=REVERSE)
	
#vertexCountSort
	
def vertexCountSort(LIST,REVERSE=False):
	SRC=[]
	for EACH in LIST:
		VC=cmds.polyEvaluate(EACH,v=True)
		SRC.append([EACH,VC])
	return sorter(SRC,COLUMN=1,REVERSE=REVERSE)
	
#nameSort
	
def nameSort(LIST,REVERSE=False):#名前でソート済みリスト作成
	SRC=[]
	for EACH in LIST:
		SRC.append([EACH,EACH])#
	return sorter(SRC,COLUMN=1,REVERSE=REVERSE)
	
def sorter(LIST,COLUMN=0,REVERSE=False):
	RET=[]
	RETSORT=sorted(LIST,key=lambda x:x[COLUMN],reverse=REVERSE)
	for EACH in RETSORT:
		RET.append(EACH[0])
	return RET
	
def layoutSort():
	cmds.columnLayout()
	cmds.checkBox('MS_vertexcountFiltering_sort_reverse',l='reverse',v=True)
	cmds.text(l=u'SortOutliner',w=200,bgc=[0.8,0.8,0.8])
	cmds.button(w=200,l=u'select',c=lambda *args:sortOutliner())
	cmds.button(w=200,l=u'name',c=lambda *args:sortOutliner('name'))
	cmds.button(w=200,l=u'attribute(fromChannelBox)',c=lambda *args:sortOutliner('attr'))
	
	cmds.rowLayout(nc=2)
	cmds.button(w=50,l=u'attribute',c=lambda *args:sortOutliner('attrDialog'))
	cmds.textField('MS_vertexcountFiltering_attribute',w=150)
	cmds.setParent('..')
	
	cmds.button(w=200,l=u'boundingBox',c=lambda *args:sortOutliner('bb'))
	cmds.button(w=200,l=u'vertexCount',c=lambda *args:sortOutliner('vertexCount'))
	#
	cmds.button(w=200,l=u'Distance',c=lambda *args:sortOutliner('distance'))
	cmds.text(l='get Target for DistanceSort',)
	cmds.rowLayout(nc=2)
	cmds.textFieldGrp('TARGET',w=150)
	cmds.button(l='GET',w=50,c=lambda *args:getTarget())
	cmds.setParent('..')
	
	cmds.setParent('..')
	
#####
#UI
#####

def do():
	MIN_VALUE=cmds.intField('MS_vertexcountFiltering_min',q=True,v=True)
	MAX_VALUE=cmds.intField('MS_vertexcountFiltering_max',q=True,v=True)
	FILTERED_OBJ=vertexcountFiltering(MIN_VALUE,MAX_VALUE)
	if FILTERED_OBJ:
		cmds.select(FILTERED_OBJ,r=True)
	else:
		cmds.select(r=True,clear=True)
	
def getVertexCount():
	OBJ=cmds.ls(sl=True)
	if not OBJ:
		OBJ=cmds.ls(hl=True)
	if not OBJ:
		return
	NUM=cmds.polyEvaluate(OBJ[0],v=True)
	cmds.intField('MS_vertexcountFiltering_min',e=True,v=NUM)
	cmds.intField('MS_vertexcountFiltering_max',e=True,v=NUM)

def grouping():
	DICT=vertexcount(cmds.ls(sl=True))
	for EACHKEY in DICT.keys():
		GP=cmds.group(DICT[EACHKEY])
		cmds.rename(GP,'_'+str(EACHKEY)+'_')
	
	
def getTarget():
	OBJ=cmds.ls(sl=True,l=True)
	cmds.textFieldGrp('TARGET',e=True,tx=OBJ[0])
	
def layoutA(
	LABEL='MS_vertexcountFiltering'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.intField(LABEL+'_min',w=WIDTH-4,v=0)
	cmds.intField(LABEL+'_max',w=WIDTH-4,v=100)
	cmds.button(w=WIDTH-4,l=u'選択オブジェクトのポリゴン数取得',c=lambda *args:getVertexCount())
	cmds.button(w=WIDTH-4,l=u'フィルター数値でポリゴン選択',c=lambda *args:do())
	
	cmds.separator(w=WIDTH,h=8)
	cmds.floatField(LABEL+'_bbmin',w=WIDTH-4,v=0)
	cmds.floatField(LABEL+'_bbmax',w=WIDTH-4,v=100)
	cmds.button(w=WIDTH-4,l=u'バウンディングボックスサイズ取得',c=lambda *args:getBBsize())
	cmds.button(w=WIDTH-4,l=u'バウンディングボックスサイズでポリゴン選択',c=lambda *args:bbfilter())
	
	cmds.separator(w=WIDTH,h=8)
	
	cmds.button(w=WIDTH-4,l=u'ポリゴン数ごとにグループ分けする',c=lambda *args:grouping())
	cmds.separator(w=WIDTH,h=8)
	cmds.setParent('..')
	cmds.setParent('..')
	
	
	
def UI():
	if cmds.window('MS_vertexcountFiltering_main_window',q=True,ex=True):
		cmds.deleteUI('MS_vertexcountFiltering_main_window')
	cmds.window('MS_vertexcountFiltering_main_window',rtf=True,s=True)
	cmds.columnLayout()
	layoutA()
	cmds.separator(w=200)
	layoutCount()
	cmds.separator(w=200)
	layoutSort()
	cmds.separator(w=200)
	layoutRenamer()
	cmds.setParent('..')
	cmds.showWindow('MS_vertexcountFiltering_main_window')
	

