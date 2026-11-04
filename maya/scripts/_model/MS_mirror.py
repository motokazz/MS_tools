# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_mirror
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds
	
def opk():
	OBJ=cmds.ls(typ='mesh')
	for EACH in OBJ:
		if cmds.getAttr(EACH+'.opposite'):
			cmds.setAttr(EACH+'.opposite',0)
			cmds.polyNormal(EACH,normalMode=0,userNormalMode=0,ch=0)

def preDo(X=False,Y=False,Z=False,CP=''):
	#CP=cmds.checkBox('MS_mirror_CP',q=True,v=True)
	MARGE_FLAG=cmds.checkBox('MS_mirror_MARGE_FLAG',q=True,v=True)
	KEEP_ORIGINAL=cmds.checkBox('MS_mirror_KEEP_ORIGINAL',q=True,v=True)
	do(X=X,Y=Y,Z=Z,CP=CP
		,MARGE_FLAG=MARGE_FLAG
		,KEEP_ORIGINAL=KEEP_ORIGINAL
		)
	
def returnVector(X=False,Y=False,Z=False):
	RX=1.0
	RY=1.0
	RZ=1.0
	if X:
		RX=-1.0
	if Y:
		RY=-1.0
	if Z:
		RZ=-1.0
	print [RX,RY,RZ]
	return [RX,RY,RZ]
	
	
def mirrorCompornent(X=False,Y=False,Z=False,CP='',MARGE_FLAG=False):
	CP=cmds.checkBox('MS_mirror_CP',q=True,v=True)
	OBJ=cmds.ls(o=True,hl=True)
	cmds.xform(OBJ[0],cp=True)
	if CP:
		PIV=[0,0,0,0,0,0]
	else:
		PIV=cmds.xform(OBJ[0],q=True,piv=True,ws=True)
	SIZEVEC=returnVector(X=X,Y=Y,Z=Z)
	cmds.polyChipOff(dup=True,kft=True,ch=False,s=SIZEVEC,pvt=[PIV[3],PIV[4],PIV[5]])
	cmds.polyNormal(normalMode=3)
	cmds.polyMergeVertex(OBJ[0],d=0.001,am=1,ch=False)
	
	
	
	
def do(X=False,Y=False,Z=False,CP='',MARGE_FLAG=False,KEEP_ORIGINAL=False):
	
	if KEEP_ORIGINAL==True:
		DUP_A=cmds.duplicate(rr=True,rc=True)
	else:
		DUP_A=cmds.ls(sl=True)
	
	#center modyfy
	if CP=='obj':
		cmds.xform(DUP_A,cp=True)
	if CP=='world':
		cmds.xform(DUP_A,ws=True,piv=[0,0,0])
		cmds.makeIdentity(DUP_A,apply=True,t=True,r=True,s=True)
	#
	cmds.makeIdentity(DUP_A,apply=True,s=True)
	DUP_B=cmds.duplicate(DUP_A,rr=True,rc=True)
	
	#mirror&oppositeKill
	SIZEVEC=returnVector(X=X,Y=Y,Z=Z)
	cmds.xform(DUP_B,s=SIZEVEC)
	cmds.makeIdentity(DUP_B,apply=True,s=True)
	
	#oppositkil
	DUPED=cmds.listRelatives(DUP_B,typ='mesh',ad=True)
	print DUPED
	for EACH in DUPED:
		if cmds.attributeQuery('opposite',n=EACH,ex=True):
			if cmds.getAttr(EACH+'.opposite'):
				cmds.setAttr(EACH+'.opposite',0)
				cmds.polyNormal(EACH,normalMode=0,userNormalMode=0,ch=0)
	#marge
	if MARGE_FLAG==True:
		MARGE=[]
		MARGE.extend(DUP_A)
		MARGE.extend(DUP_B)
		
		NEWOBJ=cmds.polyUnite(MARGE,ch=False)
		cmds.polyMergeVertex(NEWOBJ,d=0.001,am=1,ch=False)
		
	

def layoutA(
	LABEL='MS_mirror'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.checkBox('MS_mirror_CP',l='center is WorldSpace',v=False)
	cmds.checkBox('MS_mirror_MARGE_FLAG',l='uniteObject',v=False)
	cmds.checkBox('MS_mirror_KEEP_ORIGINAL',l='keepOriginal',v=False)
	#world
	cmds.text(w=WIDTH-4,l='World')
	cmds.rowLayout(nc=3)
	cmds.button(w=(WIDTH-4)/3,l=u'X',c=lambda *args:preDo(X=True,CP='world'))
	cmds.button(w=(WIDTH-4)/3,l=u'Y',c=lambda *args:preDo(Y=True,CP='world'))
	cmds.button(w=(WIDTH-4)/3,l=u'Z',c=lambda *args:preDo(Z=True,CP='world'))
	cmds.setParent('..')
	cmds.rowLayout(nc=3)
	cmds.button(w=(WIDTH-4)/3,l=u'XY',c=lambda *args:preDo(X=True,Y=True,CP='world'))
	cmds.button(w=(WIDTH-4)/3,l=u'XZ',c=lambda *args:preDo(X=True,Z=True,CP='world'))
	cmds.button(w=(WIDTH-4)/3,l=u'YZ',c=lambda *args:preDo(Y=True,Z=True,CP='world'))
	cmds.setParent('..')
	cmds.button(w=WIDTH-4,l=u'XYZ',c=lambda *args:preDo(X=True,Y=True,Z=True,CP='world'))
	
	#obj
	cmds.text(w=WIDTH-4,l='OBJ')
	cmds.rowLayout(nc=3)
	cmds.button(w=(WIDTH-4)/3,l=u'X',c=lambda *args:preDo(X=True,CP='obj'))
	cmds.button(w=(WIDTH-4)/3,l=u'Y',c=lambda *args:preDo(Y=True,CP='obj'))
	cmds.button(w=(WIDTH-4)/3,l=u'Z',c=lambda *args:preDo(Z=True,CP='obj'))
	cmds.setParent('..')
	cmds.rowLayout(nc=3)
	cmds.button(w=(WIDTH-4)/3,l=u'XY',c=lambda *args:preDo(X=True,Y=True,CP='obj'))
	cmds.button(w=(WIDTH-4)/3,l=u'XZ',c=lambda *args:preDo(X=True,Z=True,CP='obj'))
	cmds.button(w=(WIDTH-4)/3,l=u'YZ',c=lambda *args:preDo(Y=True,Z=True,CP='obj'))
	cmds.setParent('..')
	cmds.button(w=WIDTH-4,l=u'XYZ',c=lambda *args:preDo(X=True,Y=True,Z=True,CP='obj'))
	
	#component
	cmds.text(w=WIDTH-4,l='COMPONENT')
	cmds.rowLayout(nc=3)
	cmds.button(w=(WIDTH-4)/3,l=u'X',c=lambda *args:mirrorCompornent(X=True))
	cmds.button(w=(WIDTH-4)/3,l=u'Y',c=lambda *args:mirrorCompornent(Y=True))
	cmds.button(w=(WIDTH-4)/3,l=u'Z',c=lambda *args:mirrorCompornent(Z=True))
	cmds.setParent('..')
	cmds.rowLayout(nc=3)
	cmds.button(w=(WIDTH-4)/3,l=u'XY',c=lambda *args:mirrorCompornent(X=True,Y=True))
	cmds.button(w=(WIDTH-4)/3,l=u'XZ',c=lambda *args:mirrorCompornent(X=True,Z=True))
	cmds.button(w=(WIDTH-4)/3,l=u'YZ',c=lambda *args:mirrorCompornent(Y=True,Z=True))
	cmds.setParent('..')
	cmds.button(w=WIDTH-4,l=u'XYZ',c=lambda *args:mirrorCompornent(X=True,Y=True,Z=True))
	

	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_mirror_main_window',q=True,ex=True):
		cmds.deleteUI('MS_mirror_main_window')
	cmds.window('MS_mirror_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_mirror_main_window')
	


