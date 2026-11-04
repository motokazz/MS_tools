# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_catapiller
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds

def setup_motion_path():

	joints = cmds.ls(sl=True,type='joint',l=True)
	path = cmds.ls(sl=True,l=True)[-1]

	for each in joints:
		cmds.pathAnimation(each,c=path,fractionMode=True,follow=True,followAxis='y',upAxis='z',worldUpType="object",inverseUp=False,inverseFront = False,bank = False , startTimeU = 0,endTimeU = 1200)

def slide_motion_path():
	i=1
	j=0
	var = cmds.floatField('MS_catapiller_floatField_slide_motion_path',q=True,v=True)
	for i in range(0,30):
		try:
			cmds.keyframe('motionPath'+str(i)+'_uValue',e=True,iub=True,r=True,o='over',tc=j)
			j+=var
		except:
			print 'error' 
			pass
			

def main():
	pass

def LayoutA():
	cmds.frameLayout('MS_catapiller_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_catapiller',cll=True,cl=False)
	cmds.columnLayout('MS_catapiller_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_catapiller',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='setup_motion_path',c=lambda *args:setup_motion_path())


	cmds.floatField('MS_catapiller_floatField_slide_motion_path',v=1)
	cmds.button(l='slide_motion_path',c=lambda *args:slide_motion_path())
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_catapiller_window',q=True,ex=True):
		cmds.deleteUI('MS_catapiller_window')
	cmds.window('MS_catapiller_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_catapiller_window')
	