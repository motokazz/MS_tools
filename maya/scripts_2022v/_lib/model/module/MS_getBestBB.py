# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_getBestBB
# 説明
#			
# 作成日
#			
########################################


import maya.cmds as cmds
import maya.mel as mel
import math
import random

##### math util
def BBMesure(OBJ):
	if not OBJ:
		return [1,1,1]
	FACE=getFaces(OBJ)
	#ポリゴンバウンディングボックス面積
	cmds.select(FACE,r=True)
	
	BB=cmds.xform(FACE,q=True,ws=True,bb=True)
	RET=[(BB[3]-BB[0]),(BB[4]-BB[1]),(BB[5]-BB[2])]
	
	return RET
	
def bbCenter(COMP=[]):
	if not COMP:
		OBJ=cmds.ls(sl=True)
		if not OBJ:
			return [0.0,0.0,0.0]
		else:
			COMP=getVerts(OBJ)
			if not COMP:
				return [0.0,0.0,0.0]
	else:
		COMP=getVerts(COMP)
		
	if COMP:
		cmds.select(COMP,r=True)
		PREBB=cmds.polyEvaluate(COMP,bc=True,ae=True)
		BBOX=[]
		BBOX.append(PREBB[0][0])
		BBOX.append(PREBB[1][0])
		BBOX.append(PREBB[2][0])
		BBOX.append(PREBB[0][1])
		BBOX.append(PREBB[1][1])
		BBOX.append(PREBB[2][1])
		
	TRN=[]
	TRN.append((BBOX[0]+BBOX[3])*0.5)
	TRN.append((BBOX[1]+BBOX[4])*0.5)
	TRN.append((BBOX[2]+BBOX[5])*0.5)
	return TRN
	
#rotate ditect
def rotMethod(NODE,TARGET,METHOD=0):
	for EACH in TARGET:
		if METHOD==2:#use constraint
			CONSTRAINT=cmds.normalConstraint(EACH,NODE,weight=1,aimVector=(0,1,0),upVector=(0,1,0),worldUpType='vector',worldUpVector=(0,1,0))
			cmds.delete(CONSTRAINT)
		
		if ROTMETHOD_CHECK==3:
			VECTOR=componentNormalAverage(EACH)
			ROT=globalAngleCheck(VECTOR)
			cmds.xform(NODE,ro=(ROT[0],0,ROT[1]))
	
def locatorToComponents(COMPS,AIM_VECTOR=[1,0,0]):
	TRN=bbCenter(COMPS)
	LOC=cmds.spaceLocator()
	cmds.xform(LOC,ws=True,t=TRN)
	#CONSTRAINT=cmds.normalConstraint(COMPS,LOC[0],weight=1,aimVector=AIM_VECTOR,upVector=[0,1,0],worldUpType='none',worldUpVector=[0,1,0])
	CONSTRAINT=cmds.normalConstraint(COMPS,LOC[0],weight=1)
	cmds.delete(CONSTRAINT)
	return LOC
	
def rotToNormalAverage(OBJ='',COMPS=[],AIM_VECTOR=[1,0,0]):
	#fit object rotate to poly normals avarage
	if not OBJ:
		PREOBJ=cmds.ls(sl=True,type='transform')
		if not PREOBJ:
			PREOBJ=cmds.ls(o=True,hl=True)
			if not PREOBJ:
				print 'no effect'
				return
		OBJ=PREOBJ[0]
	if not COMPS:
		COMPS=cmds.filterExpand(sm=(31,32,34))
		print 'filterExpand'
		if not COMPS:
			print 'getVerts'
			COMPS=getVerts(OBJ)
			if not COMPS:
				print 'no effect'
				return
	
	PARENT=cmds.listRelatives(OBJ,p=True)
	
	LOC=locatorToComponents(COMPS,AIM_VECTOR=AIM_VECTOR)
	PARENTED=cmds.parent(OBJ,LOC)
	cmds.makeIdentity(PARENTED,a=True,t=False,r=True,s=False)
	
	if PARENT:
		cmds.parent(PARENTED,PARENT)
	else:
		cmds.parent(PARENTED,w=True)
	
	cmds.delete(LOC)


def componentNormalAverage(COMP):
	#いろんなコンポーネントで法線ベクトルの平均値を帰す
	#フェースやエッジから法線平均値取るのに便利
	#モチロンバーテックスでも使えるよ。
	PRET=[0.0,0.0,0.0]
	RET=[0.0,0.0,0.0]
	VVV=cmds.polyListComponentConversion(COMP,tv=True)
	NRM=cmds.polyNormalPerVertex(VVV,q=True,xyz=True)
	NUM=0
	while NUM<len(NRM)/3:
		PRET[0]=PRET[0]+NRM[NUM]
		PRET[1]=PRET[1]+NRM[NUM+1]
		PRET[2]=PRET[2]+NRM[NUM+2]
		NUM+=3
	try:
		RET[0]=(PRET[0]/(len(NRM)/3))
	except:
		RET[0]=0
	try:
		RET[1]=(PRET[1]/(len(NRM)/3))
	except:
		RET[1]=0
	try:
		RET[2]=(PRET[2]/(len(NRM)/3))
	except:
		RET[2]=0
	return RET


def globalAngleCheck(vec):
	#ベクトルをグローバル座標系で回転値に変換、戻り値はXとZ
	OUT=[]
	xyLength = math.sqrt((vec[0]) * (vec[0]) +(vec[1]) * (vec[1]))
	vecLength = math.sqrt((vec[0]) * (vec[0]) +(vec[1]) * (vec[1]) +  (vec[2]) * (vec[2]))
	# $xyLength will be zero when $vec is pointing
	# along the +z or -z axis
	if xyLength == 0:
		if (vec[0]) > 0:
			zAngle = mel.eval('deg_to_rad(90);')
		else:
			zAngle = mel.eval('deg_to_rad(-90);')
	else:
		zAngle = mel.eval('acos(%s);'%(float(vec[1])/xyLength))
	
	xAngle = mel.eval('acos(%s);'%(xyLength/vecLength))
	if  vec[2]<= 0:
		xAngle = -xAngle
	OUT.append(mel.eval('rad_to_deg(%s);'%xAngle))
	if vec[0]>0:
		zAngle = -zAngle
	OUT.append(mel.eval('rad_to_deg(%s);'%zAngle))
	return OUT



	
def getRot(SEL=[]):
	RET=[]
	if not SEL:
		SEL=cmds.ls(sl=True)
	if SEL:
		RET=cmds.xform(SEL,q=True,ws=True,ro=True)
	else:
		RET=[0.0,0.0,0.0]
	return RET
	
def getScl(SEL=[]):
	
	RET=[]
	if not SEL:
		SEL=cmds.ls(sl=True)
	COMP=cmds.filterExpand(SEL,ex=True,sm=(31,32,34,35,47))
	if COMP:
		RET=BBMesure(COMP)
		RET.append(1)
	elif SEL:
		RET=BBMesure(SEL)
		#RET=cmds.xform(q=True,ws=True,s=True)
		RET.append(0)
	else:
		RET=[1.0,1.0,1.0,0]
	if RET[0]<=0:
		RET[0]=1
	if RET[1]<=0:
		RET[1]=1
	if RET[2]<=0:
		RET[2]=1
		
	return RET
	
	
def getTransform(OBJ='',COMPS=[],CENTERMODE='',BBMODE='',ROTMODE=''):
	RET=[]
	DUPED=cmds.duplicate(OBJ)
	
	#componentFunction
	DUPEDCOMP=[]
	for EACHCOMP in COMPS:
		TEMP=EACHCOMP.split('.')
		TEMP[0]=DUPED[0]
		DUPEDCOMP.append('.'.join(TEMP))
	
	#getRotation
	if ROTMODE=='normalAverage':
		rotToNormalAverage(DUPED[0],DUPEDCOMP,AIM_VECTOR=[0,1,0])
		ROT=getRot(DUPED[0])
	
	else:
		#print 'non normalAverage'
		ROT=getRot(DUPED[0])
	
	
	#getBB
	#
	cmds.setAttr(DUPED[0]+'.rx',0)
	cmds.setAttr(DUPED[0]+'.ry',0)
	cmds.setAttr(DUPED[0]+'.rz',0)
	
	cmds.makeIdentity(DUPED[0],a=True,t=False,r=False,s=True)
	if BBMODE=='compornent':
		if len(DUPEDCOMP)==1 and CENTERMODE=='face':
			DUPEDCOMP=getFaces(DUPEDCOMP)
		TRN=bbCenter(COMPS)
		SCL=BBMesure(DUPEDCOMP)
	else:
		#print 'non COMPONENT'
		TRN=bbCenter(DUPED[0])
		SCL=BBMesure(DUPED[0])
		#print SCL
	####
	
	if SCL[0]<0.01:
		SCL[0]=1
	if SCL[1]<0.01:
		SCL[1]=1
	if SCL[2]<0.01:
		SCL[2]=1
	if DUPED:
		cmds.delete(DUPED[0])
	#
	
	RET.extend(TRN)
	RET.extend(ROT)
	RET.extend(SCL)
	
	return RET
	
def BBVolume(OBJ):
	MESURE=BBMesure(OBJ)
	Volume=MESURE[0]*MESURE[1]*MESURE[2]
	return Volume
	
#####コンポーネント選択

def getFaces(COMP):#フェース選択
	FACE=cmds.polyListComponentConversion(COMP,tf=True)
	result=cmds.filterExpand(FACE,ex=True,sm=34)
	return result
	
def getVerts(COMP):#頂点選択
	VTX=cmds.polyListComponentConversion(COMP,tv=True)
	result=cmds.filterExpand(VTX,ex=True,sm=31)
	return result
	
def getEdges(COMP):#エッジ選択
	EDGE=cmds.polyListComponentConversion(COMP,te=True)
	result=cmds.filterExpand(EDGE,ex=True,sm=32)
	return result

def getVertsFaces(COMP):#フェース頂点選択
	FACE=cmds.polyListComponentConversion(COMP,tvf=True)
	result=cmds.filterExpand(FACE,ex=True,sm=70)
	return result
	
def selectFaceEdge():
	#選択オブジェクトの境界線
	BORDER_EDGES=[]
	FACE=cmds.filterExpand(sm=34)
	BORDER_EDGES=cmds.polyListComponentConversion(FACE,fv=True,ff=True,fuv=True,fvf=True,te=True,bo=True)
	return BORDER_EDGES
	
##########

def getBestBB(OBJ=[]):
	if not OBJ:
		OBJ=cmds.ls(sl=True)
	#
	DUPED=cmds.duplicate(OBJ)
	cmds.makeIdentity(DUPED[0],a=True,t=False,r=True,s=False)
	BB=BBVolume(DUPED[0])
	BASE=DUPED[0]
	
	#回転リスト定義
	K=45
	ARR=[[-K,0,0],[K,0,0],[0,-K,0],[0,K,0],[0,0,-K],[0,0,K],[K,K,0],[K,-K,0],[K,0,K],[K,0,-K],[-K,K,0],[-K,-K,0],[-K,0,K],[-K,0,-K],[K,K,K],[-K,K,K],[K,-K,K],[K,K,-K],[-K,-K,K],[-K,K,-K],[K,-K,-K],[-K,-K,-K]]
	
	
	#イテレーション減衰値定義
	NUM=[1,2,4,8,16,32,40,50,60,70,80,90,100]
	
	FINROT=cmds.xform(BASE,q=True,ro=True,r=True,eu=True)
	#FINROT=cmds.xform(BASE,q=True,ro=True,r=True)
	
	for I in NUM:
		IROT=FINROT
		for EACH in ARR:
			BASEE=cmds.duplicate(BASE)[0]
			#乱数かけてみる。
			#RANDA=random.uniform(1,1.25)
			#RANDB=random.uniform(1,1.25)
			#RANDC=random.uniform(1,1.25)
			
			RANDA=1
			RANDB=1
			RANDC=1
			
			ROT=[EACH[0]/I*RANDA+IROT[0],EACH[1]/I*RANDB+IROT[1],EACH[2]/I*RANDC+IROT[2]]
			
			#cmds.xform(BASE,ro=ROT,r=True,eu=True)
			cmds.xform(BASEE,ro=ROT)
			cmds.makeIdentity(BASEE,a=True,t=False,r=True,s=False)
			BBN=BBVolume(BASEE)
			
			if BB>BBN:#新しいBB面積小さかったら残し
				BB=BBN
				FINROT=ROT
				
			cmds.delete(BASEE)
	
	cmds.delete(BASE)
	
	return FINROT
	
def primitiveBestBB(OBJ=''):
	if not OBJ:
		SEL=cmds.ls(sl=True,type='transform')
		if SEL:
			OBJ=SEL[0]
		else:
			return
	
	PIV=cmds.xform(q=True,ws=True,piv=True)
	DUPED=cmds.duplicate(OBJ)
	ROT=getBestBB(DUPED[0])
	cmds.xform(DUPED[0],ro=[ROT[0],ROT[1],ROT[2]],r=True,eu=True)
	
	SCL=BBMesure(DUPED[0])
	TRN=bbCenter(DUPED[0])
	PRIM=cmds.polyCube( sx=1, sy=1, sz=1, h=1,w=1 )
	
	cmds.xform(PRIM[0],ws=True,s=(SCL[0],SCL[1],SCL[2]))
	cmds.xform(PRIM[0],ws=True,t=(TRN[0],TRN[1],TRN[2]))
	
	NEW=cmds.parent(PRIM[0],DUPED[0])
	
	cmds.duplicate(PRIM)
	
	cmds.xform(DUPED[0],ro=[0,0,0])
	
	NEWBB=cmds.parent(NEW,w=True)
	
	cmds.delete(DUPED[0])
	
	return NEWBB
	