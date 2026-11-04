# -*- coding:utf-8 -*-
import sys
import maya.cmds as cmds
from math import sqrt

class MS_distanceValue():
	#
	def __init__(self,baseObj,distObjs):
		self.baseObj=baseObj
		self.distObjs=distObjs

	def sorted(self):
		#return:[objname,distance,distanceValue]
		#ditect distance
		baseLoc=cmds.xform(self.baseObj,q=True,ws=True,t=True)
		distances=[]
		for each in self.distObjs:
			distObjLoc=cmds.xform(each,q=True,ws=True,t=True)
			tempRange=sqrt((baseLoc[0]-distObjLoc[0])*(baseLoc[0]-distObjLoc[0])+(baseLoc[1]-distObjLoc[1])*(baseLoc[1]-distObjLoc[1])+(baseLoc[2]-distObjLoc[2])*(baseLoc[2]-distObjLoc[2]))
			distances.append([each,tempRange])
		#sort at distance
		distances.sort(cmp=lambda x,y:cmp(x[1],y[1]))
		varMin=distances[0][1]
		varMax=distances[-1][1]
		distancesVar=[]
		for var in distances:
			varTemp=1-(var[1]-varMin)/(varMax-varMin)
			distancesVar.append([var[0],var[1],varTemp])
		return distancesVar
		

def MS_nearestObjectV2_distance(target_a,target_b):
	a=cmds.xform(target_a,q=True,ws=True,t=True) 
	b=cmds.xform(target_b,q=True,ws=True,t=True) 
	#2点間の移動距離を計算
	dist = sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])+(a[2]-b[2])*(a[2]-b[2]))
	
	return dist
	


def MS_nearestObjectV2(sourceObj,distObj):
	#string sourceObj[]=ls -typ transform
	#entryObj=sourceObj.remove(distObj)
	dists=[]

	for each in sourceObj:
		ftemp=MS_nearestObjectV2_distance(distObj,each)
		dists.append([ftemp,each])
	
	#dists.sort(cmp=lambda x,y:cmp(x[1],y[1]))
	dists.sort()
	
	final=[]
	for each in dists:
		final.append(each[1])
	
	return final


'''
global proc MS_Progress():
	#プログレスウィンドウ
	if((window -ex MS_ProgressWindow) == true)deleteUI MS_ProgressWindow
	if(windowPref -ex MS_ProgressWindow): windowPref -r MS_ProgressWindow 
	window -wh 248 70 -tlc 414 516 -tlb true -s true -t 'Calculating' MS_ProgressWindow
	cmds.columnLayout()
	progressBar -maxValue 10 -width 246 MS_progress
	cmds.setParent ('..')
	showWindow MS_ProgressWindow


'''
def MS_groupVcolor_selectFilter():
	#より分け選択
	objz=cmds.ls(typ='mesh',sl=True)
	if len(objz)==0:
		objz=cmds.filterExpand(sm=(12,31,32,34)) 
	return objz

def MS_groupVcolor():
	effectiveRGB=cmds.checkBox('effectiveRGB',q=True,v=True)
	effectiveAlpha=cmds.checkBox('effectiveAlpha',q=True,v=True)
	considerNearest=cmds.checkBox('considerNearest',q=True,v=True)
	
	startRGB=cmds.colorSliderGrp('startRGB',q=True,rgb=True)
	startAlpha=cmds.colorSliderGrp('startAlpha',q=True,rgb=True)
	
	endRGB=cmds.colorSliderGrp('endRGB',q=True,rgb=True)
	endAlpha=cmds.colorSliderGrp('endAlpha',q=True,rgb=True)
	
	interpMode=cmds.radioCollection('interpMode',q=True,sl=True)
	obj=MS_groupVcolor_selectFilter()
	target=cmds.textFieldGrp('objName',q=True,tx=True) 
	distValues=MS_distanceValue(baseObj=target,distObjs=obj)
	#プログレスバー
	#MS_Progress
	#progressBar -edit -beginProgress -isInterruptable true -maxValue (len(obj)) MS_progress

	#頂点カラー割付
	if considerNearest and len(obj)>1 and target!='':
		#string target=MS_componentLastSelected#undo履歴から1オブジェクト取得
		for eachobj in distValues.sorted():
			if interpMode=='sqrt':
				DistanceValue=sqrt(eachobj[2])
			elif interpMode=='pow':
				DistanceValue=eachobj[2]**2
			else:
				DistanceValue=eachobj[2]

			if(effectiveRGB):
				colR=(startRGB[0]*DistanceValue)+(endRGB[0]*(1-DistanceValue))
				colG=(startRGB[1]*DistanceValue)+(endRGB[1]*(1-DistanceValue))
				colB=(startRGB[2]*DistanceValue)+(endRGB[2]*(1-DistanceValue))
				cmds.polyColorPerVertex(eachobj[0],r=colR,g=colG,b=colB)
			if(effectiveAlpha):
				colA=(startAlpha[0]*DistanceValue)+(endAlpha[0]*(1-DistanceValue))
				cmds.polyColorPerVertex(eachobj[0],a=colA)
	else:
		i=0
		for eachobj in obj:
			colR=endRGB[0]+((len(obj)-i)*((startRGB[0]-endRGB[0])/len(obj)))
			colG=endRGB[1]+((len(obj)-i)*((startRGB[1]-endRGB[1])/len(obj)))
			colB=endRGB[2]+((len(obj)-i)*((startRGB[2]-endRGB[2])/len(obj)))
			colA=endAlpha[0]+((len(obj)-i)*((startAlpha[0]-endAlpha[0])/len(obj)))

			if(effectiveRGB):
				cmds.polyColorPerVertex(eachobj,r=colR,g=colG,b=colB)
			if(effectiveAlpha):
				cmds.polyColorPerVertex(eachobj,a=colA)
			i+=1

	#progressBar -edit -s 1 MS_progress#プログレス
	#deleteUI -window MS_ProgressWindow#プログレス


def MS_groupVcolorUI_takeObj():
	#オブジェクトをtextFieldGrpに取得
	obj=cmds.ls(l=True,sl=True)
	cmds.textFieldGrp('objName',e=True,tx=obj[0])

def MS_groupVcolorUI_takeVcol():
	#オブジェクトをtextFieldGrpに取得
	obj=cmds.ls(l=True,sl=True)
	VCOL = cmds.polyColorPerVertex(obj[0],q=True,r=True,g=True,b=True,a=True)

	cmds.colorSliderGrp('startRGB',e=True,rgb=VCOL[0:3])
	cmds.colorSliderGrp('startAlpha',e=True,rgb=(VCOL[3],VCOL[3],VCOL[3]))


def UI():
	if(cmds.window('MS_groupVcolor',exists=True)):
		cmds.deleteUI('MS_groupVcolor')
	cmds.window('MS_groupVcolor',t='MS_groupVcolor')
	cmds.columnLayout()
	cmds.text(w=200,al='left',fn='boldLabelFont',l='D1.select objects. 2.set colors. 3.go')
	cmds.setParent ('..')
	cmds.rowLayout (nc=2)
	
	#Column1_option
	cmds.columnLayout()
	#
	cmds.frameLayout(w=105,h=35,lv=0)
	cmds.columnLayout()
	cmds.checkBox ('effectiveRGB',v=1,l='effectiveRGB')
	cmds.checkBox ('effectiveAlpha',v=1,l='effectiveAlpha')
	cmds.setParent ('..')
	cmds.setParent ('..')
	#
	cmds.frameLayout(w=105,h=80,lv=0)
	cmds.columnLayout()
	cmds.checkBox('considerNearest',v=1,l='considerNearest')
	cmds.textFieldGrp('objName',w=99,en=0)
	cmds.button(bgc=(0.8,0.8,1.0),w=100,h=15,l='takeTarget',c=lambda *args:MS_groupVcolorUI_takeObj())
	cmds.button(bgc=(0.8,0.8,1.0),w=100,h=15,l='getVcolor',c=lambda *args:MS_groupVcolorUI_takeVcol())
	cmds.setParent ('..')
	cmds.setParent ('..')

	cmds.frameLayout(lv=0)
	cmds.rowLayout(nc=2)
	cmds.columnLayout()
	cmds.text('interpMode')
	cmds.setParent('..')
	cmds.columnLayout()
	cmds.radioCollection('interpMode')
	cmds.radioButton('linear', label='linear',sl=True)
	cmds.radioButton('pow', label='pow' )
	cmds.radioButton('sqrt', label='sqrt' )
	cmds.setParent('..')
	cmds.setParent('..')




	cmds.setParent ('..')
	
	cmds.setParent ('..')
	#Column2_Color
	cmds.columnLayout()
	#
	cmds.frameLayout(h=50,lv=0)
	cmds.columnLayout()
	cmds.colorSliderGrp('startRGB',cw3=(60,50,100),rgb=(1,1,1),l='startRGB')
	cmds.colorSliderGrp('startAlpha',cw3=(60,50,100),rgb=(1,1,1),l='startAlpha')
	cmds.setParent ('..')
	cmds.setParent ('..')
	#
	cmds.frameLayout(h=50,lv=0)
	cmds.columnLayout()		
	cmds.colorSliderGrp('endRGB',cw3=(60,50,100),rgb=(0,0,0),l='endRGB')
	cmds.colorSliderGrp('endAlpha',cw3=(60,50,100),rgb=(0,0,0),l='endAlpha')
	cmds.setParent ('..')
	cmds.setParent ('..')
	
	#
	cmds.frameLayout(w=210,h=30,lv=0)
	cmds.button( 'groupVcolor',bgc=(0.8,1.0,0.8),w=100,l='groupVcolor',c=lambda *args:MS_groupVcolor())
	cmds.setParent ('..')
	

	cmds.setParent ('..')


	cmds.setParent ('..')
	
	cmds.showWindow('MS_groupVcolor')

#MS_groupVcolorUI()





