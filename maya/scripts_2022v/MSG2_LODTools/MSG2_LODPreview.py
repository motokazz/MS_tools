# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_LODPreview.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel

def getLevel(NODE):
	SEL = cmds.ls(typ='transform')
	for each in SEL:
		if cmds.attributeQuery('LodLevelMax',n=each,ex=True):
			if cmds.getAttr(each+'.LodLevelMax')==LVLMAX:
				RET.append(each)
	return RET

def createLODNode(NODE,MAX,MIN):
	NODENAME='MSG2_LODPreview_%smax_%smin'%(MAX,MIN)

	if cmds.objExists(NODENAME):#あったら消す
		cmds.delete(NODENAME)

	MINTABLE=[0,-100,3000,5000,7500,10000,20000,50000,70000,99999]

	try:
		NODE=cmds.parent(NODE,w=True)
	except:
		pass
	cmds.select(NODE,r=True)
	mel.eval('LevelOfDetailGroup;')
	LODGP=cmds.ls(sl=True)
	cmds.setAttr(LODGP[0]+'.minMaxDistance',True)
	cmds.setAttr(LODGP[0]+'.maxDistance',MINTABLE[MAX+1])
	cmds.setAttr(LODGP[0]+'.minDistance',MINTABLE[MIN])
	cmds.rename(LODGP[0],NODENAME)
	return NODENAME

def getLodModels(MAX,MIN):
	RET=[]
	MESHES=cmds.ls('root',lf=True,dag=True,l=True,type='mesh')
	for each in MESHES:
		try:
			TR=cmds.listRelatives(each,p=True,f=True)
			if cmds.getAttr(TR[0]+'.LodLevelMax')==MAX and cmds.getAttr(TR[0]+'.LodLevelMin')==MIN:
				cmds.setAttr(TR[0]+'.visibility',True)
				if not TR[0] in RET:
					RET.append(TR[0])
		except:
			pass

	return RET

def main():
	TEMP=[]

	LODSETUP=[[2,1],[8,3],[4,1],[8,5],[6,1],[8,7]]
	for each in LODSETUP:
		#TGP=createLODNode(each[0],each[1])
		TEMP=getLodModels(each[0],each[1])
		
		if TEMP:
			DUPED=cmds.duplicate(TEMP)
		else:
			continue

		if len(TEMP)>1:
			UNITED = cmds.polyUnite(DUPED,ch=False)
		else:
			UNITED = DUPED
		#
		try:
			cmds.deleteAttr(UNITED+'.LodLevelMax')
			cmds.deleteAttr(UNITED+'.LodLevelMin')
		except:
			pass

		if TEMP:
			createLODNode(UNITED,each[0],each[1])

	cmds.setAttr('root.visibility',False)

	cmds.select(clear=True)



def LayoutA():
	cmds.columnLayout('MSG2_LODPreview.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_LODPreview.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	
