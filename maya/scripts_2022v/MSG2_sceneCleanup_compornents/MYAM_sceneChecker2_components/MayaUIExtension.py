#-*- coding:UTF-8 -*-

#*******************************************************************************
'''

Tool Name     : MayaUIExtension
Description   : MayaUIを扱いやすくするためのライブラリ

Copyright     : (c)Michiyoshi Yamabe
Author Name   : Michiyoshi Yamabe
Contact       : Yamabe.Michiyoshi@me.com

------------------------------------
----- Using external libraries -----
------------------------------------
maya

-------------------------
----- UPDATE RECORD -----
-------------------------
[date] details

'''
#*******************************************************************************

import maya.cmds as cmds

import MayaUIBasic

class WindowEx( MayaUIBasic.Window ):

  def __init__( self , *args , **kwargs ):
    MayaUIBasic.Window.__init__( self , *args , **kwargs )

  def show( self ):
    cmds.showWindow( self.name )


class TextScrollListEx( MayaUIBasic.TextScrollList ):

  def __init__( self , *args , **kwargs ):
    MayaUIBasic.TextScrollList.__init__( self , *args , **kwargs )

  def set( self , setItems ):
    self.clear()
    self.add( setItems )

  def add( self , addItems ):
    for addItem in addItems:
      self.append = addItem

  def replace( self , srcItem , dstItem ):
    existItems = self.allItems

    if existItems != None:
      counter = 0
      for existItem in existItems:
        if srcItem == existItem:
          self.removeIndexedItem = counter + 1
          self.appendPosition = [ counter + 1 , dstItem ]
        counter += 1

  def delete( self , deleteItem ):
    existItems = self.allItems
    deleteIndices = []

    if existItems != None:
      counter = 0
      for existItem in existItems:
        if existItem == deleteItem:
          deleteIndices.append( counter + 1 )
        counter += 1
    self.removeIndexedItem = sorted( deleteIndices , reverse = 1 )

  def clear( self ):
    TSLItems = self.allItems
    if TSLItems != None:
      self.removeAll = 1

  def sort( self , reverse = 0 ):
    TSLItems = self.allItems
    if TSLItems != None:
      self.set( sorted( TSLItems , reverse = reverse ) )


class FormLayoutEx( MayaUIBasic.FormLayout ):

  def __init__( self , *args , **kwargs ):
    MayaUIBasic.FormLayout.__init__( self , *args , **kwargs )

  af = property( MayaUIBasic.FormLayout.getattachForm             , MayaUIBasic.FormLayout.setattachForm )
  aof = property( MayaUIBasic.FormLayout.getattachOppositeForm    , MayaUIBasic.FormLayout.setattachOppositeForm )
  ac = property( MayaUIBasic.FormLayout.getattachControl          , MayaUIBasic.FormLayout.setattachControl )
  aoc = property( MayaUIBasic.FormLayout.getattachOppositeControl , MayaUIBasic.FormLayout.setattachOppositeControl )
  ap = property( MayaUIBasic.FormLayout.getattachPosition         , MayaUIBasic.FormLayout.setattachPosition )
  an = property( MayaUIBasic.FormLayout.getattachNone             , MayaUIBasic.FormLayout.setattachNone )


class ProgressBarEx( MayaUIBasic.ProgressBar ):

  def __init__( self , *args , **kwargs ):
    MayaUIBasic.ProgressBar.__init__( self , *args , **kwargs )

  def reset( self ):
    self.progress = 0
    self.endProgress = 1


class OptionMenuEx( MayaUIBasic.OptionMenu ):

  def __init__( self , *args , **kwargs ):
    MayaUIBasic.OptionMenu.__init__( self , *args , **kwargs )

  def set( self , setItems ):
    self.clear()
    if setItems != [] and setItems != None:
      for item in setItems:
        cmds.menuItem( parent = self.name , label = item )

  def add( self , addItems = [] ):
    for addItem in addItems:
      cmds.menuItem( parent = self.name , label = addItem )

  def replace( self , srcLabel , dstLabel ):
    existItems = cmds.optionMenu( self.name , q = 1 , itemListLong = 1 )
    if existItems != None:
      for existItem in existItems:
        menuLabel = cmds.menuItem( existItem , q = 1 , label = 1 )
        if menuLabel == srcLabel:
          cmds.menuItem( existItem , e = 1 , label = dstLabel )

  def delete( self , deleteLabel ):
    existItems = cmds.optionMenu( self.name , q = 1 , itemListLong = 1 )
    if existItems != None:
      for existItem in existItems:
        menuLabel = cmds.menuItem( existItem , q = 1 , label = 1 )
        if menuLabel == deleteLabel:
          cmds.deleteUI( existItem , menuItem = 1 )

  def clear( self ):
    existItems = cmds.optionMenu( self.name , q = 1 , itemListLong = 1 )

    if existItems != None:
      for existItem in existItems:
        cmds.deleteUI( existItem , menuItem = 1 )

  def getAllLabels( self ):
    existItems = cmds.optionMenu( self.name , q = 1 , itemListLong = 1 )
    labelList = []

    for item in existItems:
      labelList.append( cmds.menuItem( item , q = 1 , label = 1 ) )

    return labelList


class PopupMenuEx( MayaUIBasic.PopupMenu ):

  def __init__( self , *args , **kwargs ):
    MayaUIBasic.PopupMenu.__init__( self , **args )


class FloatSliderGroup( object ):

  def __init__( self ):
    self.rowLayout = MayaUIBasic.RowLayout( numberOfColumns = 3 )
    self.text = Text()
    self.floatSlider = FloatSlider()
    self.floatField = FloatField()
    cmds.setParent( '..' )

    self.floatSlider.dragCommand = self.drag_floatSlider
    self.floatField.enterCommand = self.enter_floatField
    self.floatField.dragCommand = self.drag_floatField

  def drag_floatField( self , *args ):
    self.change_floatSlider()

  def enter_floatField( self , *args ):
    self.change_floatSlider()

  def drag_floatSlider( self , *args ):

    self.change_floatField()

  ##

  def change_floatField( self ):
    self.floatField.value = self.floatSlider.value

  def change_floatSlider( self ):
    self.floatSlider.value = self.floatField.value


class IntSliderGroup( object ):

  def __init__( self ):
    self.rowLayout = MayaUIBasic.RowLayout( numberOfColumns = 3 )
    self.text = Text()
    self.intSlider = IntSlider()
    self.intField = IntField()
    cmds.setParent( '..' )

    self.intSlider.dragCommand = self.drag_intSlider
    self.intField.enterCommand = self.enter_intField
    self.intField.dragCommand = self.drag_intField

  def drag_intField( self , *args ):
    self.change_intSlider()

  def enter_intField( self , *args ):
    self.change_intSlider()

  def drag_intSlider( self , *args ):
    self.change_intField()

  ##

  def change_intField( self ):
    self.intField.value = self.intSlider.value

  def change_intSlider( self ):
    self.intSlider.value = self.intField.value


class RadioButtonGrpEx( MayaUIBasic.RadioButtonGrp ):

  def __init__( self , *args , **kwargs ):
    MayaUIBasic.RadioButtonGrp.__init__( self , *args , **kwargs )





class HUniformLayout( FormLayoutEx ):

  def __init__( self ):
    FormLayoutEx.__init__( self )
    self.margin  = 0
    self.spacing = 0
    self.childResizable = 0
    self.numberOfDivisions = 100

  def arrange( self ):
    children = self.childArray
    childNum = len( children )

    spanSize = 100 / childNum
    spanGap  = 100 % childNum

    leftOffset  = 0
    rightOffset = 0

    counter = 0

    for child in children:
      leftPos  = spanSize * counter
      rightPos = spanSize * ( counter + 1 )

      if counter == 0:
        leftOffset  = self.margin
        rightOffset = self.spacing / 2

      elif counter == ( childNum - 1 ):
        leftOffset  = self.spacing / 2
        rightOffset = self.margin
        rightPos += spanGap

      else:
        leftOffset  = self.spacing / 2
        rightOffset = self.spacing / 2

      ## Adjustable Height
      if self.childResizable == 0:
        self.af = [ ( child , "top"    , 0 ) ]
        self.ap = [ ( child , "left"   , leftOffset  , leftPos ) ]
        self.ap = [ ( child , "right"  , rightOffset , rightPos ) ]
        self.an = [ ( child , "bottom" ) ]

      else:
        self.ap = [ ( child , "top"    , 0 , 0 ) ]
        self.ap = [ ( child , "left"   , leftOffset  , leftPos ) ]
        self.ap = [ ( child , "right"  , rightOffset , rightPos ) ]
        self.ap = [ ( child , "bottom" , 0 , 100 ) ]

      counter += 1

class VUniformLayout( FormLayoutEx ):

  def __init__( self ):
    FormLayoutEx.__init__( self )
    self.margin  = 0
    self.spacing = 0
    self.childResizable = 0
    self.numberOfDivisions = 100

  def arrange( self ):
    children = self.childArray
    childNum = len( children )

    spanSize = 100 / childNum
    spanGap  = 100 % childNum

    topOffset    = 0
    bottomOffset = 0

    counter = 0

    for child in children:
      topPos    = spanSize * counter
      bottomPos = spanSize * ( counter + 1 )

      if counter == 0:
        topOffset    = self.margin
        bottomOffset = self.spacing / 2

      elif counter == ( childNum - 1 ):
        topOffset    = self.spacing / 2
        bottomOffset = self.margin
        bottomPos += spanGap

      else:
        topOffset    = self.spacing / 2
        bottomOffset = self.spacing / 2

      ## Adjustable Width
      if self.childResizable == 0:
        self.ap = [ ( child , "top"    , topOffset , topPos ) ]
        self.af = [ ( child , "left"   , 0 ) ]
        self.af = [ ( child , "right"  , 0 ) ]
        self.ap = [ ( child , "bottom" , bottomOffset , bottomPos ) ]

      else:
        self.ap = [ ( child , "top"    , topOffset , topPos ) ]
        self.ap = [ ( child , "left"   , 0 , 0 ) ]
        self.ap = [ ( child , "right"  , 0 , 100 ) ]
        self.ap = [ ( child , "bottom" , bottomOffset , bottomPos ) ]

      counter += 1











