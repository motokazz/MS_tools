# _*_coding:utf-8_*_
########################################
# ファイル名
#			G2BGSceneSetup.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import s2000_tools.MSG2_breakTools.MSG2_breakNodeUtil as MSG2_breakNodeUtil
reload(MSG2_breakNodeUtil)

def selectKind(KIND='root'):
	cmds.select('*|'+KIND,r=True)
	cmds.select('*|'+KIND+'|*',add=True)

def createKindLayer(KIND='root'):
	if not cmds.objExists(KIND+'_layer'):
		cmds.createDisplayLayer(name=KIND+'_layer',number=1,nr=True)

	selectKind(KIND)

	cmds.editDisplayLayerMembers(KIND+'_layer',cmds.ls(sl=True,l=True),nr=True)
	cmds.setAttr(KIND+'_layer.visibility',0)
	cmds.setAttr(KIND+'_layer.displayType',1)
	COLDICT={'root':0,'col':17}
	cmds.setAttr(KIND+'_layer.color',COLDICT[KIND])


def changeColType(TYPE=6):
	COL=cmds.ls(type='hkNodeShape',dag=True,sl=True,l=True)
	for each in COL:
		cmds.setAttr(each+'.shapeType',TYPE)
		if TYPE==1:
			cmds.setAttr(each+'.changeExtraRadius',1)
		elif TYPE==6:
			cmds.setAttr(each+'.changeExtraRadius',0)

def G2BGSceneSetup():
	NODES = cmds.ls(sl=True,l=True)
	createStructs()
	selectedNodeToStructs(NODES)

def createMeshCollisionFromSelected(NODES=[]):
	if NODES:
		cmds.select(cmds.ls(NODES,dag=True,type='mesh'),r=True)
	else:
		cmds.select(cmds.ls(sl=True,dag=True,type='mesh'),r=True)

	#選択からメッシュコリジョンを作成
	cmds.duplicate()
	DUPED=cmds.ls(sl=True,l=True)
	try:
		UNITED=cmds.polyUnite(ch=False)[0]
		for EACHDUPED in DUPED:
			if cmds.objExists(EACHDUPED):
				cmds.delete(EACHDUPED)
	except:
		UNITED=DUPED
	cmds.delete(UNITED,ch=True)

	#一回原点にだす
	try:
		UNITED=cmds.parent(UNITED,w=True)
	except:
		pass

	#Grouping
	if not cmds.objExists('|col'):
		cmds.group(empty=True,n='|col')
	else:
		COLOLD=cmds.listRelatives('|col',ad=True,typ='transform')
		cmds.delete(COLOLD)

	cmds.parent(UNITED,'|col')
	COL=cmds.ls(sl=True,l=True)[0]

	#freeze
	cmds.xform('|col',piv=[0,0,0],ws=True)
	cmds.makeIdentity('|col',a=True,t=True,r=True,s=True)
	
	cmds.xform(COL,piv=[0,0,0],ws=True)
	cmds.makeIdentity(COL,a=True,t=True,r=True,s=True)
	
	cmds.xform('|col',piv=[0,0,0],ws=True)

	#deletePolyColorSet
	try:
		cmds.polyColorSet(COL,d=True,allColorSets=True)
	except:
		pass
		
	#setLambert
	cmds.select(COL,r=True)
	cmds.hyperShade(a='lambert1')
	
	#ADD_HAVOK
	MSG2_breakNodeUtil.toHavok(COL,MASS=0,SHAPETYPE=6)
	return COL

def createStructs():
	if not cmds.objExists('|root'):
		cmds.group(em=True,n='root')

	if not cmds.objExists('|col'):
		cmds.group(em=True,n='col')

def selectedNodeToStructs(NODES=[]):
	
	if not NODES:
		return

	COL = createMeshCollisionFromSelected(NODES)[0]
	
	cmds.parent(NODES,'|root')

	#cmds.hide(['sdw','low','col','occ'])
	cmds.hide(['|col'])

#################
# UI
#################
def LayoutA():
	cmds.columnLayout('MS_createGravityScene_mainLayout',adj=True)
	#
	cmds.separator()
	cmds.text(l='MS_createGravityScene',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.separator()
	cmds.gridLayout(cw=150)
	cmds.button(l='G2BGSceneSetup',c=lambda *args:G2BGSceneSetup(),ann=u'選択オブジェクトからrootとcolを作成し、出力可能な状態にします')
	cmds.button(l='createMeshCollision\nFromSelected',c=lambda *args:createMeshCollisionFromSelected(),ann=u'選択オブジェクトをコリジョンにします')
	cmds.setParent('..')
	#
	cmds.separator()
	cmds.text(l='KindUtil',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.separator()
	cmds.gridLayout(nc=2,cw=150)
	cmds.button(l='selectRoot',c=lambda *args:selectKind('root'))
	cmds.button(l='selectCol',c=lambda *args:selectKind('col'))
	cmds.button(l='RootToLayer',c=lambda *args:createKindLayer('root'))
	cmds.button(l='ColToLayer',c=lambda *args:createKindLayer('col'))
	cmds.button(l='ColToHULL',c=lambda *args:changeColType(1))
	cmds.button(l='ColToMESH',c=lambda *args:changeColType(6))
	cmds.setParent('..')

	#cmds.button(l='selectedNodeToStructs',c=lambda *args:selectedNodeToStructs())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	