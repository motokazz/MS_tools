# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_G2lightUtil.py
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds

#execCheckList
import s2000_tools.MS_lib.MSG2_execCheck as MSG2_execCheck
reload(MSG2_execCheck)


def previewDirectionalLights(HIDE=False):
	
	if cmds.objExists('|preview_lights'):
		cmds.delete('|preview_lights')

	MSG2_execCheck.execCheckSafe('MS_G2lightUtil')#execCheckList

	intensity=4
	ngp=cmds.group(n='preview_lights',empty=True)
	dirgp=cmds.group(n='directional',empty=True)
	ambgp=cmds.group(n='ambient',empty=True)

	#DirectionalLight
	node=cmds.createNode('G2DirectionalLight')
	cmds.setAttr(node+'.lightIntensity',intensity)
	trn = cmds.listRelatives(node,p=True)
	cmds.xform(trn,ro=(-60,30,0),ws=True)
	cmds.parent(trn,dirgp)

	#AmbientLight
	node=cmds.createNode('G2AmbientLight')
	cmds.setAttr(node+'.lightIntensity',intensity*0.5)
	trn = cmds.listRelatives(node,p=True)
	cmds.xform(trn,ro=(-60,30,0),ws=True)
	cmds.setAttr(node+'.skyColorR',0.5)
	cmds.setAttr(node+'.skyColorG',0.5)
	cmds.setAttr(node+'.skyColorB',0.5)
	cmds.setAttr(node+'.backColorR',0.3)
	cmds.setAttr(node+'.backColorG',0.3)
	cmds.setAttr(node+'.backColorB',0.3)
	
	cmds.parent(trn,ambgp)
	cmds.parent(dirgp,ngp)
	cmds.parent(ambgp,ngp)
		
	cmds.xform(ngp,t=(0,20000,0),ws=True)
	if HIDE:
		cmds.hide('|preview_lights')

def previewLights():
	size=3000
	intensity=2
	trArray=[[0,size,0,intensity*2],[size,0,size,intensity*1],[size,0,-size,intensity*1],[-size,0,size,intensity*0.5],[-size,0,-size,intensity*0.5],[0,-size,0,intensity*0.5]]
	ngp=cmds.group(n='preview_lights',empty=True)

	for each in trArray:
		node=cmds.createNode('G2PointLight')
		
		cmds.setAttr(node+'.lightIntensity',each[3])
		cmds.setAttr(node+'.innerRadius',4500)
		cmds.setAttr(node+'.outerRadius',5000)
		
		trn = cmds.listRelatives(node,p=True)
		
		cmds.xform(trn,t=(each[0],each[1],each[2]),ws=True)
		
		cmds.parent(trn,ngp)
		
	cmds.xform(ngp,t=(0,2000,0),ws=True)
		


def LayoutA():
	cmds.columnLayout('MS_G2lightUtil_mainLayout',adj=True)
	cmds.text(l='MS_G2lightUtil',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='preview_DirectionalLight',h=50,c=lambda *args:previewDirectionalLights())
	#cmds.button(l='preview_light',c=lambda *args:previewLights())
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	