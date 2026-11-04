# _*_coding:utf-8_*_
########################################
# ファイル名
#            MS_fpsCam.py
# 説明
#            
#            
# 作成日
#            
########################################


import maya.cmds as cmds

COI=cmds.getAttr('perspShape.centerOfInterest')
GX=0
GY=0
GZ=0
def cammove(MODE='idle'):
	global GX,GY,GZ
	if MODE=='idle':
		GX=0
		GY=0
		GZ=0
	if MODE=='front':GZ=-0.1
	if MODE=='back':GZ=0.1
	if MODE=='right':GX=0.1
	if MODE=='left':GX=-0.1
	if MODE=='up':GY=0.1
	if MODE=='down':GY=-0.1
		
	
	
def movemove():
	cmds.setAttr('perspShape.centerOfInterest',0.01)
	cmds.move(GX,GY,GZ,'|persp',os=True,r=True)
	
def killjob():
	cmds.setAttr('perspShape.centerOfInterest',COI)
	
def UI():
	
	#cmds.setAttr('perspShape.centerOfInterest',0.01)
	
	if cmds.window('MS_cammove_window',q=True,ex=True):
		cmds.deleteUI('MS_cammove_window')
	cmds.window('MS_cammove_window',rtf=True,s=True)
	cmds.columnLayout()
	cmds.text('MS_cammove_XXX',l='MS_cammove_XXX')
	cmds.setParent('..')
	cmds.showWindow('MS_cammove_window')
	
	cmds.scriptJob(uid=['MS_cammove_XXX',lambda *args:killjob()])
	cmds.scriptJob(e=['idle',lambda *args:movemove()],p='MS_cammove_XXX')
