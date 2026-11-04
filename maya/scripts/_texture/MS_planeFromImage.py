# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_planeFromImage.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds


def planeFromImage(img,textureWidth):
	OUTSIZE=cmds.getAttr(img+".outSize")
	PLANE=cmds.polyPlane(ch=False,o=True,w=textureWidth,h=(textureWidth*OUTSIZE[0][1]/OUTSIZE[0][0]),sw=1,sh=1,cuv=1)
	MATNODE=cmds.shadingNode('lambert',asShader=True)
	cmds.connectAttr (img+'.outColor', MATNODE+'.color' ,f=True)
	cmds.sets(renderable=True,noSurfaceShader=True,empty=True,name=(MATNODE+"SG"))
	cmds.connectAttr( MATNODE+".outColor" , MATNODE+"SG.surfaceShader" , f=True)
	cmds.select(PLANE[0],r=True)
	cmds.sets( e=True , forceElement=MATNODE+"SG")

def planeFromImageEachFile():
	imgs =cmds.ls(typ='file',sl=True)
	textureWidth = cmds.intField ('TEXTUREWIDTH',q=True,v=True)
	if imgs:
		for each in imgs:
			planeFromImage(each,textureWidth)




def LayoutA():
	cmds.columnLayout('MS_tools_mainLayout',adj=True)

	cmds.text(l="1:Select FileNode(texture).")
	cmds.text(l="2:PushButton.")

	cmds.rowLayout(nc=2,cw2=(90,110))
	cmds.text(label="TextureWidth(int)")
	cmds.intField ('TEXTUREWIDTH',w=110,v=256)
	cmds.setParent('..')

	cmds.button(bgc=[0.8,0.8,0.7],w=200,l="Create Plane From Image",c=lambda *args:planeFromImageEachFile())
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')






