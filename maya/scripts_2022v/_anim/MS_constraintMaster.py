# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_constraintMaster.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import importlib
import _lib.MS_distance as MS_distance
importlib.reload(MS_distance)



def selectionFilter(type):
	NODES=[]
	if type:
		NODES=cmds.ls(sl=True,type=type,l=True)
	else:
		NODES=cmds.ls(sl=True,l=True)
	return NODES
	
	

def MS_aimConstraint(
	AIM_VECTOR=[0.0,1.0,0.0]
	,OFFSET=[0.0,0.0,0.0]
	,UP_VECTOR=[1.0,0.0,0.0]
	,WEIGHT=1.0
	,WORLD_UP_VECTOR=[1.0,0.0,0.0]
	,WORLD_UP_OBJECT=''
	,WORLD_UP_TYPE='vector' #、「scene」、「object」、「objectrotation」、「vector」、
	,SKIP='none'#、「x」、「y」、「z」、「none」
	):
	TARGET=nodeList('targetList',q=True)
	OBJECT=cmds.ls(sl=True,l=True)
	for EACH in OBJECT:
		cmds.aimConstraint(
			TARGET
			,OBJECT
			,aimVector=AIM_VECTOR
			#,layer=string
			#,maintainOffset=True
			#,name=string
			,offset=OFFSET
			,skip=SKIP
			,upVector=UP_VECTOR
			,weight=WEIGHT
			#,worldUpObject=WORLD_UP_OBJECT
			,worldUpType=WORLD_UP_TYPE
			,worldUpVector=WORLD_UP_VECTOR
			)

def MS_arrayParentConstraint():
	TARGET=nodeList('targetList',q=True)
	SEL=cmds.ls(sl=True,l=True)
	i=0
	for EACH in SEL:
		try:
			cmds.parentConstraint(TARGET[i] ,EACH,maintainOffset=True)
		except:
			pass
		i+=1


def nearestOne(TARGET_A='',TARGET_B=[],mode='BBCenterFromAttribute'):
	#1つのオブジェクトと対象オブジェクトリストを比較して、最近接オブジェクトを返す。
	#return 'nearest in target'
	RET=''
	
	ResultDist=100000000
	for Each_B in TARGET_B:
		CurrentDist=MS_distance.distance(TARGET_A,Each_B,mode)
		if CurrentDist<ResultDist:
			ResultDist=CurrentDist
			RET=Each_B
	
	return RET
	
def MS_ditectNearest():
	RET=''
	#ターゲットの中からもっとも近いオブジェクトを探す
	TARGET=nodeList('targetList',q=True)
	SEL=cmds.ls(sl=True,l=True)
	for EACH in SEL:
		#ORGTRN=BBCenterFromAttribute(EACH)
		RET=nearestOne(EACH,TARGET)
	cmds.select(RET,r=True)
	return RET

def parentNearest():
	SEL=cmds.ls(sl=True,l=True)
	for EACH in SEL:
		cmds.select(EACH,r=True)
		NEAREST=MS_ditectNearest()
		cmds.parent(EACH,NEAREST)



def locatorFromBBAttr():
	SEL=cmds.ls(sl=True,l=True)
	for EACH in SEL:
		RET=MS_distance.BBCenterFromAttribute(EACH)
		LOC=cmds.spaceLocator()
		cmds.xform(LOC[0],t=RET,ws=True)
#####UI
def nodeList(UI_NAME,q=False,w=200,h=20,type=[]):
	if q:
		TX	=cmds.textField(UI_NAME,q=True,tx=True)
		if TX:
			LIST	=TX.split(';')
		else:
			LIST=[]
		return LIST
	
	def createList():
		NODES=selectionFilter(type)
		cmds.textField(UI_NAME,e=True,tx=';'.join(NODES))
		
	def addList():
		NODES=selectionFilter(type)
		TX=cmds.textField(UI_NAME,q=True,tx=True)
		if TX:
			LIST=TX.split(';')
		else:
			LIST=[]
		RET=list(set(LIST+NODES))
		cmds.textField(UI_NAME,e=True,tx=';'.join(RET))
		
	def removeList():
		NODES=selectionFilter(type)
		TX=cmds.textField(UI_NAME,q=True,tx=True)
		LIST=TX.split(';')
		for EACH in NODES:
			while EACH in LIST:LIST.remove(EACH)
		cmds.textField(UI_NAME,e=True,tx=';'.join(LIST))
		
	def clearList():
		cmds.textField(UI_NAME,e=True,tx='')
		
	def query():
		TX	=cmds.textField(UI_NAME,q=True,tx=True)
		if TX:
			LIST	=TX.split(';')
		else:
			LIST=[]
		return LIST
	
	def LO(UI_NAME):
		cmds.columnLayout(UI_NAME+'mainColumn')
		cmds.text(l=UI_NAME)
		cmds.textField(UI_NAME,w=w,tx='')
		cmds.rowLayout(nc=4)
		cmds.button(w=40,l=u'create',c=lambda *args:createList())
		cmds.button(w=40,l=u'add',c=lambda *args:addList())
		cmds.button(w=40,l=u'remove',c=lambda *args:removeList())
		cmds.button(w=40,l=u'clear',c=lambda *args:clearList())
		cmds.setParent('..')
		cmds.setParent('..')
	
	if not cmds.control(UI_NAME+'mainColumn',q=True,ex=True):
		LO(UI_NAME)
	
	
def LayoutA():
	cmds.columnLayout('MS_constraintMaster_mainLayout',adj=True)
	###
	#
	cmds.separator()
	nodeList('targetList')
	cmds.text(l='MS_constraintMaster.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.gridLayout(nc=8,ann=u'選択オブジェクトを、ターゲットに対して一括aimConstraint')
	cmds.text(l='aim')
	cmds.button(l='x',c=lambda *args:MS_aimConstraint(AIM_VECTOR=[1.0,0.0,0.0]))
	cmds.button(l='y',c=lambda *args:MS_aimConstraint(AIM_VECTOR=[0.0,1.0,0.0]))
	cmds.button(l='z',c=lambda *args:MS_aimConstraint(AIM_VECTOR=[0.0,0.0,1.0],UP_VECTOR=[0.0,1.0,0.0],WORLD_UP_VECTOR=[0.0,1.0,0.0],WORLD_UP_TYPE='vector',SKIP='x'))
	cmds.setParent('..')
	#
	cmds.separator()
	cmds.text(l='MS_constraintMaster.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.gridLayout(nc=4,cw=100,ann=u'選択オブジェクトを、ターゲットリストに対して、選択順に1個づつ対になるようにparentConstraint')
	cmds.text(l='array\nparent constraint')
	cmds.button(l='array',c=lambda *args:MS_arrayParentConstraint())
	cmds.setParent('..')
	#
	cmds.separator()
	cmds.text(l='MS_constraintMaster.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.gridLayout(nc=4,cw=100,ann=u'選択オブジェクトを、ターゲットリスト内の最近接オブジェクトに対して子供にする')
	cmds.text(l='array\nparent')
	cmds.button(l='sel\nnear',c=lambda *args:MS_ditectNearest(),ann=u'targetList内のオブジェクトから、選択オブジェクトに対して最近接となるオブジェクトを選択')
	cmds.button(l='loc',c=lambda *args:locatorFromBBAttr(),ann=u'バウンディングボックスの中心にロケーターを作成')
	cmds.button(l='parent\nNearest',c=lambda *args:parentNearest(),ann=u'選択オブジェクトを、ターゲットリスト内の最近接オブジェクトに対して子供にする')
	cmds.setParent('..')
	###
	cmds.setParent('..')


def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	

UI()
