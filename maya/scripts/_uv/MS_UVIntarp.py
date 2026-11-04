# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_UVIntarp
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import math

THIS_SCRIPT='MS_UVIntarp'


def fitToTargets():
	COMP=cmds.textScrollList('MS_transformIntarp_list',q=True,ai=True)
	SEL = cmds.filterExpand(sm=34,ex=True)
	for i in range(len(COMP)):
		TRN=cmds.polyEditUV(COMP[i],q=True,u=True,v=True)
		cmds.polyEditUV(SEL[i],r=False,u=TRN[0],v=TRN[1])
	


def interp(a,b,quantity,NUM):
	c=a-(((a-b)/quantity)*(NUM))
	return c
	
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


def posInterp(PA,PB,PC):
	PAPB=Distance2D(PA,PB)
	PAPC=Distance2D(PA,PC)

	PU=PA[0]+(PB[0]-PA[0])*(PAPC/PAPB)
	PV=PA[1]+(PB[1]-PA[1])*(PAPC/PAPB)
	#PZ=PA[2]+(PB[2]-PA[2])*(PAPC/PAPB)
	return [PU,PV]

def edgeLength(A,B):#エッジの長さ計算
	POINT_A = cmds.xform(A,q=True,ws=True,t=True)
	POINT_B = cmds.xform(B,q=True,ws=True,t=True)
	LEN = math.sqrt((POINT_A[0]-POINT_B[0])*(POINT_A[0]-POINT_B[0])+(POINT_A[1]-POINT_B[1])*(POINT_A[1]-POINT_B[1])+(POINT_A[2]-POINT_B[2])*(POINT_A[2]-POINT_B[2]))
	
	return LEN
	
def rangeSort():
	COMP=cmds.filterExpand(ex=True,sm=[31,32,34,35])
	RET=[]
	TMP=[]
	TMPB=[]
	for EACH in COMP:
		TRN=cmds.xform(EACH,q=True,ws=True,t=True)
		TMP.append([EACH,TRN[0]+TRN[1]+TRN[2]])
	ORG=sorted(TMP,key=lambda x:x[1],reverse=True)[0][0]
		
	for EACHB in COMP:
		LENGTH=edgeLength(ORG,EACHB)
		TMPB.append([EACHB,LENGTH])
		
	for EACHA in sorted(TMPB,key=lambda x:x[1],reverse=True):
		RET.append(EACHA[0])
	print TMPB
	return RET
	
	
def do(U=False,V=False):
	PUV = cmds.checkBox('PreserveUV',q=True,v=True)
	considerDistance = cmds.checkBox('considerDistance',q=True,v=True)
	COMP=cmds.textScrollList('MS_transformIntarp_list',q=True,ai=True)
	#COMP=rangeSort()
	QUANTITY=len(COMP)
	
	TRN_A=cmds.polyEditUV(COMP[0],q=True,u=True,v=True)
	TRN_B=cmds.polyEditUV(COMP[-1],q=True,u=True,v=True)
	NUM=0

	for EACH in COMP:
		TRN=cmds.polyEditUV(EACH,q=True,u=True,v=True)
		IXYZ=[0,0]
		if considerDistance:
			IXYZ=posInterp(TRN_A,TRN_B,TRN)
		else:
			IXYZ[0]=interp(TRN_A[0],TRN_B[0],QUANTITY-1,NUM)
			IXYZ[1]=interp(TRN_A[1],TRN_B[1],QUANTITY-1,NUM)

		if U:
			TRN[0]=IXYZ[0]
		if V:
			TRN[1]=IXYZ[1]

		cmds.polyEditUV(EACH,r=False,u=TRN[0],v=TRN[1])
		NUM+=1
		
	
def addList():
	COMP=cmds.filterExpand(ex=True,sm=[35])
	if not COMP:
		clearList()
		return
	AI=cmds.textScrollList('MS_transformIntarp_list',q=True,ai=True)
		
	if not AI:
		AI=''
	clearList()
	
	for EACH in AI:
		if EACH in COMP:
			cmds.textScrollList('MS_transformIntarp_list',e=True,append=EACH)
	for EACH in COMP:
		if not EACH in AI:
			cmds.textScrollList('MS_transformIntarp_list',e=True,append=EACH)

def clearList():
	cmds.textScrollList('MS_transformIntarp_list',e=True,ra=True)

def job():
	jobNum = cmds.scriptJob(e=["SelectionChanged",THIS_SCRIPT+".addList()"],parent='MS_transformIntarp_main_window',protected=True)
	
def layoutA(
	LABEL='MS_UVIntarp'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	# Buttons
	cmds.rowLayout(nc=3)
	cmds.button(l='U',w=50,bgc=[0.8,0.5,0.5],c=lambda *args:do(U=True))
	cmds.button(l='V',w=50,bgc=[0.5,0.8,0.5],c=lambda *args:do(V=True))
	cmds.button(l='UV',w=50,bgc=[0.5,0.5,0.8],c=lambda *args:do(U=True,V=True))
	cmds.setParent('..')
	
	#Option
	cmds.separator(w=210,h=10)
	cmds.checkBox('PreserveUV',l='PreserveUV')
	cmds.checkBox('considerDistance',l='considerDistance',v=True)
	cmds.separator(w=210,h=10)
	# Component Lists
	cmds.button(w=WIDTH-4,l=u'addlist',c=lambda *args:addList())
	cmds.textScrollList('MS_transformIntarp_list',h=100)
	cmds.button(w=WIDTH-4,l=u'clearlist',c=lambda *args:clearList())
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_transformIntarp_main_window',q=True,ex=True):
		cmds.deleteUI('MS_transformIntarp_main_window')
	cmds.window('MS_transformIntarp_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_transformIntarp_main_window')
	job()
	addList()

