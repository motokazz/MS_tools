# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_createMultiStructs.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import s2000_tools.MSG2_breakTools.MSG2_breakNodeUtil as MSG2_breakNodeUtil
reload(MSG2_breakNodeUtil)

def main():
	NODES=cmds.ls(sl=True)
	for NODE in NODES:
		createMultiStructs(NODE)
		selectedNodeToMultiStructs(NODE)
		addExportAttr(NODE)

def createMultiMeshCollisionFromSelected(NODE=''):
	if NODE:
		cmds.select(cmds.ls(NODE,dag=True,type='mesh'),r=True)
	else:
		cmds.select(cmds.ls(sl=True,dag=True,type='mesh'),r=True)

	#選択からメッシュコリジョンを作成
	cmds.duplicate()
	DUPED=cmds.ls(sl=True,l=True)
	try:
		UNITED=cmds.polyUnite(ch=False)[0]
		for EACHDUPED in DUPED:
			if cmds.objExists(EACHDUPED):
				cmds.delete(EACHDUPED)
	except:
		UNITED=DUPED
	cmds.delete(UNITED,ch=True)

	#一回原点にだす
	try:
		UNITED=cmds.parent(UNITED,w=True)
	except:
		pass

	#Grouping
	NODE=NODE.split('|')[-1]
	if not cmds.objExists('|top_'+NODE+'|col'):
		cmds.group(empty=True,n='|top_'+NODE+'|col')
	else:
		COLOLD=cmds.listRelatives('|top_'+NODE+'|col',ad=True,typ='transform')
		cmds.delete(COLOLD)

	cmds.parent(UNITED,'|top_'+NODE+'|col')
	COL=cmds.ls(sl=True,l=True)[0]

	#freeze
	cmds.xform('|top_'+NODE+'|col',piv=[0,0,0],ws=True)
	cmds.makeIdentity('|top_'+NODE+'|col',a=True,t=True,r=True,s=True)
	
	cmds.xform(COL,piv=[0,0,0],ws=True)
	cmds.makeIdentity(COL,a=True,t=True,r=True,s=True)
	
	cmds.xform('|top_'+NODE+'|col',piv=[0,0,0],ws=True)

	#deletePolyColorSet
	try:
		cmds.polyColorSet(COL,d=True,allColorSets=True)
	except:
		pass
		
	#setLambert
	cmds.select(COL,r=True)
	cmds.hyperShade(a='lambert1')
	
	#ADD_HAVOK
	MSG2_breakNodeUtil.toHavok(COL,MASS=0,SHAPETYPE=6)
	return COL

def createMultiStructs(NODE=''):
	NODE=NODE.split('|')[-1]
	if not cmds.objExists('|top_'+NODE):
		cmds.group(em=True,n='|top_'+NODE)

	if not cmds.objExists('|top_'+NODE+'|root'):
		PROOT=cmds.group(em=True,n='|proot')
		cmds.parent(PROOT,'|top_'+NODE)
		cmds.rename('|top_'+NODE+'|'+PROOT,'root')

	if not cmds.objExists('|top_'+NODE+'|col'):
		PCOL=cmds.group(em=True,n='|pcol')
		cmds.parent(PCOL,'|top_'+NODE)
		cmds.rename('|top_'+NODE+'|'+PCOL,'col')


def selectedNodeToMultiStructs(NODE=''):
	if not NODE:
		return

	COL = createMultiMeshCollisionFromSelected(NODE)[0]
	SN=NODE.split('|')[-1]
	cmds.parent(NODE,'|top_'+SN+'|root')

	#cmds.hide(['sdw','low','col','occ'])
	cmds.hide(['|top_'+SN+'|col'])

def addExportAttr(NAME):
	NAME=NAME.split('|')[-1]
	TOPNODE='top_'+NAME.split('|')[-1]
	for each in ['root','col']:
		NODE=TOPNODE+'|'+each
		if not cmds.attributeQuery('export_top',node=NODE,ex=True ):#アトリビュート追加
			cmds.addAttr(NODE,longName='export_top',at='bool')

		if not cmds.attributeQuery('export_name',node=NODE,ex=True ):#アトリビュート追加
			cmds.addAttr(NODE,longName='export_name',dt='string')

		cmds.setAttr (NODE+'.export_name',NAME,type='string')
		cmds.setAttr (NODE+'.export_top',True)


def LayoutA():
	cmds.columnLayout('MSG2_createMultiStructs.py _mainLayout',adj=True,ann=u'一個のシーンから、複数のオブジェクトを出力するためのセットアップをします。\n選択オブジェクトを、そのオブジェクト名でエキスポート可能な形式にセットアップ。\nそのままメッシュコリジョン化します。\n一個のメッシュから一個のセットアップを作ります。\n複数のオブジェクトを選ぶと、複数のセットアップが作れます。')
	cmds.separator()
	cmds.text(l='MSG2_createMultiStructs.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='createMultiStructs',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	