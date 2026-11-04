# -*- coding:utf-8 -*-
import maya.cmds as cmds

import ui.MS_window as MS_window
reload(MS_window)

win=MS_window.main

class layoutsample(win):

	def __init__(self,*av):
		win.__init__(self,*av)

	def columnLayout(self):
		cl=cmds.columnLayout( columnAttach=('both', 5), rowSpacing=10, columnWidth=250 )
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.setParent( '..' )
		return cl

	def tabLayout(self):
		tabs=cmds.tabLayout()

		child1 = cmds.columnLayout()
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.setParent( '..' )

		child2 = cmds.rowColumnLayout(numberOfColumns=2)
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.setParent( '..' )

		cmds.tabLayout( tabs, edit=True, tabLabel=((child1, 'One'), (child2, 'Two')) )

		cmds.setParent('..')

		return tabs

	def flowLayout(self):
		fl=cmds.flowLayout( columnSpacing=10 )
	 	cmds.button()
		cmds.button()
		cmds.button()
		cmds.button()
	  	cmds.setParent('..')
	  	return fl

	def formLayout(self):
		
		form = cmds.formLayout(numberOfDivisions=100)
		b1 = cmds.button()
		b2 = cmds.button()

		column = cmds.columnLayout()
		cmds.button()
		cmds.button()
		cmds.button()
		
		cmds.setParent('..')
		cmds.setParent('..')

		cmds.formLayout( form, edit=True, 
			attachForm=[
				(b1, 'top', 5), (b1, 'left', 5)
				, (b2, 'left', 5), (b2, 'bottom', 5), (b2, 'right', 5)
				, (column, 'top', 5)
				, (column, 'right', 5)
			 ], 
			 attachControl=[(b1, 'bottom', 5, b2), (column, 'bottom', 5, b2)]
			 , attachPosition=[(b1, 'right', 5, 75), (column, 'left', 0, 75)]
			 , attachNone=(b2, 'top') )
		

		return form

	def frameLayout(self):
		sl=cmds.scrollLayout()
		cmds.columnLayout( adjustableColumn=True )
		
		cmds.frameLayout( label='Buttons', borderStyle='in' )
		cmds.columnLayout()
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.setParent( '..' )
		cmds.setParent( '..' )

		cmds.frameLayout( label='Scroll Bars', borderStyle='out' )
		cmds.columnLayout()
		cmds.intSlider()
		cmds.intSlider()
		cmds.intSlider()
		cmds.setParent( '..' )
		cmds.setParent( '..' )

		cmds.frameLayout( label='Fields', borderStyle='etchedIn' )
		cmds.columnLayout()
		cmds.intField()
		cmds.intField()
		cmds.intField()
		cmds.setParent( '..' )
		cmds.setParent( '..' )

		cmds.frameLayout( label='Check Boxes', borderStyle='etchedOut' )
		cmds.columnLayout()
		cmds.checkBox()
		cmds.checkBox()
		cmds.checkBox()
		cmds.setParent( '..' )
		cmds.setParent( '..' )

		cmds.setParent( '..' )
		cmds.setParent( '..' )

		return sl

	def gridLayout(self):
		gl=cmds.gridLayout( numberOfColumns=2, cellWidthHeight=(50, 50) )
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.setParent( '..' )
		return gl

	def menuBarLayout(self):
		#    Create first menu bar layout.
		#
		menuBarLayout = cmds.columnLayout()
		cmds.menuBarLayout()
		cmds.menu( label='File' )
		cmds.menuItem( label='New' )
		cmds.menuItem( label='Open' )
		cmds.menuItem( label='Close' )

		cmds.menu( label='Help', helpMenu=True )
		cmds.menuItem( label='About...' )

		cmds.columnLayout()
		cmds.button( label='Add Menu', command=('cmds.menu(parent=\"' + menuBarLayout + '\"); cmds.menuItem()') )
		cmds.setParent( '..' )
		cmds.setParent( '..' )

		cmds.separator( height=10, style='none' )

		#    Create a second menu bar layout.
		#
		cmds.menuBarLayout()
		cmds.menu( label='Edit' )
		cmds.menuItem( label='Cut' )
		cmds.menuItem( label='Copy' )
		cmds.menuItem( label='Paste' )

		cmds.menu( label='View' )
		cmds.menuItem( label='Fonts...' )
		cmds.menuItem( label='Colors...' )

		cmds.columnLayout()
		cmds.text( label='Add some controls here.' )
		cmds.setParent( '..' )
		cmds.setParent( '..' )

		cmds.setParent( '..' )

		return menuBarLayout

	def paneLayout(self):
		pl=cmds.paneLayout( configuration='quad' )
		cmds.button()
		cmds.textScrollList( append=['one', 'two', 'three'] )
		cmds.scrollField()
		cmds.scrollLayout()
		cmds.columnLayout()
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.setParent( '..' )
		cmds.setParent( '..' )
		cmds.setParent( '..' )
		#cmds.setParent( '..' )
		#cmds.setParent( '..' )
		return pl

	def rowColumnLayout(self):
		sl=cmds.scrollLayout()

		cmds.rowColumnLayout( numberOfColumns=1 )
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.setParent('..')

		cmds.rowColumnLayout( numberOfRows=1 )
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.setParent('..')

		cmds.rowColumnLayout( numberOfColumns=3, columnWidth=[(1, 60), (2, 80), (3, 100)] )
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.setParent('..')

		cmds.rowColumnLayout( numberOfRows=2, rowHeight=[(1, 30), (2, 60)] )
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.button()
		cmds.setParent('..')

		cmds.setParent('..')

		return sl

	def rowLayout(self):
		rl=cmds.rowLayout( numberOfColumns=3
			, columnWidth3=(80, 75, 150)
			, adjustableColumn=2
			, columnAlign=(1, 'right')
			, columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)]
			)
		cmds.text()
		cmds.intField()
		cmds.intSlider()
		cmds.setParent('..')

		return rl

	def scrollLayout(self):
		scrollLayout = cmds.scrollLayout(
			horizontalScrollBarThickness=16,
			verticalScrollBarThickness=16)
		cmds.rowColumnLayout( numberOfColumns=3 )

		for index in range(10):
			cmds.text()
			cmds.intField()
			cmds.intSlider()
		cmds.setParent('..')
		cmds.setParent('..')

		value = cmds.scrollLayout(scrollLayout, query=True, scrollAreaValue=True)
		top = value[0]
		left = value[1]
		return scrollLayout

	def shelfLayout(self):
		tl=cmds.tabLayout()

		sh1 = cmds.shelfLayout("First", style="iconOnly",
		                                           backgroundColor=(.9, .2, .2))
		sh1b1 = cmds.shelfButton(image1="textureEditor.png",
			label="textureEditor", annotation="textureEditor",
			command="TextureViewWindow",
			imageOverlayLabel="1",
			overlayLabelColor=(.1, .1, .1),
			overlayLabelBackColor=(1, .25, .25, .5))
		sh1b2 = cmds.shelfButton(image1="undo.png",
			label="undo", annotation="undo",
			command="undo",
			imageOverlayLabel="1",
			overlayLabelColor=(.1, .1, .1),
			overlayLabelBackColor=(1, .25, .25, .5))
		sh1b3 = cmds.shelfButton(image1="redo.png",
			label="redo", annotation="redo",
			command="redo",
			imageOverlayLabel="1",
			overlayLabelColor=(.1, .1, .1),
			overlayLabelBackColor=(1, .25, .25, .5))
		cmds.setParent('..')

		sh2 = cmds.shelfLayout("Second", style="textOnly",
		                                           backgroundColor=(.2, .9, .2))
		sh2b1 = cmds.shelfButton(image1="textureEditor.png",
			label="textureEditor", annotation="textureEditor",
			command="TextureViewWindow",
			imageOverlayLabel="2",
			overlayLabelColor=(.1, .1, .1),
			overlayLabelBackColor=(.25, 1, .25, .5))
		sh2b2 = cmds.shelfButton(image1="undo.png",
			label="undo", annotation="undo",
			command="undo",
			imageOverlayLabel="2",
			overlayLabelColor=(.1, .1, .1),
			overlayLabelBackColor=(.25, 1, .25, .5))
		sh2b3 = cmds.shelfButton(image1="redo.png",
			label="redo", annotation="redo",
			command="redo",
			imageOverlayLabel="2",
			overlayLabelColor=(.1, .1, .1),
			overlayLabelBackColor=(.25, 1, .25, .5))
		cmds.setParent('..')

		sh3 = cmds.shelfLayout("Third", style="iconAndTextHorizontal",
		                                           backgroundColor=(.2, .2, .9))
		sh3b1 = cmds.shelfButton(image1="textureEditor.png",
			label="textureEditor", annotation="textureEditor",
			command="TextureViewWindow",
			imageOverlayLabel="3",
			overlayLabelColor=(.1, .1, .1),
			overlayLabelBackColor=(.25, .25, 1, .5))
		sh3b2 = cmds.shelfButton(image1="undo.png",
			label="undo", annotation="undo",
			command="undo",
			imageOverlayLabel="3",
			overlayLabelColor=(.1, .1, .1),
			overlayLabelBackColor=(.25, .25, 1, .5))
		sh3b3 = cmds.shelfButton(image1="redo.png",
			label="redo", annotation="redo",
			command="redo",
			imageOverlayLabel="3",
			overlayLabelColor=(.1, .1, .1),
			overlayLabelBackColor=(.25, .25, 1, .5))
		cmds.setParent('..')


		sh4 = cmds.shelfLayout("Fourth", style="iconAndTextVertical")
		sh4b1 = cmds.shelfButton(image1="textureEditor.png",
			label="textureEditor", annotation="textureEditor",
			command="TextureViewWindow",
			imageOverlayLabel="4",
			overlayLabelColor=(.1, .1, .1),
			overlayLabelBackColor=(.25, 1, 1, .5))
		sh4b2 = cmds.shelfButton(image1="undo.png",
			label="undo", annotation="undo",
			command="undo",
			imageOverlayLabel="4",
			overlayLabelColor=(.1, .1, .1),
			overlayLabelBackColor=(.25, 1, 1, .5))
		sh4b3 = cmds.shelfButton(image1="redo.png",
			label="redo", annotation="redo",
			command="redo",
			imageOverlayLabel="4",
			overlayLabelColor=(.1, .1, .1),
			overlayLabelBackColor=(.25, 1, 1, .5))
		cmds.setParent('..')

		cmds.setParent('..')

		return tl

	def shelfTabLayout(self):
		stl=cmds.shelfTabLayout( 'mainShelfTab', image='smallTrash.png', imageVisible=True )
		cmds.shelfLayout( 'Dynamics' )
		cmds.setParent( '..' )
		cmds.shelfLayout( 'Rendering' )
		cmds.setParent( '..' )
		cmds.shelfLayout( 'Animation' )
		cmds.setParent( '..' )
		return stl

#

	def layoutA(self):
		tabs=cmds.tabLayout()

		txa=self.columnLayout()
		txb=self.flowLayout()
		txc=self.formLayout()
		txd=self.frameLayout()
		txe=self.gridLayout()
		txf=self.menuBarLayout()
		txg=self.paneLayout()
		txh=self.rowColumnLayout()
		txi=self.rowLayout()
		txj=self.scrollLayout()
		txk=self.shelfLayout()
		txl=self.shelfTabLayout()

		cmds.tabLayout( tabs, edit=True,tabLabel=(
			(txa, 'columnLayout')
			,(txb,'flowLayout')
			,(txc,'formLayout')
			,(txd,'frameLayout')
			,(txe,'gridLayout')
			,(txf,'menuBarLayout')
			,(txg,'paneLayout')
			,(txh,'rowColumnLayout')
			,(txi,'rowLayout')
			,(txj,'scrollLayout')
			,(txk,'shelfLayout')
			,(txl,'shelfTabLayout')
			))

#win.layoutA=allOfTab
los=layoutsample()

los.UI()
