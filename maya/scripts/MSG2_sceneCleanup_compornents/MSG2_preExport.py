# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_preExport.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel

import s2000_tools.MSG2_LODTools.MS_polyUnite as MS_polyUnite
reload(MS_polyUnite)

import s2000_tools.MSG2_breakTools.MSG2_breakNodeUtil as MSG2_breakNodeUtil
reload(MSG2_breakNodeUtil)

def rootworkToRoot():
	#if cmds.objExists('|root'):
	#	print u'rootはもうあるから中断'
	#	return

	DUPED = cmds.duplicate('|root_work')
	cmds.rename(DUPED[0],'|temp')
	cmds.select('|temp',r=True)
	
	#スムースメッシュをコンバート

	mel.eval("performSmoothMeshPreviewToPolygon")
	cmds.delete('|temp',ch=True)

	cmds.file('D:/work/temp.ma',force=True,options="v=0;",typ="mayaAscii",es=True)
	cmds.delete('|temp')
	cmds.file('D:/work/temp.ma',i=True,type="mayaAscii",ignoreVersion=True,mergeNamespacesOnClash=True,rpr="temp",pr=True)

	#if cmds.objExists('|col'):
	#	cmds.delete('|col')

	#colision
	#DUPED=cmds.duplicate('|root')
	#cmds.select(DUPED,r=True)
	#UNITED=cmds.polyUnite()
	#cmds.group(em=True,n='col')
	#cmds.parent(UNITED,'col')

def colworkToCol():
	DUPED = cmds.duplicate('|col_work')
	cmds.select(DUPED[0],r=True)
	#
	UNITED=MS_polyUnite.MS_polyUnite()
	#
	cmds.hyperShade(a='lambert1')
	#
	try:
		cmds.polyColorSet(d=True)
	except:
		pass
	#
	MSG2_breakNodeUtil.toHavok(UNITED[0],MASS=0,SHAPETYPE=6)



def LayoutA():
	cmds.columnLayout('MSG2_preExport.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_preExport.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='rootworkToRoot',c=lambda *args:rootworkToRoot())
	cmds.button(l='colworkToCol',c=lambda *args:colworkToCol())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	

UI()