# _*_coding:utf-8_*_
########################################
# ファイル名
#           MS_getPosFromUV.py
# 説明
#           距離計測モジュール
#           
# 作成日
#           
########################################

import maya.cmds as cmds
from maya.OpenMaya import MVector
import math
import random
import MS_UILib

def distance(TARGET_A,TARGET_B,mode='translate'):
	#2つのオブジェクト指定で距離を計測
	if mode=='translate':#2つのオブジェクトを指定、ワールドトランスレートで距離計測
		POINT_A = cmds.xform(TARGET_A,q=True,ws=True,t=True)
		POINT_B = cmds.xform(TARGET_B,q=True,ws=True,t=True)
	elif mode=='pivot':#2つのオブジェクトを指定、ローテーションピボットでで距離計測
		POINT_A = cmds.xform(TARGET_A,q=True,ws=True,piv=True)
		POINT_B = cmds.xform(TARGET_B,q=True,ws=True,piv=True)
	elif mode=='vector':#実際の座標値を指定して距離計測
		POINT_A=TARGET_A
		POINT_B=TARGET_B
	elif mode=='BBCenter':#バウンディングボックスセンターで距離計測
		POINT_A=bbCenterX(TARGET_A)
		POINT_B=bbCenterX(TARGET_B)
	#2点間の移動距離を計算
	LEN = math.sqrt((POINT_A[0]-POINT_B[0])*(POINT_A[0]-POINT_B[0])+(POINT_A[1]-POINT_B[1])*(POINT_A[1]-POINT_B[1])+(POINT_A[2]-POINT_B[2])*(POINT_A[2]-POINT_B[2]))
	
	return LEN

def Distance2D(TARGET_A,TARGET_B):
	LEN = math.sqrt((TARGET_A[0]-TARGET_B[0])*(TARGET_A[0]-TARGET_B[0])+(TARGET_A[1]-TARGET_B[1])*(TARGET_A[1]-TARGET_B[1]))
	return LEN

def getWSPosFromUV(uv):
	vtx=cmds.polyListComponentConversion(uv,tv=True)
	ret = cmds.xform(vtx,q=True,t=True,ws=True)
	return ret

######################################################################



def test1(uv):

	vtx=cmds.polyListComponentConversion(uv,tv=True)
	
	uvv=cmds.polyEditUV(uv,q=True,u=True,v=True)
	
	aaa=wsb[0]-wsa[0]
	xxx=wsa[0]+uvv[0]*aaa
	bbb=wsb[2]-wsd[2]
	zzz=wsd[2]+uvv[1]*bbb
	
	cmds.xform(vtx,t=(xxx,0,zzz))


def  UVRandomPicker(NUM=10,SEL=[]):
	if not SEL:
		SEL=cmds.ls(sl=True)

	if '.' in SEL[0]:
		OBJ = SEL[0].split('.')[0]
	else:
		OBJ = SEL[0]

	UVS=cmds.polyListComponentConversion(OBJ,tuv=True)
	NUVS=cmds.filterExpand(UVS,sm=35,ex=True)
	return random.sample(NUVS,NUM)
	#return NUVS

def test2(uv):
	#4隅を定義

	uva='pPlane1.map[0]'
	uvb='pPlane1.map[5]'
	uvc='pPlane1.map[30]'
	uvd='pPlane1.map[35]'

	wsa=getWSPosFromUV(uva)
	wsb=getWSPosFromUV(uvb)
	wsc=getWSPosFromUV(uvc)
	wsd=getWSPosFromUV(uvd)

	uvap = cmds.polyEditUV(uva,q=True,u=True,v=True)
	uvbp = cmds.polyEditUV(uvb,q=True,u=True,v=True)
	uvcp = cmds.polyEditUV(uvc,q=True,u=True,v=True)
	uvdp = cmds.polyEditUV(uvd,q=True,u=True,v=True)

	print uv
	vtx=cmds.polyListComponentConversion(uv,tv=True)
	pos=getWSPosFromUV(uv)

	uvv=cmds.polyEditUV(uv,q=True,u=True,v=True)

	#
	da=Distance2D(uvap,uvv)
	print da
	db=Distance2D(uvbp,uvv)
	print db
	dc=Distance2D(uvcp,uvv)
	print dc
	dd=Distance2D(uvdp,uvv)
	print dd

	dallay=[da,db,dc,dd]
	dallay.sort(reverse=True)
	dmax = dallay[0]
	print dmax

	x=(wsa[0]*((dmax-da)/dmax)+wsb[0]*((dmax-db)/dmax)+wsc[0]*((dmax-dc)/dmax)+wsd[0]*((dmax-dd)/dmax))
	y=(wsa[1]*((dmax-da)/dmax)+wsb[1]*((dmax-db)/dmax)+wsc[1]*((dmax-dc)/dmax)+wsd[1]*((dmax-dd)/dmax))
	z=(wsa[2]*((dmax-da)/dmax)+wsb[2]*((dmax-db)/dmax)+wsc[2]*((dmax-dc)/dmax)+wsd[2]*((dmax-dd)/dmax))

	cmds.xform(vtx,t=(x,y,z),ws=True)


def test3(uv):
	print uv
	vtx=cmds.polyListComponentConversion(uv,tv=True)
	pos=getWSPosFromUV(uv)

	uvv=cmds.polyEditUV(uv,q=True,u=True,v=True)

	#
	UVRL=UVRandomPicker()
	DistanceList=[]
	WSL=[]
	ALLDIST=0
	for each in UVRL:
		UVP = cmds.polyEditUV(each,q=True,u=True,v=True)
		dist=Distance2D(UVP,uvv)
		DistanceList.append(dist)
		WS=getWSPosFromUV(each)
		WS.append(dist)
		WSL.append(WS)
		ALLDIST+=dist


	dmax = sorted(DistanceList,reverse=True)[0]
	dmin = sorted(DistanceList,reverse=True)[-1]

	x=0
	y=0
	z=0

	for eachp in WSL:
		ddd=dmax-dmin
		pc=(ddd-eachp[3])/ddd
		x+=eachp[0]*pc
		y+=eachp[1]*pc
		z+=eachp[2]*pc

	cmds.xform(vtx,t=(x,y,z),ws=True,a=True)

def DitectWeightUV(sample3,pos):
	#三角形３UV（sample3）からターゲットUV（pos）の重心を割り出す
	prepos = cmds.polyEditUV(pos,q=True,u=True,v=True)

	p=MVector(prepos[0],0,prepos[1])

	UVRL = [sample3[0],sample3[1],sample3[2]]
	v=[]
	for each in UVRL:
		pos=cmds.polyEditUV(each,q=True,u=True,v=True)
		#print pos
		vec = MVector(pos[0],0,pos[1])
		print vec.x,vec.y,vec.z
		print '++'
		v.append(vec)

	d1 = v[1] - v[0]
	d2 = v[2] - v[1]

	n = d1^d2

	u1,u2,u3,u4 = 0,0,0,0
	v1,v2,v3,v4 = 0,0,0,0

	if abs(n.x) >= abs(n.y) and abs(n.x) >= abs(n.z):
		u1 = v[0].y - v[2].y
		u2 = v[1].y - v[2].y
		u3 = p.y - v[0].y
		u4 = p.y - v[2].y

		v1 = v[0].z - v[2].z
		v2 = v[1].z - v[2].z
		v3 = p.z - v[0].z
		v4 = p.z - v[2].z

	elif abs(n.y) >= abs(n.z):
		u1 = v[0].z - v[2].z
		u2 = v[1].z - v[2].z
		u3 = p.z- v[0].z
		u4 = p.z - v[2].z

		v1 = v[0].x - v[2].x
		v2 = v[1].x - v[2].x
		v3 = p.x - v[0].x
		v4 = p.x - v[2].x

	else :
		u1 = v[0].x - v[2].x
		u2 = v[1].x - v[2].x
		u3 = p.x- v[0].x
		u4 = p.x - v[2].x

		v1 = v[0].y - v[2].y
		v2 = v[1].y - v[2].y
		v3 = p.y - v[0].y
		v4 = p.y - v[2].y

	denom = v1 * u2 - v2 * u1

	if not denom:
		print 'false'
		return False

	oneOverDenom = 1.0 / denom

	b=[]

	b.append( (v4 * u2 - v2 * u4) * oneOverDenom )
	b.append( (v1 * u3 - v3 * u1) * oneOverDenom )
	b.append( 1.0 - b[0] - b[1] )

	return b


def SetWeightPos(samplePos=['','',''],selPos=''):
	#3つのUV座標と、ターゲットUVを指定し、重心情報からターゲット頂点座標を移動する
	selUV=cmds.polyListComponentConversion(selPos,tuv=True)[0]
	selVtx=cmds.polyListComponentConversion(selPos,tv=True)[0]
	uvs=[]
	vtxs=[]
	for each in samplePos:
		uv = cmds.polyListComponentConversion(each,tuv=True)
		uvs.append(uv[0])
		vtx = cmds.polyListComponentConversion(each,tv=True)
		vtxs.append(vtx[0])
	volume = DitectWeightUV(sample3=[uvs[0],uvs[1],uvs[2]],pos=selUV)
	WeightTransform(vtxs,volume,selVtx)

def WeightTransform(vtxs,volume,selVtx):
	#selVtx（選択コンポーネント）を選択3頂点（vtxs）のポジションとそのvolume（重心比率）に基づいた移動
	x,y,z = 0,0,0
	i=0
	for i in range(0,3):
		pos=cmds.xform(vtxs[i],q=True,t=True,ws=True)
		x+=pos[0]*volume[i]
		y+=pos[1]*volume[i]
		z+=pos[2]*volume[i]
	cmds.xform(selVtx,t=(x,y,z),ws=True)

def WeightTransfromFromUV_BasedFromList():
	selUV=cmds.polyListComponentConversion(tuv=True)
	uvs=cmds.filterExpand(selUV,sm=35,ex=True)

	#ditect Base Point
	UVRL = MS_UILib.nodeList('MS_getPosFromUV_nodeList',q=True)[0:3]

	for each in uvs:
		SetWeightPos(samplePos=UVRL,selPos=each)

def WeightTransfromFromUV_BasedFromMaxTriangle():
	selUV=cmds.polyListComponentConversion(tuv=True)
	uvs=cmds.filterExpand(selUV,sm=35,ex=True)

	#ditect Base Point
	uvposs = []
	for each in uvs:
	    pos=cmds.polyEditUV(each,q=True,u=True,v=True)
	    uvposs.append([each,pos[0],pos[1]])

	UVRL = []
	res = sorted(uvposs,key=lambda x:x[1])
	res = sorted(res,key=lambda x:x[2])
	UVRL.append(res.pop(0)[0])

	res = sorted(res,key=lambda x:x[1])
	res = sorted(res,key=lambda x:x[2],reverse=True)
	UVRL.append(res.pop(0)[0])

	res = sorted(res,key=lambda x:x[1],reverse=True)
	res = sorted(res,key=lambda x:x[2])
	UVRL.append(res.pop(0)[0])

	for each in uvs:
		SetWeightPos(samplePos=UVRL,selPos=each)

def LayoutA():
	cmds.columnLayout('WeightTransfromFromUV_BasedFromMaxTriangleLayout',adj=True,w=200)
	cmds.button(l='BasedFromMaxTriangle',w=200,c=lambda *args:WeightTransfromFromUV_BasedFromMaxTriangle())
	cmds.setParent('..')

def LayoutB():
	cmds.columnLayout('MS_tools_WeightTransfromFromUV_BasedFromListLayout',adj=True)
	cmds.button(l='BasedFromList',w=200,c=lambda *args:WeightTransfromFromUV_BasedFromList())
	MS_UILib.nodeList('MS_getPosFromUV_nodeList')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	cmds.columnLayout()
	LayoutA()
	cmds.separator(w=200)
	LayoutB()
	cmds.setParent()
	cmds.showWindow('MS_tools_window')
	





