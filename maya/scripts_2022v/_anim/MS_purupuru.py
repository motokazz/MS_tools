# -*- coding: utf-8 -*-
# script created by pymel.melparse.mel2py from mel file:
# d:\ms_tools\ms_purupuru.mel

#from pymel.all import *
import maya.cmds as cmds

def MS_purupuru():
	OBJZ=cmds.ls(sl=1)
	ATTR=cmds.channelBox('mainChannelBox',q=1,sma=1)
	#string $ATTR=`MS_purupuru_getAttrNameFromChannelBox`;
	CURRENTTIME=float(cmds.currentTime(q=1))
	PURUPURU=float(cmds.floatSliderGrp("PURUPURU",
		q=1,v=1))
	STEP=float(cmds.intSliderGrp("STEP",
		q=1,v=1))
	RANGE=float(cmds.intSliderGrp("RANGE",
		q=1,v=1))
	i=0
	j=0
	for eachOBJ in OBJZ:
		for eachATTR in ATTR:
			i=0
			j=0
			VAR=[]
			for i in range(0,RANGE):
				VAR[i]=float(cmds.getAttr((str(eachOBJ) + "." + str(eachATTR)),
					t=(i * STEP + CURRENTTIME)))
				
			for eachVAR in VAR:
				if j == 0:
					cmds.setKeyframe(eachOBJ,
						at=eachATTR,t=CURRENTTIME,v=VAR[0])
				
				else:
					REVERSE=1
					if j % 2:
						REVERSE=-1
					cmds.setKeyframe(eachOBJ,
						at=eachATTR,t=(CURRENTTIME + j * STEP),v=(((PURUPURU / RANGE) * (RANGE - j) * REVERSE) + VAR[j]))
				j+=1
				
			
		
	
def MS_purupuru_getAttr():
	NEWVAR=MS_purupuru_getAttrNameFromChannelBox
	cmds.textFieldButtonGrp('attr_int',e=1,tx=NEWVAR)
	
def MS_purupuru_getAttrNameFromChannelBox():
	values=cmds.channelBox('mainChannelBox',q=1,sma=1)
	values2=cmds.channelBox('mainChannelBox',q=1,ssa=1)
	newValue=" ".join(values) + " " + " ".join(values2)
	print newValue
	return newValue

def UI():
	if cmds.window('MS_purupuruUI',exists=1):
		cmds.deleteUI('MS_purupuruUI')
		#Window Check
		
	cmds.window('MS_purupuruUI',title="MS_purupuruUI")
	#Create Window
	cmds.columnLayout()
	cmds.floatSliderGrp("PURUPURU",
		min=0.01,max=100,cw3=(100, 100, 100),f=1,l="PURUPURU",v=1)
	cmds.intSliderGrp("RANGE",
		min=1,max=100,cw3=(100, 100, 100),f=1,l="RANGE",v=10)
	cmds.intSliderGrp("STEP",
		min=1,max=100,cw3=(100, 100, 100),f=1,l="STEP",s=1,v=3)
	#float $PURUPURU=1;
	#float $STEP=2;
	#float $RANGE=10;
	cmds.button(c=MS_purupuru,l="purupuru")
	cmds.textFieldButtonGrp("attr_int",
		bl="getAttr",l="attr",bc=MS_purupuru_getAttr)
	cmds.showWindow('MS_purupuruUI')
