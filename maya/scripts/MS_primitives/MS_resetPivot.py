#! /usr/bin/python
# -*- coding: utf-8 -*-

#モデルを中心に持ってきたいときに使う
import maya.cmds as cmds

def reset():
	sl = cmds.ls( sl = True )
	cmds.select(cl=True)
	for i in sl:
		reset_exe(i)
		print i
		
def reset_exe(i):
	cmds.select(i)
	parent = cmds.listRelatives( i, p = True ,f=True)
	if parent != None:
		i0 = cmds.parent( i, w = True )[0]
	else:
		i0 = i
	a = cmds.xform( i0, q = True , ws = True, rp = True )
	p = cmds.getAttr( '%s.translate' % i0 )
	cmds.setAttr( '%s.translate' % i0, -a[0] + p[0][0], -a[1] + p[0][1], -a[2] + p[0][2] )
	cmds.makeIdentity( apply = True, t = 1 )
	cmds.setAttr( '%s.translate' % i0, a[0], a[1], a[2] )
	if parent != None:    
		cmds.parent( i0, parent )
		
	#スケールピボットの修正
	pv = cmds.xform( i, q = True, rp = True )
	cmds.xform( i, sp = pv )
	
def reset_root():
	for i in cmds.ls( sl = True ,dag =True,type='transform',l=True):
		reset_exe(i)			
	
def adjust( a ):
	sl = cmds.ls( sl = True )
	source = sl[0]
	target = sl[1]
	
	a = cmds.xform( source, q = True , ws = True, rp = True )
	cmds.xform( target, ws = True, rp = a )
	
	cmds.select( target )
	reset( 0 )
	
	
def pivot0(worldSpace = True):
	for i in cmds.ls( sl = True ):
		if not worldSpace:
			cmds.makeIdentity(i,a=True)
			cmds.xform(i,piv = (0,0,0),os=True)
		else:
			cmds.xform( i, rp = ( 0, 0, 0 ), ws = worldSpace )
			cmds.xform( i, sp = ( 0, 0, 0 ), ws = worldSpace )






