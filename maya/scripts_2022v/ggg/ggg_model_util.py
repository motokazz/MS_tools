import maya.cmds as cmds
import glob


def delete_hidden_models():
	sel = cmds.ls(s=True, typ='mesh')
	for obj in sel:
		if cmds.nodeType(obj) != 'mesh':
			continue
		parentName = cmds.listRelatives(obj, p=True)[0]
		if cmds.objExists(obj):
			if cmds.getAttr(parentName + '.visibility') == False:
				cmds.delete(parentName)


def ungroup():
	sel = cmds.ls('group')
	for obj in sel:
		children = cmds.listRelatives(obj, c=True, f=True)
		if children:
			cmds.parent(children, w=True)
			cmds.delete(obj)


def freeze_transform():
	newObject = cmds.ls(sl=True)
	cmds.makeIdentity(newObject, a=True, t=True, r=True, s=True)
	cmds.xform(newObject, piv=(0, 0, 0))

def createUV():
	newObject = cmds.ls(sl=True)
	# UV
	cmds.polyAutoProjection(newObject[0], lm=0, pb=0, cm=0, l=2, sc=1, o=1, p=6, ps=0.2, ws=0)

def export_fbx(FILEPATH = 'D:/ggg/ggg-app-client/ggg-app-client/Assets/GGG/BG/stage02/BB/'):
	newObject = cmds.ls(sl=True)
	# ExportFBX
	cmds.select(newObject[0], r=True)
	cmds.FBXExport('-f', FILEPATH + newObject[0], '-s')

def bake_texture(FILEPATH = 'D:/ggg/ggg-app-client/ggg-app-client/Assets/GGG/BG/stage02/BB/',samplingOffset=3):
	newObject = cmds.ls(sl=True)
	# BakeTexture
	cmds.surfaceSampler(
		target=newObject[0]
		, source=newObject[1]
		, fileFormat='png'
		, mapOutput='diffuseRGB'
		, filename=FILEPATH + 'tex_' + newObject[0] + '_d'
		, mapWidth=1024
		, mapHeight=1024
		, ss=1
		, so=samplingOffset
	)

	cmds.surfaceSampler(
		target=newObject[0]
		, source=newObject[1]
		, fileFormat='png'
		, mapOutput='normal'
		# ,sp='object'
		, filename=FILEPATH + 'tex_' + newObject[0] + '_n'
		, mapWidth=1024
		, mapHeight=1024
		, ss=1
		, so=samplingOffset
	)

def search_fit_texture(PATH = 'D:/ggg/ggg-app-client/ggg-app-client/Assets/'):
	files = cmds.ls(type='file')
	print(files)
	for f in files:
		ftn = cmds.getAttr(f + '.fileTextureName')
		fn = ftn.split('/')[-1].split('\\')[-1]

		name = glob.glob(PATH + '**/' + fn, recursive=True)
		print(name)
		if name:
			cmds.setAttr(f + '.fileTextureName', name[0], type='string')
		else:
			print('texture not found')

	SetBumpDepth()#Bumpの値調整

def SetBumpDepth(bumpDepth=0.1):
	sel = cmds.ls(type='bump2d')
	for obj in sel:
		cmds.setAttr(obj+'.bumpDepth',0.1)
		cmds.setAttr(obj + '.bumpInterp', 1)


def BB_workflow_all(FILEPATH = 'D:/ggg/ggg-app-client/ggg-app-client/Assets/GGG/BG/stage02/BB/',samplingOffset=3):

	newObject = cmds.ls(sl=True)

	cmds.makeIdentity(newObject, a=True, t=True, r=True, s=True)
	cmds.xform(newObject, piv=(0, 0, 0))

	# UV
	cmds.polyAutoProjection(newObject[0], lm=0, pb=0, cm=0, l=2, sc=1, o=1, p=6, ps=0.2, ws=0)

	# ExportFBX
	cmds.select(newObject[0], r=True)
	cmds.FBXExport('-f', FILEPATH + newObject[0], '-s')

	# BakeTexture
	cmds.surfaceSampler(
		target=newObject[0]
		, source=newObject[1]
		, fileFormat='png'
		, mapOutput='diffuseRGB'
		, filename=FILEPATH + 'tex_' + newObject[0] + '_d'
		, mapWidth=1024
		, mapHeight=1024
		, ss=1
		, so=samplingOffset
	)

	cmds.surfaceSampler(
		target=newObject[0]
		, source=newObject[1]
		, fileFormat='png'
		, mapOutput='normal'
		# ,sp='object'
		, filename=FILEPATH + 'tex_' + newObject[0] + '_n'
		, mapWidth=1024
		, mapHeight=1024
		, ss=1
		, so=samplingOffset
	)






