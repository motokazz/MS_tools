# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_moveKeyToParent
# 説明
#			子のアニメーションを親に移動
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel

def endKey():
	return cmds.findKeyframe(which='last')

def firstKey():
	return cmds.findKeyframe(which='first')

def core():
	attrDict={'.tx':0,'.ty':0,'.tz':0,'.rx':0,'.ry':0,'.rz':0,'.sx':1,'.sy':1,'.sz':1,'.visibility':True}
	obj = cmds.ls(sl=True,type='transform',l=True)
	keyName = ["." + k.rsplit("_",1)[1] for k in cmds.keyframe(obj[0],q=1,n=1)]
	for each in obj:
		prnt=cmds.listRelatives(each,p=True)

		cmds.cutKey([each+y for y in keyName],cl=True,t=(firstKey(),endKey()),f=(firstKey(),endKey()))
		
		cmds.pasteKey([prnt[0]+y for y in keyName],index=(firstKey(),firstKey()),o='merge')

		for eachAttr in attrDict.keys():
			cmds.setAttr(each+eachAttr,attrDict[eachAttr])

def layoutA():
	cmds.frameLayout('MS_moveKeyToParent_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'MS_moveKeyToParent',cll=True,cl=False)
	cmds.columnLayout()
	cmds.button(w=150,l=u'do',c=lambda *args:core())
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_moveKeyToParent_main_window',q=True,ex=True):
		cmds.deleteUI('MS_moveKeyToParent_main_window')
	cmds.window('MS_moveKeyToParent_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_moveKeyToParent_main_window')
	


