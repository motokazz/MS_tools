# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_copyAnims
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds
	
def do():
	OBJA=cmds.textField('MS_copyAnims_textField_a',q=True,tx=True)
	OBJA_LIST=OBJA.split(',')
	OBJB=cmds.textField('MS_copyAnims_textField_b',q=True,tx=True)
	OBJB_LIST=OBJB.split(',')
	num=0
	for EACH in OBJA_LIST:
		KF=cmds.findKeyframe(EACH,c=True)
		print KF
		if KF:
			print EACH
			cmds.copyKey(EACH)
			print OBJB_LIST[num]
			cmds.pasteKey(OBJB_LIST[num])
		num+=1



def getA():
	OBJ=cmds.ls(sl=True)
	cmds.textField('MS_copyAnims_textField_a',e=True,tx=','.join(OBJ))
def getB():
	OBJ=cmds.ls(sl=True)
	cmds.textField('MS_copyAnims_textField_b',e=True,tx=','.join(OBJ))

def layoutA(
	LABEL='MS_copyAnims'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.rowLayout(nc=2)
	cmds.textField(LABEL+'_textField_a',w=WIDTH-4,tx='')
	cmds.button(l='get',w=30,c=lambda *args:getA())
	cmds.setParent('..')
	cmds.rowLayout(nc=2)
	cmds.textField(LABEL+'_textField_b',w=WIDTH-4,tx='')
	cmds.button(l='get',w=30,c=lambda *args:getB())
	cmds.setParent('..')
	
	cmds.button(w=WIDTH-4,l=u'do',c=lambda *args:do())
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_copyAnims_main_window',q=True,ex=True):
		cmds.deleteUI('MS_copyAnims_main_window')
	cmds.window('MS_copyAnims_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_copyAnims_main_window')
	

