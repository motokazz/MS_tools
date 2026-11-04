# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_centerResetter
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds

#子供を考慮しないCenterPivot
def centerPivot(NODE):
	CHILDS=cmds.listRelatives(NODE,c=True,type='transform',f=True)
	VISLIST=[]
	if CHILDS:
		for EACHCHILD in CHILDS:
			VISLIST.append([EACHCHILD,cmds.getAttr(EACHCHILD+'.visibility')])
		cmds.setAttr(EACHCHILD+'.visibility',False)
	
	cmds.xform(NODE,cp=True)
	
	for EACH in VISLIST:
		cmds.setAttr(EACH[0]+'.visibility',EACH[1])
	
##### 移動値を正規化コア #####
def centerResetter(node):
	tmr=cmds.getAttr(node+'.transMinusRotatePivot')[0]
	cmds.xform(node,t=[tmr[0],tmr[1],tmr[2]])
	cmds.makeIdentity(node,a=True,t=True,r=False,s=False)
	cmds.xform(t=[-tmr[0],-tmr[1],-tmr[2]])

def resetTransform(node):
	cmds.xform(node,t=[0,0,0],ro=[0,0,0],s=[1,1,1])

def centerPivot(node):
	

def MS_centerResetter(MODE,NODE=[]):
	if not NODE:
		NODE=cmds.ls(l=True,typ='transform',sl=True)
	
	for EACH in NODE:
		SHAPE=cmds.listRelatives(EACH,s=True)
		
		if SHAPE:
			NODE_TYPE=cmds.nodeType(SHAPE[0])
		else:
			NODE_TYPE='group'
			
		if NODE_TYPE=='ToroLocatorNode':#TOROロケーター対策
			continue
		
		if NODE_TYPE=='locator':#ロケーター対策:centerPivot強制
			centerPivot(EACH)
		if NODE_TYPE=='group':#group対策:centerPivot強制
			centerPivot(EACH)
			
		if MODE:#MODE=Trueはピボット位置をセンターにする。
			centerPivot(EACH)
			
		#トランスフォームノードにコネクション（アニメーション）があったら処理しない
		#FCURV=cmds.findKeyframe(EACH,c=True,at=['tx','ty','tz','rx','ry','rz','sx','sy','sz'])
		#if FCURV:
		#	print 'catch',EACH
		#	continue
		
		obj_a_tx=EACH+'.tx'
		obj_a_ty=EACH+'.ty'
		obj_a_tz=EACH+'.tz'
		
		obj_a_rptx=EACH+'.transMinusRotatePivotX'
		obj_a_rpty=EACH+'.transMinusRotatePivotY'
		obj_a_rptz=EACH+'.transMinusRotatePivotZ'
		
		orgx=cmds.getAttr(obj_a_tx)
		orgy=cmds.getAttr(obj_a_ty)
		orgz=cmds.getAttr(obj_a_tz)
		
		flpx=cmds.getAttr(obj_a_rptx)
		flpy=cmds.getAttr(obj_a_rpty)
		flpz=cmds.getAttr(obj_a_rptz)
		
	
		GAP_X=orgx-flpx
		GAP_Y=orgy-flpy
		GAP_Z=orgz-flpz
		
		#キーフレーム処理
		FC=cmds.findKeyframe(EACH,c=True,at=['tx','ty','tz'])
		if FC:
			for EACH_FC in FC:
				if 'translateX' in EACH_FC:
					cmds.keyframe(EACH_FC,e=True,iub=True,r=True,o='over',vc=GAP_X)
				if 'translateY' in EACH_FC:
					cmds.keyframe(EACH_FC,e=True,iub=True,r=True,o='over',vc=GAP_Y)
				if 'translateZ' in EACH_FC:
					cmds.keyframe(EACH_FC,e=True,iub=True,r=True,o='over',vc=GAP_Z)
		else:
			try:
				cmds.setAttr(obj_a_tx,flpx)
				cmds.setAttr(obj_a_ty,flpy)
				cmds.setAttr(obj_a_tz,flpz)
				
				cmds.makeIdentity(EACH,apply=True,t=1)
				
				cmds.setAttr(obj_a_tx,GAP_X)
				cmds.setAttr(obj_a_ty,GAP_Y)
				cmds.setAttr(obj_a_tz,GAP_Z)
			except:
				print 'skip'
		cmds.xform(EACH,ztp=True)
		
		shapeLocalParam(EACH)
		
		
		
def shapeLocalParam(NODE):

	SHAPE=cmds.listRelatives(NODE,s=True,f=True)
	
	if not SHAPE:
		return
	
	CHILDS=cmds.listRelatives(NODE,c=True,type='transform',f=True)
	if not CHILDS:
		return
	
	
	NCHILDS=cmds.parent(CHILDS,w=True)
	
	for EACH in SHAPE:
		if cmds.attributeQuery('localPositionX',n=EACH,ex=True):
			VAR=cmds.getAttr(EACH+'.localPositionX')
			cmds.setAttr(EACH+'.localPositionX',0)
			cmds.xform(NODE,r=True,t=(VAR,0,0))
		if cmds.attributeQuery('localPositionY',n=EACH,ex=True):
			VAR=cmds.getAttr(EACH+'.localPositionY')
			cmds.setAttr(EACH+'.localPositionY',0)
			cmds.xform(NODE,r=True,t=(0,VAR,0))
		if cmds.attributeQuery('localPositionZ',n=EACH,ex=True):
			VAR=cmds.getAttr(EACH+'.localPositionZ')
			cmds.setAttr(EACH+'.localPositionZ',0)
			cmds.xform(NODE,r=True,t=(0,0,VAR))
		if cmds.attributeQuery('localScaleX',n=EACH,ex=True):
			VAR=cmds.getAttr(EACH+'.localScaleX')
			cmds.setAttr(EACH+'.localScaleX',1)
			cmds.xform(NODE,r=True,s=(VAR,1,1))
		if cmds.attributeQuery('localScaleY',n=EACH,ex=True):
			VAR=cmds.getAttr(EACH+'.localScaleY')
			cmds.setAttr(EACH+'.localScaleY',1)
			cmds.xform(NODE,r=True,s=(1,VAR,1))
		if cmds.attributeQuery('localScaleZ',n=EACH,ex=True):
			VAR=cmds.getAttr(EACH+'.localScaleZ')
			cmds.setAttr(EACH+'.localScaleZ',1)
			cmds.xform(NODE,r=True,s=(1,1,VAR))
		
	
	cmds.parent(NCHILDS,NODE)
	
	
def groupCenterResetter(MODE):
	NODE=cmds.ls(l=True,typ='transform',sl=True)
	for EACH in NODE:
		MS_centerResetter(MODE,NODE=[EACH])
		CHILDS=cmds.listRelatives(ad=True,type='transform',f=True)
		CHILDS.reverse()
		if CHILDS:
			for EACHCHILD in CHILDS:
				MS_centerResetter(MODE,NODE=[EACHCHILD])
				
				
##### UI移動値を正規化 #####

def layoutA(CL=False,BGC=[0.2,0.2,0.2]):
	cmds.frameLayout('MS_centerResetter_frameLayout',w=217,bgc=BGC,fn='boldLabelFont',l=u'MS_centerResetter',cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(w=217,bgc=[0.7,0.7,0.7],l=u'ピボット対策')
	cmds.button(w=200,h=40,l=u'ピボットをオブジェクトの中心にしてから\n移動値を移動値を正規化する',bgc=[0.8,0.9,0.8],c=lambda *args:MS_centerResetter(1))
	cmds.button(w=200,h=40,l=u'移動値を正規化',bgc=[0.9,0.9,0.8],c=lambda *args:MS_centerResetter(0))
	cmds.button(w=200,h=40,l=u'階層全部移動値を正規化',bgc=[0.9,0.9,0.8],c=lambda *args:groupCenterResetter(0))
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_centerResetter_main_window',q=True,ex=True):
		cmds.deleteUI('MS_centerResetter_main_window')
	cmds.window('MS_centerResetter_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_centerResetter_main_window')
	


