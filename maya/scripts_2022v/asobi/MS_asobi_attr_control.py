# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_asobi_attr_control
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds

def setExportability(exportability=True):
	TR=cmds.ls(sl=True,tr=True,l=True)
	for each in TR:
		
		FLAG=False

		if not cmds.attributeQuery('LoxFile',n=each,ex=True):
			FLAG=False
			
		if not cmds.attributeQuery('LevelMeshData',n=each,ex=True):
			FLAG=False

		lox=cmds.getAttr(each+'.LoxFile')

		if lox=='art_bg':
			FLAG=True

		if not FLAG:
			continue

		if cmds.attributeQuery('exportability',node=each,ex=True):
			cmds.deleteAttr(each,at='exportability')
		if exportability==False:
			cmds.addAttr(each,ln='exportability',at='bool')


def setTVVisible(num=0):
	TR=cmds.ls(sl=True,tr=True,l=True)
	for each in TR:
		if not cmds.attributeQuery('SceneType',n=each,ex=True):
			continue
		cmds.setAttr(each+'.SceneType',num)

def countArtBg():

	TR=cmds.ls(tr=True,l=True)
	RES=[]
	for each in TR:
		if not cmds.attributeQuery('LoxFile',node=each,ex=True):
			continue
		if cmds.getAttr(each+'.LoxFile')=='art_bg':
			RES.append(each)
			
	print len(RES)

def odx2afn():
	trn = cmds.ls(sl=True,dag=True,tr=True,l=True)
	shp = cmds.ls(sl=True,dag=True,s=True,l=True)

	odxn = cmds.getAttr(trn[0]+'.Odx')
	nafn = 'graphic\\multi_platformer\\bg\\intermediates\\'+odxn+'.atgi'

	cmds.setAttr(shp[0]+'.filename',nafn,type='string')

def attrCheck(attr='HasCollision',var=False):
	LIST = []

	TRN = cmds.ls(type='transform',l=True)
	for each in TRN:
		try:
			TEMPVAR = cmds.getAttr(each + '.' + attr)
			if TEMPVAR == var:
				LIST.append(each)
		except:
			pass

	cmds.select(LIST,r=True)



def LayoutA():
	cmds.frameLayout('MS_asobi_attr_control_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_asobi_attr_control',cll=True,cl=False)
	cmds.columnLayout('MS_asobi_attr_control_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_asobi_attr_control',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='showTV',c=lambda *args:setTVVisible(num=0))
	cmds.button(l='hideTV',c=lambda *args:setTVVisible(num=1))
	
	cmds.separator(w=200)
	cmds.button(l='exportable',c=lambda *args:setExportability(exportability=True))
	cmds.button(l='not exportable',c=lambda *args:setExportability(exportability=False))

	cmds.separator(w=200)
	cmds.button(l='countArtBg',c=lambda *args:countArtBg())

	cmds.separator(w=200)
	cmds.button(l='attrCheck',c=lambda *args:attrCheck())

	cmds.separator(w=200)
	cmds.button(l='odx>atgifilename',c=lambda *args:odx2afn())

	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_asobi_attr_control_window',q=True,ex=True):
		cmds.deleteUI('MS_asobi_attr_control_window')
	cmds.window('MS_asobi_attr_control_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_asobi_attr_control_window')
	