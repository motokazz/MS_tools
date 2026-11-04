# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_fit_UV_by_area.py
# 説明
#			
#			
# 作成日
#			
########################################

###################
#####フィットUVコア
###################
	
def preservedList(ORG,RESERVE=[]):
	if not RESERVE:
		preRESERVE=cmds.textFieldButtonGrp('MS_hahen_preserveList',q=True,tx=True)
		RESERVE=preRESERVE.split(';')
	for EACH in RESERVE:
		while EACH in ORG:ORG.remove(EACH)
	return ORG
		
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

#####
def listCompornentPerPoly(COMP):
	#オブジェクト複数選択時、オブジェクトごとのコンポーネントを辞書化
	#戻り値:{'オブジェクト名',[コンポーネントID]}
	DICT={}
	for EACH in COMP:
		TEMP=EACH.split('.')
		if not TEMP[0] in DICT.keys():
			DICT[TEMP[0]]=[TEMP[1]]
		else:
			DICT[TEMP[0]].append(TEMP[1])
	return DICT

##### フィットUV面積
def docore(OBJ,POLYS=[],Q=False,TEX_SIZE_U=1024,TEX_SIZE_V=1024,SIZE_PER_PIX=0.5,considerUVIsland=True):
	RET=[]
	DICT=listCompornentPerPoly(OBJ)
	for EACH in DICT.keys():
		preCOMP=[]
		COMPLIST=[]
		for EACHB in DICT[EACH]:
			preCOMP.append(EACH+'.'+EACHB)
		#UVShellで分ける
		if considerUVIsland:
			COMPLISTS=separateUVIslands(preCOMP)
		else:
			COMPLISTS=[preCOMP]
		#Shellごとに値リストを返す
		for COMPLIST in COMPLISTS:
			CurrentUVSet=cmds.polyUVSet(COMPLIST,q=True,cuv=True)[0]
			POLY=cmds.polyListComponentConversion(COMPLIST,tf=True)
			cmds.select(POLY,r=True)
			#エリア計測
			POLY_AREA=calcPolyArea()
			UV_AREA=calcUVArea(uvset=CurrentUVSet)

			#ギャップ計測
			try:
				SVALUE=math.sqrt((POLY_AREA*(SIZE_PER_PIX**2))/(UV_AREA*(TEX_SIZE_U*TEX_SIZE_V)))
				#SVALUE=math.sqrt(((POLY_AREA*SIZE_PER_PIX)**2)/((UV_AREA*TEX_SIZE*TEX_SIZE)**2))
				#SVALUE=math.sqrt((POLY_AREA*SIZE_PER_PIX**2)/(UV_AREA*TEX_SIZE**2))
			except:
				SVALUE=1

			if Q:
				cmds.floatField('MS_bestUVSize_checkGap',e=True,v=SVALUE)
				print '-------------------------------------------------'
				print 'polyArea = '+str(POLY_AREA)
				print 'sizePerPixels = '+str(POLY_AREA*(SIZE_PER_PIX**2))
				print 'uvArea = '+str(UV_AREA)+'*'+str(TEX_SIZE_U*TEX_SIZE_V)+'='+str(UV_AREA*TEX_SIZE_U*TEX_SIZE_V)
				print 'size gap = '+str(SVALUE)
				print '-------------------------------------------------'
			else:
				cmds.select(COMPLIST,r=True)
				#print COMPLIST
				#print  SVALUE
				#cmds.polyNormalizeUV(COMPLIST,uvs=CurrentUVSet,normalizeType=1,preserveAspectRatio=True)
				cmds.polyEditUV(COMPLIST , uvs=CurrentUVSet , scaleU=SVALUE , scaleV=SVALUE , pivotU=0.5 , pivotV=0.5 )

def fitUVbyArea(POLYS=[],Q=False,TEX_SIZE_U=1024,TEX_SIZE_V=1024,SIZE_PER_PIX=0.5,considerUVIsland=True):#フェースを利用してUVサイズをフィッティング
	if not POLYS:
		POLYS=cmds.ls(sl=True)
		if not POLYS:
			return
						
	if cmds.nodeType(POLYS[0])=='transform':
		for EACH in POLYS:
			CurrentUVSet=cmds.polyUVSet(EACH,q=True,cuv=True)[0]
			EACHPOLYS=cmds.polyListComponentConversion(EACH,tf=True)
			docore(EACHPOLYS,POLYS=POLYS,Q=Q,TEX_SIZE=TEX_SIZE,SIZE_PER_PIX=SIZE_PER_PIX,considerUVIsland=considerUVIsland)
	else:
		docore(POLYS,POLYS=POLYS,Q=Q,TEX_SIZE_U=TEX_SIZE_U,TEX_SIZE_V=TEX_SIZE_V,SIZE_PER_PIX=SIZE_PER_PIX,considerUVIsland=considerUVIsland)
	
	cmds.select(POLYS,r=True)
	
def pre_fitUVbyArea(Q=False):
	TEX_SIZE_U=cmds.intField('MS_bestUVSize_texsizeU',q=True,v=True)
	TEX_SIZE_V=cmds.intField('MS_bestUVSize_texsizeV',q=True,v=True)
	SIZE_PER_PIX=cmds.floatField('MS_bestUVSize_sizeperpix',q=True,v=True)
	considerUVIsland=cmds.checkBox('MS_bestUVSize_considerUVIsland',q=True,v=True)
	fitUVbyArea(POLYS=[],Q=Q,TEX_SIZE_U=TEX_SIZE_U,TEX_SIZE_V=TEX_SIZE_V,SIZE_PER_PIX=SIZE_PER_PIX,considerUVIsland=considerUVIsland)

def printCalcPoly():
	print calcPolyArea()
	print calcUVArea()
