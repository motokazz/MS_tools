# -*- coding:utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel
import math
import random

##### 計算 #####

def add(a,b):
	c=a+b
	return c

def minus(a,b):
	c=a-b
	return c

def multi(a,b):
	c=a*b
	return c

def divide(a,b):
	c=0
	if a or b:
		c=a/b
	return c

def randomf(a,b):
	c=random.uniform(-b,b)
	return a+c
	
def my_round(a,b):
	c = 0
	xround=lambda x:(x*2+1)//2
	if a and b:
		c = xround(a/b)*b
	else:
		c = xround(a)
	return c

def ret_a(a,b):
	return a

def interp(a,b,quantity,NUM):
	c=a-(((a-b)/quantity)*(NUM))
	return c


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


###### attrSaver
	
def TEMP_SAVE(ROW):#テンポラリのファイルを保存。保存先はワークスペース
	ACTIVE_WORKSPACE=cmds.workspace(q=True,act=True)
	f=open('%s/TEMP.mel'%ACTIVE_WORKSPACE,'w')
	f.write(ROW)
	f.close()
	print ('exported : %s/TEMP.mel'%ACTIVE_WORKSPACE)

def TEMP_EXEC():#テンポラリのファイルを実行。
	ACTIVE_WORKSPACE=cmds.workspace(q=True,act=True)
	mel.eval('source "%s/TEMP.mel"'%ACTIVE_WORKSPACE)
	print ('executed : %s/TEMP.mel'%ACTIVE_WORKSPACE)
	
def preAttrSaver():
	getChannel()
	
	NODE=cmds.ls(typ='transform',sl=True,l=True)
	SHAPE=cmds.listRelatives(s=True,f=True)
	COMPORNENT=cmds.filterExpand(sm=[31,32,34,35])
	
	VAR=cmds.floatField('STEP',q=True,v=True)
	ATTR=cmds.textField('CHANNEL',q=True,tx=True).split(':')
	SHA=cmds.textField('CHANNEL_SHA',q=True,tx=True).split(':')
	COMP_ATTR=cmds.textField('COMP_ATTR',q=True,tx=True).split(':')
	
	#何も選ばれてなかったら基本項目出力
	if ATTR[0]=='' and SHA[0]=='' and COMP_ATTR[0]=='':
		ATTR=['tx','ty','tz','rx','ry','rz','sx','sy','sz','visibility']
	#
	COMMAND='currentTime 0;\n'
	
	for EACH_NODE in NODE:
		for EACH_ATTR in ATTR:
			COMMAND+=attrSaver(EACH_NODE,EACH_ATTR)
			
	if COMPORNENT:
		print ('CONPORNET')
	
	TEMP_SAVE(COMMAND)

def attrSaver(NODE,ATTR):
	
	CT=cmds.currentTime(q=True)
	
	if not cmds.attributeQuery(ATTR,n=NODE,ex=True):
		return ''
	
	VAR=cmds.getAttr(NODE+'.'+ATTR)
	
	if VAR==True:
		VAR=1
	if VAR==False:
		VAR=0
	
	#WILDCARD_NODE=NODE.replace('|','|*:')
	WILDCARD_NODE=NODE

	COMMAND=''
	NODE=NODE.split(':')[-1]
	COMMAND+='$K=`findKeyframe -c -at "%s" "%s"`;\n' % (ATTR,WILDCARD_NODE)
	COMMAND+='if (size($K)){\n'
	COMMAND+='$a=`getAttr -t %s "%s.%s"`;\n' % (CT,WILDCARD_NODE,ATTR)
	COMMAND+='$gap=%s-$a;\n' % VAR
	COMMAND+='keyframe -e -iub true -r -o over -tc 1 -vc $gap "%s.%s" ;\n'  % (WILDCARD_NODE,ATTR)
	COMMAND+='}else{\n'
	COMMAND+='if (!`getAttr -l "%s.%s"` && `getAttr -se "%s.%s"`){\n'%(WILDCARD_NODE,ATTR,WILDCARD_NODE,ATTR)
	COMMAND+='setAttr "%s.%s" %s;\r\n' % (WILDCARD_NODE,ATTR,str(VAR))
	COMMAND+='}\n'
	COMMAND+='}\n'
	
	return COMMAND#リファレンス対策用

##### メイン #####
	
def defcom(MODE):#コマンド定義
	if MODE=='ret_a':
		COM=ret_a
	if MODE=='add':
		COM=add
	if MODE=='minus':
		COM=minus
	if MODE=='multi':
		COM=multi
	if MODE=='divide':
		COM=divide
	if MODE=='my_round':
		COM=my_round
	if MODE=='randomf':
		COM=randomf
	if MODE=='randoms':
		COM=add
	return COM
	
def exe(MODE,G_MODE):
	getChannel()

	VAR=cmds.floatField('STEP',q=True,v=True)
	ATTR=cmds.textField('CHANNEL',q=True,tx=True).split(':')
	SHA=cmds.textField('CHANNEL_SHA',q=True,tx=True).split(':')
	COMP_ATTR=cmds.textField('COMP_ATTR',q=True,tx=True).split(':')

	# Transform Node
	NODE = cmds.ls(typ='transform', sl=True)
	if NODE:
		exe2(NODE,ATTR,VAR,MODE,G_MODE)

	# Shape Node
	SHAPE = cmds.listRelatives(s=True)
	if SHAPE:
		exe2(SHAPE,SHA,VAR,MODE,G_MODE)

	# Compornents
	COMPORNENT = cmds.filterExpand(sm=[31, 32, 34, 35])
	if COMPORNENT:
		exe2(COMPORNENT,COMP_ATTR,VAR,MODE,G_MODE)

def exe2(NODE,ATTR,VAR,MODE,G_MODE):
	if not NODE:
		return
	
	#RANDOMS用乱数発生
	RANDOMS=[]
	for X in range(len(NODE)):
		RANDOMS.append(random.uniform(-VAR,VAR))
	
	COM=defcom(MODE)
	QUANTITY=len(NODE)
	for EACH_ATTR in ATTR:
		# Components
		if EACH_ATTR in ['normal','pntx','pnty','pntz']:
			for EACH_NODE in NODE:
				compornentControll(EACH_NODE, EACH_ATTR, VAR, MODE, COM)
			continue

		if EACH_ATTR=='vcol':
			vcolorControl(NODE,EACH_ATTR,VAR,MODE,COM)
			continue

		if EACH_ATTR:
			NUM=0
			FOR_INTERP_A=float(cmds.getAttr(NODE[0]+'.'+EACH_ATTR))#interpモード用
			FOR_INTERP_B=float(cmds.getAttr(NODE[-1]+'.'+EACH_ATTR))#interpモード用

			for EACH_NODE in NODE:
				
				a=cmds.getAttr(EACH_NODE+'.'+EACH_ATTR)
				b=VAR
				if MODE=='randoms':
					b=RANDOMS[NUM]
				else:
					b=VAR

				# GroupStep
				if G_MODE=='group':
					b=VAR*(NUM+1)
				# Interp
				if G_MODE=='interp':
					a=interp(FOR_INTERP_A,FOR_INTERP_B,QUANTITY-1,NUM)

				# exec
				try:
					cmds.setAttr(EACH_NODE+'.'+EACH_ATTR,COM(a,b))
				except:
					print ('error')
					pass



				NUM+=1

'''def compornentControll_bak(NODE,CC_MODE,VAR,MODE,COM):
	a=0

	VTX=cmds.polyListComponentConversion(NODE,tv=True)
	VTX=cmds.filterExpand(VTX,sm=31)


	if CC_MODE=='normal':
		for EACH_VTX in VTX:
			cmds.moveVertexAlongDirection(EACH_VTX,n=COM(a,VAR))

'''

#コンポーネント処理
def compornentControll(NODE,CC_MODE,VAR,MODE,COM):
	#
	MAG = 1

	# get modifiers
	'''
	mods = cmds.getModifiers()
	if (mods & 1) > 0: MAG = 10  # shift
	if (mods & 4) > 0: MAG = 0.5  # ctrl
	if (mods & 8) > 0: MAG = 2  # alt
	'''

	#
	MAG *= COM(MAG,VAR)
	# getDIR
	DIR = [0,0,1]
	if CC_MODE == 'pntx':
		DIR = [1, 0, 0]
	elif CC_MODE == 'pnty':
		DIR = [0, 1, 0]

	# FACE
	FACE = cmds.filterExpand(sm=34, fp=True)
	if FACE:
		cmds.polyMoveFacet(NODE,lt=[DIR[0] * MAG, DIR[1] * MAG, DIR[2] * MAG])
		return

	# EDGE
	EDGE = cmds.filterExpand(sm=32, fp=True)
	if EDGE:
		cmds.polyMoveEdge(NODE,lt=[DIR[0] * MAG, DIR[1] * MAG, DIR[2] * MAG])
		return

	#　VERTEX

	#PRECOMP = cmds.polyListComponentConversion(tv=True)
	#COMPORNENT = cmds.filterExpand(PRECOMP, sm=[31, 32, 34, 35], fp=True)

	#VTX = cmds.polyListComponentConversion(tv=True)
	VTX = cmds.filterExpand( sm=31, fp=True)
	if VTX:
		if CC_MODE == 'normal':
			cmds.moveVertexAlongDirection(NODE, n=MAG)
		else:

			cmds.moveVertexAlongDirection(NODE, d=(DIR), m=VAR * MAG)

# 頂点カラー
def vcolorControl(NODE,CC_MODE,VAR,MODE,COM):
	a=0
	for EACH_NODE in NODE:
		cmds.polyColorPerVertex(EACH_NODE,a=COM(a,VAR))


##### コンポーネントアトリビュートリスト #####
def listAttr():
	COMP=cmds.filterExpand(sm=[31,32,34,35])
	print (cmds.listAttr(COMP[0]))
	
def attrList():
	RET={}
	RET.setdefault('vtx',['pntx','pnty','pntz','normal','vcol','alpha'])
	return RET

def createlist():
	DIC=attrList()
	if cmds.window('MS_valueStepper_attributeList',q=True,ex=True):
		cmds.deleteUI('MS_valueStepper_attributeList')
	cmds.window('MS_valueStepper_attributeList')
	cmds.columnLayout(w=100)
	LIST_NAME='attribute_scrollList'
	cmds.textScrollList(LIST_NAME,allowMultiSelection=True)
	for EACH in DIC.keys():
		for EACH_ATTR in DIC[EACH]:
			cmds.textScrollList(LIST_NAME,e=True,append=EACH_ATTR)
			
	#cmds.setParent('..')
	cmds.button(l='getChannel',w=100,c=lambda *args:getChannel())
	cmds.setParent('..')
	cmds.showWindow('MS_valueStepper_attributeList')
	
##### メインUI #####

def layout_attrSaver():
	cmds.frameLayout(l=u'tool',w=170,cl=True,cll=True)
	cmds.columnLayout()
	
	cmds.text(l='this tool is transfer attributes to reffernced scene.)')
	cmds.text(l=' 1.select target objects and check target attributes in channel box \n 2.bush [AttrSaver] button to save command file (to d:\\TEMP.mel)\n 3.open refference scene \n 4.push [AttrLoader] button to load comannd file and setup ].')
	cmds.rowLayout(nc=2)
	cmds.button(l='AttrSaver',w=80,bgc=[0.7,0.8,0.7],c=lambda *args:preAttrSaver())
	cmds.button(l='AttrLoader',w=80,bgc=[0.7,0.7,0.8],c=lambda *args:TEMP_EXEC())
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.setParent('..')
	
def layout_extendFunction():
	cmds.frameLayout(l=u'拡張機能',w=170,cl=True,cll=True)
	cmds.columnLayout()
	cmds.text(l=u'トランスフォーム系')
	cmds.textField('CHANNEL',w=160,tx='')
	cmds.text(l=u'シェイプノード系')
	cmds.textField('CHANNEL_SHA',w=160,tx='')
	cmds.separator(w=150)
	cmds.text(l=u'コンポーネント系')
	cmds.textField('COMP_ATTR',w=160,tx='')
	cmds.button(bgc=[1.0,1.0,0.8],w=170,h=16,al="center",l=u'コンポーネントアトリビュートリスト',c=lambda *args:createlist(),ann=u'チャンネルボックスからは取得できないアトリビュートを取得するためのUIが開きます')
	cmds.separator(w=150)

	cmds.rowLayout(nc=2)
	cmds.button(bgc=[1.0,1.0,1.0],w=80,al="center",l='getChannel',c=lambda *args:getChannel())
	cmds.button(bgc=[1.0,1.0,1.0],w=80,al="center",l='listAttr',c=lambda *args:listAttr())
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.setParent('..')
	
def UI():
	if cmds.window('MS_valueStepperUI',q=True,ex=True):
		cmds.deleteUI('MS_valueStepperUI')
	cmds.window('MS_valueStepperUI')
	cmds.columnLayout()
	
	cmds.floatField('STEP',w=160,v=0)

	cmds.separator(w=160)
	
	cmds.separator(w=150)
	cmds.rowLayout(nc=4,cw4=[18,18,18,18],ann=u'一般的な計算を行います')
	cmds.button(bgc=[0.8,0.9,0.8],w=20,al="center",l="+",c=lambda *args:exe('add',0))
	cmds.button(bgc=[0.8,0.9,0.8],w=20,al="center",l="-",c=lambda *args:exe('minus',0))
	cmds.button(bgc=[0.8,0.9,0.8],w=20,al="center",l="*",c=lambda *args:exe('multi',0))
	cmds.button(bgc=[0.8,0.9,0.8],w=20,al="center",l="/",c=lambda *args:exe('divide',0))
	cmds.setParent('..')

	cmds.rowLayout(nc=2,cw2=[40,40],ann=u'ユーティリティー')
	cmds.button(bgc=[0.8,0.8,0.9],w=40,al="center",l=u"四捨五入",c=lambda *args:exe('my_round',0),ann=u'')
	cmds.button(bgc=[1.0,1.0,1.0],w=40,al="center",l=u'補完',c=lambda *args:exe('ret_a','interp'),ann=u'選択順にアトリビュートを補完します。')
	cmds.setParent('..')

	cmds.rowLayout(nc=2,cw2=[40,40],ann=u'乱数発生')
	cmds.button(bgc=[0.9,0.9,0.8],w=40,al="center",l="Rand",c=lambda *args:exe('randomf',0),ann=u'アトリビュートことにバラバラな乱数を発生します')
	cmds.button(bgc=[0.9,0.85,0.8],w=40,al="center",l="SRand",c=lambda *args:exe('randoms',0),ann=u'オブジェクトごとにまとまりのある乱数を発生します')
	cmds.setParent('..')

	cmds.separator(w=150)
	cmds.text(l=u'グループボタン')
	cmds.rowLayout(nc=6,cw6=[18,18,18,18,40,40],ann=u'選択順に加算していくような計算を行います')
	cmds.button(bgc=[0.8,0.8,0.9],w=20,al="center",l="+",c=lambda *args:exe('add','group'))
	cmds.button(bgc=[0.8,0.8,0.9],w=20,al="center",l="-",c=lambda *args:exe('minus','group'))
	cmds.button(bgc=[0.8,0.8,0.9],w=20,al="center",l="*",c=lambda *args:exe('multi','group'))
	cmds.button(bgc=[0.8,0.8,0.9],w=20,al="center",l="/",c=lambda *args:exe('divide','group'))
	cmds.setParent('..')

	cmds.separator(w=150)
	
	layout_extendFunction()
	layout_attrSaver()
	
	cmds.setParent('..')
	cmds.window('MS_valueStepperUI',e=True,w=160,h=150)
	
	cmds.showWindow('MS_valueStepperUI')
	#MS_fileExport.STORE_RECALL('setUtil','recall')
	#MP_MS_setUtil_storeRecallUI('recall')

#toroExporterUI

