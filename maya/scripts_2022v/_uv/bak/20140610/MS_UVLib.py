# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_UVLib.py
# 説明
#			UV関連のライブラリ
#			
# 作成日
#			
########################################
##################
#####ユーティリティ
##################
	
def getFaces(CONP):#フェース選択
	FACE=cmds.polyListComponentConversion(CONP,tf=True)
	result=cmds.filterExpand(FACE,ex=True,sm=34)
	return result
	
def getEdges(CONP):#エッジ選択
	EDGE=cmds.polyListComponentConversion(CONP,te=True)
	result=cmds.filterExpand(EDGE,ex=True,sm=32)
	return result
	
def getVerts(CONP):#頂点選択
	VTX=cmds.polyListComponentConversion(CONP,tv=True)
	result=cmds.filterExpand(VTX,ex=True,sm=31)
	return result
	
def getUV(CONP):#頂点選択
	UV=cmds.polyListComponentConversion(CONP,tuv=True)
	result=cmds.filterExpand(UV,ex=True,sm=35)
	return result
	
def edgeLength(EDGE):#エッジの長さ計算
	POINTS=getVerts(EDGE)
	POINT_A = cmds.xform(POINTS[0],q=True,ws=True,t=True)
	POINT_B = cmds.xform(POINTS[1],q=True,ws=True,t=True)
	LEN = math.sqrt((POINT_B[0]-POINT_A[0])**2+(POINT_B[1]-POINT_A[1])**2+(POINT_B[2]-POINT_A[2])**2)
	return LEN
	
def edgeUVLength(EDGE):#エッジのUV長さ計算
	POINTS=getUV(EDGE)
	POINT_A = cmds.polyEditUV(POINTS[0],q=True,u=True,v=True)
	POINT_B = cmds.polyEditUV(POINTS[1],q=True,u=True,v=True)
	LEN = math.sqrt((POINT_A[0]-POINT_B[0])**2+(POINT_A[1]-POINT_B[1])**2)
	
	return LEN
	
def getUVLength(POINTS):#エッジのUV長さ計算
	POINT_A = cmds.polyEditUV(POINTS[0],q=True,u=True,v=True)
	POINT_B = cmds.polyEditUV(POINTS[1],q=True,u=True,v=True)
	LEN = math.sqrt((POINT_A[0]-POINT_B[0])**2+(POINT_A[1]-POINT_B[1])**2)
	
	return LEN
	
def lengthCompEdge(EDG):#頂点に隣接するフェースを面積比較してソート済みリスト作成
	RET=[]
	for EACH_EDG in EDG:
		LENGTH=edgeLength(EACH_EDG)
		RET.append([EACH_EDG,LENGTH])
	return sorted(RET,key=lambda x:x[1],reverse=True)
	
def distance(TARGET_A,TARGET_B):
	
	POINT_A = cmds.xform(TARGET_A,q=True,ws=True,t=True)
	POINT_B = cmds.xform(TARGET_B,q=True,ws=True,t=True)
	#2点間の移動距離を計算
	LEN = math.sqrt((POINT_A[0]-POINT_B[0])*(POINT_A[0]-POINT_B[0])+(POINT_A[1]-POINT_B[1])*(POINT_A[1]-POINT_B[1])+(POINT_A[2]-POINT_B[2])*(POINT_A[2]-POINT_B[2]))
	
	return LEN





def selectShell(OBJ='',MODE='edge'):
	#シェル選択?
	if not OBJ:
		OBJ=cmds.ls(sl=True)
	cmds.select(OBJ,r=True)
	if MODE=='vtx':
		cmds.select(cmds.polyListComponentConversion(tv=True),r=True)
		cmds.polySelectConstraint(t=0x0001,m=2,sh=False,bo=True,pp=3)
		RET=cmds.filterExpand(sm=31)
	if MODE=='edge':
		cmds.select(cmds.polyListComponentConversion(te=True),r=True)
		cmds.polySelectConstraint(t=0x8000,m=2,sh=False,bo=True,pp=3)
		RET=cmds.filterExpand(sm=32)
	if MODE=='face':
		cmds.select(cmds.polyListComponentConversion(tf=True),r=True)
		cmds.polySelectConstraint(t=0x0008,m=2,sh=False,bo=True,pp=3)
		RET=cmds.filterExpand(sm=34)
	if MODE=='uv':
		cmds.select(cmds.polyListComponentConversion(tuv=True),r=True)
		cmds.polySelectConstraint(t=0x0010,m=2,sh=False,bo=True,pp=3)
		RET=cmds.filterExpand(sm=35)
			
	cmds.polySelectConstraint(dis=True)
	
	return RET

def separateUVIslands(UVS):
	#UVアイランドごとのUVリストを返す。
	#戻り値:[[アイランドのUVリスト１],[アイランドのUVリスト2],...]
	RET=[]
	cmds.select(UVS,r=True)
	cmds.select(cmds.polyListComponentConversion(tuv=True),r=True)
	UVS_EX=cmds.filterExpand(sm=35)
	while UVS_EX:
		cmds.select(UVS_EX[0])
		cmds.polySelectConstraint(t=0x0010,m=2,sh=True,bo=False,pp=0)
		TEMP=cmds.filterExpand(sm=35)
		UVS_EX=preservedList(UVS_EX,TEMP)
		RET.append(TEMP)
	cmds.polySelectConstraint(dis=True)
	return RET