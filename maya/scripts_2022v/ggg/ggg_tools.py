import maya.cmds as cmds
import importlib

from . import ggg_cc4_bone_rename
importlib.reload(ggg_cc4_bone_rename)

import _lib.MS_storeRecallUI as MS_storeRecallUI
importlib.reload(MS_storeRecallUI)

from . import ggg_model_util
importlib.reload(ggg_model_util)

exportPath = 'D:/ggg/ggg-app-client/ggg-app-client/Assets/GGG/BG/stage02/BB/'


def BakeTexture():
	var = cmds.floatFieldGrp('SamplingOffset',q=True,v1=True)
	ggg_model_util.bake_texture(FILEPATH = GetPath() , samplingOffset=var)

def GetPath():
	def PathNormlize(path):
		path.replace('\\', '/')
		path.replace('//','/')
		if path[-1] != '/':
			path += '/'
		return path

	reositoryPath = cmds.textField('RepositoryPath',q=True,tx=True)
	reositoryPath = PathNormlize(reositoryPath)

	assetPath = cmds.textField('BBWorkflowPath',q=True,tx=True)
	assetPath = PathNormlize(assetPath)

	ret = PathNormlize(reositoryPath + assetPath)

	return ret

def layoutTools(WIDTH=400,BGC=[0.2,0.2,0.2]):
	cmds.frameLayout('gggtools_frameLayout', w=WIDTH, bgc=BGC, fn='boldLabelFont', l='gggtools', cll=False,
					 cl=True)
	cmds.columnLayout()

	#CC4
	cmds.text(l='CC4',fn='boldLabelFont',w=200,bgc=(0.1,0.1,0.1))
	cmds.button(l='cc4_dag_rename',w=200,c=lambda *args:ggg_cc4_bone_rename.cc4_dag_rename())
	cmds.separator(h=10)

	#MISC
	cmds.text(l='misc',fn='boldLabelFont',w=200,bgc=(0.1,0.1,0.1))
	cmds.button(l='delete_hidden_models',w=200,c=lambda *args:ggg_model_util.delete_hidden_models())
	cmds.button(l='ungroup',w=200,c=lambda *args:ggg_model_util.ungroup())
	cmds.separator(h=10)

	#Texture
	cmds.text(l='search_set_texture',fn='boldLabelFont',w=200,bgc=(0.1,0.1,0.1))
	cmds.button(l='search_set_texture',w=200,bgc=(0.8,0.8,0.8) , c=lambda *args: ggg_model_util.search_fit_texture())
	cmds.separator(h=10)

	#BBWorkflow
	cmds.text(l='BBWorkflow',fn='boldLabelFont',w=200,bgc=(0.1,0.1,0.1))
	cmds.textField('RepositoryPath',tx='D:/ggg/ggg-app-client/ggg-app-client/',cc=lambda *args:MS_storeRecallUI.store('gggtools_frameLayout'),w=300)
	cmds.textField('BBWorkflowPath',tx='Assets/GGG/BG/stage01/BB/',cc=lambda *args:MS_storeRecallUI.store('gggtools_frameLayout'),w=300)
	cmds.button(l='freeze_transform',w=200, c=lambda *args: ggg_model_util.freeze_transform())
	cmds.button(l='createUV',w=200, c=lambda *args: ggg_model_util.createUV())
	cmds.button(l='export_fbx',w=200, c=lambda *args: ggg_model_util.export_fbx(FILEPATH = GetPath() ))

	# bake texture
	cmds.floatFieldGrp('SamplingOffset',l='samplingOffset',v1=3.0)
	cmds.button(l='bake_texture',w=200, c=lambda *args: BakeTexture())
	cmds.separator(h=10)
	cmds.button(l='BB_workflow_all',w=200, bgc = (0.6,0.7,0.6),c=lambda *args: ggg_model_util.BB_workflow_all( FILEPATH = GetPath() ))
	cmds.setParent('..')
	cmds.setParent('..')


def UI():
	if cmds.window('ggg_tools_main_window', q=True, ex=True):
		cmds.deleteUI('ggg_tools_main_window')
	cmds.window('ggg_tools_main_window', rtf=True, s=True)
	cmds.columnLayout()

	layoutTools()

	cmds.setParent('..')

	cmds.window('ggg_tools_main_window', e=True, w=217, h=640)

	cmds.showWindow('ggg_tools_main_window')

	MS_storeRecallUI.recall('gggtools_frameLayout')
