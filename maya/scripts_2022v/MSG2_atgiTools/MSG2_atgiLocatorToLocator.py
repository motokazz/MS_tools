# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_atgiLocatorToLocator.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import subprocess

def copyClipboard( text ):
	try:
		p = subprocess.Popen( ['clip'], stdin=subprocess.PIPE, shell=True )
		p.stdin.write( text )
		p.stdin.close()
 
		retcode = p.wait()
		return True
	except Exception, inst:
		return False

def copySelectionNameToClipboard():
	RET=[]
	SEL=cmds.ls(sl=True,sn=True)
	for each in SEL:
		RET.append(each)
	copyClipboard('\n'.join(RET))

def copySelectionAtgiToClipboard(SN=False):
	RET=[]
	SEL=cmds.ls(dag=True,type='GraviteAtgiLocatorNode',sl=True,l=True)
	for each in SEL:
		ATGINAME=cmds.getAttr(each+'.atgiFilename')
		if SN:
			ATGINAME=ATGINAME.replace('\\','/').split('/')[-1].split('.')[0]
		RET.append(ATGINAME)

	copyClipboard('\n'.join(RET))


def  atgiReplaceToLocator():
	SEL=cmds.ls(sl=True,l=True)
	for EACH in SEL:
		TRN=cmds.xform(EACH,q=True,t=True,ws=True)
		ROT=cmds.xform(EACH,q=True,ro=True,ws=True)
		
		PARENT=cmds.listRelatives(EACH,p=True,f=True)
		
		cmds.delete(EACH)

		LOC=cmds.spaceLocator()
		cmds.xform(LOC[0],t=TRN,ws=True)
		cmds.xform(LOC[0],ro=ROT,ws=True)
		LOC[0] = cmds.rename(LOC[0],EACH.split('|')[-1])
		if PARENT:
			cmds.parent(LOC[0],PARENT[0])


def main():
	SEL=cmds.ls(sl=True,l=True)
	i=1
	for EACH in SEL:
		SHAPE=cmds.listRelatives(EACH,s=True,f=True)
		NAME=cmds.getAttr(SHAPE[0]+'.atgiFilename')
		NAME=NAME.split('/')[-1].split('\\')[-1].split('.')[0]
		CHECK=True
		while(CHECK):
			if cmds.objExists(NAME+'_%d2'%i):
				i+=1
			else:
				CHECK=False
		NAME=NAME+'_%d2'%i
		TRN=cmds.xform(EACH,q=True,t=True,ws=True)
		ROT=cmds.xform(EACH,q=True,ro=True,ws=True)
		LOC=cmds.spaceLocator()
		cmds.xform(LOC,t=TRN,ws=True)
		cmds.xform(LOC,ro=ROT,ws=True)
		cmds.rename(LOC[0],NAME)

def LayoutA():
	cmds.columnLayout('MSG2_atgiLocatorToLocator.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_atgiLocatorToLocator.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.gridLayout(nc=2,cw=240)
	cmds.button(l=u'選択atgiの名前でロケーターを作成',c=lambda *args:main(),ann=u'選択atgiの名前でロケーターを作ります')
	cmds.button(l=u'選択atgiをロケーターに置換',c=lambda *args:atgiReplaceToLocator(),ann=u'選択atgiをロケーターに置換します')
	cmds.button(l=u'選択ノードの名前をクリップボードに送ります',c=lambda *args:copySelectionNameToClipboard(),ann=u'選択ノードの名前をクリップボードに送ります')
	cmds.button(l=u'選択Atgiのフルパスをクリップボードに送る',c=lambda *args:copySelectionAtgiToClipboard(),ann=u'選択Atgiのフルパスをクリップボードに送ります')
	cmds.button(l=u'選択Atgiのショートネームをクリップボードに送る',c=lambda *args:copySelectionAtgiToClipboard(SN=True),ann=u'選択Atgiのショートネームをクリップボードに送ります')
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	

