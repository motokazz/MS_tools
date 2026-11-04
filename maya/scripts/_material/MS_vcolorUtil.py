# -*- coding:utf-8 -*-
import maya.cmds as cmds

#execCheckList
#import MS_module.MS_execCheck
#reload(MS_module.MS_execCheck)
#MS_module.MS_execCheck.execCheckSafe('MS_vcolorUtil.py')

def MS_Progress():
	#プログレスウィンドウ
	if cmds.window('MS_ProgressWindow',ex=True):
		cmds.deleteUI('MS_ProgressWindow')
	if cmds.windowPref('MS_ProgressWindow',ex=True):
		cmds.windowPref('MS_ProgressWindow',r=True)
	cmds.window('MS_ProgressWindow',wh=[248,70],tlc=[414,516],tlb=True,s=True,t='Calculating')
	cmds.columnLayout()
	cmds.progressBar('MS_progress',maxValue=10,width=246)
	cmds.setParent ('..')
	cmds.showWindow ('MS_ProgressWindow')


def vcolorClamp(*args):
	FIRST_SELECTION=cmds.ls(sl=True)
	COMP=cmds.polyListComponentConversion(ff=True,fe=True,fuv=True,fvf=True,tv=True)
	if COMP:
		cmds.select(COMP,r=True)
	OBJ=cmds.filterExpand(sm=31)
	
	if OBJ:
		for EACH in OBJ:
			if cmds.polyColorPerVertex(EACH,q=True,r=True)[0]>1.0:
				cmds.polyColorPerVertex(EACH,rel=False,r=1.0)
			if cmds.polyColorPerVertex(EACH,q=True,g=True)[0]>1.0:
				cmds.polyColorPerVertex(EACH,rel=False,g=1.0)
			if cmds.polyColorPerVertex(EACH,q=True,b=True)[0]>1.0:
				cmds.polyColorPerVertex(EACH,rel=False,b=1.0)
					
			if cmds.polyColorPerVertex(EACH,q=True,r=True)[0]<0.0:
				cmds.polyColorPerVertex(EACH,rel=False,r=0.0)
			if cmds.polyColorPerVertex(EACH,q=True,g=True)[0]<0.0:
				cmds.polyColorPerVertex(EACH,rel=False,g=0.0)
			if cmds.polyColorPerVertex(EACH,q=True,b=True)[0]<0.0:
				cmds.polyColorPerVertex(EACH,rel=False,b=0.0)
	
	cmds.select(FIRST_SELECTION,r=True)
	
def vcolNormalize(*args):
	FIRST_SELECTION=cmds.ls(sl=True)
	COMP=cmds.polyListComponentConversion(ff=True,fe=True,fuv=True,fvf=True,tv=True)
	if COMP:
		cmds.select(COMP,r=True)
	OBJ=cmds.filterExpand(sm=31)
	#プログレスバー
	MS_Progress()
	cmds.progressBar('MS_progress',edit=True,beginProgress=True,isInterruptable=True,maxValue=len(OBJ))
	
	VTX_LIST=[]
	
	#頂点カラー割付
	
	if OBJ:
		for EACH in OBJ:
			VTX_LIST.append(cmds.polyColorPerVertex(EACH,q=True,rgb=True))
		MAXLIST=[]
		for EACH in VTX_LIST:
			MAXLIST+=EACH
		MAXLIST.sort()
		MINVAR=MAXLIST[0]
		MAXLIST.reverse()
		MAXVAR=1.0
		if MAXLIST[0]>0 and not MAXLIST[0]>1.0 or not MINVAR<0:
			print 'effective!'
			MAXVAR=1.0/(MAXLIST[0]-MINVAR)
		else:
			print 'not effective'
			return
		I=0
		for EACH in OBJ:
			cmds.progressBar('MS_progress',edit=True,s=1)#プログレス
			cmds.polyColorPerVertex(EACH,r=(VTX_LIST[I][0]-MINVAR)*MAXVAR,g=(VTX_LIST[I][1]-MINVAR)*MAXVAR,b=(VTX_LIST[I][2]-MINVAR)*MAXVAR)
			I+=1
	cmds.select(FIRST_SELECTION,r=True)
	
	cmds.deleteUI('MS_ProgressWindow')#プログレス

def vcolNoneToZero(*args):
	HL=cmds.ls(hl=True)[0]
	ACS=cmds.polyColorSet(HL,q=True,acs=True)
	VTX=cmds.filterExpand(sm=31)
	#プログレスバー
	MS_Progress()
	cmds.progressBar('MS_progress',edit=True,beginProgress=True,isInterruptable=True,maxValue=len(VTX)*len(ACS))
	for eachCS in ACS:
		cmds.polyColorSet(HL,ccs=True,cs=eachCS)
		for each in VTX:
			cmds.progressBar('MS_progress',edit=True,s=1)#プログレス
			R=cmds.polyColorPerVertex(each,q=True,r=True)
			if R[0]<0.0001:
				cmds.polyColorPerVertex(each,r=0)
			G=cmds.polyColorPerVertex(each,q=True,g=True)
			if G[0]<0.0001:
				cmds.polyColorPerVertex(each,g=0)
			B=cmds.polyColorPerVertex(each,q=True,b=True)
			if B[0]<0.0001:
				cmds.polyColorPerVertex(each,b=0)		
			A=cmds.polyColorPerVertex(each,q=True,a=True)
			if A[0]<0.0001:
				cmds.polyColorPerVertex(each,a=0)
	cmds.deleteUI('MS_ProgressWindow')#プログレス
				


def LayoutA():
	cmds.columnLayout()
	
	cmds.button(l='1以上,0以下を切り捨て',w=200,c=vcolorClamp)	
	cmds.button(l='0～１内に正規化',w=200,c=vcolNormalize)
	cmds.button(l='カラーデータが無い頂点に０を付加',w=200,c=vcolNoneToZero)

	cmds.setParent ('..')
	


def UI():
	if(cmds.window('MS_vcolorUtil',exists=True)):
		cmds.deleteUI('MS_vcolorUtil')
	cmds.window('MS_vcolorUtil',t='MS_vcolorUtil')
	cmds.columnLayout()
	
	LayoutA()
	
	cmds.setParent ('..')
	
	cmds.showWindow('MS_vcolorUtil')

#MS_windowSampleUI()





