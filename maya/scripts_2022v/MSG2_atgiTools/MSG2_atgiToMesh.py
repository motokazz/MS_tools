# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_atgiToMesh.py
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds
import maya.mel as mel
import os

#G2Path
BGMBRoot = 'D:/Projects/Gravite2/graphic/bg/scenes'


#指定パスからの相対パスを返す　例）module/MS_primitives.py
def searchPath(searchPath,searchFile='',searchExt='mb'):
	print searchFile+'.'+searchExt
	for (root,dir,files) in os.walk(searchPath):
		#発見時の処理
		for f in files:
			fname=f.split('.')[0]
			if (searchFile+'.'+searchExt) == f:
				root=root.replace('\\','/').replace('//','/')
				return root+'/'+f
	return False

#指定ノードを消す。
def deleteChildNodes(TOPNAME='',):
	preserveList=[]
	childs=cmds.listRelatives(TOPNAME,c=True,f=True)
	for each in childs:
		name=each.split('|')[-1]
		if 'root' in name:
			childs.remove(each)
			preserveList.append(each)

	if childs:
		cmds.delete(childs)
	return preserveList
	
#Atgiを実体化
def atgiToMesh(ATGIS=[]):
	RET=[]
	LOADED={}
	TEMP_NAME='MS_atgiTool_temp_xxxx'

	if cmds.objExists(TEMP_NAME):
		cmds.delete(TEMP_NAME)

	for EACHSEL in ATGIS:
		PARENT=cmds.listRelatives(EACHSEL,p=True,f=True)

		#選択Atgiロケーターの座標を取得
		TRN=cmds.xform(EACHSEL,q=True,ws=True,t=True)
		ROT=cmds.xform(EACHSEL,q=True,ws=True,ro=True)

		#選択AtgiファイルのMBパスを取得
		cmds.select(EACHSEL,r=True)
		AtgiFile=cmds.getAttr('.atgiFilename')


		AtgiName=AtgiFile.split('/')[-1].split('\\')[-1].split('.')[-2]
		
		#もう読み込んである物をチェック。
		CHECK_LOADED=False
		for EACHKEY in LOADED.keys():
			if AtgiName == EACHKEY:
				CHECK_LOADED=True
				break

		#読み込み処理
		if CHECK_LOADED:
			ROOTNAME=cmds.duplicate(LOADED[EACHKEY])[0]
			ROOTNAME=cmds.ls(ROOTNAME,l=True)
		else:
			FPATH=searchPath(BGMBRoot,AtgiName) 
			if not FPATH:
				#ファイル無かったらスキップ
				print 'MBFile not found ! %s'%AtgiName
				continue

			cmds.file(FPATH,i=True,rdn=True,rpr="crash",dns=True,type="mayaBinary",options="v=0",loadReferenceDepth="none",gr=True,gn=TEMP_NAME,shd=True,prompt=False)
			PRE=deleteChildNodes(TEMP_NAME)
			ROOTNAME=cmds.parent(PRE,w=True)
			cmds.delete(TEMP_NAME)
			mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')

		#リネームと親子付け
		RENAMED=cmds.rename(ROOTNAME[0],AtgiName+'_01')
		RENPARENT=cmds.listRelatives(RENAMED,p=True,f=True)
		if not PARENT == RENPARENT:
			RENAMED=cmds.parent(RENAMED,PARENT[0])

		#移動
		cmds.xform(RENAMED,t=TRN,ws=True)
		cmds.xform(RENAMED,ro=ROT,ws=True)

		#戻り値を作る
		RET.append(cmds.ls(RENAMED,s=True,dag=True,lf=True,l=True)[0])

		#読み込み済みファイル格納
		if not CHECK_LOADED:
			LOADED.setdefault(AtgiName,cmds.ls(RENAMED,l=True)[0])

		cmds.delete(EACHSEL)
		
	MELCOM='''
		{
		source "C:/Program Files/Autodesk/Maya2011/scripts/startup/cleanUpScene.mel";
		deleteUnusedNurbsSurfaces();
		deleteEmptyGroups();
		deleteEmptyLayers("Display");
		deleteEmptyLayers("Render");
		deleteUnusedConstraints;
		deleteUnusedPairBlends;
		deleteUnusedSets;
		deleteUnusedExpressions;
		//deleteUnusedInUnusedHierarchy;
		deleteUnknownNodes;
		}
		'''
	#mel.eval(MELCOM)
	#cmds.delete(ATGIS)
	return RET

def main():
	SEL=cmds.ls(sl=True,l=True)
	atgiToMesh(SEL)

def LayoutA():
	cmds.columnLayout('MSG2_atgiToMesh.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_atgiToMesh.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	
UI()