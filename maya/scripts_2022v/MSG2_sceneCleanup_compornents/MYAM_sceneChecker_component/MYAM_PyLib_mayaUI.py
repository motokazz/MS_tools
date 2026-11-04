#-*- coding:UTF-8 -*-

#*******************************************************************************
'''

Tool Name     : MYAM_PyLib_mayaUI
Description   : MayaのGUIをオブジェクト指向ライクに扱うためのモジュール

Copyright     : (c)2012 Michiyoshi Yamabe
Author Name   : Michiyoshi Yamabe
Contact       : Yamabe.Michiyoshi@gmail.com

------------------------------------
----- Using external libraries -----
------------------------------------
[lisenceType] libraryName version

-------------------------
----- UPDATE RECORD -----
-------------------------
[date] details

'''
#*******************************************************************************

######################
## Import modules
######################

import maya.cmds as cmds
import maya.mel  as mel
import sys

importedModules = sys.modules

import MYAM_PyLib_mayaUI_window  as window
import MYAM_PyLib_mayaUI_panel   as panel
import MYAM_PyLib_mayaUI_layout  as layout
import MYAM_PyLib_mayaUI_menu    as menu
import MYAM_PyLib_mayaUI_control as control
import MYAM_PyLib_mayaUI_other   as other

reload( window  )
reload( panel   )
reload( layout  )
reload( menu    )
reload( control )
reload( other   )




######################
##### UI CLASSES #####
######################












######################
## ↓↓OLD CODES↓↓##

######################
##### UI CLASSES #####
######################

class FnUI():
  def __init__( self ):
    self.OptionMenu = mayaUI.FnOptionMenu()
    self.TextScrollList = mayaUI.FnTextScrollList()
    self.TextField = mayaUI.FnTextField()
    self.IntField = mayaUI.FnIntField()
    self.FloatField = mayaUI.FnFloatField()
    self.ScrollField = mayaUI.FnScrollField()
    self.CheckBox = mayaUI.FnCheckBox()
    self.RadioCollection  = mayaUI.FnRadioCollection()
    self.IconTextCheckBox = mayaUI.FnIconTextCheckBox()
    self.IconTextRadioCollection = mayaUI.FnIconTextRadioCollection()
    self.Image  = mayaUI.FnImage()




##### optionMenu #####

class FnOptionMenu():

  def setItems( self , name , setItems ):
    if isinstance( setItems , list ):
      self.clearItems( name )
      for item in setItems:
        cmds.menuItem( parent=name , label=item )

    elif isinstance( setItems , str ):
      self.clearItems( name )
      cmds.menuItem( parent=name , label=item )

    else:
      raise ValueError , "Invalid setItems type."

  def addItems( self , name , addItems=[] ):
    if isinstance( setItems , list ):
      for item in setItems:
        cmds.menuItem( parent=name , label=item )

    elif isinstance( setItems , str ):
      cmds.menuItem( parent=name , label=item )

    else:
      raise ValueError , "Invalid addItems type."

  def replaceItem( self , name , srcLabel , dstLabel ):
    existItems = cmds.optionMenu( name , q=1 , itemListLong=1 )

    if existItems != None:
      for existItem in existItems:
        menuLabel = cmds.menuItem( existItem , q=1 , label=1 )

        if menuLabel == srcLabel:
          cmds.menuItem( existItem , e=1 , label=dstLabel )

  def deleteItems( self , name , deleteItems ):
    existItems = cmds.optionMenu( name , q=1 , itemListLong=1 )

    if existItems != None:
      for existItem in existItems:
        menuLabel = cmds.menuItem( existItem , q=1 , label=1 )

        if menuLabel in deleteItems:
          cmds.deleteUI( existItem , menuItem=1 )

  def clearItems( self , name ):
    existItems = cmds.optionMenu( name , q=1 , itemListLong=1 )

    if existItems != None:
      for existItem in existItems:
        cmds.deleteUI( existItem , menuItem=1 )

  def selectItem( self , name , targetItem ):
    existItems = cmds.optionMenu( name , q=1 , itemListShort=1 )

    if existItems != None:
      for i in range( len( existItems ) ):
        menuLabel = cmds.menuItem( existItems[0] , q=1 , label=1 )

        if menuLabel == targetItem:
          cmds.optionMenu( name , e=1 , select=i )
          break

  def getSelectedLabel( self , name , type="select" , long=0 ):
    selected = cmds.optionMenu( name , q=1 , value=1 )
    return selected

  def getAllLabels( self , name ):
    existItems = cmds.optionMenu( name , q=1 , itemListLong=1 )
    labels = []

    if existItems == None:
      existItems = ""
    else:
      for existItem in existItems:
        menuLabel = cmds.menuItem( existItem , q=1 , label=1 )
        labels.append( menuLabel )

    return labels

  def enable( self , name ):
    cmds.optionMenu( name , e=1 , enable=1 )

  def disable( self , name ):
    cmds.optionMenu( name , e=1 , enable=0 )





##### textScrollList #####

class FnTextScrollList():

  def setItems( self , name , setItems ):
    if isinstance( setItems , list ):
      self.clearItems( name )
      for item in setItems:
        cmds.textScrollList( name , e=1 , append=item )

    elif isinstance( setItems , str ):
      self.clearItems( name )
      cmds.textScrollList( name , e=1 , append=item )

    else:
      raise ValueError , "Invalid setItems type."

  def addItems( self , name , addItems=[] ):
    if isinstance( setItems , list ):
      for item in setItems:
        cmds.textScrollList( name , e=1 , append=item )

    elif isinstance( setItems , str ):
      cmds.textScrollList( name , e=1 , append=item )

    else:
      raise ValueError , "Invalid addItems type."

  def replaceItem( self , name , srcItem , dstItem ):
    existItems = cmds.textScrollList( name, q=1 , allItems=1 )

    if existItems != None:
      counter  = 0

      for existItem in existItems:
        if srcItem == existItem:
          cmds.textScrollList( name , e=1 , removeIndexedItem = counter+1 )
          cmds.textScrollList( name , e=1 , appendPosition    = [ counter+1 , dstItem ] )

        counter  += 1

  def deleteItems( self , name , deleteItems ):
    existItems = cmds.textScrollList( name, q=1 , allItems=1 )
    deleteIndices = []

    if existItems != None:
      counter  = 0

      for existItem in existItems:
        if existItem in deleteItems:
          deleteIndices.append( counter+1 )

        counter  += 1

    cmds.textScrollList( name , e=1 , removeIndexedItem=sorted( deleteIndices , reverse=1 ) )

  def clearItems( self , name ):
    TSLItems = cmds.textScrollList( name, q=1 , allItems=1 )

    if TSLItems != None:
      cmds.textScrollList( name , e=1 , removeAll=1 )

  def selectItems( self , name , selectItems ):
    existItems = cmds.textScrollList( name, q=1 , allItems=1 )
    selectIndices = []

    if existItems != None:
      counter  = 0

      for existItem in existItems:
        if existItem in selectItems:
          selectIndices.append( counter+1 )

        counter  += 1

    cmds.textScrollList( name , e=1 , selectIndexedItem=selectIndices )

  def sortItems( self , name , reverse=0 ):
    TSLItems = cmds.textScrollList( name, q=1 , allItems=1 )

    if TSLItems != None:
      self.setItems( name , sorted( TSLItems , reverse=reverse ) )

  def getSelectedItems( self , name , type="select" ):
    selected = cmds.textScrollList( name , q=1 , selectItem=1 )
    return selected

  def getAllItems( self , name ):
    existItems = cmds.textScrollList( name , q=1 , allItems=1 )
    return existItems

  def enable( self , name ):
    cmds.textScrollList( name , e=1 , enable=1 )

  def disable( self , name ):
    cmds.textScrollList( name , e=1 , enable=0 )





##### textField #####

class FnTextField():
  def setText( self , name , text ):
    self.clearText( name )
    cmds.textField( name , e=1 , text=text )

  def getText( self , name ):
    return cmds.textField( name , q=1 , text=1 )

  def clearText( self , name ):
    cmds.textField( name , e=1 , text="" )

  def enable( self , name ):
    cmds.textField( name , e=1 , enable=1 )

  def disable( self , name ):
    cmds.textField( name , e=1 , enable=0 )





##### floatField #####

class FnIntField():

  def setValue( self , name , value ):
    cmds.intField( name , e=1 , value=value )

  def getValue( self , name ):
    return cmds.intField( name , q=1 , value=1 )

  def enable( self , name ):
    cmds.intField( name , e=1 , enable=1 )

  def disable( self , name ):
    cmds.intField( name , e=1 , enable=0 )





##### floatField #####

class FnFloatField():

  def setValue( self , name , value ):
    cmds.floatField( name , e=1 , value=value )

  def getValue( self , name ):
    return cmds.floatField( name , q=1 , value=1 )

  def enable( self , name ):
    cmds.floatField( name , e=1 , enable=1 )

  def disable( self , name ):
    cmds.floatField( name , e=1 , enable=0 )





##### scrollField #####

class FnScrollField():

  def setText( self , name , text ):
    clearText( name )
    cmds.scrollField( name , e=1 , text=text )

  def getText( self , name ):
    text = cmds.scrollField( name , q=1 , text=1 )

    if 0 == len( text ):
      text = ""

    return text

  def clearText( self , name ):
    cmds.scrollField( name , e=1 , text="" )

  def enable( self , name ):
    cmds.scrollField( name , e=1 , enable=1 )

  def disable( self , name ):
    cmds.scrollField( name , e=1 , enable=0 )





##### checkBox #####

class FnCheckBox():

  def setValue( self , name , value ):
    cmds.checkBox( name , e=1 , value=value )

  def getValue( self , name ):
    return cmds.checkBox( name , q=1 , value=1 )

  def enable( self , name ):
    cmds.checkBox( name , e=1 , enable=1 )

  def disable( self , name ):
    cmds.checkBox( name , e=1 , enable=0 )





##### radioCollection #####

class FnRadioCollection():

  def select( self , name , item ):
    cmds.radioCollection( name , e=1 , select=item )

  def getSelected( self , name ):
    return cmds.radioCollection( name , q=1 , select=1 )





##### iconTextCheckBox #####

class FnIconTextCheckBox():

  def setValue( self , name , value ):
    cmds.iconTextCheckBox( name , e=1 , value=value )

  def getValue( self , name ):
    return cmds.iconTextCheckBox( name , q=1 , value=1 )

  def enable( self , name ):
    cmds.iconTextCheckBox( name , e=1 , enable=1 )

  def disable( self , name ):
    cmds.iconTextCheckBox( name , e=1 , enable=0 )





##### iconTextRadioCollection #####

class FnIconTextRadioCollection():

  def select( self , name , item ):
    cmds.iconTextRadioCollection( name , e=1 , select=item )

  def getSelected( self , name ):
    return cmds.iconTextRadioCollection( name , q=1 , select=1 )





##### image #####

class FnImage():

  def setImage( self , name , imagePath ):
    cmds.image( IMGName , e=1 , image=imagePath )

  def getImage( self , name ):
    return cmds.image( name , q=1 , image=1 )

  def enable( self , name ):
    cmds.image( name , e=1 , enable=1 )

  def disable( self , name ):
    cmds.image( name , e=1 , enable=0 )





##### DIALOG #####

def promptDialog( title="promptDialog" , message="promtDialog" , button=['YES' , 'NO'] ,
                  defaultButton ='YES'   , cancelButton  = 'NO' , dismissString='' ,
                  cancelReaction="error" , cancelMessage = 'Dialog was canceled.' ,
                  emptyReaction ="error" , emptyMessage  = 'Input is empty' ,
                  closeReaction ="error" , closeMessage  = 'Dialog was closed.' ):

  ## ダイアログ表示
  pushedButton = cmds.promptDialog( title=title , message=message , button=button ,
                                    defaultButton=defaultButton , cancelButton=cancelButton , dismissString='' )
  inputString = cmds.promptDialog( q=1 , text=1 )

  ## 無理矢理閉じられたかチェック
  if pushedButton == "":
    if closeReaction == "error":
      raiseMayaError( closeMessage )
    elif closeReaction == "warning":
      raiseMayaWarning( closeMessage )
    elif closeReaction == "through":
      pass
    else:
      raise ValueError , 'Invalid closeReaction.'

  ## キャンセルチェック
  if pushedButton == cancelButton:
    if cancelReaction == "error":
      raiseMayaError( cancelMessage )
    elif cancelReaction == "warning":
      raiseMayaWarning( cancelMessage )
    elif cancelReaction == "through":
      pass
    else:
      raise ValueError , 'Invalid cancelReaction.'

  ## 空白チェック
  if inputString == "":
    if emptyReaction == "error":
      raiseMayaError( emptyMessage )
    elif emptyReaction == "warning":
      raiseMayaWarning( emptyMessage )
    elif emptyReaction == "through":
      pass
    else:
      raise ValueError , 'Invalid emptyReaction.'

  ## チェック通過したら入力された文字列を返す
  return inputString



def confirmDialog( title="confirmDialog" , message="confirmDialog" , button=['YES' , 'NO'] ,
                   defaultButton ='YES'   , cancelButton='NO' , dismissString='' ,
                   cancelReaction="error" , cancelMessage = 'Dialog was canceled.' ,
                   closeReaction ="error" , closeMessage  = 'Dialog was closed.' ):

  pushedButton = cmds.confirmDialog( title=title , message=message , button=button ,
                                     defaultButton=defaultButton , cancelButton=cancelButton , dismissString=dismissString )

  ## 無理矢理閉じられたかチェック
  if pushedButton == "":
    if closeReaction == "error":
      raiseMayaError( closeMessage )
    elif closeReaction == "warning":
      raiseMayaWarning( closeMessage )
    elif closeReaction == "through":
      pass
    else:
      raise ValueError , 'Invalid closeReaction.'

  ## キャンセルチェック
  if pushedButton == cancelButton:
    if cancelReaction == "error":
      raiseMayaError( cancelMessage )
    elif cancelReaction == "warning":
      raiseMayaWarning( cancelMessage )
    elif cancelReaction == "through":
      pass
    else:
      raise ValueError , 'Invalid cancelReaction.'





##### WINDOW #####

class FnWindow():

  def closeUnDefaultWindow( customSafeWindows=[] ):
    allWindows  = cmds.lsUI( windows=1 )
    safeWindows = [ "MayaWindow" , "CommandWindow" , "ColorEditor" ] + customSafeWindows

    for window in allWindows:
      if window not in safeWindows:
        print "CLOSE -> " , window
        cmds.deleteUI( window )





##### PANEL #####

class FnPanel():

  def getCurrentFocusModelPanel():
    currentFocusPanel = cmds.getPanel( withFocus=1 )

    if "TmodelPane" == cmds.objectTypeUI( currentFocusPanel ):
      return currentFocusPanel

    else:
      confirmDialog( title=u"エラー" , message=u"モデルパネルを選択してから再実行してください。" , button=["OK"] , cancelButton="OK" )





##### UI RELATION CONTROL #####

def listRelativesUI( UIItems , allDescendents=1 , parent=1 , children=1 ,
                               type=None , path=1 , fullPath=1 , noIntermediate=1 ):

  resultItem = []

  for UIItem in UIItems:
    if allDescendents == 1:
      resultItem += searchDescendentsUI( UI )

def searchDescendentsUI( ancestorLayout ):
  children = cmds.layout( ancestorLayout , q=1 , childArray=1 )

  descendents = [ ancestorLayout ]

  for child in children:
    childType = cmds.objectTypeUI( child )

    if "Layout" in childType:
      descendents += searchDescendentsUI( child )

    else:
      descendents.append( child )

  return descendents



##### DISPLAY ERROR #####

def raiseMayaError( message ):
  try:
    mel.eval( 'error "' + message + '"' )
  except:
    raise ValueError , message

def raiseMayaWarning( message ):
  try:
    mel.eval( 'warning "' + message + '"' )
  except:
    print message







######################
## Imported message
######################
print "MODULE IMPORTED... MYAM_PyLib_mayaUI"