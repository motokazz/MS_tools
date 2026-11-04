# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_getTextureSize.py
# 説明
#			選択ファイルテクスチャノードからサイズを取得
#			選択フェースに貼られているテクスチャのサイズを取得
# 作成日
#			
########################################

import maya.cmds as cmds

def main():
	#選択ファイルテクスチャノードからサイズを取得
	#選択フェースに貼られているテクスチャのサイズを取得
	SEL=cmds.ls(sl=True)
	TEX=cmds.ls(sl=True,typ='file')
	if not TEX:
		cmds.hyperShade(smn=True)
		try:
			FTN=cmds.listConnections('.color')[0]
			if FTN:
				TEX_SIZE=cmds.getAttr(FTN+'.outSize')[0]
		except:
			TEX_SIZE=(0,0)
	else:
		TEX_SIZE=cmds.getAttr(TEX[0]+'.outSize')[0]

	cmds.intField('MS_getTextureSize_texsizeU',e=True,v=int(TEX_SIZE[0]))
	cmds.intField('MS_getTextureSize_texsizeV',e=True,v=int(TEX_SIZE[1]))
	
	cmds.select(SEL,r=True)

def LayoutA():
	cmds.frameLayout('MS_getTextureSize_frameLayout',w=135,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'getTextureSize',cll=True,cl=False)
	cmds.columnLayout('MS_getTextureSize_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='textureSize')
	cmds.rowLayout(nc=2,cw2=[50,50])
	cmds.intField('MS_getTextureSize_texsizeU',v=1024)
	cmds.intField('MS_getTextureSize_texsizeV',v=1024)
	cmds.setParent('..')
	cmds.button(l='getSize',c=lambda *args:main(),ann='選択ファイルテクスチャノードからサイズを取得')
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	