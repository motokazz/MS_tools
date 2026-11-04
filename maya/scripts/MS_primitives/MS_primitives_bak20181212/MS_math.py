# _*_coding:utf-8_*_
########################################
# ファイル名
#			
# 説明
#			
# 作成日
#			
########################################
import maya.cmds as cmds
##### math util
def BBMesure(OBJ):
	if not OBJ:
		return [1,1,1]
	FACE=getFaces(OBJ)
	#ポリゴンバウンディングボックス面積
	cmds.select(FACE,r=True)
	BB=cmds.xform(FACE,q=True,r=True,bb=True)
	RET=[(BB[3]-BB[0]),(BB[4]-BB[1]),(BB[5]-BB[2])]
	return RET
	
def BBMesureWorld(OBJ):
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
		#BBOX=cmds.xform(COMP,q=True,ws=True,bb=True)
		print 'COMP'
		
		cmds.select(COMP,r=True)
		PREBB=cmds.polyEvaluate(COMP,bc=True)
		print PREBB
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
	





















