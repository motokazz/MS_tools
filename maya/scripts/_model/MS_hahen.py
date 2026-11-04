# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_hahen
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import maya.mel as mel

import _lib
reload(_lib)
	
import _uv.MS_bestUVSize as MS_bestUVSize
reload(MS_bestUVSize)
	
	
#####
	
def selectBorder(OBJ='',MODE='edge'):
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
	
def borderExtrude(OBJ=''):
	BE=selectBorder(OBJ,MODE='edge')
	cmds.polyExtrudeEdge(BE, kft=True)
	RES=cmds.filterExpand(sm=[31,32,34,35])
	return RES
	
def polyExtrude(OBJ='',OFS=10):
	cmds.polyExtrudeFacet(OBJ, kft=True, ltz=2, ls=(0,OFS, 0) )
	RES=cmds.filterExpand(sm=[31,32,34,35])
	return RES
	
def connectBorderBetweenObject(OBJA,OBJB,MODE='interpAB'):
	VTX_A=selectBorder(OBJA,MODE='vtx')
	VTX_B=selectBorder(OBJB,MODE='vtx')
	
	NEAREST_LIST=_lib.nearest(VTX_A,VTX_B)
	
	if MODE=='toB':
		for EACH in NEAREST_LIST:
			POS=cmds.xform(EACH[1],q=True,ws=True,t=True)
			cmds.xform(EACH[0],ws=True,t=POS)
	
	if MODE=='eachAB':
		for EACH in NEAREST_LIST:
			POS=cmds.xform(EACH[1],q=True,ws=True,t=True)
			cmds.xform(EACH[0],ws=True,t=POS)
		NEAREST_LIST_B=_lib.nearest(VTX_B,VTX_A)
		for EACH in NEAREST_LIST_B:
			POS=cmds.xform(EACH[1],q=True,ws=True,t=True)
			cmds.xform(EACH[0],ws=True,t=POS)
	
	if MODE=='interpAB':
		Blist={}
		for EACH in NEAREST_LIST:
			POSA=cmds.xform(EACH[0],q=True,ws=True,t=True)
			if not EACH[1] in Blist.keys():
				POSB=cmds.xform(EACH[1],q=True,ws=True,t=True)
				Blist.setdefault(EACH[1],POSB)
			else:
				POSB=Blist[EACH[1]]
			X=(POSA[0]+POSB[0])*0.5
			Y=(POSA[1]+POSB[1])*0.5
			Z=(POSA[2]+POSB[2])*0.5
			cmds.xform(EACH[0],ws=True,t=[X,Y,Z])
		
		if Blist.keys():
			for EACH in Blist.keys():
				cmds.xform(EACH,ws=True,t=Blist[EACH])
	#
	UNITED=cmds.polyUnite(OBJA,OBJB,ch=False)
	if cmds.objExists(OBJA):
		cmds.delete(OBJA)
	if cmds.objExists(OBJB):
		cmds.delete(OBJB)
		
	selectBorder(UNITED)
	cmds.polyMergeVertex(d=0)
	MERGED=cmds.filterExpand(sm=31)
	return [UNITED,MERGED]
	
def toCenterPoint(CP,COMP):
	VTXS=cmds.polyListComponentConversion(COMP,tv=True)
	cmds.xform(VTXS,t=CP[0:3],ws=True)
	cmds.select(VTXS,r=True)
	RET=cmds.polyMergeVertex()
	return RET
	
	
def  directOBJFromComponent(COMP):
	FACES=cmds.filterExpand(COMP,sm=[31,32,34,35],ex=True)
	return FACES[0].split('.')[0]
	
def invert(FACE):
	FACES=cmds.filterExpand(FACE,sm=34,ex=True)
	OBJ=directOBJFromComponent(FACE)
	TF=cmds.polyListComponentConversion(OBJ,tf=True)
	EXFACE=cmds.filterExpand(TF,sm=34,ex=True)
	for EACH in FACES:
		while EACH in EXFACE:EXFACE.remove(EACH)
	return EXFACE
	
def invertUV(UV=[]):
	if not UV:
		TUV=cmds.polyListComponentConversion(tuv=True)
		UVS=cmds.filterExpand(TUV,sm=35,ex=True)
	else:
		TUV=cmds.polyListComponentConversion(UV,tuv=True)
		UVS=cmds.filterExpand(TUV,sm=35,ex=True)
	print UVS
	OBJ=directOBJFromComponent(UVS)
	TUV=cmds.polyListComponentConversion(OBJ,tuv=True)
	EXUVS=cmds.filterExpand(TUV,sm=35,ex=True)
	for EACH in UVS:
		while EACH in EXUVS:EXUVS.remove(EACH)
	return EXUVS
	
	
def saw(COMP):
	EDGES=cmds.polyListComponentConversion(COMP,te=True)
	for EACH in EDGES:
		cmds.polyMapSewMove(EACH,nf=10,lps=0,ch=0)
	
def fitToSelectedUV(COMP=[]):
	if not COMP:
		COMP=cmds.filterExpand(sm=[31,32,34,35],ex=True)
	BORDER=selectBorder(COMP)
	
	OBJ=directOBJFromComponent(COMP)
	PRE_NOFUV=cmds.polyListComponentConversion(OBJ,tuv=True)
	NOFUV=cmds.filterExpand(PRE_NOFUV,sm=35,ex=True)
	
	preUVS=cmds.polyListComponentConversion(COMP,tuv=True)
	
	UVS=cmds.filterExpand(preUVS,sm=35,ex=True)
	
	AllUV=[]
	
	#
	RESERVE=reserveList()
	UVC=preservedList(UVS,RESERVE)
	reserveUVList=preservedList(UVS,UVC)
	print UVC,'*'
	print reserveUVList
	#move
	for EACH in UVC:
		nearUV=ditectNearestUV(EACH,reserveUVList)
		UVPOS=cmds.polyEditUV(nearUV,q=True,r=False)
		cmds.polyEditUV(EACH,u=UVPOS[0],v=UVPOS[1],r=False)
		AllUV.append(EACH)
		
	
	#saw(BORDER)
	
	#NonEffectList
	for EACH in AllUV:
		while EACH in NOFUV:NOFUV.remove(EACH)
	if NOFUV:
		cmds.select(NOFUV,r=True)
	
	cmds.select(COMP,r=True)
	
	return AllUV
	
def reserveList():
	preRESERVE=cmds.textFieldButtonGrp('MS_hahen_preserveList',q=True,tx=True)
	RESERVE=preRESERVE.split(';')
	return RESERVE
	
def preservedList(ORG,RESERVED):
	#ORGリスト内からRESERVEリストを削除したリストを返す
	RET=[]
	for EACH in ORG:
		if not EACH in RESERVED:
			RET.append(EACH)
	
	return RET
	
def unfold(UVS=[]):
	if not UVS:
		UVS=cmds.polyListComponentConversion(tuv=True)
	UVS=preservedList(UVS)
	#cmds.unfold(UVS,i=100000,ss=0.001,gb=0,gmb=1,pub=False,ps=0,oa=0,us=False)
	cmds.select(UVS,r=True)
	mel.eval('unfold -i 5000 -ss 0.001 -gb 0 -gmb 1 -pub 0 -ps  0 -oa  0 -us off;')
	
def lockUV(UVS=[],LOCK=True):
	if not UVS:
		UVS=cmds.polyListComponentConversion(tuv=True)
	for EACH in UVS:
		print EACH
		cmds.setAttr(EACH,l=LOCK)
	
def ditectConnectedUV(UV):
	VTX=cmds.polyListComponentConversion(UV,tv=True)
	preUVS=cmds.polyListComponentConversion(VTX,tuv=True)
	UVS=cmds.filterExpand(preUVS,sm=35,ex=True)
	while UV in UVS:UVS.remove(UV)
	return UVS
	
def ditectNearestUV(UV,UVLIST):
	distUV=cmds.filterExpand(cmds.polyListComponentConversion(UV,tvf=True),sm=70)
	sourceUV=cmds.filterExpand(cmds.polyListComponentConversion(UVLIST,tvf=True),sm=70)
	nearestVTXF=_lib.nearestOne(distUV,sourceUV)
	ret=cmds.polyListComponentConversion(nearestVTXF,tuv=True)
	return ret
	
def all(SIZE=0.5):
	TEX_SIZE=cmds.intSliderGrp('MS_hahen_tex',q=True,v=True)
	OBJ=cmds.ls(sl=True)
	for EACHOBJ in OBJ:
		#borderExtrude
		#OBJB=cmds.duplicate(EACHOBJ)
		
		#cmds.polyNormal (OBJB,normalMode=0,userNormalMode=0,ch=0)
		#cmds.xform(OBJB[0],s=[SIZE,SIZE,SIZE])
		#cmds.xform(OBJB[0],cp=True)
		#cmds.xform(OBJB[0],ro=[0,180,0],r=True,eu=True)
		EXA=borderExtrude(EACHOBJ)
		#EXB=borderExtrude(OBJB[0])
		#UNITED_MERGED=connectBorderBetweenObject(EACHOBJ,OBJB[0],MODE='eachAB')
		
		CP=cmds.xform(EACHOBJ,q=True,piv=True,ws=True)
		toCenterPoint(CP,EXA)
		
		MERGED_CP=cmds.filterExpand(sm=31)
		cmds.polyColorPerVertex(EACHOBJ,rgb=[0,0,0])
		
		continue
		
		##UV
		#FACES=cmds.polyListComponentConversion(UNITED_MERGED[1],tf=True)
		FACES=cmds.polyListComponentConversion(tf=True)
		cmds.polyAutoProjection(FACES,ch=False)
		ORGEDGE=selectBorder(FACES,MODE='edge')
		MS_bestUVSize.fitUVbyArea(FACES,Q=False,TEX_SIZE=TEX_SIZE,SIZE_PER_PIX=0.5)
		
		ORGFACES=invert(FACES)
		saw(ORGFACES)
		
		cmds.polyColorPerVertex(MERGED_CP,rgb=[1,0,0])
		
def uv(FACES=[],UVNO=0):
	
	TEX_SIZE=cmds.intSliderGrp('MS_hahen_tex',q=True,v=True)
	if not FACES:
		SEL=cmds.ls(sl=True)
		FIRST_FACES=cmds.filterExpand(cmds.polyListComponentConversion(SEL,tf=True),sm=34)
		VTXS=cmds.polyListComponentConversion(SEL,tv=True)
		FACES=cmds.filterExpand(cmds.polyListComponentConversion(VTXS,tf=True),sm=34)
	else:
		VTXS=cmds.polyListComponentConversion(FACES,tv=True)
	
	#UV
	OBJ=directOBJFromComponent(FACES)
	UVS=cmds.polyUVSet(OBJ,q=True,auv=True)
	NUV=UVNO-len(UVS)+1
	if NUV:
		for EACH in range(1,NUV+1):
			cmds.polyUVSet(OBJ,copy=True,uvSet=UVS[0])
	NEWUVS=cmds.polyUVSet(OBJ,q=True,auv=True)
	cmds.polyUVSet(OBJ,uvSet=NEWUVS[UVNO],cuv=True)
	#
	FACES=preservedList(FACES,FIRST_FACES)
	MS_bestUVSize.bestPlaneProjection(FIRST_FACES,TEX_SIZE=TEX_SIZE,SIZE_PER_PIX=0.5)
	MS_bestUVSize.bestPlanePerPoly(FACES,TEX_SIZE=TEX_SIZE,SIZE_PER_PIX=0.5,considerUVIsland=False)
	OBJ=directOBJFromComponent(FACES)
	
	cmds.polyColorPerVertex(VTXS,rgb=[1,0,0])
	cmds.select(FIRST_FACES,r=True)
	
#####  FirstCommand
def preall(MODE='all'):
	if MODE=='all':
		VOL=cmds.floatSliderGrp('MS_hahen_volume',q=True,v=True)
		all(VOL)
		
	if MODE=='connectBorderBetweenObject':
		OBJ=cmds.ls(sl=True,typ='transform')
		if len(OBJ)>1:
			borderExtrude(OBJ[0])
			connectBorderBetweenObject(OBJ[0],OBJ[1],MODE='toB')
	
	

##### UI

def createPreserveList():
	preUVS=cmds.polyListComponentConversion(tuv=True)
	UVS=cmds.filterExpand(preUVS,sm=35,ex=True)
	cmds.textFieldGrp('MS_hahen_preserveList',e=True,tx=';'.join(UVS))
	
def addPreserveList():
	TX=cmds.textFieldButtonGrp('MS_hahen_preserveList',q=True,tx=True)
	if TX:
		LIST=TX.split(';')
	else:
		LIST=[]
	preUVS=cmds.polyListComponentConversion(tuv=True)
	UVS=cmds.filterExpand(preUVS,sm=35,ex=True)
	
	RET=list(set(LIST+UVS))
	cmds.textFieldButtonGrp('MS_hahen_preserveList',e=True,tx=';'.join(RET))
	
def removePreserveList():
	TX=cmds.textFieldButtonGrp('MS_hahen_preserveList',q=True,tx=True)
	LIST=TX.split(';')
	preUVS=cmds.polyListComponentConversion(tuv=True)
	UVS=cmds.filterExpand(preUVS,sm=35,ex=True)
	
	for EACH in UVS:
		while EACH in LIST:LIST.remove(EACH)
	
	cmds.textFieldButtonGrp('MS_hahen_preserveList',e=True,tx=';'.join(LIST))
	
def clearPreserveList():
	cmds.textFieldButtonGrp('MS_hahen_preserveList',e=True,tx='')
	
def layoutA(
	LABEL='MS_hahen'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.floatSliderGrp('MS_hahen_volume',f=True,v=0.9)
	cmds.intSliderGrp('MS_hahen_tex',min=4,max=4096,f=True,v=1024)
	cmds.button(w=WIDTH-4,l=u'MSExtrude',c=lambda *args:preall(MODE='all'))
	cmds.button(w=WIDTH-4,l=u'connectBorderBetweenObject',c=lambda *args:preall(MODE='connectBorderBetweenObject'))

	cmds.button(w=WIDTH-4,l=u'INVERT',c=lambda *args:invert())
	cmds.button(w=WIDTH-4,l=u'SEL_BORDER',c=lambda *args:selectBorder(MODE='uv'))
	#LockList
	cmds.textFieldButtonGrp('MS_hahen_preserveList',bc=lambda *args:createPreserveList())
	cmds.rowLayout(nc=4)
	cmds.button(w=40,l=u'create',c=lambda *args:createPreserveList())
	cmds.button(w=40,l=u'add',c=lambda *args:addPreserveList())
	cmds.button(w=40,l=u'remove',c=lambda *args:removePreserveList())
	cmds.button(w=40,l=u'clear',c=lambda *args:clearPreserveList())
	cmds.setParent('..')
	#createUV
	cmds.text(l='UV(bestPlanePerPoly)')
	cmds.rowLayout(nc=4)
	cmds.button(w=50,l=u'UV0',c=lambda *args:uv(UVNO=0))
	cmds.button(w=50,l=u'UV1',c=lambda *args:uv(UVNO=1))
	cmds.button(w=50,l=u'UV2',c=lambda *args:uv(UVNO=2))
	cmds.button(w=50,l=u'UV3',c=lambda *args:uv(UVNO=3))
	cmds.setParent('..')
	cmds.button(w=WIDTH-4,l=u'fitToSelectedUV',c=lambda *args:fitToSelectedUV())
	cmds.button(w=WIDTH-4,l=u'unfold',c=lambda *args:unfold())

def UI():
	if cmds.window('MS_hahen_main_window',q=True,ex=True):
		cmds.deleteUI('MS_hahen_main_window')
	cmds.window('MS_hahen_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_hahen_main_window')
	


