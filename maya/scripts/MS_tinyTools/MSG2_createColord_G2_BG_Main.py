# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_createColord_G2_BG_Main.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

if not cmds.pluginInfo('Gravite2Shader.mll',q=True,loaded=True):
	cmds.loadPlugin('Gravite2Shader.mll')

### DEFINE ###

COLTEXPATH='D:/resources/texture/color4096'
NAME=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

#################
# util
#################
#################
# shaderChanger
#################
def shaderChanger(shdName='G2_BG_Main',FROM ='selection'):
	RET=''
	SHDLIST=[]
	#### selectionmode ###
	if FROM =='selection':
		nodes=cmds.ls(sl=True,l=True)
	elif FROM =='allGBG':
		nodes=cmds.ls(type='G_BG_Main',l=True)
	elif FROM =='allG2BG':
		nodes=cmds.ls(type='G2_BG_Main',l=True)
	elif FROM =='alllambert':
		nodes=cmds.ls(type='lambert',l=True)

	### core ###
	for each in nodes:

		if each == 'lambert1':
			continue
		
		success=False
		con = cmds.listConnections(each+'.color')
		sg = cmds.listConnections(each+'.outColor')
		shd = cmds.shadingNode(shdName,asShader=True)
		SHDLIST.append(shd)
		sgs = cmds.sets(sg[0],q=True)

		certified=[]#発見できないオブジェクトを排斥したリストを作成する
		if sgs:
			for eachsgs in sgs:
				if cmds.objExists(eachsgs):
					certified.append(eachsgs)
				else:
					print each

			cmds.select(certified,r=True)
			try:
				cmds.hyperShade(a=shd)
				RET+='success : '+each+' to '+shd+'\n'
			except:
				RET+='failed : '+each+' to '+shd+'\n'
				pass

			try:
				cmds.connectAttr(con[0]+'.outColor',shd+'.color')
				cmds.connectAttr(shd+'.outColor',sg[0]+'.surfaceShader')
				success=True
				
			except:
				pass
			cmds.delete(each)
	#mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')

	return SHDLIST

def lambertToG2colorScale():
	SEL = cmds.ls(sl=True,l=True)
	NEWLIST=[]
	for each in SEL:
		COLOR=cmds.getAttr(each+'.color')[0]
		cmds.select(each,r=True)
		NEW=shaderChanger(shdName='G2_BG_Main',FROM ='selection')
		cmds.setAttr(NEW[0]+'.colorScale',COLOR[0],COLOR[1],COLOR[2],type='float3')
		NEWLIST.append(NEW[0])
	cmds.select(NEWLIST,r=True)

def G2colorScaleTolambert():
	SEL = cmds.ls(sl=True,l=True)
	NEWLIST=[]
	for each in SEL:
		COLOR=cmds.getAttr(each+'.colorScale')[0]
		print COLOR[2]
		cmds.select(each,r=True)
		NEW=shaderChanger(shdName='lambert',FROM ='selection')
		cmds.setAttr(NEW[0]+'.color',COLOR[0],COLOR[1],COLOR[2],type='float3')
		NEWLIST.append(NEW[0])
	cmds.select(NEWLIST,r=True)

def textureToG2colorScale():
	SEL = cmds.ls(sl=True,l=True)
	for each in SEL:
		FTN = cmds.listConnections(each+'.color')
		if not FTN:
			continue
		COLOR=FTN[0].replace('col','').replace('tex','')
		R=int(COLOR[0],15)*(1.0/15)
		G=int(COLOR[1],15)*(1.0/15)
		B=int(COLOR[2],15)*(1.0/15)
		cmds.setAttr(each+'.colorScale',R,G,B,type='float3')
		cmds.disconnectAttr(FTN[0]+'.outColor',each+'.color')

def renameMaterialFromTTextureName():
	SEL = cmds.ls(sl=True,l=True)
	for each in SEL:
		FTN = cmds.listConnections(each+'.color')
		cmds.rename(each,'G2_'+FTN[0])

def G2colorScaleToTexture():
	SEL = cmds.ls(sl=True,l=True)
	for EACHSEL in SEL:
		RGB=cmds.getAttr(EACHSEL+'.colorScale')[0]

		RGBSTR=NAME[int(RGB[0]*15)]+NAME[int(RGB[1]*15)]+NAME[int(RGB[2]*15)]

		TEXNAME = COLTEXPATH+'/'+RGBSTR+'.tif'

		FTN_NAME='col'+RGBSTR+'tex'
		
		if not cmds.objExists(FTN_NAME):
			cmds.shadingNode('file',n=FTN_NAME,asTexture=True)
			cmds.setAttr(FTN_NAME+'.fileTextureName',TEXNAME,type='string')

		cmds.connectAttr(FTN_NAME+'.outColor',EACHSEL+'.color',f=True)
		cmds.setAttr(EACHSEL+'.colorScale',1.0,1.0,1.0,type='float3')

def lambertColorToTexture():
	SEL = cmds.ls(sl=True,l=True)
	for EACHSEL in SEL:
		RGB=cmds.getAttr(EACHSEL+'.color')[0]
		main(RGB)
	

#################
# main
#################

def main(RGB=[0,0,0]):
	RGBSTR=NAME[int(RGB[0]*15)]+NAME[int(RGB[1]*15)]+NAME[int(RGB[2]*15)]

	TEXNAME = COLTEXPATH+'/'+RGBSTR+'.tif'
	FTN_NAME='col'+RGBSTR+'tex'

	if not cmds.objExists(FTN_NAME):
		cmds.shadingNode('file',n=FTN_NAME,asTexture=True)
		cmds.setAttr(FTN_NAME+'.fileTextureName',TEXNAME,type='string')
		NODE=cmds.shadingNode('G2_BG_Main',asShader=True)	
		cmds.connectAttr(FTN_NAME+'.outColor',NODE+'.color',f=True)

def ceditor():
	cmds.colorEditor()
	if cmds.colorEditor(query=True, result=True):

		values = cmds.colorEditor(query=True, rgb=True)
		main(values)
		print 'RGB = ' + str(values)

		values = cmds.colorEditor(query=True, hsv=True)
		print 'HSV = ' + str(values)
		alpha = cmds.colorEditor(query=True, alpha=True)
		print 'Alpha = ' + str(alpha)
	else:
		print 'Editor was dismissed'

def cgrab():
	cmds.grabColor()
	RGB=cmds.grabColor( rgb=True )
	main(RGB)


def LayoutA():
	cmds.columnLayout('MSG2_createColord_G2_BG_Main_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_createColord_G2_BG_Main',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='CEDITOR',c=lambda *args:ceditor())
	cmds.button(l='CGRAB',c=lambda *args:cgrab())

	cmds.separator(w=200)
	cmds.button(l='textureToG2colorScale',c=lambda *args:textureToG2colorScale())
	cmds.button(l='G2colorScaleToTexture',c=lambda *args:G2colorScaleToTexture())
	cmds.button(l='lambertColorToTexture',c=lambda *args:lambertColorToTexture())
	cmds.button(l='lambertToG2colorScale',c=lambda *args:lambertToG2colorScale())
	cmds.button(l='G2colorScaleTolambert',c=lambda *args:G2colorScaleTolambert())
	cmds.separator(w=200)
	cmds.button(l='renameMaterialFromTTextureName',c=lambda *args:renameMaterialFromTTextureName())

	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()

	cmds.showWindow('MS_tools_window')

	

