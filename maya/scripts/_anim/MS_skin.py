# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_skin
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds

import maya.mel as mel

import _lib.MS_distance as MS_distance

import MS_primitives.MS_getBestBB as MS_getBestBB

def transformAnimToSkinAnim():
	autokey=cmds.autoKeyframe(q=True,st=True)
	cmds.autoKeyframe(st=0)
	cmds.currentTime( 1)

	obj = cmds.ls(sl=True)
	for each in obj:
		cmds.select (cl=True)
		jnt =cmds.joint()
		PARENT = cmds.listRelatives(each , f = True , p=True )
		dup = cmds.duplicate(each)
		
		cmds.parent(dup[0] , w=True)
		
		cmds.setAttr ( dup[0]+".tx" , 0 )
		cmds.setAttr ( dup[0]+".ty" , 0 )
		cmds.setAttr ( dup[0]+".tz" , 0 )
		cmds.setAttr ( dup[0]+".rx" , 0 )
		cmds.setAttr ( dup[0]+".ry" , 0 )
		cmds.setAttr ( dup[0]+".rz" , 0 )
		cmds.setAttr ( dup[0]+".sx" , 1 )
		cmds.setAttr ( dup[0]+".sy" , 1 )
		cmds.setAttr ( dup[0]+".sz" , 1 )
		cmds.setAttr ( dup[0]+".visibility" , 1 )
		
		
		cmds.select( dup[0] , r = True )
		cmds.select( jnt , add = True )

		SKINCLUSTER = cmds.skinCluster( jnt , dup[0])
		cmds.skinPercent(SKINCLUSTER , dup[0] , resetToDefault=True , transformValue = [ jnt , 1.0 ] , )
		
		if cmds.cutKey(each , t=':' ,f=':' , at =[ "tx" , "ty" , "tz" , "rx" , "ry" , "rz" , "sx" , "sy" , "sz" , "v" ]):
			cmds.pasteKey(jnt , connect=False , at = [ "tx" , "ty" , "tz" , "rx" , "ry" , "rz" , "sx" , "sy" , "sz" , "v" ])

		cmds.delete(each)

		cmds.parent(jnt,PARENT[0])
	
	cmds.autoKeyframe(st = autokey)

# 選択コンポーネントのボリュームの中心を返す
def volumeCenter(sel=[]):
	
	if not sel:
		sel=cmds.ls(sl=True)

	precomp = cmds.polyListComponentConversion(sel,tv=True)
	comp = cmds.filterExpand(precomp,sm=31,ex=True)

	x,y,z = 0,0,0
	
	for each in comp:
		trn=cmds.xform(each,q=True,t=True,ws=True)
		x+=trn[0]
		y+=trn[1]
		z+=trn[2]

	if len(comp) != 0:
		div = 1.0/len(comp)
	else:
		div = 1.0

	return [ x*div , y*div , z*div ]

# 選択コンポーネントに対しフルウェイトスキン
def skinFullWeight():
	
	sel = cmds.ls(sl=True,l=True)
	jnt = cmds.ls(type='joint',sl=True)
	if not jnt:
		vc = volumeCenter(sel)

		cmds.select(cl=True)

		jnt = cmds.joint()
		cmds.xform( jnt , t = vc , ws = True )

	vtx = cmds.polyListComponentConversion( sel , tv=True )
	SKINCLUSTER = cmds.skinCluster( jnt , vtx)
	cmds.skinPercent(SKINCLUSTER[0] , vtx , resetToDefault=True , transformValue = [ jnt , 1.0 ] )

# script job

THIS_SCRIPT='MS_skin'

def addList():
	JOINT=cmds.ls(sl=True,type='joint',l=True)
	'''
	if not JOINT:
		clearList()
		return
	'''

	AI=cmds.textScrollList('MS_skin_joint_list',q=True,ai=True)
		
	if not AI:
		AI=''
	if JOINT:
		clearList()
	
	for EACH in AI:
		if EACH in JOINT:
			cmds.textScrollList('MS_skin_joint_list',e=True,append=EACH)
	for EACH in JOINT:
		if not EACH in AI:
			cmds.textScrollList('MS_skin_joint_list',e=True,append=EACH)


def clearList():
	cmds.textScrollList('MS_skin_joint_list',e=True,ra=True)


def job():
	jobNum = cmds.scriptJob(e=["SelectionChanged",THIS_SCRIPT+".addList()"],parent='MS_skin_window',protected=True)
	
#

def selectedjointAndComponentToFullWeight():
	JOINT = cmds.textScrollList('MS_skin_joint_list',q=True,ai=True)

	# Detect Skin Cluster
	SEL = cmds.ls(hl=True)
	SHP = cmds.listRelatives(SEL,s=True,f=True)
	SKINCLUSTER = cmds.listConnections(SHP[0]+'.inMesh',type='skinCluster')
	

	COMP = cmds.polyListComponentConversion(tv=True)
	cmds.skinPercent(SKINCLUSTER[0] , COMP , transformValue = [ JOINT[0] , 1.0 ] ,nrm=True)


def selectedComponentsFullWeightToNearestJoint():
	
	# Detect Skin Cluster
	SEL = cmds.ls(hl=True)
	SHP = cmds.listRelatives(SEL,s=True,f=True)
	SKINCLUSTER = cmds.listConnections(SHP[0]+'.inMesh',type='skinCluster')

	COMP = cmds.polyListComponentConversion(tv=True)

	BBC = MS_getBestBB.bbCenter(COMP)

	LOC = cmds.spaceLocator()

	cmds.xform(LOC,t=BBC,ws=True)

	JOINTS = cmds.ls(type='joint',dag=True,l=True)

	NEAREST = MS_distance.nearestOne(LOC[0],JOINTS)

	cmds.delete(LOC)
	
	
	cmds.skinPercent(SKINCLUSTER[0] , COMP , transformValue = [ NEAREST , 1.0 ] ,nrm=True)


def createJoint():
	sel = cmds.ls(sl=True,l=True)

	vc = volumeCenter(sel)

	cmds.select(cl=True)

	jnt = cmds.joint()
	cmds.xform( jnt , t = vc , ws = True )

	return jnt

def shellList():
	RET = []
	precomp = cmds.polyListComponentConversion(tv=True)
	comp = cmds.filterExpand(precomp,sm=31,ex=True)

	for each in range(10000):
		if not comp:
			break
		cmds.select(comp[0],r=True)
		cmds.polySelectConstraint(type=0x0001,m=2,sh=True)
		cmds.polySelectConstraint(dis=True)
		FC = cmds.filterExpand(sm=31,ex=True)
		comp = list(set(comp)-set(FC))
		RET.append(FC)
	return RET

def createJointShellBinded():
	sel = cmds.ls(sl=True,l=True)
	jnts=[]
	SL=shellList()
	for each in SL:
		cmds.select(each,r=True)
		jnts.append( createJoint() )


	SKINCLUSTER = cmds.skinCluster( jnts , sel)
	i=0
	for each in SL:
		cmds.skinPercent(SKINCLUSTER[0] , each , normalize=True , zeroRemainingInfluences = True ,transformValue = [ jnts[i] , 1.0 ] )
		i+=1


def LayoutUtil():
	cmds.frameLayout('MS_skin_utilLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='util',cll=True,cl=False)

	cmds.flowLayout('MS_skin_utilLayout',wrap=True)
	cmds.iconTextButton(i='smoothSkin.png',c=lambda *args:mel.eval('SmoothBindSkin'),ann='smoothSkin')
	cmds.iconTextButton(i='interactiveBindTool.png',c=lambda *args:mel.eval('InteractiveBindSkin'),ann='InteractiveBindSkin')
	cmds.iconTextButton(i='detachSkin.png',c=lambda *args:mel.eval('DetachSkin'),ann='DetachSkin')
	cmds.iconTextButton(i='goToBindPose.png',c=lambda *args:mel.eval('GoToBindPose'),ann='GoToBindPose')
	cmds.iconTextButton(i='paintSkinWeights.png',c=lambda *args:mel.eval('ArtPaintSkinWeightsTool'),ann='ArtPaintSkinWeightsTool')
	cmds.iconTextButton(i='mirrorSkinWeight.png',c=lambda *args:mel.eval('MirrorSkinWeights'),ann='MirrorSkinWeights')
	cmds.iconTextButton(i='copySkinWeight.png',c=lambda *args:mel.eval('CopySkinWeights'),ann='CopySkinWeights')
	cmds.iconTextButton(i='smoothSkinWeights.png',c=lambda *args:mel.eval('SmoothSkinWeights'),ann='SmoothSkinWeights')
	cmds.iconTextButton(i='menuIconSkinning.png',c=lambda *args:mel.eval('weightHammerVerts'),ann='weightHammerVerts')

	cmds.setParent('..')
	cmds.textScrollList('MS_skin_joint_list',h=100)
	cmds.button(l='selectedjointAndComponentToFullWeight',c=lambda *args:selectedjointAndComponentToFullWeight())
	cmds.button(l='selectedComponentsFullWeightToNearestJoint',c=lambda *args:selectedComponentsFullWeightToNearestJoint())

	cmds.setParent('..')



def LayoutA():
	cmds.frameLayout('MS_skin_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_skin',cll=True,cl=False)
	cmds.columnLayout('MS_skin_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_skin',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.button(l='createJoint',c=lambda *args:createJoint())
	cmds.button(l='createJointShellBinded',c=lambda *args:createJointShellBinded())
	cmds.button(l='skinFullWeight',c=lambda *args:skinFullWeight())
	cmds.button(l='shellList',c=lambda *args:shellList())

	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_skin_window',q=True,ex=True):
		cmds.deleteUI('MS_skin_window')
	cmds.window('MS_skin_window',rtf=True,s=True)
	

	LayoutA()
	
	LayoutUtil()

	cmds.showWindow('MS_skin_window')
	
	job()
	addList()
