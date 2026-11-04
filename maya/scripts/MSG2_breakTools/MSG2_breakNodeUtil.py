# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_breakNodeUtil.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel

import s2000_tools.MSG2_sceneCleanup_compornents.MSG2_loadPlugin as MSG2_loadPlugin

MSG2_loadPlugin.main()

def toHavok(DAGPATH,MASS=1,SHAPETYPE=1):
	#SHAPETYPE 1=hull,6=mesh
	cmds.select(DAGPATH,r=True)

	#CREATEHAVOK
	mel.eval('hkProcPhysics_removeNodes;')
	mel.eval('hkProcPhysics_createRigidBodies;')

	#HKMASS
	HKNODE = cmds.listRelatives(DAGPATH,type='hkNodeRigidBody',ad=True,c=True,f=True)[0]
	cmds.setAttr(HKNODE+'.mass',MASS)
	#HKSHAPE
	HKSHAPE= cmds.listRelatives(DAGPATH,type='hkNodeShape',ad=True,c=True,f=True)[0]
	cmds.setAttr(HKSHAPE+'.shapeType',SHAPETYPE)
	if SHAPETYPE==1:
		cmds.setAttr(DAGPATH+'.changeExtraRadius',1)
	elif SHAPETYPE==6:
		cmds.setAttr(DAGPATH+'.changeExtraRadius',0)

def main():
	FN=cmds.file(q=True,sn=True).split('/')[-1].split('.')[0]
	SEL=cmds.ls(sl=True)

	for EACHSEL in SEL:
		EXNAME = FN+'_'+EACHSEL.replace('top_','')
		CHILD=cmds.listRelatives(EACHSEL,c=True,f=True)
		for EACH in CHILD:
			cmds.setAttr(EACH+'.export_name',EXNAME,type='string')

def postSetup():
	FN=cmds.file(q=True,sn=True).split('/')[-1].split('.')[0]
	SEL=cmds.ls(sl=True)


	MASSV=0

	for EACHSEL in SEL:
		#デブリの質量は１
		if '_db' in EACHSEL:
			MASSV=1

		EXNAME = FN+'_'+EACHSEL.replace('top_','')

		#ROOT
		CHILDS = cmds.listRelatives(EACHSEL+'|root',c=True,f=True)
		i=0
		for each in CHILDS:
			cmds.makeIdentity(each,a=True)
			cmds.rename(each,'%s_%02d'%(EXNAME,i))
			i+=1
		#COL
		CHILDS = cmds.listRelatives(EACHSEL+'|col',c=True,f=True)
		i=0
		for each in CHILDS:
			cmds.makeIdentity(each,a=True)
			toHavok(each,MASS=MASSV,SHAPETYPE=1)
			cmds.rename(each,'%s_%02d_hkx'%(EXNAME,i))
			i+=1

def LayoutA():
	cmds.columnLayout('MSG2_breakNodeRenamer.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_breakNodeRenamer',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.text(u'エキスポート用の設定をする。\nセットアップ済みの壊れ物ノードのトップを選択（複数選択可能）\nボタンを押すと、ファイル名と、トップノードの名前からroot,col内のエクストラアトリビュートの名前を正しい名前に変更')
	cmds.button(l='exportSetup',c=lambda *args:main())
	cmds.text(u'md0 _dbのセットアップを事後にする\nトップノードつかんでGO')
	cmds.button(l='postSetup',c=lambda *args:postSetup())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	