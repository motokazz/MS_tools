# _*_coding:utf-8_*_
########################################
# ファイル名
#			MP_MS_createPE
# 説明
#			Knackの物理セットアップ補助を行うツール
# 作成日
#			
########################################

import maya.cmds as cmds
import time
import csv

import MP_MS_extraAttrList_V2
reload(MP_MS_extraAttrList_V2)

import MP_MS_extraAttrController
reload(MP_MS_extraAttrController)

import MS_primitives
reload(MS_primitives)

import MS_module.MS_getBestBB as getBestBB
reload(getBestBB)

#execCheckList
import MS_module.MS_execCheck
reload(MS_module.MS_execCheck)
MS_module.MS_execCheck.execCheckSafe('MP_MS_createPE.py')

##### プラグインチェッカー #####

if not cmds.pluginInfo('mpPhysicsNode.py',q=True,loaded=True):
	cmds.loadPlugin('mpPhysicsNode.py')

##### modules
def CSV_import(FILENAME):
	CSVFILE = open(FILENAME)
	DATA=[]
	for ROW in csv.reader(CSVFILE):
		DATA.append(ROW)
	CSVFILE.close()
	return DATA
	

#####PhysicsEffecsノード作成
	
def createPENode(MODE,TRN=[0,0,0],ROT=[0,0,0],SCL=[1,1,1],CollisionAttrID1=0,CollisionAttrID2=0,DrawCollisionAttrID=0):
	PENODE=cmds.createNode('mpPhysicsNode')

	cmds.setAttr(PENODE+'.UseTRSData',True)
	cmds.setAttr(PENODE+'.UseTRSData',False)
	
	
	PE_TRANS=cmds.listRelatives(PENODE,p=True,typ='transform',f=True)[0]
	
	#アトリビュートセットアップ
	cmds.setAttr(PENODE+'.CollisionAttrID1',CollisionAttrID1,keyable=False)
	cmds.setAttr(PENODE+'.CollisionAttrID2',CollisionAttrID2,keyable=False)
	cmds.setAttr(PENODE+'.DrawCollisionAttrID',DrawCollisionAttrID,keyable=False)
	
	#エクストラアトリビュート
	cmds.addAttr(PENODE,at='bool',longName='convex')
	cmds.setAttr(PENODE+'.convex',True,keyable=False)
	cmds.addAttr(PENODE,at='bool',longName='hide')
	cmds.setAttr(PENODE+'.hide',True,keyable=False)
	
	#createPENode
	cmds.setAttr(PENODE+'.ShapeType',1)
	cmds.setAttr(PENODE+'.BoxSizeX',SCL[0]*0.5)
	cmds.setAttr(PENODE+'.BoxSizeY',SCL[1]*0.5)
	cmds.setAttr(PENODE+'.BoxSizeZ',SCL[2]*0.5)
	cmds.setAttr(PENODE+'.CapsuleLength',SCL[0]*0.5)
	cmds.setAttr(PENODE+'.CapsuleRadius',SCL[1]*0.5)
	cmds.setAttr(PENODE+'.SphereRadius',SCL[0]*0.5)
	
	if MODE=='sphere':
		cmds.setAttr(PENODE+'.ShapeType',0)
		SCL.sort()
		SCL.reverse()
		cmds.setAttr(PE_TRANS+'.SphereRadius',SCL[0]*0.5)
	elif MODE=='capsule_v':
		if SCL[0]<=SCL[1]:
			cmds.setAttr(PENODE+'.ShapeType',2)
			cmds.setAttr(PE_TRANS+'.CapsuleLength',(SCL[1]*0.5)-(SCL[0]*0.5))
			cmds.setAttr(PE_TRANS+'.CapsuleRadius',SCL[0]*0.5)
		else:
			cmds.setAttr(PENODE+'.ShapeType',0)
			cmds.setAttr(PE_TRANS+'.SphereRadius',SCL[0]*0.5)
	elif MODE=='cylinder_v':
		cmds.setAttr(PENODE+'.ShapeType',3)
		cmds.setAttr(PE_TRANS+'.CapsuleLength',SCL[1]*0.5)
		cmds.setAttr(PE_TRANS+'.CapsuleRadius',SCL[0]*0.5)
		cmds.setAttr(PENODE+'.BoxSizeX',SCL[1]*0.5)
		cmds.setAttr(PENODE+'.BoxSizeY',SCL[0]*0.5)
	elif MODE=='capsule_h':
		if SCL[0]>=SCL[1]:
			cmds.setAttr(PENODE+'.ShapeType',2)
			cmds.setAttr(PE_TRANS+'.CapsuleLength',(SCL[0]*0.5)-(SCL[1]*0.5))
			cmds.setAttr(PE_TRANS+'.CapsuleRadius',SCL[1]*0.5)
		else:
			cmds.setAttr(PENODE+'.ShapeType',0)
			cmds.setAttr(PE_TRANS+'.SphereRadius',SCL[1]*0.5)
	elif MODE=='cylinder_h':
		cmds.setAttr(PENODE+'.ShapeType',3)
		cmds.setAttr(PE_TRANS+'.CapsuleLength',SCL[0]*0.5)
		cmds.setAttr(PE_TRANS+'.CapsuleRadius',SCL[1]*0.5)
	
	#UseTRSData
	#cmds.setAttr(PENODE+'.UseTRSData',True)
	#configure otherTransform
	cmds.xform(PE_TRANS,ws=True,t=(TRN[0],TRN[1],TRN[2]))
	cmds.xform(PE_TRANS,ws=True,ro=(ROT[0],ROT[1],ROT[2]))
	if MODE=='cylinder_v' or MODE=='capsule_v' :
		cmds.setAttr(PENODE+'.UseTRSData',True)
		cmds.setAttr(PE_TRANS+'.rotateZ',ROT[2]+90)
		cmds.setAttr(PENODE+'.UseTRSData',False)
	
	return PE_TRANS

#####BestBB
	
def createPEBestBB(SHAPE_TYPE='cube'):
	SEL=cmds.ls(typ='transform',sl=True,l=True)
	if not SEL:
		SEL=cmds.ls(o=True,hl=True,l=True)
	for preEACH in SEL:
		if cmds.listRelatives(preEACH,c=True,type='mesh'):
			cmds.select(preEACH,r=True)
			PARENT_NODE=cmds.listRelatives(preEACH,p=True,f=True)
			#bestBB作成
			EACH=getBestBB.primitiveBestBB(preEACH)[0]
			
			TRNS=MS_primitives.getTransform(EACH,[],CENTERMODE='',BBMODE='',ROTMODE='')
			
			#コリジョン属性ID設定取得
			
			PATH='D:/Mproject/mdata/db/attribute.csv'
			COL_COLOR=int(ditectCollisionID(preEACH,PATH))
			
			#UID_PATH='D:/Mproject/mdata/db/uniq_obj_list.csv'
			if cmds.attributeQuery('uniqueobjectid',node=preEACH,ex=True) or cmds.attributeQuery('uniqueobjectid',node=cmds.listRelatives(preEACH,s=True,f=True)[0],ex=True):
				COL_ID=cmds.getAttr(preEACH+'.uniqueobjectid')
			else:
				COL_ID=0
			#create
			PENODES=createPENode(SHAPE_TYPE
				,TRN=[TRNS[0],TRNS[1],TRNS[2]]
				,ROT=[TRNS[3],TRNS[4],TRNS[5]]
				,SCL=[TRNS[6],TRNS[7],TRNS[8]]#XY逆転
				,CollisionAttrID1=COL_COLOR
				,CollisionAttrID2=int(COL_ID)
				,DrawCollisionAttrID=COL_COLOR
				)
			
			ATTRSET=getDynamicAttributes(EACH)
			#swap
			#delete
			cmds.delete(EACH)
			
			#Attributes Transfer
			for EACHATTRSET in ATTRSET:
				if EACHATTRSET[0] in EXCEPTION_ATTR:
					continue
				MP_MS_extraAttrController.autoSet2([PENODES],EACHATTRSET[0],EACHATTRSET[1])
			#
			
			NEW_NAME=cmds.rename(PENODES,preEACH.split('|')[-1]+'_pe')
			
			RESULT_NODE=cmds.parent(NEW_NAME,preEACH)
	
#####コア
	
def createPE(MODE,SHAPE_TYPE,DETAILMODE=True):
	SEL=cmds.ls(typ='transform',sl=True,l=True)
	COMP=[]
	if not SEL:
		SEL=cmds.ls(o=True,hl=True,l=True)
		COMP=cmds.filterExpand(ex=True,sm=(31,32,34))
	
	#simpleCreate
	if not SEL:
		createPENode(SHAPE_TYPE)
		return
	
	if COMP:
		COMPS=COMP
		BBMODE='compornent'
	else:
		COMPS=[]
		BBMODE=''
		
	
	for EACH in SEL:
		if cmds.listRelatives(EACH,c=True,type='mesh'):#メッシュ・PEノード作成処理
			cmds.select(EACH,r=True)
			
			#コリジョン属性ID設定取得
			COL_ID,COL_COLOR=getColID(EACH)
			
			#createPE
			TRNS=MS_primitives.getTransform(EACH,COMPS,CENTERMODE='',BBMODE=BBMODE,ROTMODE='')
			PENODES=createPENode(SHAPE_TYPE
				,TRN=[TRNS[0],TRNS[1],TRNS[2]]
				,ROT=[TRNS[3],TRNS[4],TRNS[5]]
				,SCL=[TRNS[6],TRNS[7],TRNS[8]]
				,CollisionAttrID1=COL_COLOR
				,CollisionAttrID2=int(COL_ID)
				,DrawCollisionAttrID=COL_COLOR
				)
			
			attributesTransfer(EACH,PENODES,MODE=MODE)
			
			if MODE=='swap':
					possessedToKillObjects(EACH,PENODES)
					
			elif MODE=='add' or MODE=='compornent':
				RESULT_NODE=cmds.parent(PENODES,EACH)
				
		elif cmds.listRelatives(EACH,c=True,type='mpPhysicsNode'):#PEノードからメッシュ作成処理
			PENODE=cmds.listRelatives(EACH,type='mpPhysicsNode',f=True)[0]
			COL_ID=cmds.getAttr(PENODE+'.CollisionAttrID1')
			NEW=PE2Mesh(EACH,SHAPE_TYPE)
			attributesTransfer(EACH,NEW)
			possessedToKillObjects(EACH,NEW)
			#paint
			
			cmds.polyColorSet(EACH,cr=True,cs='col_flag' )
			
			COLOR=getCollisionIDValue(COL_ID)
			p=1.0/255
			cmds.polyColorPerVertex(EACH,r=COLOR[0]*p,g=COLOR[1]*p,b=COLOR[2]*p)
			
			
			
	cmds.select(SEL,r=True)
	
def attributesTransfer(SRC_NODE,DST_NODE,MODE=''):
	ATTRS=MP_MS_extraAttrList_V2.all()
	
	#例外アトリビュート
	EXCEPTION_ATTR=['parts','convex']
	if MODE=='add' or MODE=='compornent' :
		for EACHATTR in MP_MS_extraAttrList_V2.mptrn():
			EXCEPTION_ATTR.append(EACHATTR[2])
		#TransformノードのConvex消し
		SHAPE=cmds.listRelatives(SRC_NODE,s=True,f=True)
		if cmds.attributeQuery('convex',node=SRC_NODE,exists=True):
			cmds.deleteAttr(EACH,attribute='convex')
		if cmds.attributeQuery('convex',node=SHAPE[0],exists=True):
			cmds.deleteAttr(SHAPE[0],attribute='convex')
		
	ATTRSET=getDynamicAttributes(SRC_NODE)
	#Attributes Transfer
	for EACHATTRSET in ATTRSET:
		if EACHATTRSET[0] in EXCEPTION_ATTR:
			continue
		MP_MS_extraAttrController.autoSet2([DST_NODE],EACHATTRSET[0],EACHATTRSET[1])
	
def possessedToKillObjects(POSSESSED,KILLER):
	RESULT_NODE=''
	PARENT_NODE=cmds.listRelatives(POSSESSED,p=True,f=True)
	cmds.delete(POSSESSED)
	NEW_NAME=cmds.rename(KILLER,POSSESSED.split('|')[-1])
	if PARENT_NODE:
		RESULT_NODE=cmds.parent(NEW_NAME,PARENT_NODE,a=True)
	return RESULT_NODE
	
def PE2Mesh(PETrans='',MODE='box'):
	NEW=[]
	PARENT_NODE=cmds.listRelatives(PETrans,p=True,f=True)
	TRN=cmds.xform(PETrans,q=True,ws=True,t=True)
	ROT=cmds.xform(PETrans,q=True,ws=True,ro=True)
	SCL=cmds.xform(PETrans,q=True,ws=True,s=True)
	
	PENode=cmds.listRelatives(PETrans,type='mpPhysicsNode')
	
	shapeType=cmds.getAttr(PENode[0]+'.ShapeType')
	
	X=1.0
	Y=1.0
	Z=1.0
	
	if shapeType==0:
		X=cmds.getAttr(PENode[0]+'.SphereRadius')
		
	if shapeType==1:
		X=cmds.getAttr(PENode[0]+'.BoxSizeX')*2
		Y=cmds.getAttr(PENode[0]+'.BoxSizeY')*2
		Z=cmds.getAttr(PENode[0]+'.BoxSizeZ')*2
		
	if shapeType==2:
		X=cmds.getAttr(PENode[0]+'.CapsuleRadius')
		Y=(cmds.getAttr(PENode[0]+'.CapsuleLength')*2)+(X*2)
		
	if shapeType==3:
		X=cmds.getAttr(PENode[0]+'.CapsuleRadius')
		Y=cmds.getAttr(PENode[0]+'.CapsuleLength')*2
		
	if MODE=='sphere':#Sphere
		NEW=cmds.polySphere(r=X,sx=10,sy=10)
		cmds.xform(NEW[0],t=[TRN[0],TRN[1],TRN[2]],ro=[ROT[0],ROT[1],ROT[2]],s=[SCL[0],SCL[1],SCL[2]])
		
	if MODE=='box':#Box
		NEW=cmds.polyCube(w=X,h=Y,d=Z)
		cmds.xform(NEW[0],t=[TRN[0],TRN[1],TRN[2]],ro=[ROT[0],ROT[1],ROT[2]],s=[SCL[0],SCL[1],SCL[2]])
		
	if MODE=='capsule_v' or MODE=='capsule_h':
		NEW=cmds.polyCylinder(r=X,h=Y,sx=10,sy=1,sz=0)
		cmds.xform(NEW[0],t=[TRN[0],TRN[1],TRN[2]],ro=[ROT[0],ROT[1],ROT[2]],s=[SCL[0],SCL[1],SCL[2]])
		cmds.setAttr(NEW[0]+'.rotateZ',ROT[2]-90)
		
	if MODE=='cylinder_v' or MODE=='cylinder_h':
		NEW=cmds.polyCylinder(r=X,h=Y,sx=10,sy=1,sz=0)
		cmds.xform(NEW[0],t=[TRN[0],TRN[1],TRN[2]],ro=[ROT[0],ROT[1],ROT[2]],s=[SCL[0],SCL[1],SCL[2]])
		cmds.setAttr(NEW[0]+'.rotateZ',ROT[2]+90)
		
		
	return NEW[0]
	
	
##### アトリビュート処理
#頂点カラーからSE情報取得
def isCollision(NODE):
	if cmds.attributeQuery('physics',node=NODE,ex=True):
		return True
	else:
		return False
	

#SE
def checkCol0(NODE):
	checkAttr=['collision0','collision1','collision2','collision3','collisionh']
	RET=False
	for each in checkAttr:
		if cmds.attributeQuery(each,n=NODE,ex=True):
			RET=True
			break
	return RET

def ditectCollisionID(NODE,PATH='D:/Mproject/mdata/db/attribute.csv'):
	
	if not isCollision(NODE):
		ALLCOLSET=cmds.polyColorSet(NODE,q=True,acs=True)
		if not ALLCOLSET:
			return 0
		
		
		if 'col_flag' in ALLCOLSET:
			
			VTX=MS_primitives.getVerts(NODE)
			
			CCS=cmds.polyColorSet(NODE,q=True,ccs=True)
			print CCS
			cmds.polyColorSet(NODE,ccs=True,cs='col_flag' )
			RGBf=cmds.polyColorPerVertex(VTX[0],q=True,rgb=True)
			cmds.polyColorSet(NODE,ccs=True,cs=CCS[0])
			
			RGB=[int(RGBf[0]*255),int(RGBf[1]*255),int(RGBf[2]*255)]
			SEARCH_WORD=str(RGB[0])+','+str(RGB[1])+','+str(RGB[2])
			
			ROW=CSV_import(PATH)
			for EACH in ROW:
				if SEARCH_WORD in EACH[4].encode('utf-8'):
					return EACH[0].encode('utf-8')
		else:
			return 0
	else:
		return 0
	
def getColID(NODE):
		#コリジョン属性ID設定取得
	PATH='D:/Mproject/mdata/db/attribute.csv'
	COL_COLOR=int(ditectCollisionID(NODE,PATH))
	
	if cmds.attributeQuery('uniqueobjectid',node=NODE,ex=True) or cmds.attributeQuery('uniqueobjectid',node=cmds.listRelatives(NODE,s=True,f=True)[0],ex=True):
		COL_ID=cmds.getAttr(EACH+'.uniqueobjectid')
	else:
		COL_ID=0
	
	return COL_ID,COL_COLOR
	
def getCollisionID():
	node=cmds.listRelatives(type='mpPhysicsNode',f=True)
	if not node:
		node=cmds.ls(type='mpPhysicsNode',l=True)
	
	print node
	
	if not node:
		return
	
	for each in node:
		if checkCol0(each):
			var=cmds.getAttr(each+'.CollisionAttrID1')
			cmds.text('MP_MS_createPE_CollisionAttrID1',e=True,l=var)
			var=cmds.getAttr(each+'.DrawCollisionAttrID')
			cmds.text('MP_MS_createPE_DrawCollisionAttrID',e=True,l=var)
			
			break
	
def addCollisionAttrID(ID):
	#selection
	cols=cmds.listRelatives(type='mpPhysicsNode',f=True)
	if not cols:
		cols=cmds.ls(type='mpPhysicsNode')
	if not cols:
		return
		
	for each in cols:
		if checkCol0(each):
			cmds.setAttr(each+'.CollisionAttrID1',int(ID))
			cmds.setAttr(each+'.DrawCollisionAttrID',int(ID))
	getCollisionID()
	
def getCollisionIDValue(ID,PATH='D:/Mproject/mdata/db/attribute.csv'):
	ROW=CSV_import(PATH)
	for each in  ROW:
		if each[0]==str(ID):
			 COLOR=each[4].split(',')
			 return (int(COLOR[0]),int(COLOR[1]),int(COLOR[2]))
			 
			 
	return False
	
def collisionIDList(PATH='D:/Mproject/mdata/db/attribute.csv'):
	ROW=CSV_import(PATH)
	
	if cmds.window('MP_MS_createPE_collisionIDList_window',q=True,ex=True):
		cmds.deleteUI('MP_MS_createPE_collisionIDList_window')
	cmds.window('MP_MS_createPE_collisionIDList_window',rtf=True,s=True)
	cmds.columnLayout()
	
	cmds.text(l=u'オブジェクト非選択時=全てのcollision#有ノードが対象')
	cmds.text(l=u'オブジェクト選択時  =選択ノードが対象')
	
	cmds.rowLayout(nc=2)
	cmds.text(l='CollisionAttrID1',al='left',w=120)
	cmds.text('MP_MS_createPE_CollisionAttrID1',l=0)
	cmds.setParent('..')
	cmds.rowLayout(nc=2)
	cmds.text(l='DrawCollisionAttrID',al='left',w=120)
	cmds.text('MP_MS_createPE_DrawCollisionAttrID',l=0)
	cmds.setParent('..')
	cmds.button('reflesh',c=lambda *args:collisionIDList(),w=250)
	#list
	cmds.scrollLayout(w=250,h=600)
	cmds.columnLayout()
	for each in ROW:
		cmds.rowLayout(nc=3)
		cmds.text(l=each[0],w=20)
		cmds.text(l=unicode(each[1],'shift-jis'),w=80)
		command='import MP_MS_createPE\nreload(MP_MS_createPE)\nMP_MS_createPE.addCollisionAttrID("'+each[0]+'")'
		cmds.button(l='setAttr',c=command,w=40)
		cmds.setParent('..')
	
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.showWindow('MP_MS_createPE_collisionIDList_window')
		
	getCollisionID()
	
##### UI
	#ダイナミックアトリビュート取得

def getDynamicAttributes(NODE):
	ATTRSET=[]
	SHAPE=cmds.listRelatives(NODE,s=True,f=True)
	ATTRSET=MP_MS_extraAttrController.dynamicQuery(NODE)
	SHAPE_ATTRSET=MP_MS_extraAttrController.dynamicQuery(SHAPE[0])
	ATTRSET.extend(SHAPE_ATTRSET)
	return ATTRSET
	
	
#ユーティリティ

def selectAllOldCollision():
	OLD_COL=[]
	SEL=cmds.ls(type='transform')
	for EACH in SEL:
		if '_col' in EACH or 'col_' in EACH or cmds.attributeQuery('physics',node=EACH,ex=True):
			if not cmds.listRelatives(EACH,type='mpPhysicsNode'):
				OLD_COL.append(EACH)
	if OLD_COL:
		cmds.select(OLD_COL,r=True)
	return OLD_COL
	
def selectAllPE():
	PENODE=cmds.ls(type='mpPhysicsNode')
	cmds.select(PENODE,r=True)
	return PENODE
	
def selectSelectedMeshPE(NODETYPE='mpPhysicsNode'):
	SEL=cmds.ls(sl=True,l=True,type='transform')
	SELECTED_PENODES=[]
	for EACHSEL in SEL:
		if cmds.objExists(EACHSEL):
			NODES=cmds.listRelatives(EACHSEL,c=True,f=True)
		else:
			continue
		for EACHNODE in NODES:
			PENODES=cmds.listRelatives(EACHNODE,s=True,type='mpPhysicsNode')
			if PENODES:
				if NODETYPE=='mpPhysicsNode':
					SELECTED_PENODES.extend(PENODES)
				if NODETYPE=='transformPE':
					SELECTED_PENODES.append(EACHNODE)
	#print SELECTED_PENODES
	cmds.select(SELECTED_PENODES,r=True)
	
def deletePhysicsNode():
	SEL=cmds.ls(sl=True,l=True,type='transform')
	for EACHSEL in SEL:
		if cmds.objExists(EACHSEL):
			NODES=cmds.listRelatives(EACHSEL,c=True,f=True)
		else:
			continue
		for EACHNODE in NODES:
			PENODES=cmds.listRelatives(EACHNODE,s=True,type='mpPhysicsNode')
			if PENODES:
				cmds.delete(EACHNODE)
	
def deleteEmptyGroups():
	GROUPS=cmds.ls(type='transform',l=True)
	for EACH in GROUPS:
		if not cmds.listRelatives(EACH,s=True):
			if not cmds.listRelatives(EACH,c=True):
				cmds.delete(EACH)
	
def setTRSflag(FLAG=''):
	NODES=cmds.ls(sl=True,type='mpPhysicsNode')
	if not NODES:
		NODES=cmds.listRelatives(c=True,type='mpPhysicsNode')
		if not NODES:
			return
	if not FLAG:
		FLAG=cmds.checkBox('MP_MS_TRSFlag',q=True,v=True)
		
	for EACH in NODES:
		cmds.setAttr(EACH+'.UseTRSData',FLAG)
	TRANS_NODES=cmds.listRelatives(NODES,p=True,type='transform')
	cmds.select(TRANS_NODES,r=True)
		
def freezePE(NODE=[]):
	if not NODE:
		PENODE=selectAllPE()
	else:
		PENODE=NODE
		cmds.select(PENODE,r=True)
	
	PE_TRANS=cmds.listRelatives(PENODE,p=True,type='transform')
	setTRSflag(FLAG=False)
	cmds.makeIdentity(PE_TRANS,a=True,s=True)
	#setTRSflag(FLAG=True)
	
def deleteMeshConvex(MESH=[]):
	if not MESH:
		MESH=cmds.ls(type='mesh')
	
	for EACH in MESH:
		MP_MS_extraAttrController.DEL_ATTR(EACH,'convex')
	#for TransformNode
	NODE=cmds.ls(type='transform')
	for EACH in NODE:
		if cmds.attributeQuery('convex',node=EACH,exists=True):
			cmds.deleteAttr(EACH,attribute='convex')
	
def deleteShapePE():
	OBJ=cmds.ls(sl=True)
	if not OBJ:
		cmds.ls(type='transform')
	for EACH in OBJ:
		if cmds.nodeType(cmds.listRelatives(EACH,s=True))=='mpPhysicsNode':
			continue
		MP_MS_extraAttrController.DEL_EXTRA_ATTR(EACH,TYPE='shape',EXCEPTION=['parts','hide'])
		print 'modified='+EACH
		
def layoutA(
	LABEL='MP_MS_createPE'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	cmds.button(l='add PE BestBB',w=200,bgc=[0.8,0.7,0.7],c=lambda *args:createPEBestBB())
	#cmds.button(l='add PE BestBB',w=200,bgc=[0.8,0.7,0.7],c=lambda *args:createPEBestBB('cylinder_v'))
	#add
	cmds.separator(w=200)
	cmds.text(l='addPE')
	cmds.rowLayout(nc=6)
	cmds.iconTextButton( style='iconOnly', image1='polySphere.xpm', label='sphere',c=lambda *args:createPE('add','sphere',DETAILMODE=False) )
	cmds.iconTextButton( style='iconOnly', image1='polyCube.xpm', label='polyCube',c=lambda *args:createPE('add','box',DETAILMODE=False) )
	cmds.iconTextButton( style='iconOnly', image1='polyCylinder.xpm', label='polyCylinderV',c=lambda *args:createPE('add','cylinder_v',DETAILMODE=False) )
	cmds.iconTextButton( style='iconOnly', image1='polyCylinder.xpm', label='polyCylinderH',c=lambda *args:createPE('add','cylinder_h',DETAILMODE=False) )
	cmds.iconTextButton( style='iconOnly', image1='polyCone.xpm', label='polyCone',c=lambda *args:createPE('add','capsule_v',DETAILMODE=False) )
	cmds.iconTextButton( style='iconOnly', image1='polyCone.xpm', label='polyCone',c=lambda *args:createPE('add','capsule_h',DETAILMODE=False) )
	cmds.setParent('..')
	#swap
	cmds.separator(w=200)
	cmds.text(l='swapPE')
	cmds.rowLayout(nc=6)
	cmds.iconTextButton( style='iconOnly', image1='polySphere.xpm', label='sphere',c=lambda *args:createPE('swap','sphere',DETAILMODE=False) )
	cmds.iconTextButton( style='iconOnly', image1='polyCube.xpm', label='polyCube',c=lambda *args:createPE('swap','box',DETAILMODE=False) )
	cmds.iconTextButton( style='iconOnly', image1='polyCylinder.xpm', label='polyCylinderV',c=lambda *args:createPE('swap','cylinder_v',DETAILMODE=False) )
	cmds.iconTextButton( style='iconOnly', image1='polyCylinder.xpm', label='polyCylinderH',c=lambda *args:createPE('swap','cylinder_h',DETAILMODE=False) )
	cmds.iconTextButton( style='iconOnly', image1='polyCone.xpm', label='polyCone',c=lambda *args:createPE('swap','capsule_v',DETAILMODE=False) )
	cmds.iconTextButton( style='iconOnly', image1='polyCone.xpm', label='polyCone',c=lambda *args:createPE('swap','capsule_h',DETAILMODE=False) )
	cmds.setParent('..')
	
def layoutB():
	#util
	cmds.separator(w=200)
	
	cmds.button(l='select\nAll\nOldCollision',w=60,h=60,c=lambda *args:selectAllOldCollision())
	cmds.separator(w=200)
	cmds.text(l='selectPE')
	cmds.rowLayout(nc=3)
	cmds.button(l='SEL_PETRN',w=50,bgc=[0.7,0.8,0.7],c=lambda *args:selectSelectedMeshPE(NODETYPE='transformPE'))
	cmds.button(l='SEL_PE',w=50,bgc=[0.7,0.8,0.7],c=lambda *args:selectSelectedMeshPE())
	cmds.button(l='ALL',w=100,bgc=[0.7,0.7,0.8],c=lambda *args:selectAllPE())
	cmds.setParent('..')
	cmds.separator(w=200)
	#cmds.button(l='freezePE',w=200,c=lambda *args:freezePE())
	cmds.separator(w=200)
	#cmds.checkBox('MP_MS_TRSFlag',l='setTRSflag',cc=lambda *args:setTRSflag())
	cmds.separator(w=200)
	cmds.button(l='deletePhysicsNode',w=200,c=lambda *args:deletePhysicsNode())
	cmds.separator(w=200)
	cmds.button(l='deleteMeshConvex',w=200,c=lambda *args:deleteMeshConvex())
	cmds.separator(w=200)
	cmds.button(l='deleteShapePE',w=200,c=lambda *args:deleteShapePE())
	cmds.separator(w=200)
	cmds.button(l='deleteEmptyGroups',w=200,c=lambda *args:deleteEmptyGroups())
	cmds.separator(w=200)
	#SE
	cmds.button(l='collisionIDList',w=200,bgc=[0.7,0.7,0.8],c=lambda *args:collisionIDList())
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.setParent('..')
	
def UI():
	if cmds.window('MP_MS_createPE_main_window',q=True,ex=True):
		cmds.deleteUI('MP_MS_createPE_main_window')
	cmds.window('MP_MS_createPE_main_window',rtf=True,s=True)
	
	layoutA()
	layoutB()
	cmds.showWindow('MP_MS_createPE_main_window')
	
def MP_MS_createPE():
	UI()
