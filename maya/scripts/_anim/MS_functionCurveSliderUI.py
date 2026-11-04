# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_functionCurveSliderUI
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds


def hierarchyLevels():
	cmds.ls(sl=True)

def slide(mode='simple',multiply = 1):

	valueOfSlide = cmds.floatField('MS_functionCurveSliderUI_Value',q=True,v=True)

	sel = cmds.ls(sl=True)

	markedChannels = cmds.channelBox('mainChannelBox',q=True,sma=True,ssa=True,sha=True)

	if mode == 'simple':
		i=1
	else:
		i=0
		
	for each in sel:
		if markedChannels:
			for each_markedChannels in markedChannels:
				cmds.keyframe((each+"."+each_markedChannels),e=True,iub=True,r=True,o='over',tc=(valueOfSlide*i*multiply))

		if mode == 'group':
			i+=1

def setInfinity(method='both',type='cycle'):
	
	sel = cmds.ls(sl=True)

	markedChannels = cmds.channelBox('mainChannelBox',q=True,sma=True,ssa=True,sha=True)

	if method == 'both' or method == 'preInfinite':PreInfinite = type
	if method == 'both' or method == 'postInfinite':PostInfinite = type
		
	for each in sel:
		if markedChannels:
			for each_markedChannels in markedChannels:
				cmds.setInfinity((each+"."+each_markedChannels),preInfinite=PreInfinite,postInfinite=PostInfinite)


def LayoutA():
	cmds.frameLayout('MS_functionCurveSliderUI_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_functionCurveSliderUI',cll=True,cl=False)
	cmds.columnLayout('MS_functionCurveSliderUI_mainLayout',adj=True)
	cmds.separator()

	cmds.text(l='MS_functionCurveSliderUI',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	#value
	cmds.rowLayout(nc=2,cw2=[100,50])
	cmds.text('SlideValue')
	cmds.floatField('MS_functionCurveSliderUI_Value',v=1)
	cmds.setParent('..')

	#groupslide
	cmds.rowLayout(nc=3,cw3=[100,50,50],ct3=['both','both','both'])
	cmds.text('GroupSlide')
	cmds.button(l='+',c=lambda *args:slide(mode='group',multiply = 1))
	cmds.button(l='-',c=lambda *args:slide(mode='group',multiply = -1))
	cmds.setParent('..')

	#simpleSlide
	cmds.rowLayout(nc=3,cw3=[100,50,50],ct3=['both','both','both'])
	cmds.text('SimpleSlide')
	cmds.button(l='+',c=lambda *args:slide(mode='simple',multiply = 1))
	cmds.button(l='-',c=lambda *args:slide(mode='simple',multiply = -1))
	cmds.setParent('..')

	cmds.separator(w=200)
	#setInfinity
	cmds.text('setInfinity',bgc=[0.8,0.8,0.8],fn='boldLabelFont')
	cmds.rowLayout(nc=3,cw3=[70,70,70],ct3=['both','both','both'])
	cmds.button(l='Both,cycle',c=lambda *args:setInfinity(method='both',type='cycle'))
	cmds.button(l='pre,cycle',c=lambda *args:setInfinity(method='preInfinite',type='cycle'))
	cmds.button(l='post,cycle',c=lambda *args:setInfinity(method='postInfinite',type='cycle'))
	cmds.setParent('..')

	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_functionCurveSliderUI_window',q=True,ex=True):
		cmds.deleteUI('MS_functionCurveSliderUI_window')
	cmds.window('MS_functionCurveSliderUI_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_functionCurveSliderUI_window')
	