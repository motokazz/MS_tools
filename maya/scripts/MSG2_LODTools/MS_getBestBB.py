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
def xFormAverage(xf):
	#xform が連続した戻り値リスト（[[0,0,0],[1,1,1],[2,2,2],[3,3,3]...])を返してくるので、それを平均化する。
	x=0.0
	y=0.0
	z=0.0
	n=0
	RET=[0.0,0.0,0.0]

	while xf:
		x+=xf.pop(0)
		y+=xf.pop(0)
		z+=xf.pop(0)
		n+=1

	if x and n:
		RET[0]=x/n
	else:
		RET[0]=0
	if y and n:
		RET[1]=y/n
	else:
		RET[1]=0
	if z and n:
		RET[2]=z/n
	else:
		RET[2]=0
	return RET

def BBMesure_old(OBJ):
	if not OBJ:
		return [1,1,1]
	DUPED=dupObj(OBJ)
	NOBJ=unite(DUPED)
	FACE=getFaces(NOBJ)
	#ポリゴンバウンディングボックス面積
	cmds.select(FACE,r=True)
	BB=cmds.xform(q=True,ws=True,bb=True)
	RET=[(BB[3]-BB[0]),(BB[4]-BB[1]),(BB[5]-BB[2])]
	cmds.delete(NOBJ)
	return RET
	
def BBMesure(OBJ):
	if not OBJ:
		return [1,1,1]
	#ポリゴンバウンディングボックス面積
	BB=cmds.xform(OBJ,q=True,ws=True,bb=True)

	RET=[(BB[3]-BB[0]),(BB[4]-BB[1]),(BB[5]-BB[2])]
	return RET

def BBMesure_multi(OBJS):
	if not OBJS:
		return [1,1,1]
	#ポリゴンバウンディングボックス面積
	BB=BBMulti(OBJS)
	RET=[(BB[3]-BB[0]),(BB[4]-BB[1]),(BB[5]-BB[2])]
	return RET

def BBMesure_new(OBJ):
	if not OBJ:
		return [1,1,1]
	FACE=getFaces(OBJ)
	#ポリゴンバウンディングボックス面積
	cmds.select(FACE,r=True)

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

#バウンディングボックスセンターを返す。
def bbCenter(COMP=[],MODE='center'):
	#BB=cmds.polyEvaluate(bc=True)
	#RET=[(BB[0][1]-BB[0][0]),(BB[1][1]-BB[1][0]),(BB[2][1]-BB[2][0])]
	#return RET
	
	if not COMP:
		OBJ=cmds.ls(sl=True)
		if not OBJ:
			return [0.0,0.0,0.0]
		else:
			COMP=getVerts(OBJ)
			if not COMP:
				return [0.0,0.0,0.0]
	else:
		pass
		#COMP=getVerts(COMP)
	
	if COMP:
		BBOX=[]
		TRN=[]

		BBOX=cmds.xform(COMP,q=True,ws=True,bb=True)
		if MODE=='pivot':
			TRN.append((BBOX[0]+BBOX[3])*0.5)
			TRN.append((BBOX[1]+BBOX[4])*0.5)
			TRN.append((BBOX[2]+BBOX[5])*0.5)
		elif MODE=='center':
			TRN.append((BBOX[0]+BBOX[3])*0.5)
			TRN.append((BBOX[1]+BBOX[4])*0.5)
			TRN.append((BBOX[2]+BBOX[5])*0.5)
		elif MODE=='XPositive':
			TRN.append(BBOX[3])
			TRN.append((BBOX[1]+BBOX[4])*0.5)
			TRN.append((BBOX[2]+BBOX[5])*0.5)
		elif MODE=='XNegative':
			TRN.append(BBOX[0])
			TRN.append((BBOX[1]+BBOX[4])*0.5)
			TRN.append((BBOX[2]+BBOX[5])*0.5)
		elif MODE=='YPositive':
			TRN.append((BBOX[0]+BBOX[3])*0.5)
			TRN.append(BBOX[4])
			TRN.append((BBOX[2]+BBOX[5])*0.5)
		elif MODE=='YNegative':
			TRN.append((BBOX[0]+BBOX[3])*0.5)
			TRN.append(BBOX[1])
			TRN.append((BBOX[2]+BBOX[5])*0.5)
		elif MODE=='ZPositive':
			TRN.append((BBOX[0]+BBOX[3])*0.5)
			TRN.append((BBOX[1]+BBOX[4])*0.5)
			TRN.append(BBOX[5])
		elif MODE=='ZNegative':
			TRN.append((BBOX[0]+BBOX[3])*0.5)
			TRN.append((BBOX[1]+BBOX[4])*0.5)
			TRN.append(BBOX[2])
	else:
		TRN.append(0.0)
		TRN.append(0.0)
		TRN.append(0.0)
		
	return TRN
	
def BBVolume(OBJ):
	MESURE=BBMesure(OBJ)
	i=0
	for var in MESURE:
		if var<0.0001:
			MESURE[i]=0.0001
		i+=1

	Volume=MESURE[0]*MESURE[1]*MESURE[2]
	return Volume
	
#####コンポーネント選択

def getFaces(COMP):#フェース選択
	#print COMP
	FACE=cmds.polyListComponentConversion(COMP,tf=True)
	cmds.select(FACE,r=True)
	result=cmds.filterExpand(FACE,ex=True,sm=34)
	return result
	
def getVerts(COMP):#頂点選択
	VTX=cmds.polyListComponentConversion(COMP,tv=True)
	result=cmds.filterExpand(VTX,ex=True,sm=31)
	return result
	
##########
class centerResetter:

	def __init__(self,node):
		self.node=node
		self.tmr=[0,0,0]

	def centerPivot(self):#ピボットをオブジェクトの中心に
		cmds.xform(self.node,cp=True)

	def resetTransformFromPivot(self):#ピボットの中心座標を元に、オブジェクトをワールド原点に移動し、トランスフォームのフリーズ
		self.tmr=cmds.getAttr(self.node+'.transMinusRotatePivot')[0]
		cmds.xform(self.node,t=[self.tmr[0],self.tmr[1],self.tmr[2]],r=True)
		cmds.makeIdentity(self.node,a=True,t=True,r=False,s=False)
	
	def revertGap(self):#ピボットの中心座標を覚えておいて移動
		cmds.xform(self.node,t=[-self.tmr[0],-self.tmr[1],-self.tmr[2]])

	def centerResetter(self):#ピボットのワールド座標をオブジェクトのトランスフォームに変換
		self.resetTransformFromPivot()
		self.revertGap()

def duplicateComponent(comp=[]):
	face = cmds.polyListComponentConversion(comp,tf=True)
	OBJ = face[0].split('.')[0]
	DUPED = cmds.duplicate(OBJ,rc=True)

	if len(DUPED)>1:
		DUPED=cmds.polyUnite(DUPED,o=True)

	ncomp=[]
	for i in comp:
		a,b=i.split('.')
		ncomp.append(DUPED[0]+'.'+b)

	cmds.select(ncomp,r=True)
	temptrn=cmds.xform(ncomp,q=True,t=True,ws=True)
	mel.eval('InvertSelection;')
	cmds.delete()
	return DUPED
	
def unite(OBJ=[]):
	OBJS=cmds.ls(OBJ,dag=True,tr=True)
	if len(OBJS)>1:
		united=cmds.polyUnite(OBJS,ch=False)
		cmds.delete(OBJ)
		return united
	else:
		return OBJ

def dupObj(OBJ=[]):
	if not OBJ:
		OBJ=cmds.ls(sl=True)

	#コンポーネントチェック
	if '.' in OBJ[0]:
		comp = OBJ
	else:
		comp = cmds.filterExpand(sm=[31,32,34,70])

	#コア
	if comp:
		DUPED=duplicateComponent(comp)
	else:
		DUPED = cmds.duplicate(OBJ,rc=True)

	cmds.makeIdentity(DUPED,apply=True,t=False,r=True,s=False,n=False,preserveNormals=True)

	return DUPED

def dupComp(COMP=[]):
	
	face = cmds.polyListComponentConversion(COMP,tf=True)
	OBJ = face[0].split('.')[0]
	DUPED = cmds.duplicate(OBJ)
	ncomp=[]
	for i in face:
		a,b=i.split('.')
		ncomp.append(DUPED[0]+'.'+b)
	cmds.select(ncomp,r=True)
	temptrn=cmds.xform(ncomp,q=True,t=True,ws=True)
	mel.eval('InvertSelection;')
	cmds.delete()
	cmds.select(DUPED,r=True)
	return DUPED
	

### オブジェクトをrot値で回転させたときのバウンディングボックスのボリュームと、回転後の変換済のローテーション値を返す ###
def getBB(OBJ,rot):
	dup = cmds.duplicate(OBJ,rc=True)
	attrs=['tx','ty','tz','rx','ry','rz','sx','sy','sz']
	for eachDup in dup:
		for eachAttr in attrs:
			cmds.setAttr(eachDup+'.'+eachAttr,lock=False)

	cmds.xform(dup[0],ro=rot,r=True,eu=False)
	nRot = cmds.xform(dup[0],q=True,ro=True)#回転を加えてからの変換値を保存
	cmds.makeIdentity(dup[0],a=True,t=True,r=True,s=True)
	BVol = BBVolume(dup[0])
	cmds.delete(dup)
	return BVol,nRot

def getBestBB(OBJ=[]):
	#orgObj = dupObj(OBJ)[0]
	orgObj = dupComp(OBJ)[0]
	cmds.makeIdentity(orgObj,a=True,t=True,r=True,s=True)
	
	rotArr=[
		[30.0,0.0,0.0],[0.0,30.0,0.0],[0.0,0.0,30.0]
		,[23.0,0.0,0.0],[0.0,23.0,0.0],[0.0,0.0,23.0]
		,[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]
		]

	finrot=[0.0,0.0,0.0]#ローテーション初期値
	bbvOrg = getBB(orgObj,[0,0,0])#初期バウンディングボックスの値
	temp=bbvOrg
	for rot in rotArr:
		i=0
		while(i<5):
			n=2**i
			cmds.xform(orgObj,ro=finrot,r=False,eu=False)
			minRot=[-(rot[0]/n) ,-(rot[1]/n) ,-(rot[2]/n) ]
			maxRot=[ (rot[0]/n) , (rot[1]/n) , (rot[2]/n) ]

			bbvMin,nroMin = getBB(orgObj,minRot)
			bbvMax,nroMax = getBB(orgObj,maxRot)

			if bbvMin<bbvOrg and bbvMin<bbvMax:
				finrot=nroMin
				bbvOrg=bbvMin

			elif bbvMax<bbvOrg and bbvMax<bbvMin:
				finrot=nroMax
				bbvOrg=bbvMax

			i+=1

	cmds.xform(orgObj,ro=finrot,r=False,eu=False)

	################################################################
	#trn
	bbTrn=bbCenter(OBJ)

	#rot:一旦ペアレント化して逆ローテーションをとる。もっといい方法があるに違いない。。。
	cube=cmds.polyCube()
	cmds.parent(cube,orgObj)
	bbRot=cmds.xform(cube,q=True,ro=True)
	cmds.delete(cube)

	#scl
	cmds.makeIdentity(orgObj,a=True,t=True,r=True,s=True)
	bbScl=BBMesure(orgObj)
	cmds.delete(orgObj)
	'''
	#ditectPole
	if bbScl[0]>bbScl[1]>bbScl[2]:
		nbbRot=[bbRot[1],bbRot[0],bbRot[2]]
		nbbScl=[bbScl[1],bbScl[0],bbScl[2]]
	if bbScl[0]>bbScl[2]>bbScl[1]:
		nbbRot=[bbRot[0],bbRot[2],bbRot[1]]
		nbbScl=[bbScl[0],bbScl[2],bbScl[1]]
	if bbScl[1]>bbScl[0]>bbScl[2]:
		nbbRot=[bbRot[1],bbRot[0],bbRot[2]]
		nbbScl=[bbScl[1],bbScl[0],bbScl[2]]
	if bbScl[1]>bbScl[2]>bbScl[0]:
		nbbRot=[bbRot[1],bbRot[2],bbRot[0]]
		nbbScl=[bbScl[1],bbScl[2],bbScl[0]]
	if bbScl[2]>bbScl[0]>bbScl[1]:
		nbbRot=[bbRot[2],bbRot[0],bbRot[1]]
		nbbScl=[bbScl[2],bbScl[0],bbScl[1]]
	if bbScl[2]>bbScl[1]>bbScl[0]:
		nbbRot=[bbRot[2],bbRot[1],bbRot[0]]
		nbbScl=[bbScl[2],bbScl[1],bbScl[0]]
	return bbTrn+nbbRot+nbbScl
'''
	return bbTrn+bbRot+bbScl
	






