# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_G2ShaderUtil.py
# 説明
#			シェーダーの差し替えツール
#
# 作成日
#
########################################

import maya.cmds as cmds

#MS_selectInSelectedObjectWithMaterial
import MS_selectInSelectedObjectWithMaterial
reload(MS_selectInSelectedObjectWithMaterial)

##############
# マテリアル作成
##############

def createMaterial(shaderType='StingrayPBS'):
	def createStingrayPBS(dummy=True):
		# create StingrayPBS
		MAT = cmds.shadingNode(shaderType, asShader=True)
		SG = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=MAT + 'SG')
		cmds.setAttr(MAT + '.initgraph', True)
		cmds.connectAttr(MAT + '.outColor', SG + '.surfaceShader', f=True)
		return MAT

	SEL = cmds.ls(sl=True,mat=True)

	if SEL:
		for each in SEL:
			NEW = createStingrayPBS()
			col = cmds.getAttr(each+'.color')
			cmds.setAttr(NEW+'.base_color',col[0][0],col[0][1],col[0][2],type='double3')
			cmds.rename(NEW,each+'_PBS')
	else:
		createStingrayPBS()

	createPalette()


##############
#IDマップ作成用
##############
IDPallets = [
	[1,0,0]
	,[0,1,0]
	,[0,0,1]
	,[1,1,0]
	,[1,0,1]
	,[0,1,1]
	,[1,0.5,0]
	,[1,0,0.5]
	,[0.5,1,0]
	,[0,1,0.5]
	,[0.5,0,1]
	,[0,0.5,1]
	,[1,0.5,0.5]
	,[0.5,1,0.5]
	,[0.5,0.5,1]
	,[0.5,0,0]
	,[0,0.5,0]
	,[0,0,0.5]
	,[0.5,0.5,0]
	,[0.5,0,0.5]
	,[0,0.5,0.5]
]

#IDマップ作成
def autoIDMap():
	sel = cmds.ls(sl=True)
	StingrayPBS = cmds.ls(type='StingrayPBS')
	i=0
	for each in StingrayPBS:
		cmds.select(sel,r=True)
		try:
			MS_selectInSelectedObjectWithMaterial.selectInSelectedObjectWithMaterial(each)
			cmds.polyColorPerVertex(rgb=IDPallets[i])
		except:
			pass
		i+=1

#####################
#マテリアルボーダー選択
#####################

def cutUVbyMaterials():
	sel = cmds.ls(sl=True)
	result =[]
	StingrayPBS = cmds.ls(type='StingrayPBS')
	for each in StingrayPBS:
		try:
			cmds.select(sel, r=True)
			MS_selectInSelectedObjectWithMaterial.selectInSelectedObjectWithMaterial(each)
			edge_perimeter = cmds.polyListComponentConversion(te=True,bo=True)
			result.extend(edge_perimeter)
			#cmds.polyMapCut(edge_perimeter)

		except:
			pass
	cmds.select(result,r=True)

###############
#ButtonCommands
###############

def selectMaterial(material_name):
	def ret(dummy=''):
		cmds.select(material_name,r=True)
	return ret

def assignMaterial(material_name,ID=0):
	def ret(dummy=''):
		cmds.hyperShade(a=material_name)
		if cmds.checkBox('MS_materialPalette_Paint_ID_with_assign',q=True,v=True):
			cmds.polyColorPerVertex(rgb=IDPallets[ID])
	return ret

def selectObjectsFromMaterial(material_name):
	def ret(dumy=''):
		sel = cmds.ls(sl=True)
		if not sel:
			cmds.hyperShade(o=material_name)
		else:
			MS_selectInSelectedObjectWithMaterial.selectInSelectedObjectWithMaterial(material_name)

	return ret

#####
#UI
#####

def createPalette():
	if cmds.gridLayout('MS_materialPalette_gridLayout',q=True,ex=True):
		cmds.deleteUI('MS_materialPalette_gridLayout')
	cmds.gridLayout('MS_materialPalette_gridLayout',nc=4,nr=6,cw=80,ch=90,p='MS_materialPalette_scrollLayout')

	#StingrayPBS = cmds.ls(type='StingrayPBS')
	StingrayPBS = cmds.ls(mat=True)
	StingrayPBS.sort()
	i=0

	for each in StingrayPBS:
		TYPE = cmds.nodeType(each)
		if TYPE == 'lambert':base_color = cmds.getAttr(each + ".color")
		if TYPE == 'phong': base_color = cmds.getAttr(each + ".color")
		if TYPE == 'StingrayPBS': base_color = base_color = cmds.getAttr(each + ".base_color")
		if TYPE == 'particleCloud': base_color = base_color = cmds.getAttr(each + ".color")


		cmds.columnLayout(p='MS_materialPalette_gridLayout',adj=True)
		cmds.text(l=TYPE)
		cmds.button(l=each,bgc=base_color[0],c=selectMaterial(each),ann=each)
		cmds.button(l='assign',bgc=base_color[0],c=assignMaterial(each,ID=i))
		cmds.button(l='selectObj',bgc=base_color[0], c=selectObjectsFromMaterial(each),ann = u'オブジェクト選択時：オブジェクト内で使用されているもの・オブジェクト非選択時：シーン内のすべてのオブジェクトを対象にマテリアル選択')

		cmds.setParent('..')
		i+=1

	return
	# Other Materials

	Materials = cmds.ls(type='lambert')

	for each in Materials:


		cmds.columnLayout(p='MS_materialPalette_gridLayout',adj=True)

		cmds.button(l=each,bgc=base_color[0],c=selectMaterial(each),ann=each)
		cmds.button(l='assign',bgc=base_color[0],c=assignMaterial(each))
		cmds.button(l='selectObj',bgc=base_color[0], c=selectObjectsFromMaterial(each),ann = u'オブジェクト選択時：オブジェクト内で使用されているもの・オブジェクト非選択時：シーン内のすべてのオブジェクトを対象にマテリアル選択')

		cmds.setParent('..')


def LayoutC():
	cmds.frameLayout(l='hypershade',cl=True,cll=False,bgc=[0.4,0.4,0.4])
	cmds.separator()
	cmds.button(l=u'CreateMaterial',c=lambda *args:createMaterial()
				,ann=u'マテリアル選択時、その設定を反映した新規PBSを作成します。\\\n非選択時は普通に新規マテリアルを作成します。')
	cmds.checkBox('MS_materialPalette_Paint_ID_with_assign',l=u'paint ID with assign',v=True)
	cmds.separator()
	cmds.setParent('..')

def LayoutB():
	cmds.frameLayout(l='materialList',cl=True,cll=False,bgc=[0.4,0.4,0.4])
	cmds.separator()
	cmds.button(l=u'IDMAP自動作成',c=lambda *args:autoIDMap())
	cmds.button(l=u'マテリアルボーダー選択',c=lambda *args:cutUVbyMaterials())
	cmds.separator()
	cmds.setParent('..')

def LayoutA():
	cmds.frameLayout(l='materialList',cl=True,cll=False,bgc=[0.4,0.4,0.4])
	cmds.separator()
	#

	cmds.columnLayout(adj=True)
	cmds.button(l='refleshList',c=lambda *args:createPalette())
	cmds.scrollLayout('MS_materialPalette_scrollLayout',h=500)
	cmds.setParent('..')
	cmds.setParent('..')

	#
	cmds.separator()
	cmds.setParent('..')


def UI():
	if cmds.window('MS_tools_window', q=True, ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window', rtf=True, s=True)

	LayoutC()
	LayoutA()
	LayoutB()

	cmds.showWindow('MS_tools_window')

	createPalette()

