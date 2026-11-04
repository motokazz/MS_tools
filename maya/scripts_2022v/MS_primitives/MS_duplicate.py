# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_getBestBB
# 説明
#			
# 作成日
#			
########################################


import maya.cmds as cmds
import maya.mel as mel

class MS_duplicate:
	def __init__(self,obj=[],face=[]):
		self.obj=obj
		self.face=face
	### コンポーネントをデュプリケイト ###
	def dupComp(self):
		
		#self.face = cmds.polyListComponentConversion(comp,tf=True)
		OBJ = self.face[0].split('.')[0]
		DUPED = cmds.duplicate(OBJ)
		ncomp=[]
		for i in self.face:
			a,b=i.split('.')
			ncomp.append(DUPED[0]+'.'+b)
		cmds.select(ncomp,r=True)
		temptrn=cmds.xform(ncomp,q=True,t=True,ws=True)
		mel.eval('InvertSelection;')
		cmds.delete()
		cmds.select(DUPED,r=True)
		if cmds.listRelatives(DUPED,p=True):
			DUPED=cmds.parent(DUPED,w=True)
		return DUPED
		
	def dupObj(self):
		#
		DUPED = cmds.duplicate(self.obj)
		return DUPED

	def auto(self):
		self.__init__()
		if not self.obj:
			self.obj=cmds.ls(sl=True,l=True)
		if not self.face:
			comp = cmds.filterExpand(sm=[31,32,34,70])
			self.face = cmds.polyListComponentConversion(comp,tf=True)

		if self.face:
			self.dupComp()
		elif self.obj:
			self.dupObj()
		else:
			return


def layoutA(
	LABEL='MS_duplicate'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	dup=MS_duplicate()

	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	cmds.button(l='MS_duplicate',w=200,bgc=[0.7,0.8,0.6],c=lambda *args:dup.auto())
	cmds.setParent('..')
	cmds.setParent('..')







