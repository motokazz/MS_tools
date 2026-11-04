# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_reduce.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel

def trianglate():
	OBJ=cmds.ls(sl=True)
	cmds.polyTriangulate(ch=0)
	cmds.select(OBJ,r=True)

def MS_quad():

	OBJ=cmds.ls(sl=True)
	cmds.polyTriangulate(ch=0)
	cmds.polyQuad(
		a=cmds.floatField('MS_reduce_quad_angle',q=True,v=True)
		,kgb=cmds.checkBox('MS_reduce_quad_keepFaceGroupBorder',q=True,v=False)
		,ktb=cmds.checkBox('MS_reduce_quad_keepHardEdges',q=True,v=False)
		,khe=cmds.checkBox('MS_reduce_quad_keepTextureBorder',q=True,v=False)
		,ws=cmds.checkBox('MS_reduce_quad_worldSpaceCoordinates',q=True,v=False)
		)
	cmds.select(OBJ,r=True)


def deleteFlatVertex(ANGLE_MIN=170,ANGLE_MAX=360):
	cmds.polySelectConstraint(t=0x0001,m=3,a=True,ab=[ANGLE_MIN,ANGLE_MAX])
	cmds.polySelectConstraint(dis=True)
	cmds.delete()

def cleanAndOptimize(OBJ):
	#Cleanup
	cmds.select(OBJ,r=True)
	mel.eval('polyCleanupArgList 4 { "0","1","1","0","0","0","0","0","1","0.001","1","0.001","0","0.001","0","1","1","1" };')
	#mergeOverlapedEdges
	EDG=cmds.polyListComponentConversion(OBJ,te=True)
	if EDG:
		cmds.polySewEdge(EDG)



def main():

	REDUCE_ANGLE=cmds.floatField('MS_reduce_angle',q=True,v=True)
	CHECK_TRIANGULATE=cmds.checkBox('MS_reduce_check_triangulate',q=True,v=True)
	REP=cmds.intField('MS_reduce_detail',q=True,v=True)
	DFV_MIN=cmds.floatField('MS_reduce_deleteFlatVertex_min',q=True,v=True)
	DFV_MAX=cmds.floatField('MS_reduce_deleteFlatVertex_max',q=True,v=True)

	def reduce_core(SEL=[]):
		cmds.polySoftEdge(SEL,a=(REDUCE_ANGLE/REP)*(i+1),ch=False)
		
		EDG = cmds.polyListComponentConversion(SEL,te=True)
		cmds.select(EDG,r=True)
		cmds.polySelectConstraint(m=2,t=0x8000,sm=2)
		EDG=cmds.filterExpand(sm=32,ex=True)
		cmds.polySelectConstraint(dis=True)
		if not EDG:
			return
		cmds.delete(EDG)


		#フラット頂点削除
		cmds.select(SEL,r=True)
		deleteFlatVertex()
		#
		cmds.select(SEL,r=True)
		
		MS_quad()

		if CHECK_TRIANGULATE:
			cmds.polyTriangulate(SEL,ch=False)

	COMP=cmds.ls(sl=True,type='float3')
	if COMP:
		cmds.delete(COMP[0].split('.')[0],ch=True)
		for i in range(REP):
			reduce_core(COMP)	
	else:
		OBJ=cmds.ls(sl=True,type='transform')
		cmds.delete(OBJ,ch=True)
		for each in OBJ:
			for i in range(REP):
				#cleanAndOptimize(each)
				reduce_core(each)
				#頂点削除後のクリーンナップとオプティマイズ
				#cleanAndOptimize(each)

		cmds.select(OBJ,r=True)


#################
# UI
#################	


def layoutQuad():
	cmds.frameLayout('MS_reduce_quad_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_reduce',cll=True,cl=False)
	cmds.columnLayout('MS_reduce_quad_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='Quad and Triangulate',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	#
	cmds.gridLayout(nc=2,cw=80,ch=20)
	cmds.button(l='MS_quad',c=lambda *args:MS_quad())
	cmds.button(l='trianglate',c=lambda *args:trianglate())
	cmds.setParent('..')

	cmds.text(l='reduceAngle')
	cmds.floatField('MS_reduce_quad_angle',v=50)

	cmds.checkBox('MS_reduce_quad_keepFaceGroupBorder',l='keepFaceGroupBorder',v=False)
	cmds.checkBox('MS_reduce_quad_keepHardEdges',l='keepHardEdges',v=False)
	cmds.checkBox('MS_reduce_quad_keepTextureBorder',l='keepTextureBorder',v=False)
	cmds.checkBox('MS_reduce_quad_worldSpaceCoordinates',l='worldSpaceCoordinates',v=False)

	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')


def LayoutA():
	cmds.columnLayout('MS_reduce.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_reduce.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.gridLayout(nc=2,cw=80,ch=20)
	cmds.text(l='angle')
	cmds.floatField('MS_reduce_angle',w=100,v=5.0,pre=1)
	cmds.setParent('..')

	cmds.gridLayout(nc=2,cw=40,ch=20)
	cmds.text(l='detail')
	cmds.intField('MS_reduce_detail',v=5)
	cmds.setParent('..')

	cmds.checkBox('MS_reduce_check_triangulate',v=False)
	#
	cmds.separator(h=10)
	#
	cmds.text(l='deleteFlatVertex')
	cmds.gridLayout(nc=4,cw=40,ch=20)
	cmds.text(l='min')
	cmds.floatField('MS_reduce_deleteFlatVertex_min',v=170.0,pre=1)
	cmds.text(l='max')
	cmds.floatField('MS_reduce_deleteFlatVertex_max',v=360.0,pre=1)
	cmds.setParent('..')

	cmds.button(l='reduce',c=lambda *args:main())

	#
	cmds.separator(h=10)

	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_reduce_window',q=True,ex=True):
		cmds.deleteUI('MS_reduce_window')
	cmds.window('MS_reduce_window',rtf=True,s=True)
	
	LayoutA()
	layoutQuad()

	cmds.showWindow('MS_reduce_window')
	

