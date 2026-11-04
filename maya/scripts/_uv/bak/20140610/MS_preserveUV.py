# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_preserveUV
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds
import maya.mel as mel
	
def do():
	print 'do'

def directOBJFromComponent(COMP):
	COMPS=cmds.filterExpand(COMP,sm=[31,32,34,35],ex=True)
	return COMPS[0].split('.')[0]
	

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
	
def listUVIsland(UV=[]):#
	if UV:
		cmds.select(UV,r=True)
	elif 	not cmds.filterExpand(sm=35):
		return
	cmds.polySelectConstraint(t=0x0010,m=2,sh=True,bo=False,pp=0)
	UVIsland=cmds.filterExpand(sm=35)
	cmds.polySelectConstraint(dis=True)
	return UVIsland
	
def preservedList(ORG,RESERVE=[]):
	#ORGリスト内からRESERVEリストを削除したリストを返す
	if not RESERVE:
		preRESERVE=cmds.textFieldButtonGrp('MS_preserveUV_preserveList',q=True,tx=True)
		RESERVE=preRESERVE.split(';')
	for EACH in RESERVE:
		while EACH in ORG:ORG.remove(EACH)
	return ORG
	
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
	
def fitToSelectedUVcore(UVS=[]):
	RET=[]
	#move
	for EACH in UVS:
		UVC=ditectConnectedUV(EACH)
		UVIsland=listUVIsland(EACH)
		for EACHB in UVS:#remove selectedUV
			while EACHB in UVC:UVC.remove(EACHB)
		for EACHC in UVIsland:#considerUVislands
			while EACHC in UVC:UVC.remove(EACHC)
		
		#preserveUV
		UVC=preservedList(UVC)
		
		print UVC
		if UVC:
			UVPOS=cmds.polyEditUV(EACH,q=True,r=False)
			cmds.polyEditUV(UVC,u=UVPOS[0],v=UVPOS[1],r=False)
		RET.append(EACH)
		
		for EACHUVC in UVC:
			RET.append(EACHUVC)
	return RET
	
def unfoldExceptUVIsland(UV=[]):
	UVIsland=listUVIsland(UV)
	for EACHB in UV:#remove selectedUV
		while EACHB in UVIsland:UVIsland.remove(EACHB)
	cmds.select(UVIsland,r=True)
	mel.eval('unfold -i 5000 -ss 0.001 -gb 0 -gmb 1 -pub 0 -ps  0 -oa  0 -us off;')
	
	
	
def unfold(UVS=[]):
	if not UVS:
		UVS=cmds.polyListComponentConversion(tuv=True)
	UVS=preservedList(UVS)
	cmds.select(UVS,r=True)
	mel.eval('unfold -i 5000 -ss 0.001 -gb 0 -gmb 1 -pub 0 -ps  0 -oa  0 -us off;')
	
	
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
	print UVS
	AllUV=fitToSelectedUVcore(UVS)
	unfoldExceptUVIsland(AllUV)
	
	
	#saw(BORDER)
	
	#NonEffectUVList
	for EACH in AllUV:
		while EACH in NOFUV:NOFUV.remove(EACH)
	if NOFUV:
		cmds.select(NOFUV,r=True)
	
	return AllUV
	
	

def saw(COMP):
	EDGES=cmds.polyListComponentConversion(COMP,te=True)
	for EACH in EDGES:
		cmds.polyMapSewMove(EACH,nf=10,lps=0,ch=0)
	
#####UI
	
def createPreserveList():
	preUVS=cmds.polyListComponentConversion(tuv=True)
	UVS=cmds.filterExpand(preUVS,sm=35,ex=True)
	cmds.textFieldGrp('MS_preserveUV_preserveList',e=True,tx=';'.join(UVS))
	
def addPreserveList():
	TX=cmds.textFieldButtonGrp('MS_preserveUV_preserveList',q=True,tx=True)
	if TX:
		LIST=TX.split(';')
	else:
		LIST=[]
	preUVS=cmds.polyListComponentConversion(tuv=True)
	UVS=cmds.filterExpand(preUVS,sm=35,ex=True)
	
	RET=list(set(LIST+UVS))
	cmds.textFieldButtonGrp('MS_preserveUV_preserveList',e=True,tx=';'.join(RET))
	
def removePreserveList():
	TX=cmds.textFieldButtonGrp('MS_preserveUV_preserveList',q=True,tx=True)
	LIST=TX.split(';')
	preUVS=cmds.polyListComponentConversion(tuv=True)
	UVS=cmds.filterExpand(preUVS,sm=35,ex=True)
	
	for EACH in UVS:
		while EACH in LIST:LIST.remove(EACH)
	
	cmds.textFieldButtonGrp('MS_preserveUV_preserveList',e=True,tx=';'.join(LIST))
	
def clearPreserveList():
	cmds.textFieldButtonGrp('MS_preserveUV_preserveList',e=True,tx='')
	









def layoutA(
	LABEL='MS_preserveUV'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	#LockList
	cmds.textFieldButtonGrp('MS_preserveUV_preserveList',bc=lambda *args:createPreserveList())
	cmds.rowLayout(nc=4)
	cmds.button(w=40,l=u'create',c=lambda *args:createPreserveList())
	cmds.button(w=40,l=u'add',c=lambda *args:addPreserveList())
	cmds.button(w=40,l=u'remove',c=lambda *args:removePreserveList())
	cmds.button(w=40,l=u'clear',c=lambda *args:clearPreserveList())
	cmds.setParent('..')
	#button
	cmds.button(w=WIDTH-4,l=u'fitToSelectedUV',c=lambda *args:fitToSelectedUV())
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_preserveUV_main_window',q=True,ex=True):
		cmds.deleteUI('MS_preserveUV_main_window')
	cmds.window('MS_preserveUV_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_preserveUV_main_window')
	




