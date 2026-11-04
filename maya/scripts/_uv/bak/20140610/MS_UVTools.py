# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_uv.py
# 説明
#			
#			
# 作成日
#			
########################################
import os
import maya.cmds as cmds

base = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')
################
#UVパネル
################

def MS_UVfitter(trn_u=0.0,trn_v=0.0,scl_u=1.0,scl_v=1.0):
	perspectiveAspectRatio=cmds.checkBox('perspectiveAspectRatio',q=True,v=True)
	sel=cmds.ls(sl=True)
	if len(sel):
		uvs=cmds.polyListComponentConversion(tuv=True)
		if uvs:
			cmds.polyNormalizeUV(uvs,normalizeType=1,preserveAspectRatio=perspectiveAspectRatio)
		else:
			return
		PEUV(u=trn_u,v=trn_v,su=scl_u,sv=scl_v)

def MS_UVpanels(ref_u=4,ref_v=4,blank=1.0):
	if cmds.columnLayout('layoutUVPanel',q=True,ex=True):
		cmds.deleteUI('layoutUVPanel')

	cmds.columnLayout('layoutUVPanel',p='main_layout_b',adj=True)
	
	#ButtonSize
	bsize_u=(256/ref_u)
	bsize_v=(256/ref_v)
	
	cmds.gridLayout(nc=ref_u,cellWidthHeight=(bsize_u,bsize_v))

	i=0
	j=0
	for i in range(0,ref_v):
		for j in range(0,ref_u):
			scl_u=(1.0/ref_u)
			scl_v=(1.0/ref_v)
			
			trn_u=((1.0/ref_u*j)-0.5+0.5/ref_u)
			trn_v=(-(1.0/ref_v*i)+0.5-0.5/ref_v)
			
			angl=0
			
			#create commands
			button_name=(str(i)+"_"+str(j))
			cmds.button(l=button_name,c=cvCommands(trn_u,trn_v,scl_u,scl_v))
			
	cmds.setParent('..')
	cmds.setParent('..')
	#--DataPart--//
	
############
#UV操作コアユーティリティ
############

def PEUV(u=0.0,v=0.0,ro=0.0,su=1.0,sv=1.0,pu=0.5,pv=0.5,angle=0.0):

	uvs=cmds.polyListComponentConversion(tuv=True)
	npu,npv = ditectUVCenter(uvs,pug=pu,pvg=pv)

	cmds.polyEditUV(uvs
		,r=True
		,uValue=u
		,vValue=v
		,rotation=ro
		,pivotU=npu
		,pivotV=npv
		,scale=True
		,scaleU=su
		,scaleV=sv
		,angle=angle
		)

def ditectUVCenter(uvs=[],pug=0.5,pvg=0.5):
	def averageArr(arr=[]):
		var=0
		for i in arr:var+=i
		return var/len(arr)

	uvCoords = cmds.polyEditUV(uvs,q=True)
	u=uvCoords[0::2]
	v=uvCoords[1::2]
	#
	if pug==0.5:
		retU = averageArr(u)
	elif pug>0.5:
		retU = max(u)
	else:
		retU = min(u)
	#
	if pvg==0.5:
		retV = averageArr(v)
	elif pvg>0.5:
		retV = max(v)
	else:
		retV = min(v)
	print pug,pvg,retU,retV
	return retU,retV


#############
#UI用中間コマンド
#############
def cvCommands(trn_u,trn_v,scl_u,scl_v,*args):
	def Ret(args):
		MS_UVfitter(trn_u,trn_v,scl_u,scl_v)
	return Ret

def ccUVpanels():
	ref_u=cmds.intSliderGrp('panel_U',q=True,v=True)
	ref_v=cmds.intSliderGrp('panel_V',q=True,v=True)
	blank=1.0
	MS_UVpanels(ref_u,ref_v,blank)

def ccPanelU(ref_u,*args):
	def ret(args):
		cmds.intSliderGrp('panel_U',e=True,v=ref_u)
		ccUVpanels()
	return ret

def ccPanelV(ref_v,*args):
	def ret(args):
		cmds.intSliderGrp('panel_V',e=True,v=ref_v)
		ccUVpanels()
	return ret

#Move
def ccMove(u=0.0,v=0.0,*args):
	def Ret():
		mVar=cmds.floatSliderGrp('moveValue',q=True,v=True)
		mods = cmds.getModifiers()
		exVar=1
		if (mods & 1) > 0:#Shift=ToggleU
			exVar=2
		if (mods & 4) > 0:#dec
			exVar=0.5
		if (mods & 8) > 0:#Alt=ToggleV
			exVar=0.25

		PEUV(u=u*mVar*exVar,v=v*mVar*exVar)
	return Ret

def ccRotate(ro=0.0,pu=0.5,pv=0.5,angle=0.0,*args):
	def Ret():
		rVar=cmds.floatSliderGrp('rotateValue',q=True,v=True)
		mods = cmds.getModifiers()
		exVar=1
		if (mods & 1) > 0:#Shift=ToggleU
			exVar=2
		if (mods & 4) > 0:#dec
			exVar=0.5
		if (mods & 8) > 0:#Alt=ToggleV
			exVar=0.25

		PEUV(ro=ro,pu=pu,pv=pv,angle=angle*rVar*exVar)
	return Ret

def ccScale(su=1.0,sv=1.0,pu=0.5,pv=0.5,*args):
	def Ret():
		sVar=cmds.floatSliderGrp('scaleValue',q=True,v=True)
		nsu=sVar
		nsv=sVar
		mods = cmds.getModifiers()
		if (mods & 1) > 0:#Shift=ToggleU
			nsu=1
		if (mods & 8) > 0:#Alt=ToggleV
			nsv=1

		if (mods & 4) > 0:#dec
			PEUV(su=nsu**-1,sv=nsv**-1,pu=pu,pv=pv)
		else:
			PEUV(su=nsu,sv=nsv,pu=pu,pv=pv)

	return Ret

#############
#UI
#############

def layoutUVPanel():
	cmds.columnLayout(adj=True)
	cmds.text(l='UVPanel',al='left',bgc=[0.4,0.4,0.4],font='boldLabelFont')
	#U
	cmds.separator(w=200,st="single")
	cmds.intSliderGrp('panel_U',cw3=[50,30,100],adj=3,l="panel_U",field=True,min=1,max=16,v=4,cc=lambda *args:ccUVpanels())
	cmds.rowLayout(numberOfColumns=4
		,columnWidth4=[40,40,40,40]
		,columnAlign=[1,"center"]
		,columnAttach4=["both","both","both","both"]
		)
	cmds.button(l="U*2",c=ccPanelU(2))
	cmds.button(l="U*4",c=ccPanelU(4))
	cmds.button(l="U*8",c=ccPanelU(8))
	cmds.button(l="U*16",c=ccPanelU(16))
	cmds.setParent('..')
	#V
	cmds.intSliderGrp('panel_V',cw3=[50,30,100],adj=3,l="panel_V",field=True,min=1,max=16,v=4,cc=lambda *args:ccUVpanels())
	cmds.rowLayout(numberOfColumns=4
		,columnWidth4=[40,40,40,40]
		,columnAlign=[1,"center"]
		,columnAttach4=["both","both","both","both"]
		)
	cmds.button(l="V*2",c=ccPanelV(2))
	cmds.button(l="V*4",c=ccPanelV(4))
	cmds.button(l="V*8",c=ccPanelV(8))
	cmds.button(l="V*16",c=ccPanelV(16))
	cmds.setParent('..')
	
	#---------------
	#Execute Buttons
	#---------------

	cmds.separator(w=200,st="single")

	cmds.floatSliderGrp('blank',cw3=[50,30,100],adj=3,l="blank",field=True,precision=2,step=0.01,min=0.1,max=1.0,v=1.0)
	cmds.checkBox('perspectiveAspectRatio')
	cmds.setParent('..')

def LayoutA():
	cmds.columnLayout('MS_tools_mainLayout',adj=True)
	#Move
	cmds.text(l='Move',al='left',bgc=[0.4,0.4,0.4],font='boldLabelFont')
	cmds.separator(w=200,st="single")
	#
	cmds.rowLayout(nc=2)
	cmds.gridLayout(nc=3)
	moveArr=[-1,0.0,1]
	i=0
	for v in range(0,3):
		for u in range(0,3):
			iconPath=base+'/icons/move0%s.png'%i
			cmds.iconTextButton(image=iconPath,c=ccMove(u=moveArr[u],v=-moveArr[v]))
			i+=1
	cmds.setParent('..')
	cmds.columnLayout(cat=['left',20])
	cmds.text(l='+[Shift] = x2')
	cmds.text(l='+[Ctrl]  = x0.5')
	cmds.text(l='+[Alt]   = x0.25')
	cmds.setParent('..')


	cmds.setParent('..')
	#
	cmds.floatSliderGrp('moveValue',cw3=[50,30,100],adj=3,pre=3,l="moveValue",field=True,min=0,max=1,v=0.25)

	cmds.separator(w=200,st="single")

	#Rotate
	cmds.text(l='Rotate',al='left',bgc=[0.4,0.4,0.4],font='boldLabelFont')
	cmds.separator(w=200,st="single")
	#
	cmds.rowLayout(nc=2)
	cmds.gridLayout(nc=3,cellWidthHeight=(32,32))
	rotArr=[1.0,-1.0]
	i=0
	for ro in range(0,2):
		iconPath=base+'/icons/rotate0%s.png'%i
		cmds.iconTextButton(image=iconPath,c=ccRotate(ro=0.0,pu=0.5,pv=0.5,angle=rotArr[ro]))
		i+=1
	cmds.setParent('..')
	#
	cmds.columnLayout(cat=['left',20])
	cmds.text(l='+[Shift] = x2')
	cmds.text(l='+[Ctrl]  = x0.5')
	cmds.text(l='+[Alt]   = x0.25')
	cmds.setParent('..')
	#
	cmds.setParent('..')

	cmds.floatSliderGrp('rotateValue',cw3=[50,30,100],adj=3,l="rotateValue",field=True,min=0,max=360,v=45.0)

	cmds.separator(w=200,st="single")
	#Scale
	cmds.text(l='Scale',al='left',bgc=[0.4,0.4,0.4],font='boldLabelFont')
	cmds.separator(w=200,st="single")

	#
	cmds.rowLayout(nc=2)
	cmds.gridLayout(nc=3,cellWidthHeight=(32,32))
	scaleArr=[-1.0,0.0,1.0]
	pivotArr=[1.0,0.5,0.0]
	i=0
	for v in range(2,-1,-1):
		for u in range(0,3):
			iconPath=base+'/icons/scale0%s.png'%i
			cmds.iconTextButton(image=iconPath,c=ccScale(su=scaleArr[u],sv=scaleArr[v],pu=pivotArr[u],pv=pivotArr[v]))
			i+=1
	cmds.setParent('..')
	#
	cmds.columnLayout(cat=['left',20])
	cmds.text(l='+[Shift] = ToggleU')
	cmds.text(l='+[Ctrl]  = decrease')
	cmds.text(l='+[Alt]   = ToggleV')
	cmds.setParent('..')
	#
	cmds.setParent('..')
	#
	cmds.floatSliderGrp('scaleValue',cw3=[50,30,100],adj=3,l="scaleValue",field=True,min=1.0,max=4.0,v=2.0)

	cmds.separator(w=200,st="single")
	#
	cmds.setParent('..')
	
def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)

	#コントロールレイアウト用
	cmds.columnLayout('main_layout_a',adj=True)
	LayoutA()
	layoutUVPanel()
	cmds.setParent('..')

	#可変レイアウト用
	cmds.columnLayout('main_layout_b',adj=True)
	cmds.setParent('..')
	#

	cmds.showWindow('MS_tools_window')

	ccUVpanels()
	
UI()