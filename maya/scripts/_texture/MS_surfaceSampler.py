# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_surfaceSampler
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds

import _lib.MS_fileExport as MS_fileExport


def MS_surfaceSampler(TARGETS=[],SOURCES=[],FILEPATH='D:/work/baked_c',MAPWIDTH=512,MAPHEIGHT=512,SEARCH_OFFSET=0,MAX_SEARCH_DISTANCE=0):
	cmds.surfaceSampler(target=TARGETS,source=SOURCES,fileFormat='tif',mapOutput='diffuseRGB',filename=FILEPATH)

		#,uvSet='map1'
		#,searchOffset=SEARCH_OFFSET
		#,maxSearchDistance=MAX_SEARCH_DISTANCE
		#,searchCage=''

		#
		#,mapWidth=MAPWIDTH
		#,mapHeight=MAPHEIGHT
		#,max=1
		#,mapSpace='tangent'
		#,mapMaterials=1
		#,shadows=1
		#
		#,superSampling=1
		#,filterType=0
		#,filterSize=3
		#,overscan=100
		#,searchMethod=0
		#,useGeometryNormals=1
		#,ignoreMirroredFaces=0
		#,flipU=0
		#,flipV=0

def storeTargets():
	#cmds.textField('MS_surfaceSampler_targets',e=True,tx=','.join(cmds.ls(sl=True,dag=True,s=True,l=True)))
	cmds.textField('MS_surfaceSampler_targets',e=True,tx=cmds.ls(sl=True,dag=True,s=True,l=True)[0])

def storeSources():
	#cmds.textField('MS_surfaceSampler_sources',e=True,tx=','.join(cmds.ls(sl=True,dag=True,s=True,l=True)))
	cmds.textField('MS_surfaceSampler_sources',e=True,tx=cmds.ls(sl=True,dag=True,s=True,l=True)[0])

def main():
	FILEPATH=MS_fileExport.single('MS_surfaceSampler_fileBrouser',Q=True)
	FILENAME=cmds.textField('MS_surfaceSampler_filename',q=True,tx=True)
	TARGETS = cmds.textField('MS_surfaceSampler_targets',q=True,tx=True)
	SOURCES = cmds.textField('MS_surfaceSampler_sources',q=True,tx=True)
	if not SOURCES or not TARGETS:
		cmds.confirmDialog(m='WARRNING !\ncant find SOURCE or TARGET.')
		return 'ERROR ! : %s :cant find SOURCE or TARGET'%CURRENT_SCENE

	print TARGETS
	print SOURCES
	print FILEPATH+FILENAME

	MS_surfaceSampler(TARGETS,SOURCES,FILEPATH+FILENAME,MAPWIDTH=512,MAPHEIGHT=512)

	print FILEPATH

def LayoutA():
	cmds.frameLayout('MS_surfaceSampler_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_surfaceSampler',cll=True,cl=False)
	cmds.columnLayout('MS_surfaceSampler_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_surfaceSampler',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	MS_fileExport.single('MS_surfaceSampler_fileBrouser', LABEL='brouser', FILE_FILTER='*.*', MODE='dir')
	
	cmds.textField('MS_surfaceSampler_filename',tx='baked_c',en=False)

	cmds.text (l='source')
	cmds.textField('MS_surfaceSampler_sources',en=False)
	cmds.button(l='store source',c=lambda *args:storeSources())

	cmds.text (l='targets')
	cmds.textField('MS_surfaceSampler_targets',en=False)
	cmds.button(l='store targets',c=lambda *args:storeTargets())	
	
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_surfaceSampler_window',q=True,ex=True):
		cmds.deleteUI('MS_surfaceSampler_window')
	cmds.window('MS_surfaceSampler_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_surfaceSampler_window')
	