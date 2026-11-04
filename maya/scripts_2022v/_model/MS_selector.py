# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_selector
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds


def selectEdge(mode=0):

	
	result=[]
	OBJ = cmds.ls(hl=True,l=True)
	EDG=cmds.filterExpand(sm=32,ex=True)
	for each in EDG:
		temp=[]
		ID = each.split('[')[-1].split(']')[0]
		if ID+'L' in result:
			continue
		#
		if mode==0:		#EdgeLoop
			temp=cmds.polySelect(el=int(ID),add=True)
			STEP = cmds.intField('MS_selector_EdgeLoopStep',q=True,v=True)
		if mode==1:		#EdgeRing
			temp=cmds.polySelect(er=int(ID),add=True)
			STEP = cmds.intField('MS_selector_EdgeRingStep',q=True,v=True)
		#
		if not cmds.checkBox('MS_selector_Invert_selection',q=True,v=True):
			for each in temp[0::(STEP+1)]:
				name=OBJ[0]+'.e['+str(each)+']'
				result.append(name)
		else:
			for each in temp[0::(STEP+1)]:
				temp.remove(each)

			for each in temp:
				name=OBJ[0]+'.e['+str(each)+']'
				result.append(name)

	cmds.select(result,r=True)


def selectContiuousEdges():
	M2A =	 cmds.floatSliderGrp('MS_selector_Maximun_2D_angle',q=True,v=True)
	M3A =	 cmds.floatSliderGrp('MS_selector_Maximun_3D_angle',q=True,v=True)
	ED = cmds.intSliderGrp('MS_selector_Edges_either_side',q=True,v=True)

	EDGE=cmds.filterExpand(sm=32,ex=True)
	FACE=cmds.filterExpand(sm=34,ex=True)

	if EDGE:
		cmds.polySelectConstraint(
			type=0x8000
			,propagate=4
			,m2a =	 M2A
			,m3a =	 M3A
			,ed = ED
			)
	if FACE:
		cmds.polySelectConstraint(
			type=0x0008
			,m=2
			,anglePropagation=True
			,angleTolerance = M3A
			)
		#cmds.select(FACE,r=True)
		cmds.polySelectConstraint(dis=True)




def main():
	OBJ = cmds.ls(hl=True,l=True)
	EDG=cmds.filterExpand(sm=32,ex=True)
	for eee in EDG:
		ID = eee.split('[')[-1].split(']')[0]

		F = cmds.polyListComponentConversion(eee,tf=True)
		FE = cmds.polyInfo(F,fe=True)
		print FE
		for each in FE:
			print each
			NNN=each.split()
			INDEX = NNN.index(ID)
			if INDEX<4:
				INDEX+=2
			else:
				INDEX-=2
			NEDG = OBJ[0]+'.e['+str(NNN[INDEX])+']'
			print NEDG
			cmds.select(NEDG,tgl=True)
		

def LayoutA():
	cmds.frameLayout('MS_selector_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_selector',cll=True,cl=False)
	cmds.columnLayout('MS_selector_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_selector',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.button(l='do',c=lambda *args:main())

	cmds.rowLayout(nc=3)
	cmds.iconTextButton(image='polySelectEdgeLoop',l='selectEdgeLoop',c=lambda *args:selectEdge(0))
	cmds.text(l='EdgeLoopStep',w=100)
	cmds.intField('MS_selector_EdgeLoopStep',w=100,v=0)
	cmds.setParent('..')

	cmds.rowLayout(nc=3)
	cmds.iconTextButton(image='polySelectEdgeRing',l='selectEdgeLoop',c=lambda *args:selectEdge(1))
	cmds.text(l='EdgeRingStep',w=100)
	cmds.intField('MS_selector_EdgeRingStep',w=100,v=0)
	cmds.setParent('..')

	cmds.checkBox('MS_selector_Invert_selection',l='invert selection',v=False)

	cmds.separator()

	### select continuous edges ###
	def cc_MS_selector_Select_continuous_dges():
		cmds.floatSliderGrp('MS_selector_Maximun_2D_angle',e=True,en=cmds.checkBox('MS_selector_Select_continuous_dges',q=True,v=True))
		cmds.floatSliderGrp('MS_selector_Maximun_3D_angle',e=True,en=cmds.checkBox('MS_selector_Select_continuous_dges',q=True,v=True))
		cmds.intSliderGrp('MS_selector_Edges_either_side',e=True,en=cmds.checkBox('MS_selector_Select_continuous_dges',q=True,v=True))

	cmds.checkBox('MS_selector_Select_continuous_dges',l='enable Select_continuous_dges',v=False,cc= lambda *args:cc_MS_selector_Select_continuous_dges())

	cmds.floatSliderGrp('MS_selector_Maximun_2D_angle',l='Maximun_2D_angle',en=False,f=True,min=0,max=180,v=30)
	cmds.floatSliderGrp('MS_selector_Maximun_3D_angle',l='Maximun_3D_angle',en=False,f=True,min=0,max=180,v=60)
	cmds.intSliderGrp('MS_selector_Edges_either_side',l='Edges_either_side',en=False,f=True,min=0,max=50,fmx=1000000,v=0)

	cmds.iconTextButton(i='polyLoopEdge',c=lambda *args:selectContiuousEdges())

	### select continuous edges ###

	cmds.setParent('..')
	cmds.setParent('..')


def UI():
	if cmds.window('MS_selector_window',q=True,ex=True):
		cmds.deleteUI('MS_selector_window')
	cmds.window('MS_selector_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_selector_window')

	