#! /usr/bin/python
# -*- coding: utf-8 -*-

#モデルを中心に持ってきたいときに使う
import maya.cmds as cmds

class main:
	def __init__( self ):				
		self.VERSION = 'v2011-1117'
		self.LASTUPDATE = '2011/1117'
		self.SCRIPT_NAME = 'NIKO2resetPivot'
		self.DOCK_NAME = u"リセットピボット"

	def UI( self ):
		if cmds.window( '%sWin' % self.SCRIPT_NAME, ex = True ) == True :
			cmds.deleteUI( '%sWin' % self.SCRIPT_NAME )
			
		window = cmds.window( '%sWin' % self.SCRIPT_NAME , w = 150 , h = 50 , menuBar = True , title = self.VERSION )		
	
		cmds.columnLayout()	
		cmds.button( l = u'ピボットのリセット' , c = self.reset , w = 150, ann = u'複数選択できます' )	
		cmds.button( l = u'ピボットを０にする(ルート選択)' , c = self.reset_root , ann = u'ルートノードを選択して実行して複数のピボットをリセットします。', w = 150 )			
		cmds.button( l = u'別モデルに合わせる' , c = self.adjust , ann = u'ソース、ターゲットの順に選択して実行', w = 150 )	
		cmds.button( l = u'ピボットを０にする' , c = self.pivot0 , ann = u'ノードを選択して実行', w = 150 )	
		
		cmds.showWindow( window )
	
	def reset( self , a ):
		sl = cmds.ls( sl = True )
		cmds.select(cl=True)
		for i in sl:
			self.reset_exe(i)
			print i
			
	def reset_exe(self,i):
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
		
	def reset_root( self , a ):
		for i in cmds.ls( sl = True ,dag =True,type='transform',l=True):
			self.reset_exe(i)			
		
		
		
		
	def adjust( self , a ):
		sl = cmds.ls( sl = True )
		source = sl[0]
		target = sl[1]
		
		a = cmds.xform( source, q = True , ws = True, rp = True )
		cmds.xform( target, ws = True, rp = a )
		
		cmds.select( target )
		self.reset( 0 )
		
		
	def pivot0( self, a ):
		for i in cmds.ls( sl = True ):
			cmds.xform( i, rp = ( 0, 0, 0 ), ws = True )
			cmds.xform( i, sp = ( 0, 0, 0 ), ws = True )






