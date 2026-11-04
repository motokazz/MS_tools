# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_distance.py
# 説明
#			距離計測モジュール
#			
# 作成日
#			
########################################
	
import maya.cmds as cmds
import math

##### 距離

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
		#POINT_A=bbCenterX(TARGET_A)
		#POINT_B=bbCenterX(TARGET_B)
		POINT_A = cmds.objectCenter(TARGET_A)
		POINT_B = cmds.objectCenter(TARGET_B)
	elif mode=='BBCenterFromAttribute':#バウンディングボックスセンターアトリビュートで距離計測
		POINT_A=BBCenterFromAttribute(TARGET_A)
		POINT_B=BBCenterFromAttribute(TARGET_B)
	#2点間の移動距離を計算
	LEN = math.sqrt((POINT_A[0]-POINT_B[0])*(POINT_A[0]-POINT_B[0])+(POINT_A[1]-POINT_B[1])*(POINT_A[1]-POINT_B[1])+(POINT_A[2]-POINT_B[2])*(POINT_A[2]-POINT_B[2]))
	
	return LEN

def BBCenterFromAttribute(OBJ=''):
	#アトリビュート内のBoundingBoxの値を見てセンターを算出する。選択ノードの子供も考慮。
	DAG=cmds.ls(OBJ,dag=True,type='transform',l=True)
	TRN=[]
	for each in DAG:
		
		try:
			SHAPE=cmds.listRelatives(each,s=True,f=True)
			BMIN=cmds.getAttr(SHAPE[0]+'.boundingBoxMin')
			BMAX=cmds.getAttr(SHAPE[0]+'.boundingBoxMax')
		except:
			continue

		PRETRN=cmds.xform(each,q=True,t=True,ws=True)

		TRN.append([
			((BMAX[0][0]+BMIN[0][0])*0.5 )+PRETRN[0]
			,((BMAX[0][1]+BMIN[0][1])*0.5 )+PRETRN[1] 
			,((BMAX[0][2]+BMIN[0][2])*0.5 )+PRETRN[2] 
			])

	#ヒエラルキー内オブジェクトの平均値
	DIV=len(TRN)
	if DIV<1:
		DIV=1
	TOTALX,TOTALY,TOTALZ=0,0,0
	for EACHPTRN in TRN:
		TOTALX+=EACHPTRN[0]
		TOTALY+=EACHPTRN[1]
		TOTALZ+=EACHPTRN[2]
	AVE=[TOTALX/DIV,TOTALY/DIV,TOTALZ/DIV]

	return AVE


def nearest(TARGET_A=[],TARGET_B=[],mode='translate'):
	#2つのオブジェクトリストを比較して、それぞれに最近接オブジェクトを対にしたリストを返す。
	#return [[targetA,nearest in targetB]...]
	RET=[]
	
	for Each_A in TARGET_A:
		ResultDist=100000000
		for Each_B in TARGET_B:
			CurrentDist=distance(Each_A,Each_B,mode)
			if CurrentDist<ResultDist:
				ResultDist=CurrentDist
				Result=Each_B
		RET.append([Each_A,Result])
	
	return RET
	
def nearestOne(TARGET_A='',TARGET_B=[],mode='translate'):
	#1つのオブジェクトと対象オブジェクトリストを比較して、最近接オブジェクトを返す。
	#return 'nearest in target'
	RET=''
	
	ResultDist=100000000
	for Each_B in TARGET_B:
		CurrentDist=distance(TARGET_A,Each_B,mode)
		if CurrentDist<ResultDist:
			ResultDist=CurrentDist
			RET=Each_B
	
	return RET
	
	
	
def BBdistance(TARGET_A,TARGET_B,mode='translate'):
	#バウンディングボックス最近接ポイントとの距離を計測（バウンディングボックス内に収まっていたら戻り値は[0,0,0]）
	#ピボット中心との距離を計測
	#戻り値は2つの値のより小さい方
	POINT_A = cmds.xform(TARGET_A,q=True,ws=True,t=True)
	BB=cmds.xform(TARGET_B,q=True,bb=True,ws=True)
	
	def compare(org,a,b):
		if abs(org-a)<org<abs(org-b) or abs(org-a)>org>abs(org-b):
			return org
		elif abs(org-a)<abs(org-b):
			return a
		else:
			return b
			
	X=compare(POINT_A[0],BB[0],BB[3])
	Y=compare(POINT_A[1],BB[1],BB[4])
	Z=compare(POINT_A[2],BB[2],BB[5])
	
	DIST=distance(TARGET_A,TARGET_B,mode='pivot')
	BBDIST=distance(POINT_A,[X,Y,Z],mode='vector')
	
	if DIST<BBDIST:
		return DIST
	else:
		return BBDIST
	



